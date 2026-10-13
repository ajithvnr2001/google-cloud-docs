---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient
title: Class NetAppAsyncClient (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:13.157795+00:00
---

# Class NetAppAsyncClient (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NetAppAsyncClient (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    NetAppAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                typing.Callable[
                    [...],
                    google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

NetApp Files Google Cloud Service

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
`NetAppTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### NetAppAsyncClient
    
    
    NetAppAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                typing.Callable[
                    [...],
                    google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the net app async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,NetAppTransport,Callable[..., NetAppTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the NetAppTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### active_directory_path
    
    
    active_directory_path(project: str, location: str, active_directory: str) -> str

Returns a fully-qualified active_directory string.

### backup_path
    
    
    backup_path(project: str, location: str, backup_vault: str, backup: str) -> str

Returns a fully-qualified backup string.

### backup_policy_path
    
    
    backup_policy_path(project: str, location: str, backup_policy: str) -> str

Returns a fully-qualified backup_policy string.

### backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backup_vault: str) -> str

Returns a fully-qualified backup_vault string.

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

### create_active_directory
    
    
    create_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.CreateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
        ] = None,
        active_directory_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

CreateActiveDirectory Creates the active directory specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_active_directory():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        active_directory = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory.html)()
        active_directory.domain = "domain_value"
        active_directory.dns = "dns_value"
        active_directory.net_bios_prefix = "net_bios_prefix_value"
        active_directory.username = "username_value"
        active_directory.password = "password_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateActiveDirectoryRequest.html)(
            parent="parent_value",
            active_directory=active_directory,
            active_directory_id="active_directory_id_value",
        )
    
        # Make the request
        operation = await client.[create_active_directory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_active_directory)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateActiveDirectoryRequest), dict]]`   
The request object. CreateActiveDirectoryRequest for creating an active directory.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`active_directory` |  `[ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory)`   
Required. Fields of the to be created active directory. This corresponds to the `active_directory` field on the `request` instance; if `request` is provided, this should not be set.  
`active_directory_id` |  ``str``   
Required. ID of the active directory to create. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter , the last a letter or a number, and a 63 character maximum. This corresponds to the `active_directory_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory) ActiveDirectory is the public representation of the active directory config.  
  
### create_backup
    
    
    create_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.CreateBackupRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
        backup_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a backup from the volume specified in the request The backup can be created from the given snapshot if specified in the request. If no snapshot specified, there'll be a new snapshot taken to initiate the backup creation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_backup():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupRequest.html)(
            parent="parent_value",
            backup_id="backup_id_value",
        )
    
        # Make the request
        operation = await client.[create_backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupRequest), dict]]`   
The request object. CreateBackupRequest creates a backup.  
`parent` |  ``str``   
Required. The NetApp backupVault to create the backups of, in the format `projects/_/locations/_ /backupVaults/{backup_vault_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup` |  `[Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup)`   
Required. A backup resource This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_id` |  ``str``   
Required. The ID to use for the backup. The ID must be unique within the specified backupVault. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `backup_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup) A NetApp Backup.  
  
### create_backup_policy
    
    
    create_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.CreateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
        ] = None,
        backup_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates new backup policy
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_backup_policy():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupPolicyRequest.html)(
            parent="parent_value",
            backup_policy_id="backup_policy_id_value",
        )
    
        # Make the request
        operation = await client.[create_backup_policy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupPolicyRequest), dict]]`   
The request object. CreateBackupPolicyRequest creates a backupPolicy.  
`parent` |  ``str``   
Required. The location to create the backup policies of, in the format `projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_policy` |  `[BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy)`   
Required. A backupPolicy resource This corresponds to the `backup_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_policy_id` |  ``str``   
Required. The ID to use for the backup policy. The ID must be unique within the specified location. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `backup_policy_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy) Backup Policy.  
  
### create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates new backup vault
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_backup_vault():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupVaultRequest.html)(
            parent="parent_value",
            backup_vault_id="backup_vault_id_value",
        )
    
        # Make the request
        operation = await client.[create_backup_vault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupVaultRequest), dict]]`   
The request object. CreateBackupVaultRequest creates a backup vault.  
`parent` |  ``str``   
Required. The location to create the backup vaults, in the format `projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_vault` |  `[BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault)`   
Required. A backupVault resource This corresponds to the `backup_vault` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_vault_id` |  ``str``   
Required. The ID to use for the backupVault. The ID must be unique within the specified location. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `backup_vault_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault) A NetApp BackupVault.  
  
### create_host_group
    
    
    create_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.CreateHostGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
        ] = None,
        host_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new host group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_host_group():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        host_group = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup.html)()
        host_group.type_ = "ISCSI_INITIATOR"
        host_group.hosts = ['hosts_value1', 'hosts_value2']
        host_group.os_type = "ESXI"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateHostGroupRequest.html)(
            parent="parent_value",
            host_group=host_group,
            host_group_id="host_group_id_value",
        )
    
        # Make the request
        operation = await client.[create_host_group](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_host_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateHostGroupRequest), dict]]`   
