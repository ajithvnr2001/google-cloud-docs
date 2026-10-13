---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient
title: Class AuthProviderServiceAsyncClient (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:18.602781+00:00
---

# Class AuthProviderServiceAsyncClient (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AuthProviderServiceAsyncClient (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    AuthProviderServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.agentidentity_v1beta.services.auth_provider_service.transports.base.AuthProviderServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.agentidentity_v1beta.services.auth_provider_service.transports.base.AuthProviderServiceTransport,
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
`AuthProviderServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AuthProviderServiceAsyncClient
    
    
    AuthProviderServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.agentidentity_v1beta.services.auth_provider_service.transports.base.AuthProviderServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.agentidentity_v1beta.services.auth_provider_service.transports.base.AuthProviderServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auth provider service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AuthProviderServiceTransport,Callable[..., AuthProviderServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the AuthProviderServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### access_summary_path
    
    
    access_summary_path(project: str, location: str, access_summary: str) -> str

Returns a fully-qualified access_summary string.

### auth_provider_path
    
    
    auth_provider_path(project: str, location: str, auth_provider: str) -> str

Returns a fully-qualified auth_provider string.

### authorization_path
    
    
    authorization_path(
        project: str, location: str, auth_provider: str, authorization: str
    ) -> str

Returns a fully-qualified authorization string.

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

### create_auth_provider
    
    
    create_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.CreateAuthProviderRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        auth_provider: typing.Optional[
            google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider
        ] = None,
        auth_provider_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Creates a new AuthProvider in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_create_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[CreateAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.CreateAuthProviderRequest.html)(
            parent="parent_value",
            auth_provider_id="auth_provider_id_value",
        )
    
        # Make the request
        response = await client.[create_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_create_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.CreateAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.CreateAuthProviderRequest), dict]]`   
The request object. Message for creating a AuthProvider  
`parent` |  ``str``   
Required. The parent resource where the AuthProvider is created. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`auth_provider` |  `[AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)`   
Required. The AuthProvider to create. This corresponds to the `auth_provider` field on the `request` instance; if `request` is provided, this should not be set.  
`auth_provider_id` |  ``str``   
Required. The ID to use for the AuthProvider, which will become the final segment of the AuthProvider's resource name. This value should be 1-63 characters, and valid characters are /`a-z][0-9]`-/. The first character must be a lowercase letter, and the last character must be a lowercase letter or a number. This corresponds to the `auth_provider_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
### delete_auth_provider
    
    
    delete_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.DeleteAuthProviderRequest,
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

Deletes a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_delete_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[DeleteAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DeleteAuthProviderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_delete_auth_provider)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.DeleteAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DeleteAuthProviderRequest), dict]]`   
The request object. Message for deleting a AuthProvider  
`name` |  ``str``   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_authorization
    
    
    delete_authorization(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.DeleteAuthorizationRequest,
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

Deletes a single Authorization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_delete_authorization():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[DeleteAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DeleteAuthorizationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_authorization](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_delete_authorization)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.DeleteAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DeleteAuthorizationRequest), dict]]`   
The request object. Message for deleting an Authorization  
`name` |  ``str``   
Required. The name of the Authorization to delete. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}/authorizations/{authorization} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### disable_auth_provider
    
    
    disable_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.DisableAuthProviderRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Disables a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_disable_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[DisableAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DisableAuthProviderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[disable_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_disable_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.DisableAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.DisableAuthProviderRequest), dict]]`   
The request object. Message for disabling an AuthProvider  
`name` |  ``str``   
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
### enable_auth_provider
    
    
    enable_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.EnableAuthProviderRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Enables a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_enable_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[EnableAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.EnableAuthProviderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[enable_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_enable_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.EnableAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.EnableAuthProviderRequest), dict]]`   
