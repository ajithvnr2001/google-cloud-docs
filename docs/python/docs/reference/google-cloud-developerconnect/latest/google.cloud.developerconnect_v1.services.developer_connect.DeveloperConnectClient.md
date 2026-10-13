---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient
title: Class DeveloperConnectClient (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:26.403113+00:00
---

# Class DeveloperConnectClient (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeveloperConnectClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
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

Service describing handlers for resources

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
`DeveloperConnectTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DeveloperConnectClient
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DeveloperConnectTransport,Callable[..., DeveloperConnectTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the DeveloperConnectTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### account_connector_path
    
    
    account_connector_path(project: str, location: str, account_connector: str) -> str

Returns a fully-qualified account_connector string.

### cancel_operation
    
    
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

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
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

### connection_path
    
    
    connection_path(project: str, location: str, connection: str) -> str

Returns a fully-qualified connection string.

### create_account_connector
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_create_account_connector():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        account_connector = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector.html)()
        account_connector.provider_oauth_config.system_provider_id = "DYNATRACE"
        account_connector.provider_oauth_config.scopes = ['scopes_value1', 'scopes_value2']
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[CreateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateAccountConnectorRequest.html)(
            parent="parent_value",
            account_connector_id="account_connector_id_value",
            account_connector=account_connector,
        )
    
        # Make the request
        operation = client.[create_account_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_account_connector)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.CreateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateAccountConnectorRequest), dict]`   
The request object.  
`parent` |  `str`   
Required. Location resource name as the account_connector’s parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`account_connector` |  `[google.cloud.developerconnect_v1.types.AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector)`   
Required. The AccountConnector to create. This corresponds to the `account_connector` field on the `request` instance; if `request` is provided, this should not be set.  
`account_connector_id` |  `str`   
Required. The ID to use for the AccountConnector, which will become the final component of the AccountConnector's resource name. Its format should adhere to <https://google.aip.dev/122#resource-id-segments> Names must be unique per-project per-location. This corresponds to the `account_connector_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector) AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.  
  
### create_connection
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_create_connection():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        connection = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection.html)()
        connection.github_config.github_app = "GEMINI_CODE_ASSIST"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateConnectionRequest.html)(
            parent="parent_value",
            connection_id="connection_id_value",
            connection=connection,
        )
    
        # Make the request
        operation = client.[create_connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_connection)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateConnectionRequest), dict]`   
The request object. Message for creating a Connection  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`connection` |  `[google.cloud.developerconnect_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection)`   
Required. The resource being created This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`connection_id` |  `str`   
Required. Id of the requesting object If auto-generating Id server-side, remove this field and connection_id from the method_signature of Create RPC This corresponds to the `connection_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection) Message describing Connection object  
  
### create_git_repository_link
    
    
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

