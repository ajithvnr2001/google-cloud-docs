---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient
title: Class SecurityCenterManagementAsyncClient (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:19.960893+00:00
---

# Class SecurityCenterManagementAsyncClient (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SecurityCenterManagementAsyncClient (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.22 
    
    
    SecurityCenterManagementAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.securitycentermanagement_v1.services.security_center_management.transports.base.SecurityCenterManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.securitycentermanagement_v1.services.security_center_management.transports.base.SecurityCenterManagementTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
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
`SecurityCenterManagementTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### SecurityCenterManagementAsyncClient
    
    
    SecurityCenterManagementAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.securitycentermanagement_v1.services.security_center_management.transports.base.SecurityCenterManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.securitycentermanagement_v1.services.security_center_management.transports.base.SecurityCenterManagementTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the security center management async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SecurityCenterManagementTransport,Callable[..., SecurityCenterManagementTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the SecurityCenterManagementTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_event_threat_detection_custom_module
    
    
    create_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.CreateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        event_threat_detection_custom_module: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.EventThreatDetectionCustomModule
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.EventThreatDetectionCustomModule
    )

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_create_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.CreateEventThreatDetectionCustomModuleRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_create_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.CreateEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.CreateEventThreatDetectionCustomModule.  
`parent` |  ``str``   
Required. Name of parent for the module, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`event_threat_detection_custom_module` |  `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule)`   
Required. The module to create. The EventThreatDetectionCustomModule.name field is ignored; Security Command Center generates the name. This corresponds to the `event_threat_detection_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule)` | A Security Command Center resource that contains the configuration and enablement state of a custom module, which enables Event Threat Detection to write certain findings to Security Command Center.  
  
### create_security_health_analytics_custom_module
    
    
    create_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        security_health_analytics_custom_module: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityHealthAnalyticsCustomModule
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityHealthAnalyticsCustomModule
    )

Creates a resident xref_SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_create_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_create_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule.  
`parent` |  ``str``   
Required. Name of the parent organization, folder, or project of the module, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`security_health_analytics_custom_module` |  `SecurityHealthAnalyticsCustomModule`   
Required. The resource being created. This corresponds to the `security_health_analytics_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the descendant folders and projects.  
  
### delete_event_threat_detection_custom_module
    
    
    delete_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
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
    ) -> None

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_delete_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.DeleteEventThreatDetectionCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_delete_event_threat_detection_custom_module)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.DeleteEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.DeleteEventThreatDetectionCustomModule.  
`name` |  ``str``   
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: - `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` \- `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` \- `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_security_health_analytics_custom_module
    
    
    delete_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
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
    ) -> None

Deletes the specified xref_SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_delete_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_delete_security_health_analytics_custom_module)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule.  
`name` |  ``str``   
Required. The resource name of the SHA custom module, in one of the following formats: - `organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` \- `folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` \- `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### effective_event_threat_detection_custom_module_path
    
    
    effective_event_threat_detection_custom_module_path(
        organization: str,
        location: str,
        effective_event_threat_detection_custom_module: str,
    ) -> str

Returns a fully-qualified effective_event_threat_detection_custom_module string.

### effective_security_health_analytics_custom_module_path
    
    
    effective_security_health_analytics_custom_module_path(
        organization: str,
        location: str,
        effective_security_health_analytics_custom_module: str,
    ) -> str

Returns a fully-qualified effective_security_health_analytics_custom_module string.

### event_threat_detection_custom_module_path
    
    
    event_threat_detection_custom_module_path(
        organization: str, location: str, event_threat_detection_custom_module: str
    ) -> str

Returns a fully-qualified event_threat_detection_custom_module string.

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
`SecurityCenterManagementAsyncClient` | The constructed client.  
  
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
`SecurityCenterManagementAsyncClient` | The constructed client.  
  
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
`SecurityCenterManagementAsyncClient` | The constructed client.  
  
### get_effective_event_threat_detection_custom_module
    
    
    get_effective_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.EffectiveEventThreatDetectionCustomModule
    )

