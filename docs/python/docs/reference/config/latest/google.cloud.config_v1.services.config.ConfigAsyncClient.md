---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient
title: Class ConfigAsyncClient (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:36.264343+00:00
---

# Class ConfigAsyncClient (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConfigAsyncClient (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    ConfigAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                typing.Callable[
                    [...],
                    google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Infrastructure Manager is a managed service that automates the deployment and management of Google Cloud infrastructure resources.

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
`ConfigTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ConfigAsyncClient
    
    
    ConfigAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                typing.Callable[
                    [...],
                    google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the config async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ConfigTransport,Callable[..., ConfigTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ConfigTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### auto_migration_config_path
    
    
    auto_migration_config_path(project: str, location: str) -> str

Returns a fully-qualified auto_migration_config string.

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

### create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreateDeploymentRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_Deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_create_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        deployment = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment.html)()
        deployment.terraform_blueprint.gcs_source = "gcs_source_value"
    
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentRequest.html)(
            parent="parent_value",
            deployment_id="deployment_id_value",
            deployment=deployment,
        )
    
        # Make the request
        operation = await client.[create_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_create_deployment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentRequest), dict]]`   
The request object.  
`parent` |  ``str``   
Required. The parent in whose context the Deployment is created. The parent value is in the format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment` |  `Deployment`   
Required. Deployment resource to be created. This corresponds to the `deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment_id` |  ``str``   
Required. The Deployment ID. This corresponds to the `deployment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be Deployment A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### create_deployment_group
    
    
    create_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.CreateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
        ] = None,
        deployment_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_DeploymentGroup The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_create_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[CreateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentGroupRequest.html)(
            parent="parent_value",
            deployment_group_id="deployment_group_id_value",
        )
    
        # Make the request
        operation = await client.[create_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_create_deployment_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.CreateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreateDeploymentGroupRequest), dict]]`   
The request object. A request to create a deployment group  
`parent` |  ``str``   
Required. The parent in whose context the Deployment Group is created. The parent value is in the format: 'projects/{project_id}/locations/{location}' This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment_group` |  `DeploymentGroup`   
Required. [Deployment Group][] resource to create This corresponds to the `deployment_group` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment_group_id` |  ``str``   
Required. The deployment group ID. This corresponds to the `deployment_group_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeploymentGroup A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
### create_preview
    
    
    create_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreatePreviewRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        preview: typing.Optional[google.cloud.config_v1.types.config.Preview] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_Preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_create_preview():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        preview = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[Preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview.html)()
        preview.terraform_blueprint.gcs_source = "gcs_source_value"
        preview.service_account = "service_account_value"
    
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[CreatePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreatePreviewRequest.html)(
            parent="parent_value",
            preview=preview,
        )
    
        # Make the request
        operation = await client.[create_preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_create_preview)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.CreatePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.CreatePreviewRequest), dict]]`   
The request object. A request to create a preview.  
`parent` |  ``str``   
Required. The parent in whose context the Preview is created. The parent value is in the format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`preview` |  `Preview`   
Required. Preview resource to be created. This corresponds to the `preview` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be Preview A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.  
  
### delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteDeploymentRequest, dict]
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

Deletes a xref_Deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_delete_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_deployment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentRequest), dict]]`   
The request object.  
`name` |  ``str``   
Required. The name of the Deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be Deployment A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### delete_deployment_group
    
    
    delete_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeleteDeploymentGroupRequest, dict
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

Deletes a xref_DeploymentGroup
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_delete_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_deployment_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.DeleteDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest), dict]]`   
The request object. Request message for Delete DeploymentGroup  
`name` |  ``str``   
Required. The name of DeploymentGroup in the format projects/{project_id}/locations/{location_id}/deploymentGroups/{deploymentGroup} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeploymentGroup A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
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
  
### delete_preview
    
    
    delete_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeletePreviewRequest, dict]
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

Deletes a xref_Preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_delete_preview():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[DeletePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeletePreviewRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_preview)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.DeletePreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeletePreviewRequest), dict]]`   
The request object. A request to delete a preview.  
`name` |  ``str``   
Required. The name of the Preview in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be Preview A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.  
  