The request object. CreateHostGroupRequest for creating a host group.  
`parent` |  ``str``   
Required. Parent value for CreateHostGroupRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`host_group` |  `[HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup)`   
Required. Fields of the host group to create. This corresponds to the `host_group` field on the `request` instance; if `request` is provided, this should not be set.  
`host_group_id` |  ``str``   
Required. ID of the host group to create. Must be unique within the parent resource. Must contain only letters, numbers, and hyphen, with the first character a letter or underscore, the last a letter or underscore or a number, and a 63 character maximum. This corresponds to the `host_group_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup) Host group is a collection of hosts that can be used for accessing a Block Volume.  
  
### create_kms_config
    
    
    create_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.CreateKmsConfigRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
        kms_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new KMS config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_kms_config():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        kms_config = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig.html)()
        kms_config.crypto_key_name = "crypto_key_name_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateKmsConfigRequest.html)(
            parent="parent_value",
            kms_config_id="kms_config_id_value",
            kms_config=kms_config,
        )
    
        # Make the request
        operation = await client.[create_kms_config](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_kms_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateKmsConfigRequest), dict]]`   
The request object. CreateKmsConfigRequest creates a KMS Config.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`kms_config` |  `[KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig)`   
Required. The required parameters to create a new KmsConfig. This corresponds to the `kms_config` field on the `request` instance; if `request` is provided, this should not be set.  
`kms_config_id` |  ``str``   
Required. Id of the requesting KmsConfig. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `kms_config_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig) KmsConfig is the customer-managed encryption key(CMEK) configuration.  
  
### create_quota_rule
    
    
    create_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.CreateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
        ] = None,
        quota_rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new quota rule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_quota_rule():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        quota_rule = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule.html)()
        quota_rule.type_ = "DEFAULT_GROUP_QUOTA"
        quota_rule.disk_limit_mib = 1472
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateQuotaRuleRequest.html)(
            parent="parent_value",
            quota_rule=quota_rule,
            quota_rule_id="quota_rule_id_value",
        )
    
        # Make the request
        operation = await client.[create_quota_rule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_quota_rule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateQuotaRuleRequest), dict]]`   
The request object. CreateQuotaRuleRequest for creating a quota rule.  
`parent` |  ``str``   
Required. Parent value for CreateQuotaRuleRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`quota_rule` |  `[QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule)`   
Required. Fields of the to be created quota rule. This corresponds to the `quota_rule` field on the `request` instance; if `request` is provided, this should not be set.  
`quota_rule_id` |  ``str``   
Required. ID of the quota rule to create. Must be unique within the parent resource. Must contain only letters, numbers, underscore and hyphen, with the first character a letter or underscore, the last a letter or underscore or a number, and a 63 character maximum. This corresponds to the `quota_rule_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule) QuotaRule specifies the maximum disk space a user or group can use within a volume. They can be used for creating default and individual quota rules.  
  
### create_replication
    
    
    create_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.CreateReplicationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
        ] = None,
        replication_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a new replication for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        replication = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication.html)()
        replication.replication_schedule = "DAILY"
        replication.destination_volume_parameters.storage_pool = "storage_pool_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateReplicationRequest.html)(
            parent="parent_value",
            replication=replication,
            replication_id="replication_id_value",
        )
    
        # Make the request
        operation = await client.[create_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateReplicationRequest), dict]]`   
The request object. CreateReplicationRequest creates a replication.  
`parent` |  ``str``   
Required. The NetApp volume to create the replications of, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`replication` |  `[Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication)`   
Required. A replication resource This corresponds to the `replication` field on the `request` instance; if `request` is provided, this should not be set.  
`replication_id` |  ``str``   
Required. ID of the replication to create. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `replication_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### create_snapshot
    
    
    create_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.CreateSnapshotRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
        snapshot_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a new snapshot for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_snapshot():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateSnapshotRequest.html)(
            parent="parent_value",
            snapshot_id="snapshot_id_value",
        )
    
        # Make the request
        operation = await client.[create_snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_snapshot)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateSnapshotRequest), dict]]`   
The request object. CreateSnapshotRequest creates a snapshot.  
`parent` |  ``str``   
Required. The NetApp volume to create the snapshots of, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`snapshot` |  `[Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot)`   
Required. A snapshot resource This corresponds to the `snapshot` field on the `request` instance; if `request` is provided, this should not be set.  
`snapshot_id` |  ``str``   
Required. ID of the snapshot to create. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `snapshot_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot) Snapshot is a point-in-time version of a Volume's content.  
  
### create_storage_pool
    
    
    create_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.CreateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
        ] = None,
        storage_pool_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new storage pool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_storage_pool():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        storage_pool = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool.html)()
        storage_pool.service_level = "FLEX"
        storage_pool.capacity_gib = 1247
        storage_pool.network = "network_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateStoragePoolRequest.html)(
            parent="parent_value",
            storage_pool_id="storage_pool_id_value",
            storage_pool=storage_pool,
        )
    
        # Make the request
        operation = await client.[create_storage_pool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_storage_pool)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateStoragePoolRequest), dict]]`   
The request object. CreateStoragePoolRequest creates a Storage Pool.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`storage_pool` |  `[StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool)`   
Required. The required parameters to create a new storage pool. This corresponds to the `storage_pool` field on the `request` instance; if `request` is provided, this should not be set.  
`storage_pool_id` |  ``str``   
Required. Id of the requesting storage pool. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `storage_pool_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool) StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.  
  
### create_volume
    
    
    create_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.CreateVolumeRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
        volume_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Volume in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_create_volume():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        volume = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume.html)()
        volume.share_name = "share_name_value"
        volume.storage_pool = "storage_pool_value"
        volume.capacity_gib = 1247
        volume.protocols = ['ISCSI']
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[CreateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateVolumeRequest.html)(
            parent="parent_value",
            volume_id="volume_id_value",
            volume=volume,
        )
    
        # Make the request
        operation = await client.[create_volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_volume)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.CreateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateVolumeRequest), dict]]`   
