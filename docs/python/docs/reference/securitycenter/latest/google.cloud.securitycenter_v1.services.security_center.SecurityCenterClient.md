---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient
title: Class SecurityCenterClient (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:14.559631+00:00
---

# Class SecurityCenterClient (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SecurityCenterClient (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    SecurityCenterClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.securitycenter_v1.services.security_center.transports.base.SecurityCenterTransport,
                typing.Callable[
                    [...],
                    google.cloud.securitycenter_v1.services.security_center.transports.base.SecurityCenterTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

V1 APIs for Security Center service.

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
`SecurityCenterTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### SecurityCenterClient
    
    
    SecurityCenterClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.securitycenter_v1.services.security_center.transports.base.SecurityCenterTransport,
                typing.Callable[
                    [...],
                    google.cloud.securitycenter_v1.services.security_center.transports.base.SecurityCenterTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the security center client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SecurityCenterTransport,Callable[..., SecurityCenterTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the SecurityCenterTransport constructor. If set to None, a transport is chosen automatically.  
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

### asset_path
    
    
    asset_path(organization: str, asset: str) -> str

Returns a fully-qualified asset string.

### attack_path_path
    
    
    attack_path_path(
        organization: str, simulation: str, valued_resource: str, attack_path: str
    ) -> str

Returns a fully-qualified attack_path string.

### batch_create_resource_value_configs
    
    
    batch_create_resource_value_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.BatchCreateResourceValueConfigsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateResourceValueConfigRequest
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
    ) -> (
        google.cloud.securitycenter_v1.types.securitycenter_service.BatchCreateResourceValueConfigsResponse
    )

Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_batch_create_resource_value_configs():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        requests = securitycenter_v1.CreateResourceValueConfigRequest()
        requests.parent = "parent_value"
        requests.resource_value_config.resource_value = "NONE"
        requests.resource_value_config.tag_values = ['tag_values_value1', 'tag_values_value2']
    
        request = securitycenter_v1.BatchCreateResourceValueConfigsRequest(
            parent="parent_value",
            requests=requests,
        )
    
        # Make the request
        response = client.[batch_create_resource_value_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_batch_create_resource_value_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsRequest), dict]`   
The request object. Request message to create multiple resource value configs  
`parent` |  `str`   
Required. Resource name of the new ResourceValueConfig's parent. The parent field in the CreateResourceValueConfigRequest messages must either be empty or match this field. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`requests` |  `MutableSequence[[google.cloud.securitycenter_v1.types.CreateResourceValueConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateResourceValueConfigRequest)]`   
Required. The resource value configs to be created. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsResponse)` | Response message for BatchCreateResourceValueConfigs  
  
### big_query_export_path
    
    
    big_query_export_path(organization: str, export: str) -> str

Returns a fully-qualified big_query_export string.

### bulk_mute_findings
    
    
    bulk_mute_findings(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.BulkMuteFindingsRequest,
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

Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_bulk_mute_findings():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.BulkMuteFindingsRequest(
            parent="parent_value",
        )
    
        # Make the request
        operation = client.[bulk_mute_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_bulk_mute_findings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.BulkMuteFindingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BulkMuteFindingsRequest), dict]`   
The request object. Request message for bulk findings update. Note: 1. If multiple bulk update requests match the same resource, the order in which they get executed is not defined. 2. Once a bulk operation is started, there is no way to stop it.  
`parent` |  `str`   
Required. The parent, at which bulk action needs to be applied. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BulkMuteFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BulkMuteFindingsResponse) The response to a BulkMute request. Contains the LRO information.  
  
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

### create_big_query_export
    
    
    create_big_query_export(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateBigQueryExportRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        big_query_export: typing.Optional[
            google.cloud.securitycenter_v1.types.bigquery_export.BigQueryExport
        ] = None,
        big_query_export_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.bigquery_export.BigQueryExport

Creates a BigQuery export.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_big_query_export():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateBigQueryExportRequest(
            parent="parent_value",
            big_query_export_id="big_query_export_id_value",
        )
    
        # Make the request
        response = client.[create_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_big_query_export)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateBigQueryExportRequest), dict]`   
The request object. Request message for creating a BigQuery export.  
`parent` |  `str`   
Required. The name of the parent resource of the new BigQuery export. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`big_query_export` |  `[google.cloud.securitycenter_v1.types.BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport)`   
Required. The BigQuery export being created. This corresponds to the `big_query_export` field on the `request` instance; if `request` is provided, this should not be set.  
`big_query_export_id` |  `str`   
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less. This corresponds to the `big_query_export_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport)` | Configures how to deliver Findings to BigQuery Instance.  
  
### create_event_threat_detection_custom_module
    
    
    create_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        event_threat_detection_custom_module: typing.Optional[
            google.cloud.securitycenter_v1.types.event_threat_detection_custom_module.EventThreatDetectionCustomModule
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
        google.cloud.securitycenter_v1.types.event_threat_detection_custom_module.EventThreatDetectionCustomModule
    )

Creates a resident Event Threat Detection custom module at the scope of the given Resource Manager parent, and also creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateEventThreatDetectionCustomModuleRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to create an Event Threat Detection custom module.  
`parent` |  `str`   
Required. The new custom module's parent. Its format is: - `organizations/{organization}/eventThreatDetectionSettings`. - `folders/{folder}/eventThreatDetectionSettings`. - `projects/{project}/eventThreatDetectionSettings`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`event_threat_detection_custom_module` |  `[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule)`   
Required. The module to create. The event_threat_detection_custom_module.name will be ignored and server generated. This corresponds to the `event_threat_detection_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule)` | Represents an instance of an Event Threat Detection custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by child folders and projects.  
  
### create_finding
    
    
    create_finding(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateFindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        finding_id: typing.Optional[str] = None,
        finding: typing.Optional[
            google.cloud.securitycenter_v1.types.finding.Finding
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.finding.Finding

Creates a finding. The corresponding source must exist for finding creation to succeed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_finding():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateFindingRequest(
            parent="parent_value",
            finding_id="finding_id_value",
        )
    
        # Make the request
        response = client.[create_finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_finding)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateFindingRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateFindingRequest), dict]`   
The request object. Request message for creating a finding.  
`parent` |  `str`   
Required. Resource name of the new finding's parent. Its format should be `organizations/[organization_id]/sources/[source_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`finding_id` |  `str`   
Required. Unique identifier provided by the client within the parent scope. It must be alphanumeric and less than or equal to 32 characters and greater than 0 characters in length. This corresponds to the `finding_id` field on the `request` instance; if `request` is provided, this should not be set.  
`finding` |  `[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)`   
Required. The Finding being created. The name and security_marks will be ignored as they are both output only fields on this resource. This corresponds to the `finding` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding.  
  
### create_mute_config
    
    
    create_mute_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateMuteConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        mute_config: typing.Optional[
            google.cloud.securitycenter_v1.types.mute_config.MuteConfig
        ] = None,
        mute_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.mute_config.MuteConfig

