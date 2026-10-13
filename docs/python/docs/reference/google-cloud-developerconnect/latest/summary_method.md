---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/summary_method/
title: Package Methods (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:23.311422+00:00
---

# Package Methods (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 

Summary of entries of Methods for google-cloud-developerconnect.

## 

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient
    
    
    DeveloperConnectAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.developer_connect.transports.base.DeveloperConnectTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.developer_connect.transports.base.DeveloperConnectTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the developer connect async client.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_DeveloperConnectAsyncClient)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.account_connector_path
    
    
    account_connector_path(project: str, location: str, account_connector: str) -> str

Returns a fully-qualified account_connector string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.account_connector_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_account_connector_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_cancel_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_common_billing_account_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_common_folder_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_common_location_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_common_organization_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_common_project_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.connection_path
    
    
    connection_path(project: str, location: str, connection: str) -> str

Returns a fully-qualified connection string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.connection_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_connection_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_account_connector
    
    
    create_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateAccountConnectorRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        account_connector: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.AccountConnector
        ] = None,
        account_connector_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new AccountConnector in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_create_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_connection
    
    
    create_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        connection: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.Connection
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
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Connection in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_create_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_git_repository_link
    
    
    create_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateGitRepositoryLinkRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        git_repository_link: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.GitRepositoryLink
        ] = None,
        git_repository_link_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.create_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_create_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_crypto_key_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_account_connector
    
    
    delete_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteAccountConnectorRequest,
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

Deletes a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_connection
    
    
    delete_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteConnectionRequest,
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

Deletes a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_git_repository_link
    
    
    delete_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteGitRepositoryLinkRequest,
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

Deletes a single GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_self
    
    
    delete_self(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteSelfRequest,
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

Delete the User based on the user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_self](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_self)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_user
    
    
    delete_user(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteUserRequest,
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

Deletes a single User.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.delete_user](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_delete_user)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_access_token
    
    
    fetch_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchAccessTokenRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FetchAccessTokenResponse

Fetches OAuth access token based on end user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_access_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_access_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_git_hub_installations
    
    
    fetch_git_hub_installations(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitHubInstallationsRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.types.developer_connect.FetchGitHubInstallationsResponse
    )

FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_git_hub_installations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_git_hub_installations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_git_refs
    
    
    fetch_git_refs(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        ref_type: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest.RefType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsAsyncPager
    )

Fetch the list of branches or tags for a given repository.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_git_refs](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_git_refs)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_linkable_git_repositories
    
    
    fetch_linkable_git_repositories(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesAsyncPager
    )

FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_linkable_git_repositories](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_linkable_git_repositories)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_read_token
    
    
    fetch_read_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchReadTokenRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FetchReadTokenResponse

Fetches read token of a given gitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_read_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_read_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_read_write_token
    
    
    fetch_read_write_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchReadWriteTokenRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.types.developer_connect.FetchReadWriteTokenResponse
    )

Fetches read/write token of a given gitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_read_write_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_read_write_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_self
    
    
    fetch_self(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchSelfRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.User

Fetch the User based on the user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.fetch_self](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_fetch_self)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.finish_o_auth
    
    
    finish_o_auth(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FinishOAuthRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FinishOAuthResponse

Finishes OAuth flow for an account connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.finish_o_auth](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_finish_o_auth)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_from_service_account_file)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_from_service_account_info)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_from_service_account_json)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_account_connector
    
    
    get_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetAccountConnectorRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.AccountConnector

Gets details of a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_connection
    
    
    get_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetConnectionRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.Connection

Gets details of a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_git_repository_link
    
    
    get_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetGitRepositoryLinkRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.GitRepositoryLink

Gets details of a single GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_location
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_location)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.developerconnect_v1.services.developer_connect.transports.base.DeveloperConnectTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_get_transport_class)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.git_repository_link_path
    
    
    git_repository_link_path(
        project: str, location: str, connection: str, git_repository_link: str
    ) -> str

Returns a fully-qualified git_repository_link string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.git_repository_link_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_git_repository_link_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_instance_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_account_connectors
    
    
    list_account_connectors(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsAsyncPager
    )

