---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient
title: Class RegistryAsyncClient (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:06.734289+00:00
---

# Class RegistryAsyncClient (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RegistryAsyncClient (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 
    
    
    RegistryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Registry service allows teams to manage descriptions of APIs.

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
`RegistryTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### RegistryAsyncClient
    
    
    RegistryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the registry async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,RegistryTransport,Callable[..., RegistryTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the RegistryTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### api_deployment_path
    
    
    api_deployment_path(project: str, location: str, api: str, deployment: str) -> str

Returns a fully-qualified api_deployment string.

### api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

### api_spec_path
    
    
    api_spec_path(
        project: str, location: str, api: str, version: str, spec: str
    ) -> str

Returns a fully-qualified api_spec string.

### api_version_path
    
    
    api_version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified api_version string.

### artifact_path
    
    
    artifact_path(project: str, location: str, artifact: str) -> str

Returns a fully-qualified artifact string.

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

### create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
        ] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Creates a specified API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_create_api():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiRequest.html)(
            parent="parent_value",
            api_id="api_id_value",
        )
    
        # Make the request
        response = await client.[create_api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiRequest), dict]]`   
The request object. Request message for CreateApi.  
`parent` |  ``str``   
Required. The parent, which owns this collection of APIs. Format: `projects/_/locations/_` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api` |  `[Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)`   
Required. The API to create. This corresponds to the `api` field on the `request` instance; if `request` is provided, this should not be set.  
`api_id` |  ``str``   
Required. The ID to use for the API, which will become the final component of the API's resource name. This value should be 4-63 characters, and valid characters are /`a-z][0-9]`-/. Following AIP-162, IDs must not have the form of a UUID. This corresponds to the `api_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)` | A top-level description of an API. Produced by producers and are commitments to provide services.  
  
### create_api_deployment
    
    
    create_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
        ] = None,
        api_deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Creates a specified deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_create_api_deployment():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[CreateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiDeploymentRequest.html)(
            parent="parent_value",
            api_deployment_id="api_deployment_id_value",
        )
    
        # Make the request
        response = await client.[create_api_deployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.CreateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiDeploymentRequest), dict]]`   
The request object. Request message for CreateApiDeployment.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deployments. Format: `projects/_/locations/_ /apis/*` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api_deployment` |  `[ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)`   
Required. The deployment to create. This corresponds to the `api_deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`api_deployment_id` |  ``str``   
Required. The ID to use for the deployment, which will become the final component of the deployment's resource name. This value should be 4-63 characters, and valid characters are /`a-z][0-9]`-/. Following AIP-162, IDs must not have the form of a UUID. This corresponds to the `api_deployment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### create_api_spec
    
    
    create_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
        ] = None,
        api_spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Creates a specified spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_create_api_spec():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[CreateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiSpecRequest.html)(
            parent="parent_value",
            api_spec_id="api_spec_id_value",
        )
    
        # Make the request
        response = await client.[create_api_spec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.CreateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiSpecRequest), dict]]`   
The request object. Request message for CreateApiSpec.  
`parent` |  ``str``   
Required. The parent, which owns this collection of specs. Format: `projects/_/locations/_ /apis/_/versions/_` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api_spec` |  `[ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)`   
Required. The spec to create. This corresponds to the `api_spec` field on the `request` instance; if `request` is provided, this should not be set.  
`api_spec_id` |  ``str``   
Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /`a-z][0-9]`-/. Following AIP-162, IDs must not have the form of a UUID. This corresponds to the `api_spec_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
### create_api_version
    
    
    create_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
        ] = None,
        api_version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Creates a specified version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_create_api_version():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[CreateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiVersionRequest.html)(
            parent="parent_value",
            api_version_id="api_version_id_value",
        )
    
        # Make the request
        response = await client.[create_api_version](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.CreateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateApiVersionRequest), dict]]`   