Creates a mute config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_mute_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        mute_config = securitycenter_v1.MuteConfig()
        mute_config.filter = "filter_value"
    
        request = securitycenter_v1.CreateMuteConfigRequest(
            parent="parent_value",
            mute_config=mute_config,
            mute_config_id="mute_config_id_value",
        )
    
        # Make the request
        response = client.[create_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_mute_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateMuteConfigRequest), dict]`   
The request object. Request message for creating a mute config.  
`parent` |  `str`   
Required. Resource name of the new mute configs's parent. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`mute_config` |  `[google.cloud.securitycenter_v1.types.MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig)`   
Required. The mute config being created. This corresponds to the `mute_config` field on the `request` instance; if `request` is provided, this should not be set.  
`mute_config_id` |  `str`   
Required. Unique identifier provided by the client within the parent scope. It must consist of only lowercase letters, numbers, and hyphens, must start with a letter, must end with either a letter or a number, and must be 63 characters or less. This corresponds to the `mute_config_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig)` | A mute config is a Cloud SCC resource that contains the configuration to mute create/update events of findings.  
  
### create_notification_config
    
    
    create_notification_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateNotificationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        config_id: typing.Optional[str] = None,
        notification_config: typing.Optional[
            google.cloud.securitycenter_v1.types.notification_config.NotificationConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.notification_config.NotificationConfig

Creates a notification config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_notification_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateNotificationConfigRequest(
            parent="parent_value",
            config_id="config_id_value",
        )
    
        # Make the request
        response = client.[create_notification_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_notification_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateNotificationConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateNotificationConfigRequest), dict]`   
The request object. Request message for creating a notification config.  
`parent` |  `str`   
Required. Resource name of the new notification config's parent. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`config_id` |  `str`   
Required. Unique identifier provided by the client within the parent scope. It must be between 1 and 128 characters and contain alphanumeric characters, underscores, or hyphens only. This corresponds to the `config_id` field on the `request` instance; if `request` is provided, this should not be set.  
`notification_config` |  `[google.cloud.securitycenter_v1.types.NotificationConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.NotificationConfig)`   
Required. The notification config being created. The name and the service account will be ignored as they are both output only fields on this resource. This corresponds to the `notification_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.NotificationConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.NotificationConfig)` | Cloud Security Command Center (Cloud SCC) notification configs. A notification config is a Cloud SCC resource that contains the configuration to send notifications for create/update events of findings, assets and etc.  
  
### create_security_health_analytics_custom_module
    
    
    create_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        security_health_analytics_custom_module: typing.Optional[
            google.cloud.securitycenter_v1.types.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
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
        google.cloud.securitycenter_v1.types.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    )

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateSecurityHealthAnalyticsCustomModuleRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message for creating Security Health Analytics custom modules.  
`parent` |  `str`   
Required. Resource name of the new custom module's parent. Its format is `organizations/{organization}/securityHealthAnalyticsSettings`, `folders/{folder}/securityHealthAnalyticsSettings`, or `projects/{project}/securityHealthAnalyticsSettings` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`security_health_analytics_custom_module` |  `[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule)`   
Required. SecurityHealthAnalytics custom module to create. The provided name is ignored and reset with provided parent information and server-generated ID. This corresponds to the `security_health_analytics_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the child folders and projects.  
  
### create_source
    
    
    create_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.CreateSourceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        source: typing.Optional[google.cloud.securitycenter_v1.types.source.Source] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.source.Source

Creates a source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_create_source():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.CreateSourceRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_source)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.CreateSourceRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateSourceRequest), dict]`   
The request object. Request message for creating a source.  
`parent` |  `str`   
Required. Resource name of the new source's parent. Its format should be `organizations/[organization_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`source` |  `[google.cloud.securitycenter_v1.types.Source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Source)`   
Required. The Source being created, only the display_name and description will be used. All other fields will be ignored. This corresponds to the `source` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Source)` | Security Command Center finding source. A finding source is an entity or a mechanism that can produce a finding. A source is like a container of findings that come from the same scanner, logger, monitor, and other tools.  
  
### delete_big_query_export
    
    
    delete_big_query_export(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteBigQueryExportRequest,
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
    ) -> None

Deletes an existing BigQuery export.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_big_query_export():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteBigQueryExportRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_big_query_export)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteBigQueryExportRequest), dict]`   
The request object. Request message for deleting a BigQuery export.  
`name` |  `str`   
Required. The name of the BigQuery export to delete. Its format is `organizations/{organization}/bigQueryExports/{export_id}`, `folders/{folder}/bigQueryExports/{export_id}`, or `projects/{project}/bigQueryExports/{export_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_event_threat_detection_custom_module
    
    
    delete_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
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
    ) -> None

Deletes the specified Event Threat Detection custom module and all of its descendants in the Resource Manager hierarchy. This method is only supported for resident custom modules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteEventThreatDetectionCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_event_threat_detection_custom_module)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to delete an Event Threat Detection custom module.  
`name` |  `str`   
Required. Name of the custom module to delete. Its format is: - `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`. - `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`. - `projects/{project}/eventThreatDetectionSettings/customModules/{module}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_mute_config
    
    
    delete_mute_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteMuteConfigRequest,
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
    ) -> None

Deletes an existing mute config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_mute_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteMuteConfigRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_mute_config)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteMuteConfigRequest), dict]`   
The request object. Request message for deleting a mute config.  
`name` |  `str`   
Required. Name of the mute config to delete. Its format is `organizations/{organization}/muteConfigs/{config_id}`, `folders/{folder}/muteConfigs/{config_id}`, `projects/{project}/muteConfigs/{config_id}`, `organizations/{organization}/locations/global/muteConfigs/{config_id}`, `folders/{folder}/locations/global/muteConfigs/{config_id}`, or `projects/{project}/locations/global/muteConfigs/{config_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_notification_config
    
    
    delete_notification_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteNotificationConfigRequest,
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
    ) -> None