### delete_statefile
    
    
    delete_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteStatefileRequest, dict]
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

Deletes Terraform state file in a given deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_delete_statefile():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[DeleteStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteStatefileRequest.html)(
            name="name_value",
            lock_id=725,
        )
    
        # Make the request
        await client.[delete_statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_statefile)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.DeleteStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteStatefileRequest), dict]]`   
The request object. A request to delete a state file passed to a 'DeleteStatefile' call.  
`name` |  ``str``   
Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### deployment_group_path
    
    
    deployment_group_path(project: str, location: str, deployment_group: str) -> str

Returns a fully-qualified deployment_group string.

### deployment_group_revision_path
    
    
    deployment_group_revision_path(
        project: str, location: str, deployment_group: str, revision: str
    ) -> str

Returns a fully-qualified deployment_group_revision string.

### deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

### deprovision_deployment_group
    
    
    deprovision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeprovisionDeploymentGroupRequest, dict
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

Deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ xref_DeploymentGroupRevision but are _no longer_ included in the _current_ xref_DeploymentGroup definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_deprovision_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeprovisionDeploymentGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[deprovision_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_deprovision_deployment_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeprovisionDeploymentGroupRequest), dict]]`   
The request object. The request message for the DeprovisionDeploymentGroup method.  
`name` |  ``str``   
Required. The name of the deployment group to deprovision. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeploymentGroup A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
### export_deployment_statefile
    
    
    export_deployment_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportDeploymentStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_export_deployment_statefile():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportDeploymentStatefileRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[export_deployment_statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_export_deployment_statefile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ExportDeploymentStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportDeploymentStatefileRequest), dict]]`   
The request object. A request to export a state file passed to a 'ExportDeploymentStatefile' call.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Statefile)` | Contains info about a Terraform state file  
  
### export_lock_info
    
    
    export_lock_info(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ExportLockInfoRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.LockInfo

Exports the lock info on a locked deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_export_lock_info():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ExportLockInfoRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportLockInfoRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[export_lock_info](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_export_lock_info)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ExportLockInfoRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportLockInfoRequest), dict]]`   
The request object. A request to get a state file lock info passed to a 'ExportLockInfo' call.  
`name` |  ``str``   
Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.LockInfo](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.LockInfo)` | Details about the lock which locked the deployment.  
  
### export_preview_result
    
    
    export_preview_result(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportPreviewResultRequest, dict
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
    ) -> google.cloud.config_v1.types.config.ExportPreviewResultResponse

Export xref_Preview results.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_export_preview_result():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ExportPreviewResultRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportPreviewResultRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[export_preview_result](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_export_preview_result)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ExportPreviewResultRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportPreviewResultRequest), dict]]`   
The request object. A request to export preview results.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.ExportPreviewResultResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportPreviewResultResponse)` | A response to ExportPreviewResult call. Contains preview results.  
  
### export_revision_statefile
    
    
    export_revision_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportRevisionStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given revision.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_export_revision_statefile():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ExportRevisionStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportRevisionStatefileRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[export_revision_statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_export_revision_statefile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ExportRevisionStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ExportRevisionStatefileRequest), dict]]`   
The request object. A request to export a state file passed to a 'ExportRevisionStatefile' call.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Statefile)` | Contains info about a Terraform state file  
  
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
`ConfigAsyncClient` | The constructed client.  
  
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
`ConfigAsyncClient` | The constructed client.  
  
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
`ConfigAsyncClient` | The constructed client.  
  
### get_auto_migration_config
    
    
    get_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetAutoMigrationConfigRequest, dict
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
    ) -> google.cloud.config_v1.types.config.AutoMigrationConfig

