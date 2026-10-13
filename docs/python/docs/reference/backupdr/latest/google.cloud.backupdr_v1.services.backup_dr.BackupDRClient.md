---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient
title: Class BackupDRClient (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:42.712497+00:00
---

# Class BackupDRClient (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupDRClient (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupDRClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The BackupDR Service

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
`BackupDRTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### BackupDRClient
    
    
    BackupDRClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,BackupDRTransport,Callable[..., BackupDRTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the BackupDRTransport constructor. If set to None, a transport is chosen automatically.  
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

### backup_path
    
    
    backup_path(
        project: str, location: str, backupvault: str, datasource: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

### backup_plan_association_path
    
    
    backup_plan_association_path(
        project: str, location: str, backup_plan_association: str
    ) -> str

Returns a fully-qualified backup_plan_association string.

### backup_plan_path
    
    
    backup_plan_path(project: str, location: str, backup_plan: str) -> str

Returns a fully-qualified backup_plan string.

### backup_plan_revision_path
    
    
    backup_plan_revision_path(
        project: str, location: str, backup_plan: str, revision: str
    ) -> str

Returns a fully-qualified backup_plan_revision string.

### backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backupvault: str) -> str

Returns a fully-qualified backup_vault string.

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
  
### cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

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

### create_backup_plan
    
    
    create_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.CreateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
        ] = None,
        backup_plan_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlan
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_create_backup_plan():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        backup_plan = backupdr_v1.[BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan.html)()
        backup_plan.backup_rules.standard_schedule.recurrence_type = "YEARLY"
        backup_plan.backup_rules.standard_schedule.backup_window.start_hour_of_day = 1820
        backup_plan.backup_rules.standard_schedule.backup_window.end_hour_of_day = 1573
        backup_plan.backup_rules.standard_schedule.time_zone = "time_zone_value"
        backup_plan.backup_rules.rule_id = "rule_id_value"
        backup_plan.backup_rules.backup_retention_days = 2237
        backup_plan.resource_type = "resource_type_value"
        backup_plan.backup_vault = "backup_vault_value"
    
        request = backupdr_v1.[CreateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanRequest.html)(
            parent="parent_value",
            backup_plan_id="backup_plan_id_value",
            backup_plan=backup_plan,
        )
    
        # Make the request
        operation = client.[create_backup_plan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_plan)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.CreateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanRequest), dict]`   
The request object. The request message for creating a `BackupPlan`.  
`parent` |  `str`   
Required. The `BackupPlan` project and location in the format `projects/{project}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_plan` |  `[google.cloud.backupdr_v1.types.BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan)`   
Required. The `BackupPlan` resource object to create. This corresponds to the `backup_plan` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_plan_id` |  `str`   
Required. The name of the `BackupPlan` to create. The name must be unique for the specified project and location.The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /`a-z][a-z0-9-]`{,62}/. This corresponds to the `backup_plan_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan) A BackupPlan specifies some common fields, such as description as well as one or more BackupRule messages. Each BackupRule has a retention policy and defines a schedule by which the system is to perform backup workloads.  
  
### create_backup_plan_association
    
    
    create_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.CreateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlanAssociation
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_create_backup_plan_association():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        backup_plan_association = backupdr_v1.[BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation.html)()
        backup_plan_association.resource_type = "resource_type_value"
        backup_plan_association.resource = "resource_value"
        backup_plan_association.backup_plan = "backup_plan_value"
    
        request = backupdr_v1.[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest.html)(
            parent="parent_value",
            backup_plan_association_id="backup_plan_association_id_value",
            backup_plan_association=backup_plan_association,
        )
    
        # Make the request
        operation = client.[create_backup_plan_association](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_plan_association)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest), dict]`   
The request object. Request message for creating a backup plan.  
`parent` |  `str`   
Required. The backup plan association project and location in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_plan_association` |  `[google.cloud.backupdr_v1.types.BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation)`   
Required. The resource being created This corresponds to the `backup_plan_association` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_plan_association_id` |  `str`   
Required. The name of the backup plan association to create. The name must be unique for the specified project and location. This corresponds to the `backup_plan_association_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation) A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc  
  