Deletes a notification config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_notification_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteNotificationConfigRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_notification_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_notification_config)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteNotificationConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteNotificationConfigRequest), dict]`   
The request object. Request message for deleting a notification config.  
`name` |  `str`   
Required. Name of the notification config to delete. Its format is `organizations/[organization_id]/notificationConfigs/[config_id]`, `folders/[folder_id]/notificationConfigs/[config_id]`, or `projects/[project_id]/notificationConfigs/[config_id]`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
  
### delete_resource_value_config
    
    
    delete_resource_value_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteResourceValueConfigRequest,
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
    ) -> None

Deletes a ResourceValueConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_resource_value_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteResourceValueConfigRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_resource_value_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_resource_value_config)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteResourceValueConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteResourceValueConfigRequest), dict]`   
The request object. Request message to delete resource value config  
`name` |  `str`   
Required. Name of the ResourceValueConfig to delete This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_security_health_analytics_custom_module
    
    
    delete_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
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
    ) -> None

Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_delete_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.DeleteSecurityHealthAnalyticsCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        client.[delete_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_security_health_analytics_custom_module)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message for deleting Security Health Analytics custom modules.  
`name` |  `str`   
Required. Name of the custom module to delete. Its format is `organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}`, `folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}`, or `projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### dlp_job_path
    
    
    dlp_job_path(project: str, dlp_job: str) -> str

Returns a fully-qualified dlp_job string.

### effective_event_threat_detection_custom_module_path
    
    
    effective_event_threat_detection_custom_module_path(
        organization: str, module: str
    ) -> str

Returns a fully-qualified effective_event_threat_detection_custom_module string.

### effective_security_health_analytics_custom_module_path
    
    
    effective_security_health_analytics_custom_module_path(
        organization: str, effective_custom_module: str
    ) -> str

Returns a fully-qualified effective_security_health_analytics_custom_module string.

### event_threat_detection_custom_module_path
    
    
    event_threat_detection_custom_module_path(organization: str, module: str) -> str

Returns a fully-qualified event_threat_detection_custom_module string.

### external_system_path
    
    
    external_system_path(
        organization: str, source: str, finding: str, externalsystem: str
    ) -> str

Returns a fully-qualified external_system string.

### finding_path
    
    
    finding_path(organization: str, source: str, finding: str) -> str

Returns a fully-qualified finding string.

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
`SecurityCenterClient` | The constructed client.  
  
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
`SecurityCenterClient` | The constructed client.  
  
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
`SecurityCenterClient` | The constructed client.  
  
### get_big_query_export
    
    
    get_big_query_export(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetBigQueryExportRequest,
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
    ) -> google.cloud.securitycenter_v1.types.bigquery_export.BigQueryExport

Gets a BigQuery export.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_big_query_export():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetBigQueryExportRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_big_query_export)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetBigQueryExportRequest), dict]`   
The request object. Request message for retrieving a BigQuery export.  
`name` |  `str`   
Required. Name of the BigQuery export to retrieve. Its format is `organizations/{organization}/bigQueryExports/{export_id}`, `folders/{folder}/bigQueryExports/{export_id}`, or `projects/{project}/bigQueryExports/{export_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport)` | Configures how to deliver Findings to BigQuery Instance.  
  
### get_effective_event_threat_detection_custom_module
    
    
    get_effective_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
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
        google.cloud.securitycenter_v1.types.effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule
    )

Gets an effective Event Threat Detection custom module at the given level.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_effective_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetEffectiveEventThreatDetectionCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_effective_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_effective_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to get an EffectiveEventThreatDetectionCustomModule.  
`name` |  `str`   
Required. The resource name of the effective Event Threat Detection custom module. Its format is: - `organizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}`. - `folders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}`. - `projects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EffectiveEventThreatDetectionCustomModule)` | An EffectiveEventThreatDetectionCustomModule is the representation of an Event Threat Detection custom module at a specified level of the resource hierarchy: organization, folder, or project. If a custom module is inherited from a parent organization or folder, the value of the enablement_state property in EffectiveEventThreatDetectionCustomModule is set to the value that is effective in the parent, instead of INHERITED. For example, if the module is enabled in a parent organization or folder, the effective enablement_state for the module in all child folders or projects is also enabled. EffectiveEventThreatDetectionCustomModule is read-only.  
  
### get_effective_security_health_analytics_custom_module
    
    
    get_effective_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
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
        google.cloud.securitycenter_v1.types.effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule
    )

Retrieves an EffectiveSecurityHealthAnalyticsCustomModule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_effective_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_effective_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_effective_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message for getting effective Security Health Analytics custom modules.  
`name` |  `str`   
Required. Name of the effective custom module to get. Its format is `organizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}`, `folders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}`, or `projects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EffectiveSecurityHealthAnalyticsCustomModule)` | An EffectiveSecurityHealthAnalyticsCustomModule is the representation of a Security Health Analytics custom module at a specified level of the resource hierarchy: organization, folder, or project. If a custom module is inherited from a parent organization or folder, the value of the enablementState property in EffectiveSecurityHealthAnalyticsCustomModule is set to the value that is effective in the parent, instead of INHERITED. For example, if the module is enabled in a parent organization or folder, the effective enablement_state for the module in all child folders or projects is also enabled. EffectiveSecurityHealthAnalyticsCustomModule is read-only.  
  
### get_event_threat_detection_custom_module
    
    
    get_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetEventThreatDetectionCustomModuleRequest,
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
        google.cloud.securitycenter_v1.types.event_threat_detection_custom_module.EventThreatDetectionCustomModule
    )

Gets an Event Threat Detection custom module.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetEventThreatDetectionCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to get an Event Threat Detection custom module.  
`name` |  `str`   
Required. Name of the custom module to get. Its format is: - `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`. - `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`. - `projects/{project}/eventThreatDetectionSettings/customModules/{module}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule)` | Represents an instance of an Event Threat Detection custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by child folders and projects.  
  
### get_iam_policy
    
    
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

Gets the access control policy on the specified Source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_get_iam_policy():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
  
### get_mute_config
    
    
    get_mute_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetMuteConfigRequest,
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
    ) -> google.cloud.securitycenter_v1.types.mute_config.MuteConfig

Gets a mute config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_mute_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetMuteConfigRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_mute_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetMuteConfigRequest), dict]`   
The request object. Request message for retrieving a mute config.  
`name` |  `str`   
Required. Name of the mute config to retrieve. Its format is `organizations/{organization}/muteConfigs/{config_id}`, `folders/{folder}/muteConfigs/{config_id}`, `projects/{project}/muteConfigs/{config_id}`, `organizations/{organization}/locations/global/muteConfigs/{config_id}`, `folders/{folder}/locations/global/muteConfigs/{config_id}`, or `projects/{project}/locations/global/muteConfigs/{config_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig)` | A mute config is a Cloud SCC resource that contains the configuration to mute create/update events of findings.  
  
### get_notification_config
    
    
    get_notification_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetNotificationConfigRequest,
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
    ) -> google.cloud.securitycenter_v1.types.notification_config.NotificationConfig

Gets a notification config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_notification_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetNotificationConfigRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_notification_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_notification_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetNotificationConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetNotificationConfigRequest), dict]`   
The request object. Request message for getting a notification config.  
`name` |  `str`   
Required. Name of the notification config to get. Its format is `organizations/[organization_id]/notificationConfigs/[config_id]`, `folders/[folder_id]/notificationConfigs/[config_id]`, or `projects/[project_id]/notificationConfigs/[config_id]`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.NotificationConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.NotificationConfig)` | Cloud Security Command Center (Cloud SCC) notification configs. A notification config is a Cloud SCC resource that contains the configuration to send notifications for create/update events of findings, assets and etc.  
  
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
  
### get_organization_settings
    
    
    get_organization_settings(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetOrganizationSettingsRequest,
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
    ) -> google.cloud.securitycenter_v1.types.organization_settings.OrganizationSettings

Gets the settings for an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_organization_settings():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.[GetOrganizationSettingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetOrganizationSettingsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_organization_settings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_organization_settings)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetOrganizationSettingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetOrganizationSettingsRequest), dict]`   
The request object. Request message for getting organization settings.  
`name` |  `str`   
Required. Name of the organization to get organization settings for. Its format is `organizations/[organization_id]/organizationSettings`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.OrganizationSettings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.OrganizationSettings)` | User specified settings that are attached to the Security Command Center organization.  
  
### get_resource_value_config
    
    
    get_resource_value_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetResourceValueConfigRequest,
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
    ) -> google.cloud.securitycenter_v1.types.resource_value_config.ResourceValueConfig

Gets a ResourceValueConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_resource_value_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetResourceValueConfigRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_resource_value_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_resource_value_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetResourceValueConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetResourceValueConfigRequest), dict]`   
The request object. Request message to get resource value config  
`name` |  `str`   
Required. Name of the resource value config to retrieve. Its format is `organizations/{organization}/resourceValueConfigs/{config_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.ResourceValueConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ResourceValueConfig)` | A resource value configuration (RVC) is a mapping configuration of user's resources to resource values. Used in Attack path simulations.  
  