The request object. Request message for CreateApiVersion.  
`parent` |  ``str``   
Required. The parent, which owns this collection of versions. Format: `projects/_/locations/_ /apis/*` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api_version` |  `[ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)`   
Required. The version to create. This corresponds to the `api_version` field on the `request` instance; if `request` is provided, this should not be set.  
`api_version_id` |  ``str``   
Required. The ID to use for the version, which will become the final component of the version's resource name. This value should be 1-63 characters, and valid characters are /`a-z][0-9]`-/. Following AIP-162, IDs must not have the form of a UUID. This corresponds to the `api_version_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)` | Describes a particular version of an API. ApiVersions are what consumers actually use.  
  
### create_artifact
    
    
    create_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        artifact_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Creates a specified artifact.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_create_artifact():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[CreateArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateArtifactRequest.html)(
            parent="parent_value",
            artifact_id="artifact_id_value",
        )
    
        # Make the request
        response = await client.[create_artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_artifact)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.CreateArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.CreateArtifactRequest), dict]]`   
The request object. Request message for CreateArtifact.  
`parent` |  ``str``   
Required. The parent, which owns this collection of artifacts. Format: `{parent}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`artifact` |  `[Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)`   
Required. The artifact to create. This corresponds to the `artifact` field on the `request` instance; if `request` is provided, this should not be set.  
`artifact_id` |  ``str``   
Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /`a-z][0-9]`-/. Following AIP-162, IDs must not have the form of a UUID. This corresponds to the `artifact_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)` | Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The ListArtifacts method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.  
  
### delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiRequest,
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

Removes a specified API and all of the resources that it owns.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiRequest), dict]]`   
The request object. Request message for DeleteApi.  
`name` |  ``str``   
Required. The name of the API to delete. Format: `projects/_/locations/_ /apis/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_api_deployment
    
    
    delete_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRequest,
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

Removes a specified deployment, all revisions, and all child resources (e.g., artifacts).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api_deployment():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api_deployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_deployment)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRequest), dict]]`   
The request object. Request message for DeleteApiDeployment.  
`name` |  ``str``   
Required. The name of the deployment to delete. Format: `projects/_/locations/_ /apis/_/deployments/_` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_api_deployment_revision
    
    
    delete_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Deletes a revision of a deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api_deployment_revision():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRevisionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[delete_api_deployment_revision](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_deployment_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiDeploymentRevisionRequest), dict]]`   
The request object. Request message for DeleteApiDeploymentRevision.  
`name` |  ``str``   
Required. The name of the deployment revision to be deleted, with a revision ID explicitly included. Example: `projects/sample/locations/global/apis/petstore/deployments/prod@c7cfa2a8` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### delete_api_spec
    
    
    delete_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRequest,
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

Removes a specified spec, all revisions, and all child resources (e.g., artifacts).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api_spec():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api_spec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_spec)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRequest), dict]]`   
The request object. Request message for DeleteApiSpec.  
`name` |  ``str``   
Required. The name of the spec to delete. Format: `projects/_/locations/_ /apis/_/versions/_ /specs/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_api_spec_revision
    
    
    delete_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Deletes a revision of a spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api_spec_revision():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRevisionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[delete_api_spec_revision](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_spec_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiSpecRevisionRequest), dict]]`   
The request object. Request message for DeleteApiSpecRevision.  
`name` |  ``str``   
Required. The name of the spec revision to be deleted, with a revision ID explicitly included. Example: `projects/sample/locations/global/apis/petstore/versions/1.0.0/specs/openapi.yaml@c7cfa2a8` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
### delete_api_version
    
    
    delete_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiVersionRequest,
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

Removes a specified version and all of the resources that it owns.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_api_version():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api_version](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_version)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteApiVersionRequest), dict]]`   
The request object. Request message for DeleteApiVersion.  
`name` |  ``str``   
Required. The name of the version to delete. Format: `projects/_/locations/_ /apis/_/versions/_` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_artifact
    
    
    delete_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteArtifactRequest,
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

Removes a specified artifact.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_delete_artifact():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[DeleteArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteArtifactRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_artifact)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.DeleteArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.DeleteArtifactRequest), dict]]`   
The request object. Request message for DeleteArtifact.  
`name` |  ``str``   
Required. The name of the artifact to delete. Format: `{parent}/artifacts/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
`RegistryAsyncClient` | The constructed client.  
  
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
`RegistryAsyncClient` | The constructed client.  
  
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
`RegistryAsyncClient` | The constructed client.  
  
### get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Returns a specified API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_api():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiRequest), dict]]`   
The request object. Request message for GetApi.  
`name` |  ``str``   
Required. The name of the API to retrieve. Format: `projects/_/locations/_ /apis/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)` | A top-level description of an API. Produced by producers and are commitments to provide services.  
  
