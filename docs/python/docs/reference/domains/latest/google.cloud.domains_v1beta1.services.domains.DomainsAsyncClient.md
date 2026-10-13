---
url: https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient
title: Class DomainsAsyncClient (1.15.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:41.931606+00:00
---

# Class DomainsAsyncClient (1.15.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DomainsAsyncClient (1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.5  1.6.0  1.5.2  1.4.1  1.3.0  1.2.3  1.1.3  1.0.0  0.4.3  0.3.0  0.2.3  0.1.0 
    
    
    DomainsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.domains_v1beta1.services.domains.transports.base.DomainsTransport,
                typing.Callable[
                    [...],
                    google.cloud.domains_v1beta1.services.domains.transports.base.DomainsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Cloud Domains API enables management and configuration of domain names.

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
`DomainsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DomainsAsyncClient
    
    
    DomainsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.domains_v1beta1.services.domains.transports.base.DomainsTransport,
                typing.Callable[
                    [...],
                    google.cloud.domains_v1beta1.services.domains.transports.base.DomainsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the domains async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DomainsTransport,Callable[..., DomainsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DomainsTransport constructor. If set to None, a transport is chosen automatically.  
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

### configure_contact_settings
    
    
    configure_contact_settings(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ConfigureContactSettingsRequest,
                dict,
            ]
        ] = None,
        *,
        registration: typing.Optional[str] = None,
        contact_settings: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.ContactSettings
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

Updates a `Registration`'s contact settings. Some changes require confirmation by the domain's registrant contact .
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_configure_contact_settings():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ConfigureContactSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureContactSettingsRequest.html)(
            registration="registration_value",
        )
    
        # Make the request
        operation = await client.[configure_contact_settings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_configure_contact_settings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ConfigureContactSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureContactSettingsRequest), dict]]`   
The request object. Request for the `ConfigureContactSettings` method.  
`registration` |  ``str``   
Required. The name of the `Registration` whose contact settings are being updated, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`contact_settings` |  `[ContactSettings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ContactSettings)`   
Fields of the `ContactSettings` to update. This corresponds to the `contact_settings` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the registrant contact is being updated, the `update_mask` is `"registrant_contact"`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### configure_dns_settings
    
    
    configure_dns_settings(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ConfigureDnsSettingsRequest, dict
            ]
        ] = None,
        *,
        registration: typing.Optional[str] = None,
        dns_settings: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.DnsSettings
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

Updates a `Registration`'s DNS settings.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_configure_dns_settings():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureDnsSettingsRequest.html)(
            registration="registration_value",
        )
    
        # Make the request
        operation = await client.[configure_dns_settings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_configure_dns_settings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ConfigureDnsSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureDnsSettingsRequest), dict]]`   
The request object. Request for the `ConfigureDnsSettings` method.  
`registration` |  ``str``   
Required. The name of the `Registration` whose DNS settings are being updated, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`dns_settings` |  `[DnsSettings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.DnsSettings)`   
Fields of the `DnsSettings` to update. This corresponds to the `dns_settings` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the name servers are being updated for an existing Custom DNS configuration, the `update_mask` is `"custom_dns.name_servers"`. When changing the DNS provider from one type to another, pass the new provider's field name as part of the field mask. For example, when changing from a Google Domains DNS configuration to a Custom DNS configuration, the `update_mask` is `"custom_dns"`. // This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### configure_management_settings
    
    
    configure_management_settings(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ConfigureManagementSettingsRequest,
                dict,
            ]
        ] = None,
        *,
        registration: typing.Optional[str] = None,
        management_settings: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.ManagementSettings
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

Updates a `Registration`'s management settings.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_configure_management_settings():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ConfigureManagementSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureManagementSettingsRequest.html)(
            registration="registration_value",
        )
    
        # Make the request
        operation = await client.[configure_management_settings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_configure_management_settings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ConfigureManagementSettingsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ConfigureManagementSettingsRequest), dict]]`   