### get_security_health_analytics_custom_module
    
    
    get_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
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
        google.cloud.securitycenter_v1.types.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    )

Retrieves a SecurityHealthAnalyticsCustomModule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetSecurityHealthAnalyticsCustomModuleRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message for getting Security Health Analytics custom modules.  
`name` |  `str`   
Required. Name of the custom module to get. Its format is `organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}`, `folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}`, or `projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the child folders and projects.  
  
### get_simulation
    
    
    get_simulation(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetSimulationRequest,
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
    ) -> google.cloud.securitycenter_v1.types.simulation.Simulation

Get the simulation by name or the latest simulation for the given organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_simulation():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetSimulationRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_simulation](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_simulation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetSimulationRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetSimulationRequest), dict]`   
The request object. Request message for getting simulation. Simulation name can include "latest" to retrieve the latest simulation For example, "organizations/123/simulations/latest".  
`name` |  `str`   
Required. The organization name or simulation name of this simulation Valid format: `organizations/{organization}/simulations/latest` `organizations/{organization}/simulations/{simulation}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Simulation](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Simulation)` | Attack path simulation  
  
### get_source
    
    
    get_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetSourceRequest,
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
    ) -> google.cloud.securitycenter_v1.types.source.Source

Gets a source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_source():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetSourceRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_source)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetSourceRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetSourceRequest), dict]`   
The request object. Request message for getting a source.  
`name` |  `str`   
Required. Relative resource name of the source. Its format is `organizations/[organization_id]/source/[source_id]`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Source)` | Security Command Center finding source. A finding source is an entity or a mechanism that can produce a finding. A source is like a container of findings that come from the same scanner, logger, monitor, and other tools.  
  
### get_valued_resource
    
    
    get_valued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GetValuedResourceRequest,
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
    ) -> google.cloud.securitycenter_v1.types.valued_resource.ValuedResource

Get the valued resource by name
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_get_valued_resource():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GetValuedResourceRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_valued_resource](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_valued_resource)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GetValuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetValuedResourceRequest), dict]`   
The request object. Request message for getting a valued resource.  
`name` |  `str`   
Required. The name of this valued resource Valid format: `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.ValuedResource](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ValuedResource)` | A resource that is determined to have value to a user's system  
  
### group_assets
    
    
    group_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GroupAssetsRequest,
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
    ) -> google.cloud.securitycenter_v1.services.security_center.pagers.GroupAssetsPager

Filters an organization's assets and groups them by their specified properties.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_group_assets():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.[GroupAssetsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GroupAssetsRequest.html)(
            parent="parent_value",
            group_by="group_by_value",
        )
    
        # Make the request
        page_result = client.[group_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_group_assets)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GroupAssetsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GroupAssetsRequest), dict]`   
The request object. Request message for grouping by assets.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.GroupAssetsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.GroupAssetsPager)` | Response message for grouping by assets. Iterating over this object will yield results and resolve additional pages automatically.  
  
### group_findings
    
    
    group_findings(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.GroupFindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.services.security_center.pagers.GroupFindingsPager

Filters an organization or source's findings and groups them by their specified properties.

To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_group_findings():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.GroupFindingsRequest(
            parent="parent_value",
            group_by="group_by_value",
        )
    
        # Make the request
        page_result = client.[group_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_group_findings)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.GroupFindingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GroupFindingsRequest), dict]`   