Creates a GitRepositoryLink. Upon linking a Git Repository, Developer Connect will configure the Git Repository to send webhook events to Developer Connect. Connections that use Firebase GitHub Application will have events forwarded to the Firebase service. Connections that use Gemini Code Assist will have events forwarded to Gemini Code Assist service. All other Connections will have events forwarded to Cloud Build.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_create_git_repository_link():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        git_repository_link = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GitRepositoryLink](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitRepositoryLink.html)()
        git_repository_link.clone_uri = "clone_uri_value"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[CreateGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateGitRepositoryLinkRequest.html)(
            parent="parent_value",
            git_repository_link=git_repository_link,
            git_repository_link_id="git_repository_link_id_value",
        )
    
        # Make the request
        operation = client.[create_git_repository_link](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_create_git_repository_link)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.CreateGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateGitRepositoryLinkRequest), dict]`   
The request object. Message for creating a GitRepositoryLink  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`git_repository_link` |  `[google.cloud.developerconnect_v1.types.GitRepositoryLink](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitRepositoryLink)`   
Required. The resource being created This corresponds to the `git_repository_link` field on the `request` instance; if `request` is provided, this should not be set.  
`git_repository_link_id` |  `str`   
Required. The ID to use for the repository, which will become the final component of the repository's resource name. This ID should be unique in the connection. Allows alphanumeric characters and any of -._`%!$&'()*+,;=@. This corresponds to the `git_repository_link_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [GitRepositoryLink](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitRepositoryLink) Message describing the GitRepositoryLink object  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### delete_account_connector
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_account_connector():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteAccountConnectorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_account_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_account_connector)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteAccountConnectorRequest), dict]`   
The request object. Message for deleting a AccountConnector  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_connection
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_connection():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_connection)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteConnectionRequest), dict]`   
The request object. Message for deleting a Connection  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_git_repository_link
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_git_repository_link():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteGitRepositoryLinkRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_git_repository_link](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_git_repository_link)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteGitRepositoryLinkRequest), dict]`   
The request object. Message for deleting a GitRepositoryLink  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_operation
    
    
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

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_self
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_self():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteSelfRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_self](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_self)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteSelfRequest), dict]`   
The request object. Message for deleting a User of the user themselves.  
`name` |  `str`   
Required. Name of the AccountConnector resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_user
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_user():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteUserRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_user](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_delete_user)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteUserRequest), dict]`   
The request object. Message for deleting a User  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### fetch_access_token
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_access_token():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchAccessTokenRequest.html)(
            account_connector="account_connector_value",
        )
    
        # Make the request
        response = client.[fetch_access_token](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_access_token)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchAccessTokenRequest), dict]`   
The request object. Message for fetching an OAuth access token.  
`account_connector` |  `str`   
Required. The resource name of the AccountConnector in the format `projects/_/locations/_ /accountConnectors/*`. This corresponds to the `account_connector` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.FetchAccessTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchAccessTokenResponse)` | Message for responding to getting an OAuth access token.  
  
### fetch_git_hub_installations
    
    
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

FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection. For github.com, only installations accessible to the authorizer token are returned. For GitHub Enterprise, all installations are returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_git_hub_installations():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchGitHubInstallationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitHubInstallationsRequest.html)(
            connection="connection_value",
        )
    
        # Make the request
        response = client.[fetch_git_hub_installations](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_git_hub_installations)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchGitHubInstallationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitHubInstallationsRequest), dict]`   
The request object. Request for fetching github installations.  
`connection` |  `str`   
Required. The resource name of the connection in the format `projects/_/locations/_ /connections/*`. This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.FetchGitHubInstallationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitHubInstallationsResponse)` | Response of fetching github installations.  
  
### fetch_git_refs
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_git_refs():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchGitRefsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsRequest.html)(
            git_repository_link="git_repository_link_value",
            ref_type="BRANCH",
        )
    
        # Make the request
        page_result = client.[fetch_git_refs](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_git_refs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchGitRefsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsRequest), dict]`   