### create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new BackupVault in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_create_backup_vault():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupVaultRequest.html)(
            parent="parent_value",
            backup_vault_id="backup_vault_id_value",
        )
    
        # Make the request
        operation = client.[create_backup_vault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupVaultRequest), dict]`   
The request object. Message for creating a BackupVault.  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_vault` |  `[google.cloud.backupdr_v1.types.BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault)`   
Required. The resource being created This corresponds to the `backup_vault` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_vault_id` |  `str`   
Required. ID of the requesting object If auto-generating ID server-side, remove this field and backup_vault_id from the method_signature of Create RPC This corresponds to the `backup_vault_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault) Message describing a BackupVault object.  
  
### create_management_server
    
    
    create_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.CreateManagementServerRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        management_server: typing.Optional[
            google.cloud.backupdr_v1.types.backupdr.ManagementServer
        ] = None,
        management_server_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new ManagementServer in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_create_management_server():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[CreateManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateManagementServerRequest.html)(
            parent="parent_value",
            management_server_id="management_server_id_value",
        )
    
        # Make the request
        operation = client.[create_management_server](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_management_server)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.CreateManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateManagementServerRequest), dict]`   
The request object. Request message for creating a management server instance.  
`parent` |  `str`   
Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`management_server` |  `[google.cloud.backupdr_v1.types.ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer)`   
Required. A [management server resource][google.cloud.backupdr.v1.ManagementServer] This corresponds to the `management_server` field on the `request` instance; if `request` is provided, this should not be set.  
`management_server_id` |  `str`   
Required. The name of the management server to create. The name must be unique for the specified project and location. This corresponds to the `management_server_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer) ManagementServer describes a single BackupDR ManagementServer instance.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, ring: str, key: str) -> str

Returns a fully-qualified crypto_key string.

### crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

### data_source_path
    
    
    data_source_path(
        project: str, location: str, backupvault: str, datasource: str
    ) -> str

Returns a fully-qualified data_source string.

### data_source_reference_path
    
    
    data_source_reference_path(
        project: str, location: str, data_source_reference: str
    ) -> str

Returns a fully-qualified data_source_reference string.

### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupRequest, dict
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

Deletes a Backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_delete_backup():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupRequest), dict]`   
The request object. Message for deleting a Backup.  
`name` |  `str`   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup) Message describing a Backup object.  
  
### delete_backup_plan
    
    
    delete_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.DeleteBackupPlanRequest, dict
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

Deletes a single BackupPlan.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_delete_backup_plan():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[DeleteBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_backup_plan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_plan)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.DeleteBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanRequest), dict]`   
The request object. The request message for deleting a `BackupPlan`.  
`name` |  `str`   
Required. The resource name of the `BackupPlan` to delete. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_backup_plan_association
    
    
    delete_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.DeleteBackupPlanAssociationRequest,
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

Deletes a single BackupPlanAssociation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_delete_backup_plan_association():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_backup_plan_association](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_plan_association)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest), dict]`   
The request object. Request message for deleting a backup plan association.  
`name` |  `str`   
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupVaultRequest, dict
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

Deletes a BackupVault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_delete_backup_vault():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupVaultRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_backup_vault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupVaultRequest), dict]`   
The request object. Message for deleting a BackupVault.  
`name` |  `str`   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_management_server
    
    
    delete_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.DeleteManagementServerRequest, dict
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

Deletes a single ManagementServer.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_delete_management_server():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[DeleteManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteManagementServerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_management_server](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_management_server)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.DeleteManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteManagementServerRequest), dict]`   
The request object. Request message for deleting a management server instance.  
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
  
### fetch_backup_plan_associations_for_resource_type
    
    
    fetch_backup_plan_associations_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager
    )

List BackupPlanAssociations for a given resource type.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_fetch_backup_plan_associations_for_resource_type():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest.html)(
            parent="parent_value",
            resource_type="resource_type_value",
        )
    
        # Make the request
        page_result = client.[fetch_backup_plan_associations_for_resource_type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_backup_plan_associations_for_resource_type)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest), dict]`   