The request object. Message for enabling an AuthProvider  
`name` |  ``str``   
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
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
`AuthProviderServiceAsyncClient` | The constructed client.  
  
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
`AuthProviderServiceAsyncClient` | The constructed client.  
  
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
`AuthProviderServiceAsyncClient` | The constructed client.  
  
### get_access_summary
    
    
    get_access_summary(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.GetAccessSummaryRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AccessSummary

Gets details of a single AccessSummary.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_get_access_summary():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[GetAccessSummaryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAccessSummaryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_access_summary](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_get_access_summary)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.GetAccessSummaryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAccessSummaryRequest), dict]]`   
The request object. Message for getting a AccessSummary  
`name` |  ``str``   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AccessSummary](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AccessSummary)` | Message describing AccessSummary object  
  
### get_auth_provider
    
    
    get_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.GetAuthProviderRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Gets details of a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_get_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[GetAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAuthProviderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_get_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.GetAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAuthProviderRequest), dict]]`   
The request object. Message for getting a AuthProvider  
`name` |  ``str``   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
### get_authorization
    
    
    get_authorization(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.GetAuthorizationRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.Authorization

Gets details of a single Authorization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_get_authorization():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[GetAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAuthorizationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_authorization](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_get_authorization)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.GetAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.GetAuthorizationRequest), dict]]`   
The request object. Message for getting a Authorization  
`name` |  ``str``   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.Authorization](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.Authorization)` | Message describing Authorization object  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.agentidentity_v1beta.services.auth_provider_service.transports.base.AuthProviderServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_access_summaries
    
    
    list_access_summaries(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.ListAccessSummariesRequest,
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
        google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAccessSummariesAsyncPager
    )

Lists AccessSummaries in a given project and location. Supported Filters:

  * `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_list_access_summaries():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[ListAccessSummariesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAccessSummariesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_access_summaries](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_list_access_summaries)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.ListAccessSummariesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAccessSummariesRequest), dict]]`   
The request object. Message for requesting list of AccessSummaries  
`parent` |  ``str``   
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAccessSummariesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAccessSummariesAsyncPager)` | Message for response to listing AccessSummaries Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_auth_providers
    
    
    list_auth_providers(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.ListAuthProvidersRequest,
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
        google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthProvidersAsyncPager
    )

Lists AuthProviders in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_list_auth_providers():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[ListAuthProvidersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAuthProvidersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_auth_providers](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_list_auth_providers)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.ListAuthProvidersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAuthProvidersRequest), dict]]`   
The request object. Message for requesting list of AuthProviders  
`parent` |  ``str``   
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthProvidersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthProvidersAsyncPager)` | Message for response to listing AuthProviders Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_authorizations
    
    
    list_authorizations(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.ListAuthorizationsRequest,
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
        google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthorizationsAsyncPager
    )

Lists Authorizations in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_list_authorizations():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[ListAuthorizationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAuthorizationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_authorizations](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_list_authorizations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.ListAuthorizationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.ListAuthorizationsRequest), dict]]`   
The request object. Message for requesting list of Authorizations  
`parent` |  ``str``   
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthorizationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.ListAuthorizationsAsyncPager)` | Message for response to listing Authorizations Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_access_summary_path
    
    
    parse_access_summary_path(path: str) -> typing.Dict[str, str]

Parses a access_summary path into its component segments.

### parse_auth_provider_path
    
    
    parse_auth_provider_path(path: str) -> typing.Dict[str, str]

Parses a auth_provider path into its component segments.

### parse_authorization_path
    
    
    parse_authorization_path(path: str) -> typing.Dict[str, str]

Parses a authorization path into its component segments.

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

### query_auth_providers
    
    
    query_auth_providers(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.QueryAuthProvidersRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        workload_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryAuthProvidersAsyncPager
    )