Gets the effective Event Threat Detection custom module at the given level.

The difference between an xref_EffectiveEventThreatDetectionCustomModule and an xref_EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_get_effective_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_effective_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_get_effective_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule.  
`name` |  ``str``   
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: - `organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}` \- `folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}` \- `projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EffectiveEventThreatDetectionCustomModule)` | The representation of an EventThreatDetectionCustomModule at a given level, taking hierarchy into account and resolving various fields accordingly. For example, if the module is enabled at the ancestor level, then effective modules at all descendant levels will have their enablement state set to ENABLED. Similarly, if module.inherited is set, then the effective module's configuration will reflect the ancestor's configuration.  
  
### get_effective_security_health_analytics_custom_module
    
    
    get_effective_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.EffectiveSecurityHealthAnalyticsCustomModule
    )

Gets details of a single xref_EffectiveSecurityHealthAnalyticsCustomModule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_get_effective_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_effective_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_get_effective_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule.  
`name` |  ``str``   
Required. The full resource name of the custom module, specified in one of the following formats: - `organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}` \- `folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}` \- `projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EffectiveSecurityHealthAnalyticsCustomModule)` | The representation of a Security Health Analytics custom module at a specified level of the resource hierarchy: organization, folder, or project. If a custom module is inherited from an ancestor organization or folder, then the enablement state is set to the value that is effective in the parent, not to INHERITED. For example, if the module is enabled in an organization or folder, then the effective enablement state for the module is ENABLED in all descendant folders or projects.  
  
### get_event_threat_detection_custom_module
    
    
    get_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.GetEventThreatDetectionCustomModuleRequest,
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.EventThreatDetectionCustomModule
    )

Gets an Event Threat Detection custom module.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_get_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEventThreatDetectionCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_get_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.GetEventThreatDetectionCustomModule.  
`name` |  ``str``   
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: - `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` \- `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` \- `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule)` | A Security Command Center resource that contains the configuration and enablement state of a custom module, which enables Event Threat Detection to write certain findings to Security Command Center.  
  
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
  
### get_security_center_service
    
    
    get_security_center_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.GetSecurityCenterServiceRequest,
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityCenterService
    )

Gets service settings for the specified Security Command Center service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_get_security_center_service():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetSecurityCenterServiceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_security_center_service](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_get_security_center_service)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.GetSecurityCenterServiceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetSecurityCenterServiceRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.GetSecurityCenterService.  
`name` |  ``str``   
Required. The Security Command Center service to retrieve, in one of the following formats: - organizations/{organization}/locations/{location}/securityCenterServices/{service} - folders/{folder}/locations/{location}/securityCenterServices/{service} - projects/{project}/locations/{location}/securityCenterServices/{service} The following values are valid for `{service}`: - `container-threat-detection` \- `event-threat-detection` \- `security-health-analytics` \- `vm-threat-detection` \- `web-security-scanner` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SecurityCenterService](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityCenterService)` | Represents a particular Security Command Center service. This includes settings information such as top-level enablement in addition to individual module settings. Service settings can be configured at the organization, folder, or project level. Service settings at the organization or folder level are inherited by those in descendant folders and projects.  
  
### get_security_health_analytics_custom_module
    
    
    get_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityHealthAnalyticsCustomModule
    )

Retrieves a xref_SecurityHealthAnalyticsCustomModule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_get_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_get_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule.  
`name` |  ``str``   
Required. Name of the resource, in the format `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the descendant folders and projects.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.securitycentermanagement_v1.services.security_center_management.transports.base.SecurityCenterManagementTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_descendant_event_threat_detection_custom_modules
    
    
    list_descendant_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager
    )

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_descendant_event_threat_detection_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_descendant_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_descendant_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules.  
`parent` |  ``str``   
Required. Name of parent to list custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_descendant_security_health_analytics_custom_modules
    
    
    list_descendant_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager
    )