The request object. Request message for grouping by findings.  
`parent` |  `str`   
Required. Name of the source to groupBy. Its format is `organizations/[organization_id]/sources/[source_id]`, `folders/[folder_id]/sources/[source_id]`, or `projects/[project_id]/sources/[source_id]`. To groupBy across all sources provide a source_id of `-`. For example: `organizations/{organization_id}/sources/-, folders/{folder_id}/sources/-`, or `projects/{project_id}/sources/-` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`group_by` |  `str`   
Required. Expression that defines what assets fields to use for grouping (including `state_change`). The string value should follow SQL syntax: comma separated list of fields. For example: "parent,resource_name". The following fields are supported when compare_duration is set: - state_change This corresponds to the `group_by` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.GroupFindingsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.GroupFindingsPager)` | Response message for group by findings. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListAssetsRequest,
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
    ) -> google.cloud.securitycenter_v1.services.security_center.pagers.ListAssetsPager

Lists an organization's assets.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_assets():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.[ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListAssetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListAssetsRequest), dict]`   
The request object. Request message for listing assets.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListAssetsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListAssetsPager)` | Response message for listing assets. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_attack_paths
    
    
    list_attack_paths(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListAttackPathsRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListAttackPathsPager
    )

Lists the attack paths for a set of simulation results or valued resources and filter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_attack_paths():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListAttackPathsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_attack_paths](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_attack_paths)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListAttackPathsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListAttackPathsRequest), dict]`   
The request object. Request message for listing the attack paths for a given simulation or valued resource.  
`parent` |  `str`   
Required. Name of parent to list attack paths. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` `organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListAttackPathsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListAttackPathsPager)` | Response message for listing the attack paths for a given simulation or valued resource. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_big_query_exports
    
    
    list_big_query_exports(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListBigQueryExportsRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListBigQueryExportsPager
    )

Lists BigQuery exports. Note that when requesting BigQuery exports at a given level all exports under that level are also returned e.g. if requesting BigQuery exports under a folder, then all BigQuery exports immediately under the folder plus the ones created under the projects within the folder are returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_big_query_exports():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListBigQueryExportsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_big_query_exports](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_big_query_exports)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListBigQueryExportsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListBigQueryExportsRequest), dict]`   
The request object. Request message for listing BigQuery exports at a given scope e.g. organization, folder or project.  
`parent` |  `str`   
Required. The parent, which owns the collection of BigQuery exports. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListBigQueryExportsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListBigQueryExportsPager)` | Response message for listing BigQuery exports. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_descendant_event_threat_detection_custom_modules
    
    
    list_descendant_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantEventThreatDetectionCustomModulesPager
    )

Lists all resident Event Threat Detection custom modules under the given Resource Manager parent and its descendants.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_descendant_event_threat_detection_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListDescendantEventThreatDetectionCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_descendant_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_descendant_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest), dict]`   
The request object. Request to list current and descendant resident Event Threat Detection custom modules.  
`parent` |  `str`   
Required. Name of the parent to list custom modules under. Its format is: - `organizations/{organization}/eventThreatDetectionSettings`. - `folders/{folder}/eventThreatDetectionSettings`. - `projects/{project}/eventThreatDetectionSettings`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantEventThreatDetectionCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantEventThreatDetectionCustomModulesPager)` | Response for listing current and descendant resident Event Threat Detection custom modules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_descendant_security_health_analytics_custom_modules
    
    
    list_descendant_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager
    )

Returns a list of all resident SecurityHealthAnalyticsCustomModules under the given CRM parent and all of the parent’s CRM descendants.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_descendant_security_health_analytics_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_descendant_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_descendant_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest), dict]`   
The request object. Request message for listing descendant Security Health Analytics custom modules.  
`parent` |  `str`   
Required. Name of parent to list descendant custom modules. Its format is `organizations/{organization}/securityHealthAnalyticsSettings`, `folders/{folder}/securityHealthAnalyticsSettings`, or `projects/{project}/securityHealthAnalyticsSettings` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesPager)` | Response message for listing descendant Security Health Analytics custom modules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_effective_event_threat_detection_custom_modules
    
    
    list_effective_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveEventThreatDetectionCustomModulesPager
    )

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_effective_event_threat_detection_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListEffectiveEventThreatDetectionCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_effective_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_effective_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest), dict]`   
The request object. Request to list effective Event Threat Detection custom modules.  
`parent` |  `str`   
Required. Name of the parent to list custom modules for. Its format is: - `organizations/{organization}/eventThreatDetectionSettings`. - `folders/{folder}/eventThreatDetectionSettings`. - `projects/{project}/eventThreatDetectionSettings`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveEventThreatDetectionCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveEventThreatDetectionCustomModulesPager)` | Response for listing EffectiveEventThreatDetectionCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_effective_security_health_analytics_custom_modules
    
    
    list_effective_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager
    )

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_effective_security_health_analytics_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_effective_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_effective_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest), dict]`   
The request object. Request message for listing effective Security Health Analytics custom modules.  
`parent` |  `str`   
Required. Name of parent to list effective custom modules. Its format is `organizations/{organization}/securityHealthAnalyticsSettings`, `folders/{folder}/securityHealthAnalyticsSettings`, or `projects/{project}/securityHealthAnalyticsSettings` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesPager)` | Response message for listing effective Security Health Analytics custom modules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_event_threat_detection_custom_modules
    
    
    list_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListEventThreatDetectionCustomModulesPager
    )

Lists all Event Threat Detection custom modules for the given Resource Manager parent. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_event_threat_detection_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListEventThreatDetectionCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListEventThreatDetectionCustomModulesRequest), dict]`   
The request object. Request to list Event Threat Detection custom modules.  
`parent` |  `str`   
Required. Name of the parent to list custom modules under. Its format is: - `organizations/{organization}/eventThreatDetectionSettings`. - `folders/{folder}/eventThreatDetectionSettings`. - `projects/{project}/eventThreatDetectionSettings`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListEventThreatDetectionCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListEventThreatDetectionCustomModulesPager)` | Response for listing Event Threat Detection custom modules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_findings
    
    
    list_findings(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListFindingsRequest,
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
    ) -> google.cloud.securitycenter_v1.services.security_center.pagers.ListFindingsPager

Lists an organization or source's findings.

To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_findings():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListFindingsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListFindingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListFindingsRequest), dict]`   
The request object. Request message for listing findings.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListFindingsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListFindingsPager)` | Response message for listing findings. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_mute_configs
    
    
    list_mute_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListMuteConfigsRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListMuteConfigsPager
    )

Lists mute configs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_mute_configs():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListMuteConfigsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_mute_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_mute_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListMuteConfigsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListMuteConfigsRequest), dict]`   
The request object. Request message for listing mute configs at a given scope e.g. organization, folder or project.  
`parent` |  `str`   
Required. The parent, which owns the collection of mute configs. Its format is `organizations/[organization_id]`, `folders/[folder_id]`, `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListMuteConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListMuteConfigsPager)` | Response message for listing mute configs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_notification_configs
    
    
    list_notification_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListNotificationConfigsRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListNotificationConfigsPager
    )

Lists notification configs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_notification_configs():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListNotificationConfigsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_notification_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_notification_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListNotificationConfigsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListNotificationConfigsRequest), dict]`   
The request object. Request message for listing notification configs.  
`parent` |  `str`   
Required. The name of the parent in which to list the notification configurations. Its format is "organizations/[organization_id]", "folders/[folder_id]", or "projects/[project_id]". This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListNotificationConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListNotificationConfigsPager)` | Response message for listing notification configs. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_resource_value_configs
    
    
    list_resource_value_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListResourceValueConfigsRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListResourceValueConfigsPager
    )

Lists all ResourceValueConfigs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_resource_value_configs():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListResourceValueConfigsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_resource_value_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_resource_value_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListResourceValueConfigsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListResourceValueConfigsRequest), dict]`   
The request object. Request message to list resource value configs of a parent  
`parent` |  `str`   
Required. The parent, which owns the collection of resource value configs. Its format is `organizations/[organization_id]` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListResourceValueConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListResourceValueConfigsPager)` | Response message to list resource value configs Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_security_health_analytics_custom_modules
    
    
    list_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListSecurityHealthAnalyticsCustomModulesPager
    )

Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_security_health_analytics_custom_modules():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListSecurityHealthAnalyticsCustomModulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest), dict]`   
The request object. Request message for listing Security Health Analytics custom modules.  
`parent` |  `str`   
Required. Name of parent to list custom modules. Its format is `organizations/{organization}/securityHealthAnalyticsSettings`, `folders/{folder}/securityHealthAnalyticsSettings`, or `projects/{project}/securityHealthAnalyticsSettings` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListSecurityHealthAnalyticsCustomModulesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListSecurityHealthAnalyticsCustomModulesPager)` | Response message for listing Security Health Analytics custom modules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_sources
    
    
    list_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListSourcesRequest,
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
    ) -> google.cloud.securitycenter_v1.services.security_center.pagers.ListSourcesPager