The request object. Request for the `ConfigureManagementSettings` method.  
`registration` |  ``str``   
Required. The name of the `Registration` whose management settings are being updated, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`management_settings` |  `[ManagementSettings](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ManagementSettings)`   
Fields of the `ManagementSettings` to update. This corresponds to the `management_settings` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the transfer lock is being updated, the `update_mask` is `"transfer_lock_state"`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### delete_registration
    
    
    delete_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.DeleteRegistrationRequest, dict
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

Deletes a `Registration` resource.

This method works on any `Registration` resource using `Subscription or Commitment billing </domains/pricing#billing-models>`__, provided that the resource was created at least 1 day in the past.

For `Registration` resources using `Monthly billing </domains/pricing#billing-models>`__, this method works if:

  * `state` is `EXPORTED` with `expire_time` in the past
  * `state` is `REGISTRATION_FAILED`
  * `state` is `TRANSFER_FAILED`



When an active registration is successfully deleted, you can continue to use the domain in `Google Domains <https://domains.google/>`__ until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_delete_registration():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[DeleteRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.DeleteRegistrationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_delete_registration)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.DeleteRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.DeleteRegistrationRequest), dict]]`   
The request object. Request for the `DeleteRegistration` method.  
`name` |  ``str``   
Required. The name of the `Registration` to delete, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### export_registration
    
    
    export_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ExportRegistrationRequest, dict
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

Exports a `Registration` resource, such that it is no longer managed by Cloud Domains.

When an active domain is successfully exported, you can continue to use the domain in `Google Domains <https://domains.google/>`__ until it expires. The calling user becomes the domain's sole owner in Google Domains, and permissions for the domain are subsequently managed there. The domain does not renew automatically unless the new owner sets up billing in Google Domains.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_export_registration():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ExportRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ExportRegistrationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[export_registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_export_registration)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ExportRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ExportRegistrationRequest), dict]]`   
The request object. Request for the `ExportRegistration` method.  
`name` |  ``str``   
Required. The name of the `Registration` to export, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
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
`DomainsAsyncClient` | The constructed client.  
  
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
`DomainsAsyncClient` | The constructed client.  
  
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
`DomainsAsyncClient` | The constructed client.  
  
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
  
### get_registration
    
    
    get_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.GetRegistrationRequest, dict
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
    ) -> google.cloud.domains_v1beta1.types.domains.Registration

Gets the details of a `Registration` resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_get_registration():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[GetRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.GetRegistrationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_get_registration)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.GetRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.GetRegistrationRequest), dict]]`   
The request object. Request for the `GetRegistration` method.  
`name` |  ``str``   
Required. The name of the `Registration` to get, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration)` | The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.domains_v1beta1.services.domains.transports.base.DomainsTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_registrations
    
    
    list_registrations(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ListRegistrationsRequest, dict
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
    ) -> google.cloud.domains_v1beta1.services.domains.pagers.ListRegistrationsAsyncPager

Lists the `Registration` resources in a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_list_registrations():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ListRegistrationsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ListRegistrationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_registrations](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_list_registrations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ListRegistrationsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ListRegistrationsRequest), dict]]`   
The request object. Request for the `ListRegistrations` method.  
`parent` |  ``str``   
Required. The project and location from which to list `Registration`\ s, specified in the format `projects/_/locations/_`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.services.domains.pagers.ListRegistrationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.pagers.ListRegistrationsAsyncPager)` | Response for the ListRegistrations method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_registration_path
    
    
    parse_registration_path(path: str) -> typing.Dict[str, str]

Parses a registration path into its component segments.

### register_domain
    
    
    register_domain(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.RegisterDomainRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        registration: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.Registration
        ] = None,
        yearly_price: typing.Optional[google.type.money_pb2.Money] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Registers a new domain name and creates a corresponding `Registration` resource.

Call `RetrieveRegisterParameters` first to check availability of the domain name and determine parameters like price that are needed to build a call to this method.