Returns a list of all resident xref_SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_descendant_security_health_analytics_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_descendant_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_descendant_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules.  
`parent` |  ``str``   
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_effective_event_threat_detection_custom_modules
    
    
    list_effective_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager
    )

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_effective_event_threat_detection_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_effective_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_effective_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules.  
`parent` |  ``str``   
Required. Name of parent to list effective custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_effective_security_health_analytics_custom_modules
    
    
    list_effective_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager
    )

Returns a list of all xref_EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_effective_security_health_analytics_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_effective_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_effective_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules.  
`parent` |  ``str``   
Required. Name of parent to list effective custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_event_threat_detection_custom_modules
    
    
    list_event_threat_detection_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListEventThreatDetectionCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEventThreatDetectionCustomModulesAsyncPager
    )

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_event_threat_detection_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_event_threat_detection_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_event_threat_detection_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListEventThreatDetectionCustomModules.  
`parent` |  ``str``   
Required. Name of parent to list custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEventThreatDetectionCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEventThreatDetectionCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListEventThreatDetectionCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_security_center_services
    
    
    list_security_center_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListSecurityCenterServicesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityCenterServicesAsyncPager
    )

Returns a list of all Security Command Center services for the given parent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_security_center_services():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_security_center_services](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_security_center_services)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListSecurityCenterServices.  
`parent` |  ``str``   
Required. The name of the parent to list Security Command Center services, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityCenterServicesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityCenterServicesAsyncPager)` | Response message for SecurityCenterManagement.ListSecurityCenterServices. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_security_health_analytics_custom_modules
    
    
    list_security_health_analytics_custom_modules(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
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
        google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager
    )

Returns a list of all xref_SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_list_security_health_analytics_custom_modules():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_security_health_analytics_custom_modules](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_list_security_health_analytics_custom_modules)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules.  
`parent` |  ``str``   
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `folders/{folder}/locations/{location}` \- `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager)` | Response message for SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_finding_path
    
    
    parse_finding_path(path: str) -> typing.Dict[str, str]

Parses a finding path into its component segments.

### parse_security_center_service_path
    
    
    parse_security_center_service_path(path: str) -> typing.Dict[str, str]

Parses a security_center_service path into its component segments.

### parse_security_health_analytics_custom_module_path
    
    
    parse_security_health_analytics_custom_module_path(
        path: str,
    ) -> typing.Dict[str, str]

Parses a security_health_analytics_custom_module path into its component segments.

### security_center_service_path
    
    
    security_center_service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified security_center_service string.

### security_health_analytics_custom_module_path
    
    
    security_health_analytics_custom_module_path(
        organization: str, location: str, security_health_analytics_custom_module: str
    ) -> str

Returns a fully-qualified security_health_analytics_custom_module string.

### simulate_security_health_analytics_custom_module
    
    
    simulate_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        custom_config: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.CustomConfig
        ] = None,
        resource: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
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
        google.cloud.securitycentermanagement_v1.types.security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse
    )

Simulates the result of using a xref_SecurityHealthAnalyticsCustomModule to check a resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_simulate_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        resource = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SimulatedResource](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource.html)()
        resource.resource_type = "resource_type_value"
    
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.html)(
            parent="parent_value",
            resource=resource,
        )
    
        # Make the request
        response = await client.[simulate_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_simulate_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule. The maximum size of the request is 4 MiB.  
`parent` |  ``str``   
Required. The relative resource name of the organization, project, or folder. For more information about relative resource names, see `AIP-122: Resource names <https://google.aip.dev/122>`__. Example: `organizations/{organization_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`custom_config` |  `[CustomConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.CustomConfig)`   
Required. The custom configuration that you need to test. This corresponds to the `custom_config` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `[SimulatedResource](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource)`   
Required. Resource data to simulate custom module against. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | Response message for SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule.  
  