Lists AccountConnectors in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_account_connectors](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_account_connectors)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_connections
    
    
    list_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsAsyncPager
    )

Lists Connections in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_connections](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_connections)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_git_repository_links
    
    
    list_git_repository_links(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksAsyncPager
    )

Lists GitRepositoryLinks in a given project, location, and connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_git_repository_links](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_git_repository_links)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_locations
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_locations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_operations
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_operations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_users
    
    
    list_users(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersAsyncPager
    )

Lists Users in a given project, location, and account_connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.list_users](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_list_users)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_account_connector_path
    
    
    parse_account_connector_path(path: str) -> typing.Dict[str, str]

Parses a account_connector path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_account_connector_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_account_connector_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_common_billing_account_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_common_folder_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_common_location_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_common_organization_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_common_project_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_connection_path
    
    
    parse_connection_path(path: str) -> typing.Dict[str, str]

Parses a connection path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_connection_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_connection_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_crypto_key_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_git_repository_link_path
    
    
    parse_git_repository_link_path(path: str) -> typing.Dict[str, str]

Parses a git_repository_link path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_git_repository_link_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_git_repository_link_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_instance_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_secret_version_path
    
    
    parse_secret_version_path(path: str) -> typing.Dict[str, str]

Parses a secret_version path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_secret_version_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_secret_version_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_service_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_service_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_user_path
    
    
    parse_user_path(path: str) -> typing.Dict[str, str]

Parses a user path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.parse_user_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_parse_user_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.secret_version_path
    
    
    secret_version_path(project: str, secret: str, secret_version: str) -> str

Returns a fully-qualified secret_version string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.secret_version_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_secret_version_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.service_path
    
    
    service_path(project: str, location: str, namespace: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.service_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_service_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.start_o_auth
    
    
    start_o_auth(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.StartOAuthRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.StartOAuthResponse

Starts OAuth flow for an account connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.start_o_auth](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_start_o_auth)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.update_account_connector
    
    
    update_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.UpdateAccountConnectorRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.AccountConnector
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

Updates the parameters of a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.update_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_update_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.update_connection
    
    
    update_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.UpdateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.Connection
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

Updates the parameters of a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.update_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_update_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.user_path
    
    
    user_path(project: str, location: str, account_connector: str, user: str) -> str

Returns a fully-qualified user string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient.user_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectAsyncClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectAsyncClient_user_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient
    
    
    DeveloperConnectClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.developer_connect.transports.base.DeveloperConnectTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.developer_connect.transports.base.DeveloperConnectTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the developer connect client.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_DeveloperConnectClient)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient___exit__)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.account_connector_path
    
    
    account_connector_path(project: str, location: str, account_connector: str) -> str

Returns a fully-qualified account_connector string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.account_connector_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_account_connector_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.cancel_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_cancel_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_common_billing_account_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_common_folder_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_common_location_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_common_organization_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_common_project_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.connection_path
    
    
    connection_path(project: str, location: str, connection: str) -> str

Returns a fully-qualified connection string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.connection_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_connection_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_account_connector
    
    
    create_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateAccountConnectorRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        account_connector: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.AccountConnector
        ] = None,
        account_connector_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new AccountConnector in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_connection
    
    
    create_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        connection: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.Connection
        ] = None,
        connection_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Connection in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_git_repository_link
    
    
    create_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.CreateGitRepositoryLinkRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        git_repository_link: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.GitRepositoryLink
        ] = None,
        git_repository_link_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.create_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_crypto_key_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_account_connector
    
    
    delete_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteAccountConnectorRequest,
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

Deletes a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_connection
    
    
    delete_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteConnectionRequest,
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

Deletes a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_git_repository_link
    
    
    delete_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteGitRepositoryLinkRequest,
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

Deletes a single GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_self
    
    
    delete_self(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteSelfRequest,
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

Delete the User based on the user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_self](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_self)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_user
    
    
    delete_user(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.DeleteUserRequest,
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

Deletes a single User.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.delete_user](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_user)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_access_token
    
    
    fetch_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchAccessTokenRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FetchAccessTokenResponse

Fetches OAuth access token based on end user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_access_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_access_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_git_hub_installations
    
    
    fetch_git_hub_installations(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitHubInstallationsRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.types.developer_connect.FetchGitHubInstallationsResponse
    )

FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_git_hub_installations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_git_hub_installations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_git_refs
    
    
    fetch_git_refs(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        ref_type: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest.RefType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager
    )

Fetch the list of branches or tags for a given repository.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_git_refs](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_git_refs)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_linkable_git_repositories
    
    
    fetch_linkable_git_repositories(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager
    )

FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_linkable_git_repositories](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_linkable_git_repositories)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_read_token
    
    
    fetch_read_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchReadTokenRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FetchReadTokenResponse

Fetches read token of a given gitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_read_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_read_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_read_write_token
    
    
    fetch_read_write_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchReadWriteTokenRequest,
                dict,
            ]
        ] = None,
        *,
        git_repository_link: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.developerconnect_v1.types.developer_connect.FetchReadWriteTokenResponse
    )

Fetches read/write token of a given gitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_read_write_token](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_read_write_token)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_self
    
    
    fetch_self(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FetchSelfRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.User

Fetch the User based on the user credentials.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.fetch_self](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_self)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.finish_o_auth
    
    
    finish_o_auth(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.FinishOAuthRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.FinishOAuthResponse

Finishes OAuth flow for an account connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.finish_o_auth](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_finish_o_auth)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_from_service_account_file)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_from_service_account_info)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_from_service_account_json)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_account_connector
    
    
    get_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetAccountConnectorRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.AccountConnector

Gets details of a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_connection
    
    
    get_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetConnectionRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.Connection

Gets details of a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_git_repository_link
    
    
    get_git_repository_link(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.GetGitRepositoryLinkRequest,
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
    ) -> google.cloud.developerconnect_v1.types.developer_connect.GitRepositoryLink

Gets details of a single GitRepositoryLink.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_git_repository_link](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_git_repository_link)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_location
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_location)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_mtls_endpoint_and_cert_source)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_operation)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.git_repository_link_path
    
    
    git_repository_link_path(
        project: str, location: str, connection: str, git_repository_link: str
    ) -> str

Returns a fully-qualified git_repository_link string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.git_repository_link_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_git_repository_link_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.instance_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_instance_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_account_connectors
    
    
    list_account_connectors(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager
    )

Lists AccountConnectors in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_account_connectors](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_account_connectors)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_connections
    
    
    list_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager
    )

Lists Connections in a given project and location.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_connections](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_connections)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_git_repository_links
    
    
    list_git_repository_links(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
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
        google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager
    )

Lists GitRepositoryLinks in a given project, location, and connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_git_repository_links](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_git_repository_links)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_locations
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_locations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_operations
    
    
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_operations)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_users
    
    
    list_users(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
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
    ) -> google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager

Lists Users in a given project, location, and account_connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.list_users](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_users)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_account_connector_path
    
    
    parse_account_connector_path(path: str) -> typing.Dict[str, str]

Parses a account_connector path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_account_connector_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_account_connector_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_common_billing_account_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_common_folder_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_common_location_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_common_organization_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_common_project_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_connection_path
    
    
    parse_connection_path(path: str) -> typing.Dict[str, str]

Parses a connection path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_connection_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_connection_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_crypto_key_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_git_repository_link_path
    
    
    parse_git_repository_link_path(path: str) -> typing.Dict[str, str]

Parses a git_repository_link path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_git_repository_link_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_git_repository_link_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_instance_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_secret_version_path
    
    
    parse_secret_version_path(path: str) -> typing.Dict[str, str]

Parses a secret_version path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_secret_version_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_secret_version_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_service_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_service_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_user_path
    
    
    parse_user_path(path: str) -> typing.Dict[str, str]

Parses a user path into its component segments.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.parse_user_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_parse_user_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.secret_version_path
    
    
    secret_version_path(project: str, secret: str, secret_version: str) -> str

Returns a fully-qualified secret_version string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.secret_version_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_secret_version_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.service_path
    
    
    service_path(project: str, location: str, namespace: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.service_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_service_path)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.start_o_auth
    
    
    start_o_auth(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.StartOAuthRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.developerconnect_v1.types.developer_connect.StartOAuthResponse

Starts OAuth flow for an account connector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.start_o_auth](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_start_o_auth)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.update_account_connector
    
    
    update_account_connector(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.UpdateAccountConnectorRequest,
                dict,
            ]
        ] = None,
        *,
        account_connector: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.AccountConnector
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