Queries what all auth_providers are used by a given workload_id.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_query_auth_providers():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[QueryAuthProvidersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.QueryAuthProvidersRequest.html)(
            parent="parent_value",
            workload_id="workload_id_value",
        )
    
        # Make the request
        page_result = client.[query_auth_providers](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_query_auth_providers)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.QueryAuthProvidersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.QueryAuthProvidersRequest), dict]]`   
The request object. Request message for QueryAuthProviders.  
`parent` |  ``str``   
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`workload_id` |  ``str``   
Required. The workload identifier to filter by. This corresponds to the `workload_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryAuthProvidersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryAuthProvidersAsyncPager)` | Response message for QueryAuthProviders. Iterating over this object will yield results and resolve additional pages automatically.  
  
### query_workloads
    
    
    query_workloads(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.QueryWorkloadsRequest,
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
        google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryWorkloadsAsyncPager
    )

Queries what all workloads are using a given auth_provider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_query_workloads():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[QueryWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.QueryWorkloadsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[query_workloads](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_query_workloads)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.QueryWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.QueryWorkloadsRequest), dict]]`   
The request object. Request message for QueryWorkloads.  
`name` |  ``str``   
Required. The name of the auth_provider to query. Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryWorkloadsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.pagers.QueryWorkloadsAsyncPager)` | Response message for QueryWorkloads. Iterating over this object will yield results and resolve additional pages automatically.  
  
### revoke_authorization
    
    
    revoke_authorization(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.RevokeAuthorizationRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.agentidentity_v1beta.types.auth_provider_service.RevokeAuthorizationResponse
    )

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_revoke_authorization():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[RevokeAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.RevokeAuthorizationRequest.html)(
            name="name_value",
            user_id="user_id_value",
        )
    
        # Make the request
        response = await client.[revoke_authorization](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_revoke_authorization)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.RevokeAuthorizationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.RevokeAuthorizationRequest), dict]]`   
The request object. Request message for RevokeAuthorization.  
`name` |  ``str``   
Required. The resource name of the AuthProvider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`user_id` |  ``str``   
Required. The identity of the user to revoke authorization for. This corresponds to the `user_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.RevokeAuthorizationResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.RevokeAuthorizationResponse)` | Response message for RevokeAuthorization.  
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### undelete_auth_provider
    
    
    undelete_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.UndeleteAuthProviderRequest,
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Undeletes a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_undelete_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[UndeleteAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.UndeleteAuthProviderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[undelete_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_undelete_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.UndeleteAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.UndeleteAuthProviderRequest), dict]]`   
The request object. Message for undeleting a AuthProvider  
`name` |  ``str``   
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
### update_auth_provider
    
    
    update_auth_provider(
        request: typing.Optional[
            typing.Union[
                google.cloud.agentidentity_v1beta.types.auth_provider_service.UpdateAuthProviderRequest,
                dict,
            ]
        ] = None,
        *,
        auth_provider: typing.Optional[
            google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider
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
    ) -> google.cloud.agentidentity_v1beta.types.auth_provider_service.AuthProvider

Updates the parameters of a single AuthProvider.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import agentidentity_v1beta
    
    async def sample_update_auth_provider():
        # Create a client
        client = agentidentity_v1beta.[AuthProviderServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = agentidentity_v1beta.[UpdateAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.UpdateAuthProviderRequest.html)(
        )
    
        # Make the request
        response = await client.[update_auth_provider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.services.auth_provider_service.AuthProviderServiceAsyncClient.html#google_cloud_agentidentity_v1beta_services_auth_provider_service_AuthProviderServiceAsyncClient_update_auth_provider)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.agentidentity_v1beta.types.UpdateAuthProviderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.UpdateAuthProviderRequest), dict]]`   
The request object. Message for updating a AuthProvider  
`auth_provider` |  `[AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)`   
Required. The AuthProvider resource which replaces the resource on the server. This corresponds to the `auth_provider` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the AuthProvider resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.agentidentity_v1beta.types.AuthProvider](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1beta.types.AuthProvider)` | Message describing AuthProvider object  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