### update_event_threat_detection_custom_module
    
    
    update_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        event_threat_detection_custom_module: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.EventThreatDetectionCustomModule
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
    ) -> (
        google.cloud.securitycentermanagement_v1.types.security_center_management.EventThreatDetectionCustomModule
    )

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_update_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateEventThreatDetectionCustomModuleRequest.html)(
        )
    
        # Make the request
        response = await client.[update_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_update_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Message for updating a EventThreatDetectionCustomModule  
`event_threat_detection_custom_module` |  `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule)`   
Required. The module being updated. This corresponds to the `event_threat_detection_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The fields to update. If omitted, then all fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule)` | A Security Command Center resource that contains the configuration and enablement state of a custom module, which enables Event Threat Detection to write certain findings to Security Command Center.  
  
### update_security_center_service
    
    
    update_security_center_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.UpdateSecurityCenterServiceRequest,
                dict,
            ]
        ] = None,
        *,
        security_center_service: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityCenterService
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
    ) -> (
        google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityCenterService
    )

Updates a Security Command Center service using the given update mask.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_update_security_center_service():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateSecurityCenterServiceRequest.html)(
        )
    
        # Make the request
        response = await client.[update_security_center_service](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_update_security_center_service)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateSecurityCenterServiceRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.UpdateSecurityCenterService.  
`security_center_service` |  `[SecurityCenterService](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityCenterService)`   
Required. The updated service. This corresponds to the `security_center_service` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The fields to update. Accepts the following values: - `intended_enablement_state` \- `modules` If omitted, then all eligible fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SecurityCenterService](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityCenterService)` | Represents a particular Security Command Center service. This includes settings information such as top-level enablement in addition to individual module settings. Service settings can be configured at the organization, folder, or project level. Service settings at the organization or folder level are inherited by those in descendant folders and projects.  
  
### update_security_health_analytics_custom_module
    
    
    update_security_health_analytics_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        security_health_analytics_custom_module: typing.Optional[
            google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityHealthAnalyticsCustomModule
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
    ) -> (
        google.cloud.securitycentermanagement_v1.types.security_center_management.SecurityHealthAnalyticsCustomModule
    )

Updates the xref_SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_update_security_health_analytics_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest.html)(
        )
    
        # Make the request
        response = await client.[update_security_health_analytics_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_update_security_health_analytics_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule.  
`security_health_analytics_custom_module` |  `SecurityHealthAnalyticsCustomModule`   
Required. The resource being updated. This corresponds to the `security_health_analytics_custom_module` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The fields to update. The following values are valid: - `custom_config` \- `enablement_state` If you omit this field or set it to the wildcard value `*`, then all eligible fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule)` | Represents an instance of a Security Health Analytics custom module, including its full module name, display name, enablement state, and last updated time. You can create a custom module at the organization, folder, or project level. Custom modules that you create at the organization or folder level are inherited by the descendant folders and projects.  
  
### validate_event_threat_detection_custom_module
    
    
    validate_event_threat_detection_custom_module(
        request: typing.Optional[
            typing.Union[
                google.cloud.securitycentermanagement_v1.types.security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
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
    ) -> (
        google.cloud.securitycentermanagement_v1.types.security_center_management.ValidateEventThreatDetectionCustomModuleResponse
    )

Validates the given Event Threat Detection custom module.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest)
    
    async def sample_validate_event_threat_detection_custom_module():
        # Create a client
        client = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[SecurityCenterManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [securitycentermanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest).[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleRequest.html)(
            parent="parent_value",
            raw_text="raw_text_value",
            type_="type__value",
        )
    
        # Make the request
        response = await client.[validate_event_threat_detection_custom_module](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.services.security_center_management.SecurityCenterManagementAsyncClient.html#google_cloud_securitycentermanagement_v1_services_security_center_management_SecurityCenterManagementAsyncClient_validate_event_threat_detection_custom_module)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleRequest), dict]]`   
The request object. Request message for SecurityCenterManagement.ValidateEventThreatDetectionCustomModule.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-securitycentermanagement/latest/google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleResponse)` | Response message for SecurityCenterManagement.ValidateEventThreatDetectionCustomModule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