The request object. Request for the FetchBackupPlanAssociationsForResourceType method.  
`parent` |  `str`   
Required. The parent resource name. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`resource_type` |  `str`   
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance This corresponds to the `resource_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager)` | Response for the FetchBackupPlanAssociationsForResourceType method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_backups_for_resource_type
    
    
    fetch_backups_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager
    )

Fetch Backups for a given resource type.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_fetch_backups_for_resource_type():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest.html)(
            parent="parent_value",
            resource_type="resource_type_value",
        )
    
        # Make the request
        page_result = client.[fetch_backups_for_resource_type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_backups_for_resource_type)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest), dict]`   
The request object. Request for the FetchBackupsForResourceType method.  
`parent` |  `str`   
Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`resource_type` |  `str`   
Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance This corresponds to the `resource_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager)` | Response for the FetchBackupsForResourceType method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_data_source_references_for_resource_type
    
    
    fetch_data_source_references_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager
    )

Fetch DataSourceReferences for a given project, location and resource type.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_fetch_data_source_references_for_resource_type():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest.html)(
            parent="parent_value",
            resource_type="resource_type_value",
        )
    
        # Make the request
        page_result = client.[fetch_data_source_references_for_resource_type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_data_source_references_for_resource_type)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest), dict]`   
The request object. Request for the FetchDataSourceReferencesForResourceType method.  
`parent` |  `str`   
Required. The parent resource name. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`resource_type` |  `str`   
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance This corresponds to the `resource_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager)` | Response for the FetchDataSourceReferencesForResourceType method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_usable_backup_vaults
    
    
    fetch_usable_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_fetch_usable_backup_vaults():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[fetch_usable_backup_vaults](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_usable_backup_vaults)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest), dict]`   
The request object. Request message for fetching usable BackupVaults.  
`parent` |  `str`   
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager)` | Response message for fetching usable BackupVaults. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
`BackupDRClient` | The constructed client.  
  
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
`BackupDRClient` | The constructed client.  
  
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
`BackupDRClient` | The constructed client.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.backupdr_v1.types.backupvault.GetBackupRequest, dict]
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
    ) -> google.cloud.backupdr_v1.types.backupvault.Backup

Gets details of a Backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_backup():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupRequest), dict]`   
The request object. Request message for getting a Backup.  
`name` |  `str`   
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}' This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup)` | Message describing a Backup object.  
  
### get_backup_plan
    
    
    get_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlan

Gets details of a single BackupPlan.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_backup_plan():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup_plan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRequest), dict]`   
The request object. The request message for getting a `BackupPlan`.  
`name` |  `str`   
Required. The resource name of the `BackupPlan` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan)` | A BackupPlan specifies some common fields, such as description as well as one or more BackupRule messages. Each BackupRule has a retention policy and defines a schedule by which the system is to perform backup workloads.  
  
### get_backup_plan_association
    
    
    get_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.GetBackupPlanAssociationRequest,
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
    ) -> google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation

Gets details of a single BackupPlanAssociation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_backup_plan_association():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup_plan_association](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan_association)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest), dict]`   
The request object. Request message for getting a BackupPlanAssociation resource.  
`name` |  `str`   
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation)` | A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc  
  
### get_backup_plan_revision
    
    
    get_backup_plan_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRevisionRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlanRevision

Gets details of a single BackupPlanRevision.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_backup_plan_revision():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetBackupPlanRevisionRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup_plan_revision](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest), dict]`   
The request object. The request message for getting a `BackupPlanRevision`.  
`name` |  `str`   
Required. The resource name of the `BackupPlanRevision` to retrieve. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.BackupPlanRevision](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision)` | BackupPlanRevision represents a snapshot of a BackupPlan at a point in time.  
  
### get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.BackupVault

Gets details of a BackupVault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_backup_vault():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupVaultRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup_vault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_vault)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupVaultRequest), dict]`   
The request object. Request message for getting a BackupVault.  
`name` |  `str`   
Required. Name of the backupvault store resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}' This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault)` | Message describing a BackupVault object.  
  