Updates the parameters of a single AccountConnector.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.update_account_connector](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_update_account_connector)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.update_connection
    
    
    update_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.developer_connect.UpdateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        connection: typing.Optional[
            google.cloud.developerconnect_v1.types.developer_connect.Connection
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

Updates the parameters of a single Connection.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.update_connection](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_update_connection)

### google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.user_path
    
    
    user_path(project: str, location: str, account_connector: str, user: str) -> str

Returns a fully-qualified user string.

See more: [google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.user_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_user_path)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsAsyncPager
    
    
    FetchGitRefsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_FetchGitRefsAsyncPager_FetchGitRefsAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager
    
    
    FetchGitRefsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_FetchGitRefsPager_FetchGitRefsPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesAsyncPager
    
    
    FetchLinkableGitRepositoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_FetchLinkableGitRepositoriesAsyncPager_FetchLinkableGitRepositoriesAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager
    
    
    FetchLinkableGitRepositoriesPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_FetchLinkableGitRepositoriesPager_FetchLinkableGitRepositoriesPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsAsyncPager
    
    
    ListAccountConnectorsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListAccountConnectorsAsyncPager_ListAccountConnectorsAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager
    
    
    ListAccountConnectorsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListAccountConnectorsPager_ListAccountConnectorsPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsAsyncPager
    
    
    ListConnectionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListConnectionsAsyncPager_ListConnectionsAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager
    
    
    ListConnectionsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListConnectionsPager_ListConnectionsPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksAsyncPager
    
    
    ListGitRepositoryLinksAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListGitRepositoryLinksAsyncPager_ListGitRepositoryLinksAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager
    
    
    ListGitRepositoryLinksPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListGitRepositoryLinksPager_ListGitRepositoryLinksPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersAsyncPager
    
    
    ListUsersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersAsyncPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListUsersAsyncPager_ListUsersAsyncPager)

### google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager
    
    
    ListUsersPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
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

See more: [google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager#google_cloud_developerconnect_v1_services_developer_connect_pagers_ListUsersPager_ListUsersPager)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient
    
    
    InsightsConfigServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the insights config service async client.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_InsightsConfigServiceAsyncClient)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_cancel_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_common_billing_account_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_common_folder_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_common_location_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_common_organization_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_common_project_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.create_insights_config
    
    
    create_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.CreateInsightsConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        insights_config: typing.Optional[
            google.cloud.developerconnect_v1.types.insights_config.InsightsConfig
        ] = None,
        insights_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new InsightsConfig in a given project and location.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.create_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_create_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.delete_insights_config
    
    
    delete_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.DeleteInsightsConfigRequest,
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

Deletes a single Insight.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.delete_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_delete_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_delete_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.deployment_event_path
    
    
    deployment_event_path(
        project: str, location: str, insights_config: str, deployment_event: str
    ) -> str

Returns a fully-qualified deployment_event string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.deployment_event_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_deployment_event_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_from_service_account_file)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_from_service_account_info)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_from_service_account_json)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_deployment_event
    
    
    get_deployment_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetDeploymentEventRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.DeploymentEvent

Gets a single Deployment Event.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_deployment_event](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_deployment_event)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_insights_config
    
    
    get_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetInsightsConfigRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.InsightsConfig

Gets details of a single Insight.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_location)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_get_transport_class)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.insights_config_path
    
    
    insights_config_path(project: str, location: str, insights_config: str) -> str

Returns a fully-qualified insights_config string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.insights_config_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_insights_config_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_deployment_events
    
    
    list_deployment_events(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsAsyncPager
    )

Lists Deployment Events in a given insights config.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_deployment_events](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_list_deployment_events)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_insights_configs
    
    
    list_insights_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsAsyncPager
    )

Lists InsightsConfigs in a given project and location.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_insights_configs](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_list_insights_configs)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_list_locations)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_list_operations)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_common_folder_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_common_location_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_common_organization_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_common_project_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_deployment_event_path
    
    
    parse_deployment_event_path(path: str) -> typing.Dict[str, str]