The request object. Message for creating a Volume  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`volume` |  `[Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume)`   
Required. The volume being created. This corresponds to the `volume` field on the `request` instance; if `request` is provided, this should not be set.  
`volume_id` |  ``str``   
Required. Id of the requesting volume. Must be unique within the parent resource. Must contain only letters, numbers and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum. This corresponds to the `volume_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume) Volume provides a filesystem that you can mount.  
  
### delete_active_directory
    
    
    delete_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.DeleteActiveDirectoryRequest,
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

Delete the active directory specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_active_directory():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteActiveDirectoryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_active_directory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_active_directory)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteActiveDirectoryRequest), dict]]`   
The request object. DeleteActiveDirectoryRequest for deleting a single active directory.  
`name` |  ``str``   
Required. Name of the active directory. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.DeleteBackupRequest, dict]
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

Warning! This operation will permanently delete the backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_backup():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupRequest), dict]]`   
The request object. DeleteBackupRequest deletes a backup.  
`name` |  ``str``   
Required. The backup resource name, in the format `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_backup_policy
    
    
    delete_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.DeleteBackupPolicyRequest, dict
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

Warning! This operation will permanently delete the backup policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_backup_policy():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_backup_policy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupPolicyRequest), dict]]`   
The request object. DeleteBackupPolicyRequest deletes a backup policy.  
`name` |  ``str``   
Required. The backup policy resource name, in the format `projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.DeleteBackupVaultRequest, dict
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

Warning! This operation will permanently delete the backup vault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_backup_vault():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupVaultRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_backup_vault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupVaultRequest), dict]]`   
The request object. DeleteBackupVaultRequest deletes a backupVault.  
`name` |  ``str``   
Required. The backupVault resource name, in the format `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_host_group
    
    
    delete_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.DeleteHostGroupRequest, dict
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

Deletes a host group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_host_group():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteHostGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_host_group](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_host_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteHostGroupRequest), dict]]`   
The request object. DeleteHostGroupRequest for deleting a single host group.  
`name` |  ``str``   
Required. The resource name of the host group. Format: `projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_kms_config
    
    
    delete_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.DeleteKmsConfigRequest, dict]
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

Warning! This operation will permanently delete the Kms config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_kms_config():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteKmsConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_kms_config](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_kms_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteKmsConfigRequest), dict]]`   
The request object. DeleteKmsConfigRequest deletes a KMS Config.  
`name` |  ``str``   
Required. Name of the KmsConfig. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_quota_rule
    
    
    delete_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.DeleteQuotaRuleRequest, dict
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

Deletes a quota rule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_quota_rule():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteQuotaRuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_quota_rule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_quota_rule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteQuotaRuleRequest), dict]]`   
The request object. DeleteQuotaRuleRequest for deleting a single quota rule.  
`name` |  ``str``   
Required. Name of the quota rule. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_replication
    
    
    delete_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.DeleteReplicationRequest, dict
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

Deletes a replication.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteReplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteReplicationRequest), dict]]`   
The request object. DeleteReplicationRequest deletes a replication.  
`name` |  ``str``   
Required. The replication resource name, in the format `projects/_/locations/_ /volumes/*/replications/{replication_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_snapshot
    
    
    delete_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.DeleteSnapshotRequest, dict]
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

Deletes a snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_snapshot():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteSnapshotRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_snapshot)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteSnapshotRequest), dict]]`   
The request object. DeleteSnapshotRequest deletes a snapshot.  
`name` |  ``str``   
Required. The snapshot resource name, in the format `projects/_/locations/_ /volumes/*/snapshots/{snapshot_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_storage_pool
    
    
    delete_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.DeleteStoragePoolRequest, dict
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

Warning! This operation will permanently delete the storage pool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_storage_pool():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteStoragePoolRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_storage_pool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_storage_pool)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteStoragePoolRequest), dict]]`   
The request object. DeleteStoragePoolRequest deletes a Storage Pool.  
`name` |  ``str``   
Required. Name of the storage pool This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_volume
    
    
    delete_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.DeleteVolumeRequest, dict]
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

Deletes a single Volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_delete_volume():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[DeleteVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteVolumeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_volume)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.DeleteVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteVolumeRequest), dict]]`   
The request object. Message for deleting a Volume  
`name` |  ``str``   
Required. Name of the volume This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### encrypt_volumes
    
    
    encrypt_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.EncryptVolumesRequest, dict]
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

Encrypt the existing volumes without CMEK encryption with the desired the KMS config for the whole region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_encrypt_volumes():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[EncryptVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EncryptVolumesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[encrypt_volumes](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_encrypt_volumes)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.EncryptVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EncryptVolumesRequest), dict]]`   
The request object. EncryptVolumesRequest specifies the KMS config to encrypt existing volumes.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig) KmsConfig is the customer-managed encryption key(CMEK) configuration.  
  
### establish_peering
    
    
    establish_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.EstablishPeeringRequest, dict
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

Establish replication peering.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_establish_peering():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[EstablishPeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishPeeringRequest.html)(
            name="name_value",
            peer_cluster_name="peer_cluster_name_value",
            peer_svm_name="peer_svm_name_value",
            peer_volume_name="peer_volume_name_value",
        )
    
        # Make the request
        operation = await client.[establish_peering](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_establish_peering)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.EstablishPeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishPeeringRequest), dict]]`   