### get_data_source
    
    
    get_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetDataSourceRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.DataSource

Gets details of a DataSource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_data_source():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_data_source](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_data_source)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceRequest), dict]`   
The request object. Request message for getting a DataSource instance.  
`name` |  `str`   
Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}' This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource)` | Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.  
  
### get_data_source_reference
    
    
    get_data_source_reference(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.GetDataSourceReferenceRequest,
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
    ) -> google.cloud.backupdr_v1.types.datasourcereference.DataSourceReference

Gets details of a single DataSourceReference.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_data_source_reference():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetDataSourceReferenceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_data_source_reference](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_data_source_reference)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest), dict]`   
The request object. Request for the GetDataSourceReference method.  
`name` |  `str`   
Required. The name of the DataSourceReference to retrieve. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.DataSourceReference](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceReference)` | DataSourceReference is a reference to a DataSource resource.  
  
### get_iam_policy
    
    
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

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
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
  
### get_management_server
    
    
    get_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.GetManagementServerRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupdr.ManagementServer

Gets details of a single ManagementServer.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_get_management_server():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[GetManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetManagementServerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_management_server](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_management_server)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.GetManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetManagementServerRequest), dict]`   
The request object. Request message for getting a management server instance.  
`name` |  `str`   
Required. Name of the management server resource name, in the format 'projects/{project_id}/locations/{location}/managementServers/{resource_name}' This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.types.ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer)` | ManagementServer describes a single BackupDR ManagementServer instance.  
  
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
  
### initialize_service
    
    
    initialize_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.InitializeServiceRequest, dict
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

Initializes the service related config for a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_initialize_service():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        cloud_sql_instance_initialization_config = backupdr_v1.[CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig.html)()
        cloud_sql_instance_initialization_config.edition = "ENTERPRISE_PLUS"
    
        request = backupdr_v1.[InitializeServiceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceRequest.html)(
            cloud_sql_instance_initialization_config=cloud_sql_instance_initialization_config,
            name="name_value",
            resource_type="resource_type_value",
        )
    
        # Make the request
        operation = client.[initialize_service](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_initialize_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.InitializeServiceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceRequest), dict]`   
The request object. Request message for initializing the service.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [InitializeServiceResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceResponse) Response message for initializing the service.  
  
### instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

### list_backup_plan_associations
    
    
    list_backup_plan_associations(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager

Lists BackupPlanAssociations in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_backup_plan_associations():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_plan_associations](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plan_associations)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest), dict]`   
The request object. Request message for List BackupPlanAssociation  
`parent` |  `str`   
Required. The project and location for which to retrieve backup Plan Associations information, in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for example **us-central1**. To retrieve backup plan associations for all locations, use "-" for the `{location}` value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager)` | Response message for List BackupPlanAssociation Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_plan_revisions
    
    
    list_backup_plan_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager

Lists BackupPlanRevisions in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_backup_plan_revisions():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_plan_revisions](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plan_revisions)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest), dict]`   
The request object. The request message for getting a list of `BackupPlanRevision`.  
`parent` |  `str`   
Required. The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager)` | The response message for getting a list of BackupPlanRevision. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_plans
    
    
    list_backup_plans(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager

Lists BackupPlans in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_backup_plans():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListBackupPlansRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_plans](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plans)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListBackupPlansRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansRequest), dict]`   
The request object. The request message for getting a list `BackupPlan`.  
`parent` |  `str`   
Required. The project and location for which to retrieve `BackupPlans` information. Format: `projects/{project}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. To retrieve backup plans for all locations, use "-" for the `{location}` value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager)` | The response message for getting a list of BackupPlan. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager

Lists BackupVaults in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_backup_vaults():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_vaults](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_vaults)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsRequest), dict]`   
The request object. Request message for listing backupvault stores.  
`parent` |  `str`   
Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager)` | Response message for listing BackupVaults. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager

Lists Backups in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_backups():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backups](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backups)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsRequest), dict]`   
The request object. Request message for listing Backups.  
`parent` |  `str`   
Required. The project and location for which to retrieve backup information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager)` | Response message for listing Backups. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_data_source_references
    
    
    list_data_source_references(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager

Lists DataSourceReferences for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_data_source_references():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListDataSourceReferencesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_data_source_references](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_data_source_references)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest), dict]`   
The request object. Request for the ListDataSourceReferences method.  
`parent` |  `str`   
Required. The parent resource name. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager)` | Response for the ListDataSourceReferences method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_data_sources
    
    
    list_data_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager

Lists DataSources in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_data_sources():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListDataSourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_data_sources](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_data_sources)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListDataSourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesRequest), dict]`   
The request object. Request message for listing DataSources.  
`parent` |  `str`   
Required. The project and location for which to retrieve data sources information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager)` | Response message for listing DataSources. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_management_servers
    
    
    list_management_servers(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager

Lists ManagementServers in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_list_management_servers():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[ListManagementServersRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_management_servers](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_management_servers)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.ListManagementServersRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersRequest), dict]`   
The request object. Request message for listing management servers.  
`parent` |  `str`   
Required. The project and location for which to retrieve management servers information, in the format 'projects/{project_id}/locations/{location}'. In Cloud BackupDR, locations map to Google Cloud regions, for example **us-central1**. To retrieve management servers for all locations, use "-" for the '{location}' value. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager)` | Response message for listing management servers. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### management_server_path
    
    
    management_server_path(project: str, location: str, managementserver: str) -> str

Returns a fully-qualified management_server string.

### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

### parse_backup_plan_association_path
    
    
    parse_backup_plan_association_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_association path into its component segments.

### parse_backup_plan_path
    
    
    parse_backup_plan_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan path into its component segments.

### parse_backup_plan_revision_path
    
    
    parse_backup_plan_revision_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_revision path into its component segments.

### parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

### parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

### parse_data_source_path
    
    
    parse_data_source_path(path: str) -> typing.Dict[str, str]

Parses a data_source path into its component segments.

### parse_data_source_reference_path
    
    
    parse_data_source_reference_path(path: str) -> typing.Dict[str, str]

Parses a data_source_reference path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### parse_management_server_path
    
    
    parse_management_server_path(path: str) -> typing.Dict[str, str]

Parses a management_server path into its component segments.

### parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

### restore_backup
    
    
    restore_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.RestoreBackupRequest, dict
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

Restore from a Backup
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_restore_backup():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        compute_instance_target_environment = backupdr_v1.[ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment.html)()
        compute_instance_target_environment.project = "project_value"
        compute_instance_target_environment.zone = "zone_value"
    
        request = backupdr_v1.[RestoreBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest.html)(
            compute_instance_target_environment=compute_instance_target_environment,
            name="name_value",
        )
    
        # Make the request
        operation = client.[restore_backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_restore_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.RestoreBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest), dict]`   
The request object. Request message for restoring from a Backup.  
`name` |  `str`   
Required. The resource name of the Backup instance, in the format 'projects/_/locations/_ /backupVaults/_/dataSources/_ /backups/'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [RestoreBackupResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupResponse) Response message for restoring from a Backup.  
  
### set_iam_policy
    
    
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

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### storage_pool_path
    
    
    storage_pool_path(project: str, zone: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

### test_iam_permissions
    
    
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

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### trigger_backup
    
    
    trigger_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.TriggerBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Triggers a new Backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_trigger_backup():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[TriggerBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TriggerBackupRequest.html)(
            name="name_value",
            rule_id="rule_id_value",
        )
    
        # Make the request
        operation = client.[trigger_backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_trigger_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.TriggerBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TriggerBackupRequest), dict]`   
The request object. Request message for triggering a backup.  
`name` |  `str`   
Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`rule_id` |  `str`   
Required. backup rule_id for which a backup needs to be triggered. This corresponds to the `rule_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation) A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc  
  
### update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupRequest, dict
            ]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.backupdr_v1.types.backupvault.Backup] = None,
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

Updates the settings of a Backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_update_backup():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupRequest.html)(
        )
    
        # Make the request
        operation = client.[update_backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupRequest), dict]`   