Lists all sources belonging to an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_sources():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListSourcesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_sources](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_sources)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListSourcesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListSourcesRequest), dict]`   
The request object. Request message for listing sources.  
`parent` |  `str`   
Required. Resource name of the parent of sources to list. Its format should be `organizations/[organization_id]`, `folders/[folder_id]`, or `projects/[project_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListSourcesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListSourcesPager)` | Response message for listing sources. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_valued_resources
    
    
    list_valued_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ListValuedResourcesRequest,
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
        google.cloud.securitycenter_v1.services.security_center.pagers.ListValuedResourcesPager
    )

Lists the valued resources for a set of simulation results and filter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_list_valued_resources():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ListValuedResourcesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_valued_resources](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_valued_resources)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ListValuedResourcesRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListValuedResourcesRequest), dict]`   
The request object. Request message for listing the valued resources for a given simulation.  
`parent` |  `str`   
Required. Name of parent to list valued resources. Valid formats: `organizations/{organization}`, `organizations/{organization}/simulations/{simulation}` `organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.services.security_center.pagers.ListValuedResourcesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.pagers.ListValuedResourcesPager)` | Response message for listing the valued resources for a given simulation. Iterating over this object will yield results and resolve additional pages automatically.  
  
### mute_config_path
    
    
    mute_config_path(organization: str, mute_config: str) -> str

Returns a fully-qualified mute_config string.

### notification_config_path
    
    
    notification_config_path(organization: str, notification_config: str) -> str

Returns a fully-qualified notification_config string.

### organization_settings_path
    
    
    organization_settings_path(organization: str) -> str

Returns a fully-qualified organization_settings string.

### parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

### parse_attack_path_path
    
    
    parse_attack_path_path(path: str) -> typing.Dict[str, str]

Parses a attack_path path into its component segments.

### parse_big_query_export_path
    
    
    parse_big_query_export_path(path: str) -> typing.Dict[str, str]

Parses a big_query_export path into its component segments.

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

### parse_dlp_job_path
    
    
    parse_dlp_job_path(path: str) -> typing.Dict[str, str]

Parses a dlp_job path into its component segments.

### parse_effective_event_threat_detection_custom_module_path
    
    
    parse_effective_event_threat_detection_custom_module_path(
        path: str,
    ) -> typing.Dict[str, str]

Parses a effective_event_threat_detection_custom_module path into its component segments.

### parse_effective_security_health_analytics_custom_module_path
    
    
    parse_effective_security_health_analytics_custom_module_path(
        path: str,
    ) -> typing.Dict[str, str]

Parses a effective_security_health_analytics_custom_module path into its component segments.

### parse_event_threat_detection_custom_module_path
    
    
    parse_event_threat_detection_custom_module_path(path: str) -> typing.Dict[str, str]

Parses a event_threat_detection_custom_module path into its component segments.

### parse_external_system_path
    
    
    parse_external_system_path(path: str) -> typing.Dict[str, str]

Parses a external_system path into its component segments.

### parse_finding_path
    
    
    parse_finding_path(path: str) -> typing.Dict[str, str]

Parses a finding path into its component segments.

### parse_mute_config_path
    
    
    parse_mute_config_path(path: str) -> typing.Dict[str, str]

Parses a mute_config path into its component segments.

### parse_notification_config_path
    
    
    parse_notification_config_path(path: str) -> typing.Dict[str, str]

Parses a notification_config path into its component segments.

### parse_organization_settings_path
    
    
    parse_organization_settings_path(path: str) -> typing.Dict[str, str]

Parses a organization_settings path into its component segments.

### parse_policy_path
    
    
    parse_policy_path(path: str) -> typing.Dict[str, str]

Parses a policy path into its component segments.

### parse_resource_value_config_path
    
    
    parse_resource_value_config_path(path: str) -> typing.Dict[str, str]

Parses a resource_value_config path into its component segments.

### parse_security_health_analytics_custom_module_path
    
    
    parse_security_health_analytics_custom_module_path(
        path: str,
    ) -> typing.Dict[str, str]

Parses a security_health_analytics_custom_module path into its component segments.

### parse_security_marks_path
    
    
    parse_security_marks_path(path: str) -> typing.Dict[str, str]

Parses a security_marks path into its component segments.

### parse_simulation_path
    
    
    parse_simulation_path(path: str) -> typing.Dict[str, str]

Parses a simulation path into its component segments.

### parse_source_path
    
    
    parse_source_path(path: str) -> typing.Dict[str, str]

Parses a source path into its component segments.

### parse_table_data_profile_path
    
    
    parse_table_data_profile_path(path: str) -> typing.Dict[str, str]

Parses a table_data_profile path into its component segments.

### parse_topic_path
    
    
    parse_topic_path(path: str) -> typing.Dict[str, str]

Parses a topic path into its component segments.

### parse_valued_resource_path
    
    
    parse_valued_resource_path(path: str) -> typing.Dict[str, str]

Parses a valued_resource path into its component segments.

### policy_path
    
    
    policy_path(organization: str, constraint_name: str) -> str

Returns a fully-qualified policy string.

### resource_value_config_path
    
    
    resource_value_config_path(organization: str, resource_value_config: str) -> str

Returns a fully-qualified resource_value_config string.

### run_asset_discovery
    
    
    run_asset_discovery(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.RunAssetDiscoveryRequest,
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

Runs asset discovery. The discovery is tracked with a long-running operation.

This API can only be called with limited frequency for an organization. If it is called too frequently the caller will receive a TOO_MANY_REQUESTS error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_run_asset_discovery():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.[RunAssetDiscoveryRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.RunAssetDiscoveryRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = client.[run_asset_discovery](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_run_asset_discovery)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.RunAssetDiscoveryRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.RunAssetDiscoveryRequest), dict]`   
The request object. Request message for running asset discovery for an organization.  
`parent` |  `str`   
Required. Name of the organization to run asset discovery for. Its format is `organizations/[organization_id]`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [RunAssetDiscoveryResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.RunAssetDiscoveryResponse) Response of asset discovery run  
  
### security_health_analytics_custom_module_path
    
    
    security_health_analytics_custom_module_path(
        organization: str, custom_module: str
    ) -> str

Returns a fully-qualified security_health_analytics_custom_module string.

### security_marks_path
    
    
    security_marks_path(organization: str, asset: str) -> str

Returns a fully-qualified security_marks string.

### set_finding_state
    
    
    set_finding_state(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.SetFindingStateRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        state: typing.Optional[
            google.cloud.securitycenter_v1.types.finding.Finding.State
        ] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.finding.Finding

Updates the state of a finding.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_set_finding_state():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.SetFindingStateRequest(
            name="name_value",
            state="INACTIVE",
        )
    
        # Make the request
        response = client.[set_finding_state](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_finding_state)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.SetFindingStateRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SetFindingStateRequest), dict]`   