The request object. EstablishPeeringRequest establishes cluster and svm peerings between the source and the destination replications.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### establish_volume_peering
    
    
    establish_volume_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.EstablishVolumePeeringRequest, dict
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

Establish volume peering. This is used to establish cluster and svm peerings between the GCNV and OnPrem clusters.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_establish_volume_peering():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[EstablishVolumePeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishVolumePeeringRequest.html)(
            name="name_value",
            peer_cluster_name="peer_cluster_name_value",
            peer_svm_name="peer_svm_name_value",
            peer_volume_name="peer_volume_name_value",
        )
    
        # Make the request
        operation = await client.[establish_volume_peering](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_establish_volume_peering)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.EstablishVolumePeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishVolumePeeringRequest), dict]]`   
The request object. EstablishVolumePeeringRequest establishes cluster and svm peerings between the source and destination clusters.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume) Volume provides a filesystem that you can mount.  
  
### execute_ontap_delete
    
    
    execute_ontap_delete(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteResponse

`ExecuteOntapDelete` dispatches the ONTAP `DELETE` request to the `StoragePool` cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_execute_ontap_delete():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ExecuteOntapDeleteRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapDeleteRequest.html)(
            ontap_path="ontap_path_value",
        )
    
        # Make the request
        response = await client.[execute_ontap_delete](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ExecuteOntapDeleteRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapDeleteRequest), dict]]`   
The request object. Request message for `ExecuteOntapDelete` API.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.ExecuteOntapDeleteResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapDeleteResponse)` | Response message for ExecuteOntapDelete API.  
  
### execute_ontap_get
    
    
    execute_ontap_get(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapGetRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapGetResponse

`ExecuteOntapGet` dispatches the ONTAP `GET` request to the `StoragePool` cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_execute_ontap_get():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ExecuteOntapGetRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapGetRequest.html)(
            ontap_path="ontap_path_value",
        )
    
        # Make the request
        response = await client.[execute_ontap_get](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ExecuteOntapGetRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapGetRequest), dict]]`   
The request object. Request message for `ExecuteOntapGet` API.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.ExecuteOntapGetResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapGetResponse)` | Response message for ExecuteOntapGet API.  
  
### execute_ontap_patch
    
    
    execute_ontap_patch(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchResponse

`ExecuteOntapPatch` dispatches the ONTAP `PATCH` request to the `StoragePool` cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_execute_ontap_patch():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ExecuteOntapPatchRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPatchRequest.html)(
            ontap_path="ontap_path_value",
        )
    
        # Make the request
        response = await client.[execute_ontap_patch](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ExecuteOntapPatchRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPatchRequest), dict]]`   
The request object. Request message for `ExecuteOntapPatch` API.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.ExecuteOntapPatchResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPatchResponse)` | Response message for ExecuteOntapPatch API.  
  
### execute_ontap_post
    
    
    execute_ontap_post(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPostRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPostResponse

`ExecuteOntapPost` dispatches the ONTAP `POST` request to the `StoragePool` cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_execute_ontap_post():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ExecuteOntapPostRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPostRequest.html)(
            ontap_path="ontap_path_value",
        )
    
        # Make the request
        response = await client.[execute_ontap_post](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_post)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ExecuteOntapPostRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPostRequest), dict]]`   
The request object. Request message for `ExecuteOntapPost` API.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.ExecuteOntapPostResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPostResponse)` | Response message for ExecuteOntapPost API.  
  
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
`NetAppAsyncClient` | The constructed client.  
  
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
`NetAppAsyncClient` | The constructed client.  
  
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
`NetAppAsyncClient` | The constructed client.  
  
### get_active_directory
    
    
    get_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.GetActiveDirectoryRequest,
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
    ) -> google.cloud.netapp_v1.types.active_directory.ActiveDirectory

Describes a specified active directory.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_active_directory():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetActiveDirectoryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_active_directory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_active_directory)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetActiveDirectoryRequest), dict]]`   
The request object. GetActiveDirectory for getting a single active directory.  
`name` |  ``str``   
Required. Name of the active directory. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory)` | ActiveDirectory is the public representation of the active directory config.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.GetBackupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.backup.Backup

Returns the description of the specified backup
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_backup():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupRequest), dict]]`   
The request object. GetBackupRequest gets the state of a backup.  
`name` |  ``str``   
Required. The backup resource name, in the format `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup)` | A NetApp Backup.  
  
### get_backup_policy
    
    
    get_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.GetBackupPolicyRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_policy.BackupPolicy

Returns the description of the specified backup policy by backup_policy_id.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_backup_policy():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_backup_policy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupPolicyRequest), dict]]`   
The request object. GetBackupPolicyRequest gets the state of a backupPolicy.  
`name` |  ``str``   
Required. The backupPolicy resource name, in the format `projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy)` | Backup Policy.  
  
### get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_vault.BackupVault

Returns the description of the specified backup vault
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_backup_vault():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupVaultRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_backup_vault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup_vault)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupVaultRequest), dict]]`   
The request object. GetBackupVaultRequest gets the state of a backupVault.  
`name` |  ``str``   
Required. The backupVault resource name, in the format `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault)` | A NetApp BackupVault.  
  