The request object. Request message for updating a Backup.  
`backup` |  `[google.cloud.backupdr_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup)`   
Required. The resource being updated This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup) Message describing a Backup object.  
  
### update_backup_plan
    
    
    update_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.UpdateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
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

Update a BackupPlan.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_update_backup_plan():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        backup_plan = backupdr_v1.[BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan.html)()
        backup_plan.backup_rules.standard_schedule.recurrence_type = "YEARLY"
        backup_plan.backup_rules.standard_schedule.backup_window.start_hour_of_day = 1820
        backup_plan.backup_rules.standard_schedule.backup_window.end_hour_of_day = 1573
        backup_plan.backup_rules.standard_schedule.time_zone = "time_zone_value"
        backup_plan.backup_rules.rule_id = "rule_id_value"
        backup_plan.backup_rules.backup_retention_days = 2237
        backup_plan.resource_type = "resource_type_value"
        backup_plan.backup_vault = "backup_vault_value"
    
        request = backupdr_v1.[UpdateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanRequest.html)(
            backup_plan=backup_plan,
        )
    
        # Make the request
        operation = client.[update_backup_plan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_plan)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.UpdateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanRequest), dict]`   
The request object. Request message for updating a backup plan.  
`backup_plan` |  `[google.cloud.backupdr_v1.types.BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan)`   
Required. The resource being updated This corresponds to the `backup_plan` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlan resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently, these fields are supported in update: description, schedules, retention period, adding and removing Backup Rules. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan) A BackupPlan specifies some common fields, such as description as well as one or more BackupRule messages. Each BackupRule has a retention policy and defines a schedule by which the system is to perform backup workloads.  
  
### update_backup_plan_association
    
    
    update_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.UpdateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
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

Update a BackupPlanAssociation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_update_backup_plan_association():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        backup_plan_association = backupdr_v1.[BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation.html)()
        backup_plan_association.resource_type = "resource_type_value"
        backup_plan_association.resource = "resource_value"
        backup_plan_association.backup_plan = "backup_plan_value"
    
        request = backupdr_v1.[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest.html)(
            backup_plan_association=backup_plan_association,
        )
    
        # Make the request
        operation = client.[update_backup_plan_association](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_plan_association)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest), dict]`   
The request object. Request message for updating a backup plan association.  
`backup_plan_association` |  `[google.cloud.backupdr_v1.types.BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation)`   
Required. The resource being updated This corresponds to the `backup_plan_association` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlanAssociation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently backup_plan_association.backup_plan is the only supported field. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation) A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc  
  
### update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
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

Updates the settings of a BackupVault.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_update_backup_vault():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupVaultRequest.html)(
        )
    
        # Make the request
        operation = client.[update_backup_vault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_vault)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupVaultRequest), dict]`   
The request object. Request message for updating a BackupVault.  
`backup_vault` |  `[google.cloud.backupdr_v1.types.BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault)`   
Required. The resource being updated This corresponds to the `backup_vault` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Field mask is used to specify the fields to be overwritten in the BackupVault resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault) Message describing a BackupVault object.  
  
### update_data_source
    
    
    update_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateDataSourceRequest, dict
            ]
        ] = None,
        *,
        data_source: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.DataSource
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

Updates the settings of a DataSource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import backupdr_v1
    
    def sample_update_data_source():
        # Create a client
        client = backupdr_v1.[BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html)()
    
        # Initialize request argument(s)
        request = backupdr_v1.[UpdateDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateDataSourceRequest.html)(
        )
    
        # Make the request
        operation = client.[update_data_source](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.html#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_data_source)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.backupdr_v1.types.UpdateDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateDataSourceRequest), dict]`   
The request object. Request message for updating a data source instance.  
`data_source` |  `[google.cloud.backupdr_v1.types.DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource)`   
Required. The resource being updated This corresponds to the `data_source` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Field mask is used to specify the fields to be overwritten in the DataSource resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource) Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