Get the AutoMigrationConfig for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_auto_migration_config():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetAutoMigrationConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_auto_migration_config](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_auto_migration_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetAutoMigrationConfigRequest), dict]]`   
The request object. The request message for the GetAutoMigrationConfig method.  
`name` |  ``str``   
Required. The name of the AutoMigrationConfig. Format: 'projects/{project_id}/locations/{location}/AutoMigrationConfig'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.AutoMigrationConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.AutoMigrationConfig)` | AutoMigrationConfig contains the automigration configuration for a project.  
  
### get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetDeploymentRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Deployment

Gets details about a xref_Deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentRequest), dict]]`   
The request object.  
`name` |  ``str``   
Required. The name of the deployment. Format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment)` | A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### get_deployment_group
    
    
    get_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroup

Get a DeploymentGroup for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRequest), dict]]`   
The request object. The request message for the GetDeploymentGroup method.  
`name` |  ``str``   
Required. The name of the deployment group to retrieve. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.DeploymentGroup](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup)` | A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
### get_deployment_group_revision
    
    
    get_deployment_group_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRevisionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroupRevision

Gets details about a xref_DeploymentGroupRevision.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_deployment_group_revision():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRevisionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deployment_group_revision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment_group_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetDeploymentGroupRevisionRequest), dict]]`   
The request object. The request message for the GetDeploymentGroupRevision method.  
`name` |  ``str``   
Required. The name of the deployment group revision to retrieve. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}/revisions/{revision}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.DeploymentGroupRevision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroupRevision)` | A DeploymentGroupRevision represents a snapshot of a DeploymentGroup at a given point in time, created when a DeploymentGroup is provisioned or deprovisioned.  
  
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
  
### get_preview
    
    
    get_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetPreviewRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Preview

Gets details about a xref_Preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_preview():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetPreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetPreviewRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_preview)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetPreviewRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetPreviewRequest), dict]]`   
The request object. A request to get details about a preview.  
`name` |  ``str``   
Required. The name of the preview. Format: 'projects/{project_id}/locations/{location}/previews/{preview}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Preview](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Preview)` | A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.  
  
### get_resource
    
    
    get_resource(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Resource

Gets details about a xref_Resource deployed by Infra Manager.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_resource():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetResourceRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_resource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetResourceRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceRequest), dict]]`   
The request object. A request to get a Resource from a 'GetResource' call.  
`name` |  ``str``   
Required. The name of the Resource in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}/resource/{resource}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Resource](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Resource)` | Resource represents a Google Cloud Platform resource actuated by IM. Resources are child resources of Revisions.  
  
### get_resource_change
    
    
    get_resource_change(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceChangeRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceChange

Get a ResourceChange for a given preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_resource_change():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetResourceChangeRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceChangeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_resource_change](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource_change)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetResourceChangeRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceChangeRequest), dict]]`   
The request object. The request message for the GetResourceChange method.  
`name` |  ``str``   
Required. The name of the resource change to retrieve. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceChanges/{resource_change}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.ResourceChange](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceChange)` | A resource change represents a change to a resource in the state file.  
  
### get_resource_drift
    
    
    get_resource_drift(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceDriftRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceDrift

Get a ResourceDrift for a given preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_resource_drift():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetResourceDriftRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceDriftRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_resource_drift](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource_drift)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetResourceDriftRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetResourceDriftRequest), dict]]`   
The request object. The request message for the GetResourceDrift method.  
`name` |  ``str``   
Required. The name of the resource drift to retrieve. Format: 'projects/{project_id}/locations/{location}/previews/{preview}/resourceDrifts/{resource_drift}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.ResourceDrift](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ResourceDrift)` | A resource drift represents a drift to a resource in the state file.  
  
### get_revision
    
    
    get_revision(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetRevisionRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Revision

Gets details about a xref_Revision.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_revision():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetRevisionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_revision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_revision)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetRevisionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetRevisionRequest), dict]]`   
The request object. A request to get a Revision from a 'GetRevision' call.  
`name` |  ``str``   
Required. The name of the Revision in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Revision](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Revision)` | A child resource of a Deployment generated by a 'CreateDeployment' or 'UpdateDeployment' call. Each Revision contains metadata pertaining to a snapshot of a particular Deployment.  
  