### get_host_group
    
    
    get_host_group(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.host_group.GetHostGroupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.host_group.HostGroup

Returns details of the specified host group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_host_group():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetHostGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_host_group](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_host_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetHostGroupRequest), dict]]`   
The request object. GetHostGroupRequest for getting a host group.  
`name` |  ``str``   
Required. The resource name of the host group. Format: `projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup)` | Host group is a collection of hosts that can be used for accessing a Block Volume.  
  
### get_kms_config
    
    
    get_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.GetKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.KmsConfig

Returns the description of the specified KMS config by kms_config_id.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_kms_config():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetKmsConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_kms_config](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_kms_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetKmsConfigRequest), dict]]`   
The request object. GetKmsConfigRequest gets a KMS Config.  
`name` |  ``str``   
Required. Name of the KmsConfig This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig)` | KmsConfig is the customer-managed encryption key(CMEK) configuration.  
  
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
  
### get_quota_rule
    
    
    get_quota_rule(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.quota_rule.GetQuotaRuleRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.quota_rule.QuotaRule

Returns details of the specified quota rule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_quota_rule():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetQuotaRuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_quota_rule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_quota_rule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetQuotaRuleRequest), dict]]`   
The request object. GetQuotaRuleRequest for getting a quota rule.  
`name` |  ``str``   
Required. Name of the quota rule This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule)` | QuotaRule specifies the maximum disk space a user or group can use within a volume. They can be used for creating default and individual quota rules.  
  
### get_replication
    
    
    get_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.GetReplicationRequest, dict
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
    ) -> google.cloud.netapp_v1.types.replication.Replication

Describe a replication for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetReplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_replication)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetReplicationRequest), dict]]`   
The request object. GetReplicationRequest gets the state of a replication.  
`name` |  ``str``   
Required. The replication resource name, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication)` | Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### get_snapshot
    
    
    get_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.GetSnapshotRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.snapshot.Snapshot

Describe a snapshot for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_snapshot():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetSnapshotRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_snapshot)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetSnapshotRequest), dict]]`   
The request object. GetSnapshotRequest gets the state of a snapshot.  
`name` |  ``str``   
Required. The snapshot resource name, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot)` | Snapshot is a point-in-time version of a Volume's content.  
  
### get_storage_pool
    
    
    get_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.GetStoragePoolRequest, dict
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
    ) -> google.cloud.netapp_v1.types.storage_pool.StoragePool

Returns the description of the specified storage pool by poolId.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_storage_pool():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetStoragePoolRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_storage_pool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_storage_pool)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetStoragePoolRequest), dict]]`   
The request object. GetStoragePoolRequest gets a Storage Pool.  
`name` |  ``str``   
Required. Name of the storage pool This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool)` | StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### get_volume
    
    
    get_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.GetVolumeRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.volume.Volume

Gets details of a single Volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_get_volume():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[GetVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetVolumeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_volume)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.GetVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetVolumeRequest), dict]]`   
The request object. Message for getting a Volume  
`name` |  ``str``   
Required. Name of the volume This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume)` | Volume provides a filesystem that you can mount.  
  
### host_group_path
    
    
    host_group_path(project: str, location: str, host_group: str) -> str

Returns a fully-qualified host_group string.

### kms_config_path
    
    
    kms_config_path(project: str, location: str, kms_config: str) -> str

Returns a fully-qualified kms_config string.

### list_active_directories
    
    
    list_active_directories(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager

Lists active directories.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_active_directories():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListActiveDirectoriesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_active_directories](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_active_directories)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListActiveDirectoriesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesRequest), dict]]`   
The request object. ListActiveDirectoriesRequest for requesting multiple active directories.  
`parent` |  ``str``   
Required. Parent value for ListActiveDirectoriesRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager)` | ListActiveDirectoriesResponse contains all the active directories requested. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_policies
    
    
    list_backup_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager

Returns list of all available backup policies.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_backup_policies():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListBackupPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_policies](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backup_policies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListBackupPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesRequest), dict]]`   
The request object. ListBackupPoliciesRequest for requesting multiple backup policies.  
`parent` |  ``str``   
Required. Parent value for ListBackupPoliciesRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager)` | ListBackupPoliciesResponse contains all the backup policies requested. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager

Returns list of all available backup vaults.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_backup_vaults():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_vaults](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backup_vaults)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsRequest), dict]]`   
The request object. ListBackupVaultsRequest lists backupVaults.  
`parent` |  ``str``   
Required. The location for which to retrieve backupVault information, in the format `projects/{project_id}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager)` | ListBackupVaultsResponse is the result of ListBackupVaultsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.ListBackupsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager

Returns descriptions of all backups for a backupVault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_backups():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backups](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsRequest), dict]]`   
The request object. ListBackupsRequest lists backups.  
`parent` |  ``str``   
Required. The backupVault for which to retrieve backup information, in the format `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}`. To retrieve backup information for all locations, use "-" for the `{location}` value. To retrieve backup information for all backupVaults, use "-" for the `{backup_vault_id}` value. To retrieve backup information for a volume, use "-" for the `{backup_vault_id}` value and specify volume full name with the filter. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager)` | ListBackupsResponse is the result of ListBackupsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_host_groups
    
    
    list_host_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager

Returns a list of host groups in a `location`. Use `-` as location to list host groups across all locations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_host_groups():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListHostGroupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_host_groups](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_host_groups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListHostGroupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsRequest), dict]]`   
The request object. ListHostGroupsRequest for listing host groups.  
`parent` |  ``str``   
Required. Parent value for ListHostGroupsRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager)` | ListHostGroupsResponse is the response to a ListHostGroupsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_kms_configs
    
    
    list_kms_configs(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager

Returns descriptions of all KMS configs owned by the caller.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_kms_configs():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListKmsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_kms_configs](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_kms_configs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListKmsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsRequest), dict]]`   
The request object. ListKmsConfigsRequest lists KMS Configs.  
`parent` |  ``str``   
Required. Parent value This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager)` | ListKmsConfigsResponse is the response to a ListKmsConfigsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_quota_rules
    
    
    list_quota_rules(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager

Returns list of all quota rules in a location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_quota_rules():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListQuotaRulesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_quota_rules](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_quota_rules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListQuotaRulesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesRequest), dict]]`   
The request object. ListQuotaRulesRequest for listing quota rules.  
`parent` |  ``str``   
Required. Parent value for ListQuotaRulesRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager)` | ListQuotaRulesResponse is the response to a ListQuotaRulesRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_replications
    
    
    list_replications(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ListReplicationsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager

Returns descriptions of all replications for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_replications():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListReplicationsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_replications](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_replications)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListReplicationsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsRequest), dict]]`   
The request object. ListReplications lists replications.  
`parent` |  ``str``   
Required. The volume for which to retrieve replication information, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager)` | ListReplicationsResponse is the result of ListReplicationsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_snapshots
    
    
    list_snapshots(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager

Returns descriptions of all snapshots for a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_snapshots():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListSnapshotsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_snapshots](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_snapshots)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListSnapshotsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsRequest), dict]]`   
The request object. ListSnapshotsRequest lists snapshots.  
`parent` |  ``str``   
Required. The volume for which to retrieve snapshot information, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager)` | ListSnapshotsResponse is the result of ListSnapshotsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_storage_pools
    
    
    list_storage_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager

Returns descriptions of all storage pools owned by the caller.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_storage_pools():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListStoragePoolsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_storage_pools](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_storage_pools)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListStoragePoolsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsRequest), dict]]`   
The request object. ListStoragePoolsRequest lists Storage Pools.  
`parent` |  ``str``   
Required. Parent value This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager)` | ListStoragePoolsResponse is the response to a ListStoragePoolsRequest. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_volumes
    
    
    list_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.ListVolumesRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager

Lists Volumes in a given project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_list_volumes():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ListVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_volumes](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_volumes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ListVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesRequest), dict]]`   
The request object. Message for requesting list of Volumes  
`parent` |  ``str``   
Required. Parent value for ListVolumesRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager)` | Message for response to listing Volumes Iterating over this object will yield results and resolve additional pages automatically.  
  
### network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

### parse_active_directory_path
    
    
    parse_active_directory_path(path: str) -> typing.Dict[str, str]

Parses a active_directory path into its component segments.

### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

### parse_backup_policy_path
    
    
    parse_backup_policy_path(path: str) -> typing.Dict[str, str]

Parses a backup_policy path into its component segments.

### parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

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

### parse_host_group_path
    
    
    parse_host_group_path(path: str) -> typing.Dict[str, str]

Parses a host_group path into its component segments.

### parse_kms_config_path
    
    
    parse_kms_config_path(path: str) -> typing.Dict[str, str]

Parses a kms_config path into its component segments.

### parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

### parse_quota_rule_path
    
    
    parse_quota_rule_path(path: str) -> typing.Dict[str, str]

Parses a quota_rule path into its component segments.

### parse_replication_path
    
    
    parse_replication_path(path: str) -> typing.Dict[str, str]

Parses a replication path into its component segments.

### parse_snapshot_path
    
    
    parse_snapshot_path(path: str) -> typing.Dict[str, str]

Parses a snapshot path into its component segments.

### parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

### parse_volume_path
    
    
    parse_volume_path(path: str) -> typing.Dict[str, str]

Parses a volume path into its component segments.

### quota_rule_path
    
    
    quota_rule_path(project: str, location: str, volume: str, quota_rule: str) -> str

Returns a fully-qualified quota_rule string.

### replication_path
    
    
    replication_path(project: str, location: str, volume: str, replication: str) -> str

Returns a fully-qualified replication string.

### restore_backup_files
    
    
    restore_backup_files(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.RestoreBackupFilesRequest, dict
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

Restore files from a backup to a volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_restore_backup_files():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[RestoreBackupFilesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreBackupFilesRequest.html)(
            name="name_value",
            backup="backup_value",
            file_list=['file_list_value1', 'file_list_value2'],
        )
    
        # Make the request
        operation = await client.[restore_backup_files](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_restore_backup_files)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.RestoreBackupFilesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreBackupFilesRequest), dict]]`   
The request object. RestoreBackupFilesRequest restores files from a backup to a volume.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [RestoreBackupFilesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreBackupFilesResponse) RestoreBackupFilesResponse is the result of RestoreBackupFilesRequest.  
  
### resume_replication
    
    
    resume_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ResumeReplicationRequest, dict
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

Resume Cross Region Replication.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_resume_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ResumeReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ResumeReplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[resume_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_resume_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ResumeReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ResumeReplicationRequest), dict]]`   
The request object. ResumeReplicationRequest resumes a stopped replication.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### reverse_replication_direction
    
    
    reverse_replication_direction(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ReverseReplicationDirectionRequest,
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

Reverses direction of replication. Source becomes destination and destination becomes source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_reverse_replication_direction():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ReverseReplicationDirectionRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ReverseReplicationDirectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[reverse_replication_direction](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_reverse_replication_direction)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ReverseReplicationDirectionRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ReverseReplicationDirectionRequest), dict]]`   
The request object. ReverseReplicationDirectionRequest reverses direction of replication. Source becomes destination and destination becomes source.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### revert_volume
    
    
    revert_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.RevertVolumeRequest, dict]
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

Revert an existing volume to a specified snapshot. Warning! This operation will permanently revert all changes made after the snapshot was created.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_revert_volume():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[RevertVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RevertVolumeRequest.html)(
            name="name_value",
            snapshot_id="snapshot_id_value",
        )
    
        # Make the request
        operation = await client.[revert_volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_revert_volume)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.RevertVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RevertVolumeRequest), dict]]`   