### get_api_deployment
    
    
    get_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Returns a specified deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_api_deployment():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api_deployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiDeploymentRequest), dict]]`   
The request object. Request message for GetApiDeployment.  
`name` |  ``str``   
Required. The name of the deployment to retrieve. Format: `projects/_/locations/_ /apis/_/deployments/_` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### get_api_spec
    
    
    get_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Returns a specified spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_api_spec():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api_spec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecRequest), dict]]`   
The request object. Request message for GetApiSpec.  
`name` |  ``str``   
Required. The name of the spec to retrieve. Format: `projects/_/locations/_ /apis/_/versions/_ /specs/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
### get_api_spec_contents
    
    
    get_api_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified spec. If specs are stored with GZip compression, the default behavior is to return the spec uncompressed (the mime_type response field indicates the exact format returned).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_api_spec_contents():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetApiSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecContentsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api_spec_contents](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_spec_contents)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetApiSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiSpecContentsRequest), dict]]`   
The request object. Request message for GetApiSpecContents.  
`name` |  ``str``   
Required. The name of the spec whose contents should be retrieved. Format: `projects/_/locations/_ /apis/_/versions/_ /specs/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api.httpbody_pb2.HttpBody` | Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest { // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; } service ResourceService { rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); } Example with streaming methods: service CaldavService { rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.  
  
### get_api_version
    
    
    get_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiVersionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Returns a specified version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_api_version():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api_version](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetApiVersionRequest), dict]]`   
The request object. Request message for GetApiVersion.  
`name` |  ``str``   
Required. The name of the version to retrieve. Format: `projects/_/locations/_ /apis/_/versions/_` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)` | Describes a particular version of an API. ApiVersions are what consumers actually use.  
  
### get_artifact
    
    
    get_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Returns a specified artifact.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_artifact():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_artifact)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactRequest), dict]]`   
The request object. Request message for GetArtifact.  
`name` |  ``str``   
Required. The name of the artifact to retrieve. Format: `{parent}/artifacts/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)` | Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The ListArtifacts method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.  
  
### get_artifact_contents
    
    
    get_artifact_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_get_artifact_contents():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[GetArtifactContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactContentsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_artifact_contents](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_artifact_contents)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.GetArtifactContentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.GetArtifactContentsRequest), dict]]`   