Parses a deployment_event path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_deployment_event_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_deployment_event_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_insights_config_path
    
    
    parse_insights_config_path(path: str) -> typing.Dict[str, str]

Parses a insights_config path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.parse_insights_config_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_parse_insights_config_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.update_insights_config
    
    
    update_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.UpdateInsightsConfigRequest,
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

Updates the parameters of a single InsightsConfig.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient.update_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceAsyncClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceAsyncClient_update_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient
    
    
    InsightsConfigServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the insights config service client.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_InsightsConfigServiceClient)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient___exit__)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.cancel_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_cancel_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_common_billing_account_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_common_folder_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_common_location_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_common_organization_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_common_project_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.create_insights_config
    
    
    create_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.CreateInsightsConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        insights_config: typing.Optional[
            google.cloud.developerconnect_v1.types.insights_config.InsightsConfig
        ] = None,
        insights_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new InsightsConfig in a given project and location.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.create_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_create_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.delete_insights_config
    
    
    delete_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.DeleteInsightsConfigRequest,
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

Deletes a single Insight.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.delete_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_delete_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.delete_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_delete_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.deployment_event_path
    
    
    deployment_event_path(
        project: str, location: str, insights_config: str, deployment_event: str
    ) -> str

Returns a fully-qualified deployment_event string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.deployment_event_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_deployment_event_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_from_service_account_file)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_from_service_account_info)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_from_service_account_json)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_deployment_event
    
    
    get_deployment_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetDeploymentEventRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.DeploymentEvent

Gets a single Deployment Event.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_deployment_event](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_deployment_event)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_insights_config
    
    
    get_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetInsightsConfigRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.InsightsConfig

Gets details of a single Insight.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_location
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_location)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_operation
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_operation)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.insights_config_path
    
    
    insights_config_path(project: str, location: str, insights_config: str) -> str

Returns a fully-qualified insights_config string.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.insights_config_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_insights_config_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_deployment_events
    
    
    list_deployment_events(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager
    )

Lists Deployment Events in a given insights config.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_deployment_events](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_deployment_events)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_insights_configs
    
    
    list_insights_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager
    )

Lists InsightsConfigs in a given project and location.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_insights_configs](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_insights_configs)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_locations
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_locations)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_operations
    
    
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_operations)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_common_billing_account_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_common_folder_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_common_location_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_common_organization_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_common_project_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_deployment_event_path
    
    
    parse_deployment_event_path(path: str) -> typing.Dict[str, str]

Parses a deployment_event path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_deployment_event_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_deployment_event_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_insights_config_path
    
    
    parse_insights_config_path(path: str) -> typing.Dict[str, str]

Parses a insights_config path into its component segments.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.parse_insights_config_path](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_parse_insights_config_path)

### google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.update_insights_config
    
    
    update_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.UpdateInsightsConfigRequest,
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

Updates the parameters of a single InsightsConfig.

See more: [google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.update_insights_config](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_update_insights_config)

### google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsAsyncPager
    
    
    ListDeploymentEventsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsRequest,
        response: google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsResponse,
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsAsyncPager#google_cloud_developerconnect_v1_services_insights_config_service_pagers_ListDeploymentEventsAsyncPager_ListDeploymentEventsAsyncPager)

### google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager
    
    
    ListDeploymentEventsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsRequest,
        response: google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsResponse,
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager#google_cloud_developerconnect_v1_services_insights_config_service_pagers_ListDeploymentEventsPager_ListDeploymentEventsPager)

### google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsAsyncPager
    
    
    ListInsightsConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsRequest,
        response: google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsResponse,
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsAsyncPager#google_cloud_developerconnect_v1_services_insights_config_service_pagers_ListInsightsConfigsAsyncPager_ListInsightsConfigsAsyncPager)

### google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager
    
    
    ListInsightsConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsRequest,
        response: google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsResponse,
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

See more: [google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager](https://cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager#google_cloud_developerconnect_v1_services_insights_config_service_pagers_ListInsightsConfigsPager_ListInsightsConfigsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