The request object. RevertVolumeRequest reverts the given volume to the specified snapshot.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume) Volume provides a filesystem that you can mount.  
  
### snapshot_path
    
    
    snapshot_path(project: str, location: str, volume: str, snapshot: str) -> str

Returns a fully-qualified snapshot string.

### stop_replication
    
    
    stop_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.StopReplicationRequest, dict
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

Stop Cross Region Replication.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_stop_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[StopReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StopReplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[stop_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_stop_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.StopReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StopReplicationRequest), dict]]`   
The request object. StopReplicationRequest stops a replication until resumed.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### storage_pool_path
    
    
    storage_pool_path(project: str, location: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

### switch_active_replica_zone
    
    
    switch_active_replica_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.SwitchActiveReplicaZoneRequest,
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

This operation will switch the active/replica zone for a regional storagePool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_switch_active_replica_zone():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SwitchActiveReplicaZoneRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[switch_active_replica_zone](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_switch_active_replica_zone)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SwitchActiveReplicaZoneRequest), dict]]`   
The request object. SwitchActiveReplicaZoneRequest switch the active/replica zone for a regional storagePool.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool) StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.  
  
### sync_replication
    
    
    sync_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.SyncReplicationRequest, dict
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

Syncs the replication. This will invoke one time volume data transfer from source to destination.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_sync_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[SyncReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SyncReplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[sync_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_sync_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.SyncReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SyncReplicationRequest), dict]]`   
The request object. SyncReplicationRequest syncs the replication from source to destination.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### update_active_directory
    
    
    update_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.UpdateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
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

Update the parameters of an active directories.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_active_directory():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        active_directory = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory.html)()
        active_directory.domain = "domain_value"
        active_directory.dns = "dns_value"
        active_directory.net_bios_prefix = "net_bios_prefix_value"
        active_directory.username = "username_value"
        active_directory.password = "password_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateActiveDirectoryRequest.html)(
            active_directory=active_directory,
        )
    
        # Make the request
        operation = await client.[update_active_directory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_active_directory)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateActiveDirectoryRequest), dict]]`   
The request object. UpdateActiveDirectoryRequest for updating an active directory.  
`active_directory` |  `[ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory)`   
Required. The volume being updated This corresponds to the `active_directory` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the Active Directory resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory) ActiveDirectory is the public representation of the active directory config.  
  
### update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.UpdateBackupRequest, dict]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
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

Update backup with full spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_backup():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupRequest), dict]]`   
The request object. UpdateBackupRequest updates description and/or labels for a backup.  
`backup` |  `[Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup)`   
Required. The backup being updated This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the Backup resource to be updated. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup) A NetApp Backup.  
  
### update_backup_policy
    
    
    update_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.UpdateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
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

Updates settings of a specific backup policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_backup_policy():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupPolicyRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_backup_policy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupPolicyRequest), dict]]`   
The request object. UpdateBackupPolicyRequest for updating a backup policy.  
`backup_policy` |  `[BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy)`   
Required. The backup policy being updated This corresponds to the `backup_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the Backup Policy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy) Backup Policy.  
  
### update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
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

Updates the settings of a specific backup vault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_backup_vault():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupVaultRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_backup_vault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupVaultRequest), dict]]`   
The request object. UpdateBackupVaultRequest updates description and/or labels for a backupVault.  
`backup_vault` |  `[BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault)`   
Required. The backupVault being updated This corresponds to the `backup_vault` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the Backup resource to be updated. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault) A NetApp BackupVault.  
  
### update_host_group
    
    
    update_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.UpdateHostGroupRequest, dict
            ]
        ] = None,
        *,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
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

Updates an existing host group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_host_group():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        host_group = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup.html)()
        host_group.type_ = "ISCSI_INITIATOR"
        host_group.hosts = ['hosts_value1', 'hosts_value2']
        host_group.os_type = "ESXI"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateHostGroupRequest.html)(
            host_group=host_group,
        )
    
        # Make the request
        operation = await client.[update_host_group](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_host_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateHostGroupRequest), dict]]`   
The request object. UpdateHostGroupRequest for updating a host group.  
`host_group` |  `[HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup)`   
Required. The host group to update. The host group's `name` field is used to identify the host group. Format: `projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}`. This corresponds to the `host_group` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup) Host group is a collection of hosts that can be used for accessing a Block Volume.  
  
### update_kms_config
    
    
    update_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.UpdateKmsConfigRequest, dict]
        ] = None,
        *,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
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

Updates the Kms config properties with the full spec
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_kms_config():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        kms_config = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig.html)()
        kms_config.crypto_key_name = "crypto_key_name_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateKmsConfigRequest.html)(
            kms_config=kms_config,
        )
    
        # Make the request
        operation = await client.[update_kms_config](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_kms_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateKmsConfigRequest), dict]]`   