A successful call creates a `Registration` resource in state `REGISTRATION_PENDING`, which resolves to `ACTIVE` within 1-2 minutes, indicating that the domain was successfully registered. If the resource ends up in state `REGISTRATION_FAILED`, it indicates that the domain was not registered successfully, and you can safely delete the resource and retry registration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_register_domain():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        registration = domains_v1beta1.[Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration.html)()
        registration.domain_name = "domain_name_value"
        registration.contact_settings.privacy = "REDACTED_CONTACT_DATA"
        registration.contact_settings.registrant_contact.email = "email_value"
        registration.contact_settings.registrant_contact.phone_number = "phone_number_value"
        registration.contact_settings.admin_contact.email = "email_value"
        registration.contact_settings.admin_contact.phone_number = "phone_number_value"
        registration.contact_settings.technical_contact.email = "email_value"
        registration.contact_settings.technical_contact.phone_number = "phone_number_value"
    
        request = domains_v1beta1.[RegisterDomainRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RegisterDomainRequest.html)(
            parent="parent_value",
            registration=registration,
        )
    
        # Make the request
        operation = await client.[register_domain](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_register_domain)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.RegisterDomainRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RegisterDomainRequest), dict]]`   
The request object. Request for the `RegisterDomain` method.  
`parent` |  ``str``   
Required. The parent resource of the `Registration`. Must be in the format `projects/_/locations/_`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`registration` |  `[Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration)`   
Required. The complete `Registration` resource to be created. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`yearly_price` |  ``google.type.money_pb2.Money``   
Required. Yearly price to register or renew the domain. The value that should be put here can be obtained from RetrieveRegisterParameters or SearchDomains calls. This corresponds to the `yearly_price` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### registration_path
    
    
    registration_path(project: str, location: str, registration: str) -> str

Returns a fully-qualified registration string.

### reset_authorization_code
    
    
    reset_authorization_code(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.ResetAuthorizationCodeRequest,
                dict,
            ]
        ] = None,
        *,
        registration: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.domains_v1beta1.types.domains.AuthorizationCode

Resets the authorization code of the `Registration` to a new random string.

You can call this method only after 60 days have elapsed since the initial domain registration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_reset_authorization_code():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ResetAuthorizationCodeRequest.html)(
            registration="registration_value",
        )
    
        # Make the request
        response = await client.[reset_authorization_code](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_reset_authorization_code)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.ResetAuthorizationCodeRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.ResetAuthorizationCodeRequest), dict]]`   
The request object. Request for the `ResetAuthorizationCode` method.  
`registration` |  ``str``   
Required. The name of the `Registration` whose authorization code is being reset, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.AuthorizationCode](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.AuthorizationCode)` | Defines an authorization code.  
  
### retrieve_authorization_code
    
    
    retrieve_authorization_code(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.RetrieveAuthorizationCodeRequest,
                dict,
            ]
        ] = None,
        *,
        registration: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.domains_v1beta1.types.domains.AuthorizationCode

Gets the authorization code of the `Registration` for the purpose of transferring the domain to another registrar.

You can call this method only after 60 days have elapsed since the initial domain registration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_retrieve_authorization_code():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveAuthorizationCodeRequest.html)(
            registration="registration_value",
        )
    
        # Make the request
        response = await client.[retrieve_authorization_code](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_retrieve_authorization_code)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.RetrieveAuthorizationCodeRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveAuthorizationCodeRequest), dict]]`   
The request object. Request for the `RetrieveAuthorizationCode` method.  
`registration` |  ``str``   
Required. The name of the `Registration` whose authorization code is being retrieved, in the format `projects/_/locations/_ /registrations/*`. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.AuthorizationCode](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.AuthorizationCode)` | Defines an authorization code.  
  
### retrieve_register_parameters
    
    
    retrieve_register_parameters(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.RetrieveRegisterParametersRequest,
                dict,
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        domain_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.domains_v1beta1.types.domains.RetrieveRegisterParametersResponse

Gets parameters needed to register a new domain name, including price and up-to-date availability. Use the returned values to call `RegisterDomain`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_retrieve_register_parameters():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[RetrieveRegisterParametersRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveRegisterParametersRequest.html)(
            domain_name="domain_name_value",
            location="location_value",
        )
    
        # Make the request
        response = await client.[retrieve_register_parameters](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_retrieve_register_parameters)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.RetrieveRegisterParametersRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveRegisterParametersRequest), dict]]`   