### get_terraform_version
    
    
    get_terraform_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetTerraformVersionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.TerraformVersion

Gets details about a xref_TerraformVersion.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_get_terraform_version():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[GetTerraformVersionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetTerraformVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_terraform_version](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_get_terraform_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.GetTerraformVersionRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.GetTerraformVersionRequest), dict]]`   
The request object. The request message for the GetTerraformVersion method.  
`name` |  ``str``   
Required. The name of the TerraformVersion. Format: 'projects/{project_id}/locations/{location}/terraformVersions/{terraform_version}' This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.TerraformVersion](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.TerraformVersion)` | A TerraformVersion represents the support state the corresponding Terraform version.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.config_v1.services.config.transports.base.ConfigTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### import_statefile
    
    
    import_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ImportStatefileRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.config_v1.types.config.Statefile

Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_import_statefile():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ImportStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ImportStatefileRequest.html)(
            parent="parent_value",
            lock_id=725,
        )
    
        # Make the request
        response = await client.[import_statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_import_statefile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ImportStatefileRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ImportStatefileRequest), dict]]`   
The request object. A request to import a state file passed to a 'ImportStatefile' call.  
`parent` |  ``str``   
Required. The parent in whose context the statefile is listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`lock_id` |  ``int``   
Required. Lock ID of the lock file to verify that the user who is importing the state file previously locked the Deployment. This corresponds to the `lock_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.types.Statefile](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Statefile)` | Contains info about a Terraform state file  
  
### list_deployment_group_revisions
    
    
    list_deployment_group_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
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
        google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager
    )

Lists xref_DeploymentGroupRevisions in a given xref_DeploymentGroup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_deployment_group_revisions():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deployment_group_revisions](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployment_group_revisions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsRequest), dict]]`   
The request object. The request message for the ListDeploymentGroupRevisions method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deployment group revisions. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager)` | The response message for the ListDeploymentGroupRevisions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_deployment_groups
    
    
    list_deployment_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager

List DeploymentGroups for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_deployment_groups():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListDeploymentGroupsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deployment_groups](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployment_groups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListDeploymentGroupsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsRequest), dict]]`   
The request object. The request message for the ListDeploymentGroups method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deployment groups. Format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager)` | The response message for the ListDeploymentGroups method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListDeploymentsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager

Lists xref_Deployments in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_deployments():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deployments](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployments)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsRequest), dict]]`   
The request object.  
`parent` |  ``str``   
Required. The parent in whose context the Deployments are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_previews
    
    
    list_previews(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListPreviewsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager

Lists xref_Previews in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_previews():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListPreviewsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_previews](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_previews)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListPreviewsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsRequest), dict]]`   
The request object. A request to list all previews for a given project and location.  
`parent` |  ``str``   
Required. The parent in whose context the Previews are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager)` | A response to a ListPreviews call. Contains a list of Previews. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_resource_changes
    
    
    list_resource_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceChangesRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager

Lists ResourceChanges for a given preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_resource_changes():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListResourceChangesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_resource_changes](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resource_changes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListResourceChangesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesRequest), dict]]`   
The request object. The request message for the ListResourceChanges method.  
`parent` |  ``str``   
Required. The parent in whose context the ResourceChanges are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager)` | A response to a 'ListResourceChanges' call. Contains a list of ResourceChanges. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_resource_drifts
    
    
    list_resource_drifts(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceDriftsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager

List ResourceDrifts for a given preview.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_resource_drifts():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListResourceDriftsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_resource_drifts](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resource_drifts)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListResourceDriftsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsRequest), dict]]`   
The request object. The request message for the ListResourceDrifts method.  
`parent` |  ``str``   
Required. The parent in whose context the ResourceDrifts are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager)` | A response to a 'ListResourceDrifts' call. Contains a list of ResourceDrifts. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_resources
    
    
    list_resources(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListResourcesRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager

Lists xref_Resources in a given revision.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_resources():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListResourcesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_resources](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resources)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListResourcesRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesRequest), dict]]`   
The request object. A request to list Resources passed to a 'ListResources' call.  
`parent` |  ``str``   
Required. The parent in whose context the Resources are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}/revisions/{revision}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager)` | A response to a 'ListResources' call. Contains a list of Resources. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_revisions
    
    
    list_revisions(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListRevisionsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager

Lists xref_Revisions of a deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_revisions():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_revisions](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_revisions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsRequest), dict]]`   
The request object. A request to list Revisions passed to a 'ListRevisions' call.  
`parent` |  ``str``   
Required. The parent in whose context the Revisions are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager)` | A response to a 'ListRevisions' call. Contains a list of Revisions. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_terraform_versions
    
    
    list_terraform_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListTerraformVersionsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager

Lists xref_TerraformVersions in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_list_terraform_versions():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ListTerraformVersionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_terraform_versions](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_list_terraform_versions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ListTerraformVersionsRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsRequest), dict]]`   
The request object. The request message for the ListTerraformVersions method.  
`parent` |  ``str``   
Required. The parent in whose context the TerraformVersions are listed. The parent value is in the format: 'projects/{project_id}/locations/{location}'. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager)` | The response message for the ListTerraformVersions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### lock_deployment
    
    
    lock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.LockDeploymentRequest, dict]
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

Locks a deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_lock_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[LockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.LockDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[lock_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_lock_deployment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.LockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.LockDeploymentRequest), dict]]`   
The request object. A request to lock a deployment passed to a 'LockDeployment' call.  
`name` |  ``str``   
Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment) A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### parse_auto_migration_config_path
    
    
    parse_auto_migration_config_path(path: str) -> typing.Dict[str, str]

Parses a auto_migration_config path into its component segments.

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

### parse_deployment_group_path
    
    
    parse_deployment_group_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group path into its component segments.

### parse_deployment_group_revision_path
    
    
    parse_deployment_group_revision_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group_revision path into its component segments.

### parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

### parse_preview_path
    
    
    parse_preview_path(path: str) -> typing.Dict[str, str]

Parses a preview path into its component segments.

### parse_resource_change_path
    
    
    parse_resource_change_path(path: str) -> typing.Dict[str, str]

Parses a resource_change path into its component segments.

### parse_resource_drift_path
    
    
    parse_resource_drift_path(path: str) -> typing.Dict[str, str]

Parses a resource_drift path into its component segments.

### parse_resource_path
    
    
    parse_resource_path(path: str) -> typing.Dict[str, str]

Parses a resource path into its component segments.

### parse_revision_path
    
    
    parse_revision_path(path: str) -> typing.Dict[str, str]

Parses a revision path into its component segments.

### parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

### parse_terraform_version_path
    
    
    parse_terraform_version_path(path: str) -> typing.Dict[str, str]

Parses a terraform_version path into its component segments.

### parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

### preview_path
    
    
    preview_path(project: str, location: str, preview: str) -> str

Returns a fully-qualified preview string.

### provision_deployment_group
    
    
    provision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ProvisionDeploymentGroupRequest, dict
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

Provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the _last successful_ xref_DeploymentGroupRevision but are _no longer_ included in the _current_ xref_DeploymentGroup definition (e.g., following an `UpdateDeploymentGroup` call), along with their actuated resources.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_provision_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProvisionDeploymentGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[provision_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_provision_deployment_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProvisionDeploymentGroupRequest), dict]]`   
The request object. The request message for the ProvisionDeploymentGroup method.  
`name` |  ``str``   
Required. The name of the deployment group to provision. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeploymentGroup A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
### resource_change_path
    
    
    resource_change_path(
        project: str, location: str, preview: str, resource_change: str
    ) -> str

Returns a fully-qualified resource_change string.

### resource_drift_path
    
    
    resource_drift_path(
        project: str, location: str, preview: str, resource_drift: str
    ) -> str