The request object. Request message for updating a finding's state.  
`name` |  `str`   
Required. The `relative resource name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__ of the finding. Example: `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}`, `folders/{folder_id}/sources/{source_id}/findings/{finding_id}`, `projects/{project_id}/sources/{source_id}/findings/{finding_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`state` |  `[google.cloud.securitycenter_v1.types.Finding.State](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding.State)`   
Required. The desired State of the finding. This corresponds to the `state` field on the `request` instance; if `request` is provided, this should not be set.  
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The time at which the updated state takes effect. This corresponds to the `start_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding.  
  
### set_iam_policy
    
    
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

Sets the access control policy on the specified Source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_set_iam_policy():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### set_mute
    
    
    set_mute(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.SetMuteRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        mute: typing.Optional[
            google.cloud.securitycenter_v1.types.finding.Finding.Mute
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.finding.Finding

Updates the mute state of a finding.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_set_mute():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.SetMuteRequest(
            name="name_value",
            mute="UNDEFINED",
        )
    
        # Make the request
        response = client.[set_mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_mute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.SetMuteRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SetMuteRequest), dict]`   
The request object. Request message for updating a finding's mute status.  
`name` |  `str`   
Required. The `relative resource name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__ of the finding. Example: `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}`, `folders/{folder_id}/sources/{source_id}/findings/{finding_id}`, `projects/{project_id}/sources/{source_id}/findings/{finding_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`mute` |  `[google.cloud.securitycenter_v1.types.Finding.Mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding.Mute)`   
Required. The desired state of the Mute. This corresponds to the `mute` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding.  
  
### simulate_security_health_analytics_custom_module
    
    
    simulate_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        custom_config: typing.Optional[
            google.cloud.securitycenter_v1.types.security_health_analytics_custom_config.CustomConfig
        ] = None,
        resource: typing.Optional[
            google.cloud.securitycenter_v1.types.securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
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
        google.cloud.securitycenter_v1.types.securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse
    )

Simulates a given SecurityHealthAnalyticsCustomModule and Resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_simulate_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        resource = securitycenter_v1.SimulatedResource()
        resource.resource_type = "resource_type_value"
    
        request = securitycenter_v1.SimulateSecurityHealthAnalyticsCustomModuleRequest(
            parent="parent_value",
            resource=resource,
        )
    
        # Make the request
        response = client.[simulate_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_simulate_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message to simulate a CustomConfig against a given test resource. Maximum size of the request is 4 MB by default.  
`parent` |  `str`   
Required. The relative resource name of the organization, project, or folder. For more information about relative resource names, see `Relative Resource Name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__ Example: `organizations/{organization_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`custom_config` |  `[google.cloud.securitycenter_v1.types.CustomConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CustomConfig)`   
Required. The custom configuration that you need to test. This corresponds to the `custom_config` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `[google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource)`   
Required. Resource data to simulate custom module against. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | Response message for simulating a SecurityHealthAnalyticsCustomModule against a given resource.  
  
### simulation_path
    
    
    simulation_path(organization: str, simulation: str) -> str

Returns a fully-qualified simulation string.

### source_path
    
    
    source_path(organization: str, source: str) -> str

Returns a fully-qualified source string.

### table_data_profile_path
    
    
    table_data_profile_path(project: str, table_profile: str) -> str

Returns a fully-qualified table_data_profile string.

### test_iam_permissions
    
    
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

Returns the permissions that a caller has on the specified source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_test_iam_permissions():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]`   
The request object. Request message for `TestIamPermissions` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`permissions` |  `MutableSequence[str]`   
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__. This corresponds to the `permissions` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### topic_path
    
    
    topic_path(project: str, topic: str) -> str

Returns a fully-qualified topic string.

### update_big_query_export
    
    
    update_big_query_export(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateBigQueryExportRequest,
                dict,
            ]
        ] = None,
        *,
        big_query_export: typing.Optional[
            google.cloud.securitycenter_v1.types.bigquery_export.BigQueryExport
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
    ) -> google.cloud.securitycenter_v1.types.bigquery_export.BigQueryExport

Updates a BigQuery export.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_big_query_export():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateBigQueryExportRequest(
        )
    
        # Make the request
        response = client.[update_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_big_query_export)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateBigQueryExportRequest), dict]`   
The request object. Request message for updating a BigQuery export.  
`big_query_export` |  `[google.cloud.securitycenter_v1.types.BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport)`   
Required. The BigQuery export being updated. This corresponds to the `big_query_export` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport)` | Configures how to deliver Findings to BigQuery Instance.  
  
### update_event_threat_detection_custom_module
    
    
    update_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        event_threat_detection_custom_module: typing.Optional[
            google.cloud.securitycenter_v1.types.event_threat_detection_custom_module.EventThreatDetectionCustomModule
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
    ) -> (
        google.cloud.securitycenter_v1.types.event_threat_detection_custom_module.EventThreatDetectionCustomModule
    )

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateEventThreatDetectionCustomModuleRequest(
        )
    
        # Make the request
        response = client.[update_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to update an Event Threat Detection custom module.  
`event_threat_detection_custom_module` |  `[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule)`   
Required. The module being updated. This corresponds to the `event_threat_detection_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule)` | Represents an instance of an Event Threat Detection custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by child folders and projects.  
  
### update_external_system
    
    
    update_external_system(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateExternalSystemRequest,
                dict,
            ]
        ] = None,
        *,
        external_system: typing.Optional[
            google.cloud.securitycenter_v1.types.external_system.ExternalSystem
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
    ) -> google.cloud.securitycenter_v1.types.external_system.ExternalSystem

Updates external system. This is for a given finding.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_external_system():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateExternalSystemRequest(
        )
    
        # Make the request
        response = client.[update_external_system](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_external_system)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateExternalSystemRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateExternalSystemRequest), dict]`   
The request object. Request message for updating a ExternalSystem resource.  
`external_system` |  `[google.cloud.securitycenter_v1.types.ExternalSystem](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ExternalSystem)`   
Required. The external system resource to update. This corresponds to the `external_system` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The FieldMask to use when updating the external system resource. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.ExternalSystem](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ExternalSystem)` | Representation of third party SIEM/SOAR fields within SCC.  
  
### update_finding
    
    
    update_finding(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateFindingRequest,
                dict,
            ]
        ] = None,
        *,
        finding: typing.Optional[
            google.cloud.securitycenter_v1.types.finding.Finding
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.finding.Finding

Creates or updates a finding. The corresponding source must exist for a finding creation to succeed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_finding():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateFindingRequest(
        )
    
        # Make the request
        response = client.[update_finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_finding)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateFindingRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateFindingRequest), dict]`   
The request object. Request message for updating or creating a finding.  
`finding` |  `[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)`   
Required. The finding resource to update or create if it does not already exist. parent, security_marks, and update_time will be ignored. In the case of creation, the finding id portion of the name must be alphanumeric and less than or equal to 32 characters and greater than 0 characters in length. This corresponds to the `finding` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Finding)` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding.  
  
### update_mute_config
    
    
    update_mute_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateMuteConfigRequest,
                dict,
            ]
        ] = None,
        *,
        mute_config: typing.Optional[
            google.cloud.securitycenter_v1.types.mute_config.MuteConfig
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
    ) -> google.cloud.securitycenter_v1.types.mute_config.MuteConfig

Updates a mute config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_mute_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        mute_config = securitycenter_v1.MuteConfig()
        mute_config.filter = "filter_value"
    
        request = securitycenter_v1.UpdateMuteConfigRequest(
            mute_config=mute_config,
        )
    
        # Make the request
        response = client.[update_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_mute_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateMuteConfigRequest), dict]`   