The request object. UpdateKmsConfigRequest updates a KMS Config.  
`kms_config` |  `[KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig)`   
Required. The KmsConfig being updated This corresponds to the `kms_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the KmsConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig) KmsConfig is the customer-managed encryption key(CMEK) configuration.  
  
### update_quota_rule
    
    
    update_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.UpdateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
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

Updates a quota rule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_quota_rule():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        quota_rule = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule.html)()
        quota_rule.type_ = "DEFAULT_GROUP_QUOTA"
        quota_rule.disk_limit_mib = 1472
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateQuotaRuleRequest.html)(
            quota_rule=quota_rule,
        )
    
        # Make the request
        operation = await client.[update_quota_rule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_quota_rule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateQuotaRuleRequest), dict]]`   
The request object. UpdateQuotaRuleRequest for updating a quota rule.  
`quota_rule` |  `[QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule)`   
Required. The quota rule being updated This corresponds to the `quota_rule` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the Quota Rule resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule) QuotaRule specifies the maximum disk space a user or group can use within a volume. They can be used for creating default and individual quota rules.  
  
### update_replication
    
    
    update_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.UpdateReplicationRequest, dict
            ]
        ] = None,
        *,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
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

Updates the settings of a specific replication.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_replication():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        replication = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication.html)()
        replication.replication_schedule = "DAILY"
        replication.destination_volume_parameters.storage_pool = "storage_pool_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateReplicationRequest.html)(
            replication=replication,
        )
    
        # Make the request
        operation = await client.[update_replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_replication)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateReplicationRequest), dict]]`   
The request object. UpdateReplicationRequest updates description and/or labels for a replication.  
`replication` |  `[Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication)`   
Required. A replication resource This corresponds to the `replication` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Mask of fields to update. At least one path must be supplied in this field. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication) Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.  
  
### update_snapshot
    
    
    update_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.UpdateSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
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

Updates the settings of a specific snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_snapshot():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateSnapshotRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_snapshot)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateSnapshotRequest), dict]]`   
The request object. UpdateSnapshotRequest updates description and/or labels for a snapshot.  
`snapshot` |  `[Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot)`   
Required. A snapshot resource This corresponds to the `snapshot` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Mask of fields to update. At least one path must be supplied in this field. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot) Snapshot is a point-in-time version of a Volume's content.  
  
### update_storage_pool
    
    
    update_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.UpdateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
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

Updates the storage pool properties with the full spec
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_storage_pool():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        storage_pool = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool.html)()
        storage_pool.service_level = "FLEX"
        storage_pool.capacity_gib = 1247
        storage_pool.network = "network_value"
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateStoragePoolRequest.html)(
            storage_pool=storage_pool,
        )
    
        # Make the request
        operation = await client.[update_storage_pool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_storage_pool)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateStoragePoolRequest), dict]]`   
The request object. UpdateStoragePoolRequest updates a Storage Pool.  
`storage_pool` |  `[StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool)`   
Required. The pool being updated This corresponds to the `storage_pool` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the StoragePool resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool) StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.  
  
### update_volume
    
    
    update_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.UpdateVolumeRequest, dict]
        ] = None,
        *,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
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

Updates the parameters of a single Volume.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_update_volume():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        volume = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume.html)()
        volume.share_name = "share_name_value"
        volume.storage_pool = "storage_pool_value"
        volume.capacity_gib = 1247
        volume.protocols = ['ISCSI']
    
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[UpdateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateVolumeRequest.html)(
            volume=volume,
        )
    
        # Make the request
        operation = await client.[update_volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_volume)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.UpdateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateVolumeRequest), dict]]`   
The request object. Message for updating a Volume  
`volume` |  `[Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume)`   
Required. The volume being updated This corresponds to the `volume` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the Volume resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume) Volume provides a filesystem that you can mount.  
  
### validate_directory_service
    
    
    validate_directory_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ValidateDirectoryServiceRequest,
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

ValidateDirectoryService does a connectivity check for a directory service policy attached to the storage pool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_validate_directory_service():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[ValidateDirectoryServiceRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ValidateDirectoryServiceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[validate_directory_service](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_validate_directory_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.ValidateDirectoryServiceRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ValidateDirectoryServiceRequest), dict]]`   
The request object. ValidateDirectoryServiceRequest validates the directory service policy attached to the storage pool.  
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
  
### verify_kms_config
    
    
    verify_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.VerifyKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.VerifyKmsConfigResponse

Verifies KMS config reachability.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest)
    
    async def sample_verify_kms_config():
        # Create a client
        client = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[NetAppAsyncClient](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [netapp_v1](https://docs.cloud.google.com/python/docs/reference/netapp/latest).[VerifyKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.VerifyKmsConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[verify_kms_config](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.html#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_verify_kms_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.netapp_v1.types.VerifyKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.VerifyKmsConfigRequest), dict]]`   
The request object. VerifyKmsConfigRequest specifies the KMS config to be validated.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.netapp_v1.types.VerifyKmsConfigResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.VerifyKmsConfigResponse)` | VerifyKmsConfigResponse contains the information if the config is correctly and error message.  
  
### volume_path
    
    
    volume_path(project: str, location: str, volume: str) -> str

Returns a fully-qualified volume string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