The request object. Request for the `RetrieveRegisterParameters` method.  
`location` |  ``str``   
Required. The location. Must be in the format `projects/_/locations/_`. This corresponds to the `location` field on the `request` instance; if `request` is provided, this should not be set.  
`domain_name` |  ``str``   
Required. The domain name. Unicode domain names must be expressed in Punycode format. This corresponds to the `domain_name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.RetrieveRegisterParametersResponse](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveRegisterParametersResponse)` | Response for the RetrieveRegisterParameters method.  
  
### retrieve_transfer_parameters
    
    
    retrieve_transfer_parameters(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.RetrieveTransferParametersRequest,
                dict,
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        domain_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.domains_v1beta1.types.domains.RetrieveTransferParametersResponse

Gets parameters needed to transfer a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Use the returned values to call `TransferDomain`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_retrieve_transfer_parameters():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[RetrieveTransferParametersRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveTransferParametersRequest.html)(
            domain_name="domain_name_value",
            location="location_value",
        )
    
        # Make the request
        response = await client.[retrieve_transfer_parameters](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_retrieve_transfer_parameters)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.RetrieveTransferParametersRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveTransferParametersRequest), dict]]`   
The request object. Request for the `RetrieveTransferParameters` method.  
`location` |  ``str``   
Required. The location. Must be in the format `projects/_/locations/_`. This corresponds to the `location` field on the `request` instance; if `request` is provided, this should not be set.  
`domain_name` |  ``str``   
Required. The domain name. Unicode domain names must be expressed in Punycode format. This corresponds to the `domain_name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.RetrieveTransferParametersResponse](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.RetrieveTransferParametersResponse)` | Response for the RetrieveTransferParameters method.  
  
### search_domains
    
    
    search_domains(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.SearchDomainsRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.domains_v1beta1.types.domains.SearchDomainsResponse

Searches for available domain names similar to the provided query.

Availability results from this method are approximate; call `RetrieveRegisterParameters` on a domain before registering to confirm availability.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_search_domains():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[SearchDomainsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.SearchDomainsRequest.html)(
            query="query_value",
            location="location_value",
        )
    
        # Make the request
        response = await client.[search_domains](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_search_domains)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.SearchDomainsRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.SearchDomainsRequest), dict]]`   
The request object. Request for the `SearchDomains` method.  
`location` |  ``str``   
Required. The location. Must be in the format `projects/_/locations/_`. This corresponds to the `location` field on the `request` instance; if `request` is provided, this should not be set.  
`query` |  ``str``   
Required. String used to search for available domain names. This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.domains_v1beta1.types.SearchDomainsResponse](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.SearchDomainsResponse)` | Response for the SearchDomains method.  
  
### transfer_domain
    
    
    transfer_domain(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.TransferDomainRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        registration: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.Registration
        ] = None,
        yearly_price: typing.Optional[google.type.money_pb2.Money] = None,
        authorization_code: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.AuthorizationCode
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

Transfers a domain name from another registrar to Cloud Domains. For domains managed by Google Domains, transferring to Cloud Domains is not supported.

Before calling this method, go to the domain's current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call `RetrieveTransferParameters` to confirm that the domain is unlocked and to get values needed to build a call to this method.

A successful call creates a `Registration` resource in state `TRANSFER_PENDING`. It can take several days to complete the transfer process. The registrant can often speed up this process by approving the transfer through the current registrar, either by clicking a link in an email from the registrar or by visiting the registrar's website.

A few minutes after transfer approval, the resource transitions to state `ACTIVE`, indicating that the transfer was successful. If the transfer is rejected or the request expires without being approved, the resource can end up in state `TRANSFER_FAILED`. If transfer fails, you can safely delete the resource and retry the transfer.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_transfer_domain():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        registration = domains_v1beta1.[Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration.html)()
        registration.domain_name = "domain_name_value"
        registration.contact_settings.privacy = "REDACTED_CONTACT_DATA"
        registration.contact_settings.registrant_contact.email = "email_value"
        registration.contact_settings.registrant_contact.phone_number = "phone_number_value"
        registration.contact_settings.admin_contact.email = "email_value"
        registration.contact_settings.admin_contact.phone_number = "phone_number_value"
        registration.contact_settings.technical_contact.email = "email_value"
        registration.contact_settings.technical_contact.phone_number = "phone_number_value"
    
        request = domains_v1beta1.[TransferDomainRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.TransferDomainRequest.html)(
            parent="parent_value",
            registration=registration,
        )
    
        # Make the request
        operation = await client.[transfer_domain](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_transfer_domain)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.TransferDomainRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.TransferDomainRequest), dict]]`   