The request object. Request message for updating a mute config.  
`mute_config` |  `[google.cloud.securitycenter_v1.types.MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig)`   
Required. The mute config being updated. This corresponds to the `mute_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig)` | A mute config is a Cloud SCC resource that contains the configuration to mute create/update events of findings.  
  
### update_notification_config
    
    
    update_notification_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateNotificationConfigRequest,
                dict,
            ]
        ] = None,
        *,
        notification_config: typing.Optional[
            google.cloud.securitycenter_v1.types.notification_config.NotificationConfig
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
    ) -> google.cloud.securitycenter_v1.types.notification_config.NotificationConfig

Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_notification_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateNotificationConfigRequest(
        )
    
        # Make the request
        response = client.[update_notification_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_notification_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateNotificationConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateNotificationConfigRequest), dict]`   
The request object. Request message for updating a notification config.  
`notification_config` |  `[google.cloud.securitycenter_v1.types.NotificationConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.NotificationConfig)`   
Required. The notification config to update. This corresponds to the `notification_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The FieldMask to use when updating the notification config. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.NotificationConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.NotificationConfig)` | Cloud Security Command Center (Cloud SCC) notification configs. A notification config is a Cloud SCC resource that contains the configuration to send notifications for create/update events of findings, assets and etc.  
  
### update_organization_settings
    
    
    update_organization_settings(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateOrganizationSettingsRequest,
                dict,
            ]
        ] = None,
        *,
        organization_settings: typing.Optional[
            google.cloud.securitycenter_v1.types.organization_settings.OrganizationSettings
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.organization_settings.OrganizationSettings

Updates an organization's settings.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_organization_settings():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.[UpdateOrganizationSettingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateOrganizationSettingsRequest.html)(
        )
    
        # Make the request
        response = client.[update_organization_settings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_organization_settings)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateOrganizationSettingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateOrganizationSettingsRequest), dict]`   
The request object. Request message for updating an organization's settings.  
`organization_settings` |  `[google.cloud.securitycenter_v1.types.OrganizationSettings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.OrganizationSettings)`   
Required. The organization settings resource to update. This corresponds to the `organization_settings` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.OrganizationSettings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.OrganizationSettings)` | User specified settings that are attached to the Security Command Center organization.  
  
### update_resource_value_config
    
    
    update_resource_value_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateResourceValueConfigRequest,
                dict,
            ]
        ] = None,
        *,
        resource_value_config: typing.Optional[
            google.cloud.securitycenter_v1.types.resource_value_config.ResourceValueConfig
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
    ) -> google.cloud.securitycenter_v1.types.resource_value_config.ResourceValueConfig

Updates an existing ResourceValueConfigs with new rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_resource_value_config():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        resource_value_config = securitycenter_v1.ResourceValueConfig()
        resource_value_config.resource_value = "NONE"
        resource_value_config.tag_values = ['tag_values_value1', 'tag_values_value2']
    
        request = securitycenter_v1.UpdateResourceValueConfigRequest(
            resource_value_config=resource_value_config,
        )
    
        # Make the request
        response = client.[update_resource_value_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_resource_value_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateResourceValueConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateResourceValueConfigRequest), dict]`   
The request object. Request message to update resource value config  
`resource_value_config` |  `[google.cloud.securitycenter_v1.types.ResourceValueConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ResourceValueConfig)`   
Required. The resource value config being updated. This corresponds to the `resource_value_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. If empty all mutable fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.ResourceValueConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ResourceValueConfig)` | A resource value configuration (RVC) is a mapping configuration of user's resources to resource values. Used in Attack path simulations.  
  
### update_security_health_analytics_custom_module
    
    
    update_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        security_health_analytics_custom_module: typing.Optional[
            google.cloud.securitycenter_v1.types.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
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
    ) -> (
        google.cloud.securitycenter_v1.types.security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    )

Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_security_health_analytics_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateSecurityHealthAnalyticsCustomModuleRequest(
        )
    
        # Make the request
        response = client.[update_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest), dict]`   
The request object. Request message for updating Security Health Analytics custom modules.  
`security_health_analytics_custom_module` |  `[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule)`   
Required. The SecurityHealthAnalytics custom module to update. This corresponds to the `security_health_analytics_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. The only fields that can be updated are `enablement_state` and `custom_config`. If empty or set to the wildcard value `*`, both `enablement_state` and `custom_config` are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the child folders and projects.  
  
### update_security_marks
    
    
    update_security_marks(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateSecurityMarksRequest,
                dict,
            ]
        ] = None,
        *,
        security_marks: typing.Optional[
            google.cloud.securitycenter_v1.types.security_marks.SecurityMarks
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.security_marks.SecurityMarks

Updates security marks.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_security_marks():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateSecurityMarksRequest(
        )
    
        # Make the request
        response = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateSecurityMarksRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateSecurityMarksRequest), dict]`   
The request object. Request message for updating a SecurityMarks resource.  
`security_marks` |  `[google.cloud.securitycenter_v1.types.SecurityMarks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityMarks)`   
Required. The security marks resource to update. This corresponds to the `security_marks` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.SecurityMarks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SecurityMarks)` | User specified security marks that are attached to the parent Security Command Center resource. Security marks are scoped within a Security Command Center organization -- they can be modified and viewed by all users who have proper permissions on the organization.  
  
### update_source
    
    
    update_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.UpdateSourceRequest,
                dict,
            ]
        ] = None,
        *,
        source: typing.Optional[google.cloud.securitycenter_v1.types.source.Source] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.securitycenter_v1.types.source.Source

Updates a source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_update_source():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.UpdateSourceRequest(
        )
    
        # Make the request
        response = client.[update_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_source)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.UpdateSourceRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateSourceRequest), dict]`   
The request object. Request message for updating a source.  
`source` |  `[google.cloud.securitycenter_v1.types.Source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Source)`   
Required. The source resource to update. This corresponds to the `source` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.Source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.Source)` | Security Command Center finding source. A finding source is an entity or a mechanism that can produce a finding. A source is like a container of findings that come from the same scanner, logger, monitor, and other tools.  
  
### validate_event_threat_detection_custom_module
    
    
    validate_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycenter_v1.types.securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
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
    ) -> (
        google.cloud.securitycenter_v1.types.securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse
    )

Validates the given Event Threat Detection custom module.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import securitycenter_v1
    
    def sample_validate_event_threat_detection_custom_module():
        # Create a client
        client = securitycenter_v1.SecurityCenterClient()
    
        # Initialize request argument(s)
        request = securitycenter_v1.ValidateEventThreatDetectionCustomModuleRequest(
            parent="parent_value",
            raw_text="raw_text_value",
            type_="type__value",
        )
    
        # Make the request
        response = client.[validate_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_validate_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleRequest), dict]`   
The request object. Request to validate an Event Threat Detection custom module.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleResponse)` | Response to validating an Event Threat Detection custom module.  
  
### valued_resource_path
    
    
    valued_resource_path(
        organization: str, simulation: str, valued_resource: str
    ) -> str

Returns a fully-qualified valued_resource string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