The request object. Request message for GetArtifactContents.  
`name` |  ``str``   
Required. The name of the artifact whose contents should be retrieved. Format: `{parent}/artifacts/*` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api.httpbody_pb2.HttpBody` | Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest { // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; } service ResourceService { rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); } Example with streaming methods: service CaldavService { rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_api_deployment_revisions
    
    
    list_api_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
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
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager
    )

Lists all revisions of a deployment. Revisions are returned in descending order of revision creation time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_api_deployment_revisions():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_api_deployment_revisions](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_deployment_revisions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsRequest), dict]]`   
The request object. Request message for ListApiDeploymentRevisions.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager)` | Response message for ListApiDeploymentRevisionsResponse. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_api_deployments
    
    
    list_api_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
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
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager
    )

Returns matching deployments.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_api_deployments():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApiDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_api_deployments](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_deployments)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApiDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsRequest), dict]]`   
The request object. Request message for ListApiDeployments.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deployments. Format: `projects/_/locations/_ /apis/*` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager)` | Response message for ListApiDeployments. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_api_spec_revisions
    
    
    list_api_spec_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
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
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager
    )

Lists all revisions of a spec. Revisions are returned in descending order of revision creation time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_api_spec_revisions():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApiSpecRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_api_spec_revisions](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_spec_revisions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsRequest), dict]]`   
The request object. Request message for ListApiSpecRevisions.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager)` | Response message for ListApiSpecRevisionsResponse. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_api_specs
    
    
    list_api_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager

Returns matching specs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_api_specs():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApiSpecsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_api_specs](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_specs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApiSpecsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsRequest), dict]]`   
The request object. Request message for ListApiSpecs.  
`parent` |  ``str``   
Required. The parent, which owns this collection of specs. Format: `projects/_/locations/_ /apis/_/versions/_` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager)` | Response message for ListApiSpecs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_api_versions
    
    
    list_api_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager

Returns matching versions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_api_versions():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApiVersionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_api_versions](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_versions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApiVersionsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsRequest), dict]]`   
The request object. Request message for ListApiVersions.  
`parent` |  ``str``   
Required. The parent, which owns this collection of versions. Format: `projects/_/locations/_ /apis/*` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager)` | Response message for ListApiVersions. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager

Returns matching APIs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_apis():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListApisRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_apis](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_apis)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListApisRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisRequest), dict]]`   
The request object. Request message for ListApis.  
`parent` |  ``str``   
Required. The parent, which owns this collection of APIs. Format: `projects/_/locations/_` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager)` | Response message for ListApis. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_artifacts
    
    
    list_artifacts(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager

Returns matching artifacts.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_list_artifacts():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ListArtifactsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_artifacts](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_artifacts)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ListArtifactsRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsRequest), dict]]`   
The request object. Request message for ListArtifacts.  
`parent` |  ``str``   
Required. The parent, which owns this collection of artifacts. Format: `{parent}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager)` | Response message for ListArtifacts. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_api_deployment_path
    
    
    parse_api_deployment_path(path: str) -> typing.Dict[str, str]

Parses a api_deployment path into its component segments.

### parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

### parse_api_spec_path
    
    
    parse_api_spec_path(path: str) -> typing.Dict[str, str]

Parses a api_spec path into its component segments.

### parse_api_version_path
    
    
    parse_api_version_path(path: str) -> typing.Dict[str, str]

Parses a api_version path into its component segments.

### parse_artifact_path
    
    
    parse_artifact_path(path: str) -> typing.Dict[str, str]

Parses a artifact path into its component segments.

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