Returns a fully-qualified resource_drift string.

### resource_path
    
    
    resource_path(
        project: str, location: str, deployment: str, revision: str, resource: str
    ) -> str

Returns a fully-qualified resource string.

### revision_path
    
    
    revision_path(project: str, location: str, deployment: str, revision: str) -> str

Returns a fully-qualified revision string.

### service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

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
  
### terraform_version_path
    
    
    terraform_version_path(project: str, location: str, terraform_version: str) -> str

Returns a fully-qualified terraform_version string.

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
  
### unlock_deployment
    
    
    unlock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UnlockDeploymentRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Unlocks a locked deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_unlock_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[UnlockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UnlockDeploymentRequest.html)(
            name="name_value",
            lock_id=725,
        )
    
        # Make the request
        operation = await client.[unlock_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_unlock_deployment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.UnlockDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UnlockDeploymentRequest), dict]]`   
The request object. A request to unlock a state file passed to a 'UnlockDeployment' call.  
`name` |  ``str``   
Required. The name of the deployment in the format: 'projects/{project_id}/locations/{location}/deployments/{deployment}'. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`lock_id` |  ``int``   
Required. Lock ID of the lock file to be unlocked. This corresponds to the `lock_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment) A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### update_auto_migration_config
    
    
    update_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateAutoMigrationConfigRequest, dict
            ]
        ] = None,
        *,
        auto_migration_config: typing.Optional[
            google.cloud.config_v1.types.config.AutoMigrationConfig
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

Updates the AutoMigrationConfig for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_update_auto_migration_config():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateAutoMigrationConfigRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_auto_migration_config](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_update_auto_migration_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateAutoMigrationConfigRequest), dict]]`   
The request object. The request message for the UpdateAutoMigrationConfig method.  
`auto_migration_config` |  `[AutoMigrationConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.AutoMigrationConfig)`   
Required. The AutoMigrationConfig to update. This corresponds to the `auto_migration_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. The update mask applies to the resource. See `google.protobuf.FieldMask][google.protobuf.FieldMask]`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [AutoMigrationConfig](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.AutoMigrationConfig) AutoMigrationConfig contains the automigration configuration for a project.  
  
### update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UpdateDeploymentRequest, dict]
        ] = None,
        *,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
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

Updates a xref_Deployment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_update_deployment():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        deployment = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[Deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.Deployment.html)()
        deployment.terraform_blueprint.gcs_source = "gcs_source_value"
    
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentRequest.html)(
            deployment=deployment,
        )
    
        # Make the request
        operation = await client.[update_deployment](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_update_deployment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentRequest), dict]]`   
The request object.  
`deployment` |  `Deployment`   
Required. Deployment to update. The deployment's `name` field is used to identify the resource to be updated. Format: `projects/{project}/locations/{location}/deployments/{deployment}` This corresponds to the `deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask used to specify the fields to be overwritten in the Deployment resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be Deployment A Deployment is a group of resources and configs managed and provisioned by Infra Manager.  
  
### update_deployment_group
    
    
    update_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
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

Updates a xref_DeploymentGroup
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest)
    
    async def sample_update_deployment_group():
        # Create a client
        client = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[ConfigAsyncClient](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [config_v1](https://docs.cloud.google.com/python/docs/reference/config/latest).[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentGroupRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_deployment_group](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient.html#google_cloud_config_v1_services_config_ConfigAsyncClient_update_deployment_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.config_v1.types.UpdateDeploymentGroupRequest](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.UpdateDeploymentGroupRequest), dict]]`   
The request object. A request message for updating a deployment group  
`deployment_group` |  `DeploymentGroup`   
Required. DeploymentGroup to update. The deployment group's `name` field is used to identify the resource to be updated. Format: `projects/{project}/locations/{location}/deploymentGroups/{deployment_group_id}` This corresponds to the `deployment_group` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask used to specify the fields to be overwritten in the Deployment Group resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeploymentGroup A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.  
  
### worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