The request object. Request for fetching git refs.  
`git_repository_link` |  `str`   
Required. The resource name of GitRepositoryLink in the format `projects/_/locations/_ /connections/_/gitRepositoryLinks/_`. This corresponds to the `git_repository_link` field on the `request` instance; if `request` is provided, this should not be set.  
`ref_type` |  `[google.cloud.developerconnect_v1.types.FetchGitRefsRequest.RefType](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsRequest.RefType)`   
Required. Type of refs to fetch. This corresponds to the `ref_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager)` | Response for fetching git refs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_linkable_git_repositories
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_linkable_git_repositories():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchLinkableGitRepositoriesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest.html)(
            connection="connection_value",
        )
    
        # Make the request
        page_result = client.[fetch_linkable_git_repositories](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_linkable_git_repositories)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest), dict]`   
The request object. Request message for FetchLinkableGitRepositoriesRequest.  
`connection` |  `str`   
Required. The name of the Connection. Format: `projects/_/locations/_ /connections/*`. This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager)` | Response message for FetchLinkableGitRepositories. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_read_token
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_read_token():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchReadTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadTokenRequest.html)(
            git_repository_link="git_repository_link_value",
        )
    
        # Make the request
        response = client.[fetch_read_token](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_read_token)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchReadTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadTokenRequest), dict]`   
The request object. Message for fetching SCM read token.  
`git_repository_link` |  `str`   
Required. The resource name of the gitRepositoryLink in the format `projects/_/locations/_ /connections/_/gitRepositoryLinks/_`. This corresponds to the `git_repository_link` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.FetchReadTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadTokenResponse)` | Message for responding to get read token.  
  
### fetch_read_write_token
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_read_write_token():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchReadWriteTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadWriteTokenRequest.html)(
            git_repository_link="git_repository_link_value",
        )
    
        # Make the request
        response = client.[fetch_read_write_token](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_read_write_token)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchReadWriteTokenRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadWriteTokenRequest), dict]`   
The request object. Message for fetching SCM read/write token.  
`git_repository_link` |  `str`   
Required. The resource name of the gitRepositoryLink in the format `projects/_/locations/_ /connections/_/gitRepositoryLinks/_`. This corresponds to the `git_repository_link` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.FetchReadWriteTokenResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchReadWriteTokenResponse)` | Message for responding to get read/write token.  
  
### fetch_self
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_fetch_self():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FetchSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchSelfRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[fetch_self](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_fetch_self)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FetchSelfRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchSelfRequest), dict]`   
The request object. Message for fetching a User of the user themselves.  
`name` |  `str`   
Required. Name of the AccountConnector resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.User](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.User)` | User represents a user connected to the service providers through a AccountConnector.  
  
### finish_o_auth
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_finish_o_auth():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        oauth_params = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[OAuthParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthRequest.OAuthParams.html)()
        oauth_params.code = "code_value"
        oauth_params.ticket = "ticket_value"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[FinishOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthRequest.html)(
            oauth_params=oauth_params,
            account_connector="account_connector_value",
        )
    
        # Make the request
        response = client.[finish_o_auth](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_finish_o_auth)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.FinishOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthRequest), dict]`   
The request object. Message for finishing an OAuth flow.  
`account_connector` |  `str`   
Required. The resource name of the AccountConnector in the format `projects/_/locations/_ /accountConnectors/*`. This corresponds to the `account_connector` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.FinishOAuthResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FinishOAuthResponse)` | Message for responding to finishing an OAuth flow.  
  
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
`DeveloperConnectClient` | The constructed client.  
  
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
`DeveloperConnectClient` | The constructed client.  
  
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
`DeveloperConnectClient` | The constructed client.  
  
### get_account_connector
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_get_account_connector():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GetAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetAccountConnectorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_account_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_account_connector)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.GetAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetAccountConnectorRequest), dict]`   
The request object. Message for getting a AccountConnector  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector)` | AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.  
  
### get_connection
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_get_connection():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetConnectionRequest), dict]`   
The request object. Message for getting a Connection  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection)` | Message describing Connection object  
  
### get_git_repository_link
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_get_git_repository_link():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GetGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetGitRepositoryLinkRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_git_repository_link](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_get_git_repository_link)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.GetGitRepositoryLinkRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetGitRepositoryLinkRequest), dict]`   
The request object. Message for getting a GitRepositoryLink  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.GitRepositoryLink](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitRepositoryLink)` | Message describing the GitRepositoryLink object  
  
### get_location
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
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

Deprecated. Return the API endpoint and client cert source for mutual TLS.

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
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### git_repository_link_path
    
    
    git_repository_link_path(
        project: str, location: str, connection: str, git_repository_link: str
    ) -> str

Returns a fully-qualified git_repository_link string.

### instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

### list_account_connectors
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_account_connectors():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListAccountConnectorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_account_connectors](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_account_connectors)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest), dict]`   
The request object. Message for requesting list of AccountConnectors  
`parent` |  `str`   
Required. Parent value for ListAccountConnectorsRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager)` | Message for response to listing AccountConnectors Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_connections
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_connections():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_connections](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_connections)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsRequest), dict]`   
The request object. Message for requesting list of Connections  
`parent` |  `str`   
Required. Parent value for ListConnectionsRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager)` | Message for response to listing Connections Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_git_repository_links
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_git_repository_links():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListGitRepositoryLinksRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_git_repository_links](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_git_repository_links)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest), dict]`   
The request object. Message for requesting a list of GitRepositoryLinks  
`parent` |  `str`   
Required. Parent value for ListGitRepositoryLinksRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager)` | Message for response to listing GitRepositoryLinks Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
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
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_users
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_users():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListUsersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_users](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_list_users)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListUsersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersRequest), dict]`   
The request object. Message for requesting a list of Users  
`parent` |  `str`   
Required. Parent value for ListUsersRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager)` | Message for response to listing Users Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_account_connector_path
    
    
    parse_account_connector_path(path: str) -> typing.Dict[str, str]

Parses a account_connector path into its component segments.

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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_git_repository_link_path
    
    
    parse_git_repository_link_path(path: str) -> typing.Dict[str, str]

Parses a git_repository_link path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### parse_secret_version_path
    
    
    parse_secret_version_path(path: str) -> typing.Dict[str, str]

Parses a secret_version path into its component segments.

### parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

### parse_user_path
    
    
    parse_user_path(path: str) -> typing.Dict[str, str]

Parses a user path into its component segments.

### secret_version_path
    
    
    secret_version_path(project: str, secret: str, secret_version: str) -> str

Returns a fully-qualified secret_version string.

### service_path
    
    
    service_path(project: str, location: str, namespace: str, service: str) -> str

Returns a fully-qualified service string.

### start_o_auth
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_start_o_auth():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[StartOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.StartOAuthRequest.html)(
            account_connector="account_connector_value",
        )
    
        # Make the request
        response = client.[start_o_auth](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_start_o_auth)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.StartOAuthRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.StartOAuthRequest), dict]`   
The request object. Message for starting an OAuth flow.  
`account_connector` |  `str`   
Required. The resource name of the AccountConnector in the format `projects/_/locations/_ /accountConnectors/*`. This corresponds to the `account_connector` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.StartOAuthResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.StartOAuthResponse)` | Message for responding to starting an OAuth flow.  
  
### update_account_connector
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_update_account_connector():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        account_connector = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector.html)()
        account_connector.provider_oauth_config.system_provider_id = "DYNATRACE"
        account_connector.provider_oauth_config.scopes = ['scopes_value1', 'scopes_value2']
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[UpdateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateAccountConnectorRequest.html)(
            account_connector=account_connector,
        )
    
        # Make the request
        operation = client.[update_account_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_update_account_connector)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.UpdateAccountConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateAccountConnectorRequest), dict]`   
The request object. Message for updating a AccountConnector  
`account_connector` |  `[google.cloud.developerconnect_v1.types.AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector)`   
Required. The AccountConnector to update. This corresponds to the `account_connector` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The list of fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [AccountConnector](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector) AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.  
  
### update_connection
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_update_connection():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeveloperConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html)()
    
        # Initialize request argument(s)
        connection = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection.html)()
        connection.github_config.github_app = "GEMINI_CODE_ASSIST"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateConnectionRequest.html)(
            connection=connection,
        )
    
        # Make the request
        operation = client.[update_connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.DeveloperConnectClient.html#google_cloud_developerconnect_v1_services_developer_connect_DeveloperConnectClient_update_connection)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateConnectionRequest), dict]`   
The request object. Message for updating a Connection  
`connection` |  `[google.cloud.developerconnect_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection)`   
Required. The resource being updated This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Field mask is used to specify the fields to be overwritten in the Connection resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Connection](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection) Message describing Connection object  
  
### user_path
    
    
    user_path(project: str, location: str, account_connector: str, user: str) -> str

Returns a fully-qualified user string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