### replace_artifact
    
    
    replace_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ReplaceArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Used to replace a specified artifact.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_replace_artifact():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[ReplaceArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ReplaceArtifactRequest.html)(
        )
    
        # Make the request
        response = await client.[replace_artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_replace_artifact)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.ReplaceArtifactRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ReplaceArtifactRequest), dict]]`   
The request object. Request message for ReplaceArtifact.  
`artifact` |  `[Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)`   
Required. The artifact to replace. The `name` field is used to identify the artifact to replace. Format: `{parent}/artifacts/*` This corresponds to the `artifact` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Artifact](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact)` | Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The ListArtifacts method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.  
  
### rollback_api_deployment
    
    
    rollback_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_rollback_api_deployment():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RollbackApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiDeploymentRequest.html)(
            name="name_value",
            revision_id="revision_id_value",
        )
    
        # Make the request
        response = await client.[rollback_api_deployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_rollback_api_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.RollbackApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiDeploymentRequest), dict]]`   
The request object. Request message for RollbackApiDeployment.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### rollback_api_spec
    
    
    rollback_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_rollback_api_spec():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RollbackApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiSpecRequest.html)(
            name="name_value",
            revision_id="revision_id_value",
        )
    
        # Make the request
        response = await client.[rollback_api_spec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_rollback_api_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.RollbackApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.RollbackApiSpecRequest), dict]]`   
The request object. Request message for RollbackApiSpec.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
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
  
### tag_api_deployment_revision
    
    
    tag_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Adds a tag to a specified revision of a deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_tag_api_deployment_revision():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[TagApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiDeploymentRevisionRequest.html)(
            name="name_value",
            tag="tag_value",
        )
    
        # Make the request
        response = await client.[tag_api_deployment_revision](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_tag_api_deployment_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.TagApiDeploymentRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiDeploymentRevisionRequest), dict]]`   
The request object. Request message for TagApiDeploymentRevision.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### tag_api_spec_revision
    
    
    tag_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Adds a tag to a specified revision of a spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_tag_api_spec_revision():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[TagApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiSpecRevisionRequest.html)(
            name="name_value",
            tag="tag_value",
        )
    
        # Make the request
        response = await client.[tag_api_spec_revision](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_tag_api_spec_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.TagApiSpecRevisionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.TagApiSpecRevisionRequest), dict]]`   
The request object. Request message for TagApiSpecRevision.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
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
  
### update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiRequest,
                dict,
            ]
        ] = None,
        *,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Used to modify a specified API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_update_api():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiRequest.html)(
        )
    
        # Make the request
        response = await client.[update_api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiRequest), dict]]`   
The request object. Request message for UpdateApi.  
`api` |  `[Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)`   
Required. The API to update. The `name` field is used to identify the API to update. Format: `projects/_/locations/_ /apis/*` This corresponds to the `api` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Api)` | A top-level description of an API. Produced by producers and are commitments to provide services.  
  
### update_api_deployment
    
    
    update_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Used to modify a specified deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_update_api_deployment():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[UpdateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiDeploymentRequest.html)(
        )
    
        # Make the request
        response = await client.[update_api_deployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.UpdateApiDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiDeploymentRequest), dict]]`   
The request object. Request message for UpdateApiDeployment.  
`api_deployment` |  `[ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)`   
Required. The deployment to update. The `name` field is used to identify the deployment to update. Format: `projects/_/locations/_ /apis/_/deployments/_` This corresponds to the `api_deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiDeployment](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiDeployment)` | Describes a service running at particular address that provides a particular version of an API. ApiDeployments have revisions which correspond to different configurations of a single deployment in time. Revision identifiers should be updated whenever the served API spec or endpoint address changes.  
  
### update_api_spec
    
    
    update_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Used to modify a specified spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_update_api_spec():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[UpdateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiSpecRequest.html)(
        )
    
        # Make the request
        response = await client.[update_api_spec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.UpdateApiSpecRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiSpecRequest), dict]]`   
The request object. Request message for UpdateApiSpec.  
`api_spec` |  `[ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)`   
Required. The spec to update. The `name` field is used to identify the spec to update. Format: `projects/_/locations/_ /apis/_/versions/_ /specs/*` This corresponds to the `api_spec` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiSpec](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiSpec)` | Describes a version of an API in a structured way. ApiSpecs provide formal descriptions that consumers can use to use a version. ApiSpec resources are intended to be fully-resolved descriptions of an ApiVersion. When specs consist of multiple files, these should be bundled together (e.g., in a zip archive) and stored as a unit. Multiple specs can exist to provide representations in different API description formats. Synchronization of these representations would be provided by tooling and background services.  
  
### update_api_version
    
    
    update_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Used to modify a specified version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest)
    
    async def sample_update_api_version():
        # Create a client
        client = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[RegistryAsyncClient](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apigee_registry_v1](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest).[UpdateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiVersionRequest.html)(
        )
    
        # Make the request
        response = await client.[update_api_version](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.html#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apigee_registry_v1.types.UpdateApiVersionRequest](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.UpdateApiVersionRequest), dict]]`   
The request object. Request message for UpdateApiVersion.  
`api_version` |  `[ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)`   
Required. The version to update. The `name` field is used to identify the version to update. Format: `projects/_/locations/_ /apis/_/versions/_` This corresponds to the `api_version` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If an asterisk "*" is specified, all fields are updated, including fields that are unspecified/default in the request. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apigee_registry_v1.types.ApiVersion](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ApiVersion)` | Describes a particular version of an API. ApiVersions are what consumers actually use.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