The request object. Request for the `TransferDomain` method.  
`parent` |  ``str``   
Required. The parent resource of the `Registration`. Must be in the format `projects/_/locations/_`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`registration` |  `[Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration)`   
Required. The complete `Registration` resource to be created. You can leave `registration.dns_settings` unset to import the domain's current DNS configuration from its current registrar. Use this option only if you are sure that the domain's current DNS service does not cease upon transfer, as is often the case for DNS services provided for free by the registrar. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`yearly_price` |  ``google.type.money_pb2.Money``   
Required. Acknowledgement of the price to transfer or renew the domain for one year. Call `RetrieveTransferParameters` to obtain the price, which you must acknowledge. This corresponds to the `yearly_price` field on the `request` instance; if `request` is provided, this should not be set.  
`authorization_code` |  `[AuthorizationCode](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.AuthorizationCode)`   
The domain's transfer authorization code. You can obtain this from the domain's current registrar. This corresponds to the `authorization_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
### update_registration
    
    
    update_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.domains_v1beta1.types.domains.UpdateRegistrationRequest, dict
            ]
        ] = None,
        *,
        registration: typing.Optional[
            google.cloud.domains_v1beta1.types.domains.Registration
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

Updates select fields of a `Registration` resource, notably `labels`. To update other fields, use the appropriate custom update method:

  * To update management settings, see `ConfigureManagementSettings`
  * To update DNS configuration, see `ConfigureDnsSettings`
  * To update contact information, see `ConfigureContactSettings`


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import domains_v1beta1
    
    async def sample_update_registration():
        # Create a client
        client = domains_v1beta1.[DomainsAsyncClient](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = domains_v1beta1.[UpdateRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.UpdateRegistrationRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.services.domains.DomainsAsyncClient.html#google_cloud_domains_v1beta1_services_domains_DomainsAsyncClient_update_registration)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.domains_v1beta1.types.UpdateRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.UpdateRegistrationRequest), dict]]`   
The request object. Request for the `UpdateRegistration` method.  
`registration` |  `[Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration)`   
Fields of the `Registration` to update. This corresponds to the `registration` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The field mask describing which fields to update as a comma-separated list. For example, if only the labels are being updated, the `update_mask` is `"labels"`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Registration](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1beta1.types.Registration) The Registration resource facilitates managing and configuring domain name registrations. There are several ways to create a new Registration resource: To create a new Registration resource, find a suitable domain name by calling the SearchDomains method with a query to see available domain name options. After choosing a name, call RetrieveRegisterParameters to ensure availability and obtain information like pricing, which is needed to build a call to RegisterDomain. Another way to create a new Registration is to transfer an existing domain from another registrar. First, go to the current registrar to unlock the domain for transfer and retrieve the domain's transfer authorization code. Then call RetrieveTransferParameters to confirm that the domain is unlocked and to get values needed to build a call to TransferDomain.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
