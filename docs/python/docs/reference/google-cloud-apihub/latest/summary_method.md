---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/summary_method/
title: Package Methods (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:12.567624+00:00
---

# Package Methods (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 

Summary of entries of Methods for google-cloud-apihub.

## 

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient
    
    
    ApiHubAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub async client.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_ApiHubAsyncClient)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.api_operation_path
    
    
    api_operation_path(
        project: str, location: str, api: str, version: str, operation: str
    ) -> str

Returns a fully-qualified api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_api_operation_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.CreateApiRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Create an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_api_operation
    
    
    create_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateApiOperationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
        ] = None,
        api_operation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Create an apiOperation in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_attribute
    
    
    create_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateAttributeRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
        ] = None,
        attribute_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Create a user defined attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateDeploymentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Create a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_external_api
    
    
    create_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateExternalApiRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
        ] = None,
        external_api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Create an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_spec
    
    
    create_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateSpecRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Add a spec to an API version in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_version
    
    
    create_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateVersionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Create an API version for an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.create_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.definition_path
    
    
    definition_path(
        project: str, location: str, api: str, version: str, definition: str
    ) -> str

Returns a fully-qualified definition string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_definition_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.DeleteApiRequest, dict]
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

Delete an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_api_operation
    
    
    delete_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteApiOperationRequest, dict
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

Delete an operation in an API version and we can delete only the operations created via create API.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_attribute
    
    
    delete_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteAttributeRequest, dict
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

Delete an attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteDeploymentRequest, dict
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

Delete a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_external_api
    
    
    delete_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteExternalApiRequest, dict
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

Delete an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_spec
    
    
    delete_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteSpecRequest, dict
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

Delete a spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_version
    
    
    delete_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteVersionRequest, dict
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

Delete an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.delete_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_deployment_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.external_api_path
    
    
    external_api_path(project: str, location: str, external_api: str) -> str

Returns a fully-qualified external_api string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.external_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_external_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetApiRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Get API resource details including the API versions contained in it.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_api_operation
    
    
    get_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetApiOperationRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Get details about a particular operation in API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_attribute
    
    
    get_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetAttributeRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Get details about the attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_definition
    
    
    get_definition(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDefinitionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Definition

Get details about a definition in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_definition](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_definition)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDeploymentRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Get details about a deployment and the API versions linked to it.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_external_api
    
    
    get_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetExternalApiRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Get details about an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_spec
    
    
    get_spec(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetSpecRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Get details about the information parsed from a spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_spec_contents
    
    
    get_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetSpecContentsRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.SpecContents

Get spec contents.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_spec_contents](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_spec_contents)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_version
    
    
    get_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetVersionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Get details about the API version of an API resource.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.get_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_api_operations
    
    
    list_api_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager

List operations in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_api_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_api_operations)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListApisRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager

List API resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_apis](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_apis)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_attributes
    
    
    list_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager

List all attributes.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_attributes](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_attributes)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager

List deployment resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_deployments)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_external_apis
    
    
    list_external_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager

List External API resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_external_apis](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_external_apis)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_specs
    
    
    list_specs(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager

List specs corresponding to a particular API resource.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_specs](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_specs)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_versions
    
    
    list_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager

List API versions of an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.list_versions](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_versions)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_api_operation_path
    
    
    parse_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_api_operation_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_definition_path
    
    
    parse_definition_path(path: str) -> typing.Dict[str, str]

Parses a definition path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_definition_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_deployment_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_external_api_path
    
    
    parse_external_api_path(path: str) -> typing.Dict[str, str]

Parses a external_api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_external_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_external_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_spec_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_version_path
    
    
    parse_version_path(path: str) -> typing.Dict[str, str]

Parses a version path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.parse_version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_parse_version_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.search_resources
    
    
    search_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager

Search across API-Hub resources.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.search_resources](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_search_resources)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_spec_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.UpdateApiRequest, dict]
        ] = None,
        *,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Update an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_api_operation
    
    
    update_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateApiOperationRequest, dict
            ]
        ] = None,
        *,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Update an operation in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_attribute
    
    
    update_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateAttributeRequest, dict
            ]
        ] = None,
        *,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Update the attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateDeploymentRequest, dict
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Update a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_external_api
    
    
    update_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateExternalApiRequest, dict
            ]
        ] = None,
        *,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Update an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_spec
    
    
    update_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateSpecRequest, dict
            ]
        ] = None,
        *,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Update spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_version
    
    
    update_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateVersionRequest, dict
            ]
        ] = None,
        *,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Update API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.update_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.version_path
    
    
    version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified version string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_version_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient
    
    
    ApiHubClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub client.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_ApiHubClient)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient___exit__)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.api_operation_path
    
    
    api_operation_path(
        project: str, location: str, api: str, version: str, operation: str
    ) -> str

Returns a fully-qualified api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_api_operation_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.CreateApiRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Create an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_api_operation
    
    
    create_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateApiOperationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
        ] = None,
        api_operation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Create an apiOperation in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_attribute
    
    
    create_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateAttributeRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
        ] = None,
        attribute_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Create a user defined attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateDeploymentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Create a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_external_api
    
    
    create_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateExternalApiRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
        ] = None,
        external_api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Create an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_spec
    
    
    create_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateSpecRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Add a spec to an API version in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_version
    
    
    create_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateVersionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Create an API version for an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.create_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_create_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.definition_path
    
    
    definition_path(
        project: str, location: str, api: str, version: str, definition: str
    ) -> str

Returns a fully-qualified definition string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_definition_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.DeleteApiRequest, dict]
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

Delete an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_api_operation
    
    
    delete_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteApiOperationRequest, dict
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

Delete an operation in an API version and we can delete only the operations created via create API.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_attribute
    
    
    delete_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteAttributeRequest, dict
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

Delete an attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteDeploymentRequest, dict
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

Delete a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_external_api
    
    
    delete_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteExternalApiRequest, dict
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

Delete an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_spec
    
    
    delete_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteSpecRequest, dict
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

Delete a spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_version
    
    
    delete_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteVersionRequest, dict
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

Delete an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.delete_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_delete_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_deployment_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.external_api_path
    
    
    external_api_path(project: str, location: str, external_api: str) -> str

Returns a fully-qualified external_api string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.external_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_external_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetApiRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Get API resource details including the API versions contained in it.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_api_operation
    
    
    get_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetApiOperationRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Get details about a particular operation in API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_attribute
    
    
    get_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetAttributeRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Get details about the attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_definition
    
    
    get_definition(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDefinitionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Definition

Get details about a definition in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_definition](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_definition)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDeploymentRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Get details about a deployment and the API versions linked to it.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_external_api
    
    
    get_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetExternalApiRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Get details about an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_location)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_spec
    
    
    get_spec(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetSpecRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Get details about the information parsed from a spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_spec_contents
    
    
    get_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetSpecContentsRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.SpecContents

Get spec contents.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_spec_contents](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_spec_contents)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_version
    
    
    get_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetVersionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Get details about the API version of an API resource.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.get_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_get_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_api_operations
    
    
    list_api_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsPager

List operations in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_api_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_api_operations)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListApisRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApisPager

List API resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_apis](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_apis)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_attributes
    
    
    list_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesPager

List all attributes.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_attributes](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_attributes)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsPager

List deployment resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_deployments)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_external_apis
    
    
    list_external_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisPager

List External API resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_external_apis](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_external_apis)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_locations)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_operations)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_specs
    
    
    list_specs(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsPager

List specs corresponding to a particular API resource.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_specs](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_specs)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_versions
    
    
    list_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsPager

List API versions of an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.list_versions](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_list_versions)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_api_operation_path
    
    
    parse_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_api_operation_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_definition_path
    
    
    parse_definition_path(path: str) -> typing.Dict[str, str]

Parses a definition path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_definition_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_deployment_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_external_api_path
    
    
    parse_external_api_path(path: str) -> typing.Dict[str, str]

Parses a external_api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_external_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_external_api_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_spec_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_version_path
    
    
    parse_version_path(path: str) -> typing.Dict[str, str]

Parses a version path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.parse_version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_parse_version_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.search_resources
    
    
    search_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesPager

Search across API-Hub resources.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.search_resources](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_search_resources)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_spec_path)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.UpdateApiRequest, dict]
        ] = None,
        *,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Update an API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_api_operation
    
    
    update_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateApiOperationRequest, dict
            ]
        ] = None,
        *,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Update an operation in an API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_api_operation)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_attribute
    
    
    update_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateAttributeRequest, dict
            ]
        ] = None,
        *,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Update the attribute.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_attribute](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_attribute)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateDeploymentRequest, dict
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Update a deployment resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_deployment)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_external_api
    
    
    update_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateExternalApiRequest, dict
            ]
        ] = None,
        *,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Update an External API resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_external_api](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_external_api)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_spec
    
    
    update_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateSpecRequest, dict
            ]
        ] = None,
        *,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Update spec.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_spec)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_version
    
    
    update_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateVersionRequest, dict
            ]
        ] = None,
        *,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Update API version.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.update_version](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_update_version)

### google.cloud.apihub_v1.services.api_hub.ApiHubClient.version_path
    
    
    version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified version string.

See more: [google.cloud.apihub_v1.services.api_hub.ApiHubClient.version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubClient#google_cloud_apihub_v1_services_api_hub_ApiHubClient_version_path)

### google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager
    
    
    ListApiOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListApiOperationsAsyncPager_ListApiOperationsAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsPager
    
    
    ListApiOperationsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsPager#google_cloud_apihub_v1_services_api_hub_pagers_ListApiOperationsPager_ListApiOperationsPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager
    
    
    ListApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.apihub_v1.types.apihub_service.ListApisResponse],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApisResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListApisAsyncPager_ListApisAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListApisPager
    
    
    ListApisPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListApisResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApisResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListApisPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApisPager#google_cloud_apihub_v1_services_api_hub_pagers_ListApisPager_ListApisPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager
    
    
    ListAttributesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListAttributesAsyncPager_ListAttributesAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesPager
    
    
    ListAttributesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesPager#google_cloud_apihub_v1_services_api_hub_pagers_ListAttributesPager_ListAttributesPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListDeploymentsAsyncPager_ListDeploymentsAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsPager
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsPager#google_cloud_apihub_v1_services_api_hub_pagers_ListDeploymentsPager_ListDeploymentsPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager
    
    
    ListExternalApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListExternalApisAsyncPager_ListExternalApisAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisPager
    
    
    ListExternalApisPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisPager#google_cloud_apihub_v1_services_api_hub_pagers_ListExternalApisPager_ListExternalApisPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager
    
    
    ListSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListSpecsAsyncPager_ListSpecsAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsPager
    
    
    ListSpecsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsPager#google_cloud_apihub_v1_services_api_hub_pagers_ListSpecsPager_ListSpecsPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager
    
    
    ListVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_ListVersionsAsyncPager_ListVersionsAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsPager
    
    
    ListVersionsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsPager#google_cloud_apihub_v1_services_api_hub_pagers_ListVersionsPager_ListVersionsPager)

### google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager
    
    
    SearchResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager#google_cloud_apihub_v1_services_api_hub_pagers_SearchResourcesAsyncPager_SearchResourcesAsyncPager)

### google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesPager
    
    
    SearchResourcesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesPager#google_cloud_apihub_v1_services_api_hub_pagers_SearchResourcesPager_SearchResourcesPager)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient
    
    
    ApiHubCollectAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_collect.transports.base.ApiHubCollectTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_collect.transports.base.ApiHubCollectTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub collect async client.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_ApiHubCollectAsyncClient)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.api_operation_path
    
    
    api_operation_path(
        project: str, location: str, api: str, version: str, operation: str
    ) -> str

Returns a fully-qualified api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_api_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.collect_api_data
    
    
    collect_api_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.collect_service.CollectApiDataRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        collection_type: typing.Optional[
            google.cloud.apihub_v1.types.collect_service.CollectionType
        ] = None,
        api_data: typing.Optional[
            google.cloud.apihub_v1.types.collect_service.ApiData
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

Collect API data from a source and push it to Hub's collect layer.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.collect_api_data](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_collect_api_data)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.definition_path
    
    
    definition_path(
        project: str, location: str, api: str, version: str, definition: str
    ) -> str

Returns a fully-qualified definition string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_definition_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_deployment_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_collect.transports.base.ApiHubCollectTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_api_operation_path
    
    
    parse_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_api_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_definition_path
    
    
    parse_definition_path(path: str) -> typing.Dict[str, str]

Parses a definition path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_definition_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_deployment_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_spec_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_version_path
    
    
    parse_version_path(path: str) -> typing.Dict[str, str]

Parses a version path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.parse_version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_parse_version_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_spec_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.version_path
    
    
    version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified version string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient.version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectAsyncClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectAsyncClient_version_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient
    
    
    ApiHubCollectClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_collect.transports.base.ApiHubCollectTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_collect.transports.base.ApiHubCollectTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub collect client.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_ApiHubCollectClient)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient___exit__)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.api_operation_path
    
    
    api_operation_path(
        project: str, location: str, api: str, version: str, operation: str
    ) -> str

Returns a fully-qualified api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_api_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.collect_api_data
    
    
    collect_api_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.collect_service.CollectApiDataRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        collection_type: typing.Optional[
            google.cloud.apihub_v1.types.collect_service.CollectionType
        ] = None,
        api_data: typing.Optional[
            google.cloud.apihub_v1.types.collect_service.ApiData
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Collect API data from a source and push it to Hub's collect layer.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.collect_api_data](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_collect_api_data)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.definition_path
    
    
    definition_path(
        project: str, location: str, api: str, version: str, definition: str
    ) -> str

Returns a fully-qualified definition string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_definition_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_deployment_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_get_location)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_api_operation_path
    
    
    parse_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_api_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_api_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_definition_path
    
    
    parse_definition_path(path: str) -> typing.Dict[str, str]

Parses a definition path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_definition_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_definition_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_deployment_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_spec_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_version_path
    
    
    parse_version_path(path: str) -> typing.Dict[str, str]

Parses a version path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.parse_version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_parse_version_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_spec_path)

### google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.version_path
    
    
    version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified version string.

See more: [google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient.version_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_collect.ApiHubCollectClient#google_cloud_apihub_v1_services_api_hub_collect_ApiHubCollectClient_version_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient
    
    
    ApiHubCurateAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_curate.transports.base.ApiHubCurateTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_curate.transports.base.ApiHubCurateTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub curate async client.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_ApiHubCurateAsyncClient)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.create_curation
    
    
    create_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.CreateCurationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        curation: typing.Optional[
            google.cloud.apihub_v1.types.curate_service.Curation
        ] = None,
        curation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Create a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.create_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_create_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.curation_path
    
    
    curation_path(project: str, location: str, curation: str) -> str

Returns a fully-qualified curation string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.curation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_curation_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.delete_curation
    
    
    delete_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.DeleteCurationRequest, dict
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

Delete a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.delete_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_delete_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_curation
    
    
    get_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.GetCurationRequest, dict
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
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Get curation resource details.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_get_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_curate.transports.base.ApiHubCurateTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_curations
    
    
    list_curations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.ListCurationsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsAsyncPager

List curation resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_curations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_list_curations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_curation_path
    
    
    parse_curation_path(path: str) -> typing.Dict[str, str]

Parses a curation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_curation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_curation_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.update_curation
    
    
    update_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.UpdateCurationRequest, dict
            ]
        ] = None,
        *,
        curation: typing.Optional[
            google.cloud.apihub_v1.types.curate_service.Curation
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
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Update a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient.update_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateAsyncClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateAsyncClient_update_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient
    
    
    ApiHubCurateClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_curate.transports.base.ApiHubCurateTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_curate.transports.base.ApiHubCurateTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub curate client.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_ApiHubCurateClient)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient___exit__)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.create_curation
    
    
    create_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.CreateCurationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        curation: typing.Optional[
            google.cloud.apihub_v1.types.curate_service.Curation
        ] = None,
        curation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Create a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.create_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_create_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.curation_path
    
    
    curation_path(project: str, location: str, curation: str) -> str

Returns a fully-qualified curation string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.curation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_curation_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.delete_curation
    
    
    delete_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.DeleteCurationRequest, dict
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

Delete a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.delete_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_delete_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_curation
    
    
    get_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.GetCurationRequest, dict
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
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Get curation resource details.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_get_curation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_get_location)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_curations
    
    
    list_curations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.ListCurationsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsPager

List curation resources in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_curations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_list_curations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_curation_path
    
    
    parse_curation_path(path: str) -> typing.Dict[str, str]

Parses a curation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_curation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_curation_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.update_curation
    
    
    update_curation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.curate_service.UpdateCurationRequest, dict
            ]
        ] = None,
        *,
        curation: typing.Optional[
            google.cloud.apihub_v1.types.curate_service.Curation
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
    ) -> google.cloud.apihub_v1.types.curate_service.Curation

Update a curation resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient.update_curation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.ApiHubCurateClient#google_cloud_apihub_v1_services_api_hub_curate_ApiHubCurateClient_update_curation)

### google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsAsyncPager
    
    
    ListCurationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.curate_service.ListCurationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.curate_service.ListCurationsRequest,
        response: google.cloud.apihub_v1.types.curate_service.ListCurationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsAsyncPager#google_cloud_apihub_v1_services_api_hub_curate_pagers_ListCurationsAsyncPager_ListCurationsAsyncPager)

### google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsPager
    
    
    ListCurationsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.curate_service.ListCurationsResponse
        ],
        request: google.cloud.apihub_v1.types.curate_service.ListCurationsRequest,
        response: google.cloud.apihub_v1.types.curate_service.ListCurationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_curate.pagers.ListCurationsPager#google_cloud_apihub_v1_services_api_hub_curate_pagers_ListCurationsPager_ListCurationsPager)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient
    
    
    ApiHubDependenciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_dependencies.transports.base.ApiHubDependenciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_dependencies.transports.base.ApiHubDependenciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub dependencies async client.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_ApiHubDependenciesAsyncClient)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.create_dependency
    
    
    create_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateDependencyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dependency: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Dependency
        ] = None,
        dependency_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Create a dependency between two entities in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.create_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_create_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.delete_dependency
    
    
    delete_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteDependencyRequest, dict
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

Delete the dependency resource.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.delete_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_delete_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.dependency_path
    
    
    dependency_path(project: str, location: str, dependency: str) -> str

Returns a fully-qualified dependency string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.dependency_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_dependency_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_dependency
    
    
    get_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDependencyRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Get details about a dependency resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_get_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_dependencies.transports.base.ApiHubDependenciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_dependencies
    
    
    list_dependencies(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListDependenciesRequest, dict
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
        google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesAsyncPager
    )

List dependencies based on the provided filter and pagination parameters.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_dependencies](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_list_dependencies)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_dependency_path
    
    
    parse_dependency_path(path: str) -> typing.Dict[str, str]

Parses a dependency path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.parse_dependency_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_parse_dependency_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.update_dependency
    
    
    update_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateDependencyRequest, dict
            ]
        ] = None,
        *,
        dependency: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Dependency
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
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Update a dependency based on the xref_update_mask provided in the request.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient.update_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesAsyncClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesAsyncClient_update_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient
    
    
    ApiHubDependenciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_dependencies.transports.base.ApiHubDependenciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_dependencies.transports.base.ApiHubDependenciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub dependencies client.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_ApiHubDependenciesClient)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient___exit__)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.create_dependency
    
    
    create_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateDependencyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dependency: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Dependency
        ] = None,
        dependency_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Create a dependency between two entities in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.create_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_create_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.delete_dependency
    
    
    delete_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteDependencyRequest, dict
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

Delete the dependency resource.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.delete_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_delete_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.dependency_path
    
    
    dependency_path(project: str, location: str, dependency: str) -> str

Returns a fully-qualified dependency string.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.dependency_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_dependency_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_dependency
    
    
    get_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDependencyRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Get details about a dependency resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_get_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_get_location)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_dependencies
    
    
    list_dependencies(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListDependenciesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesPager

List dependencies based on the provided filter and pagination parameters.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_dependencies](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_list_dependencies)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_dependency_path
    
    
    parse_dependency_path(path: str) -> typing.Dict[str, str]

Parses a dependency path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.parse_dependency_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_parse_dependency_path)

### google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.update_dependency
    
    
    update_dependency(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateDependencyRequest, dict
            ]
        ] = None,
        *,
        dependency: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Dependency
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
    ) -> google.cloud.apihub_v1.types.common_fields.Dependency

Update a dependency based on the xref_update_mask provided in the request.

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient.update_dependency](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.ApiHubDependenciesClient#google_cloud_apihub_v1_services_api_hub_dependencies_ApiHubDependenciesClient_update_dependency)

### google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesAsyncPager
    
    
    ListDependenciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListDependenciesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDependenciesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDependenciesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesAsyncPager#google_cloud_apihub_v1_services_api_hub_dependencies_pagers_ListDependenciesAsyncPager_ListDependenciesAsyncPager)

### google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesPager
    
    
    ListDependenciesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListDependenciesResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDependenciesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDependenciesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_dependencies.pagers.ListDependenciesPager#google_cloud_apihub_v1_services_api_hub_dependencies_pagers_ListDependenciesPager_ListDependenciesPager)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient
    
    
    ApiHubDiscoveryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_discovery.transports.base.ApiHubDiscoveryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_discovery.transports.base.ApiHubDiscoveryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub discovery async client.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_ApiHubDiscoveryAsyncClient)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.discovered_api_observation_path
    
    
    discovered_api_observation_path(
        project: str, location: str, discovered_api_observation: str
    ) -> str

Returns a fully-qualified discovered_api_observation string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.discovered_api_observation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_discovered_api_observation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.discovered_api_operation_path
    
    
    discovered_api_operation_path(
        project: str,
        location: str,
        discovered_api_observation: str,
        discovered_api_operation: str,
    ) -> str

Returns a fully-qualified discovered_api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.discovered_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_discovered_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_discovered_api_observation
    
    
    get_discovered_api_observation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.GetDiscoveredApiObservationRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.DiscoveredApiObservation

Gets a DiscoveredAPIObservation in a given project, location and ApiObservation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_discovered_api_observation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_discovered_api_observation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_discovered_api_operation
    
    
    get_discovered_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.GetDiscoveredApiOperationRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.DiscoveredApiOperation

Gets a DiscoveredAPIOperation in a given project, location, ApiObservation and ApiOperation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_discovered_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_discovered_api_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_discovery.transports.base.ApiHubDiscoveryTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_discovered_api_observations
    
    
    list_discovered_api_observations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsRequest,
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
        google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsAsyncPager
    )

Lists all the DiscoveredAPIObservations in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_discovered_api_observations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_list_discovered_api_observations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_discovered_api_operations
    
    
    list_discovered_api_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsRequest,
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
        google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsAsyncPager
    )

Lists all the DiscoveredAPIOperations in a given project, location and ApiObservation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_discovered_api_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_list_discovered_api_operations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_discovered_api_observation_path
    
    
    parse_discovered_api_observation_path(path: str) -> typing.Dict[str, str]

Parses a discovered_api_observation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_discovered_api_observation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_discovered_api_observation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_discovered_api_operation_path
    
    
    parse_discovered_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a discovered_api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_discovered_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_discovered_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryAsyncClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryAsyncClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient
    
    
    ApiHubDiscoveryClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_discovery.transports.base.ApiHubDiscoveryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_discovery.transports.base.ApiHubDiscoveryTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub discovery client.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_ApiHubDiscoveryClient)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient___exit__)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.discovered_api_observation_path
    
    
    discovered_api_observation_path(
        project: str, location: str, discovered_api_observation: str
    ) -> str

Returns a fully-qualified discovered_api_observation string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.discovered_api_observation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_discovered_api_observation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.discovered_api_operation_path
    
    
    discovered_api_operation_path(
        project: str,
        location: str,
        discovered_api_observation: str,
        discovered_api_operation: str,
    ) -> str

Returns a fully-qualified discovered_api_operation string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.discovered_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_discovered_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_discovered_api_observation
    
    
    get_discovered_api_observation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.GetDiscoveredApiObservationRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.DiscoveredApiObservation

Gets a DiscoveredAPIObservation in a given project, location and ApiObservation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_discovered_api_observation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_get_discovered_api_observation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_discovered_api_operation
    
    
    get_discovered_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.GetDiscoveredApiOperationRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.DiscoveredApiOperation

Gets a DiscoveredAPIOperation in a given project, location, ApiObservation and ApiOperation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_discovered_api_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_get_discovered_api_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_get_location)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_discovered_api_observations
    
    
    list_discovered_api_observations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsRequest,
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
        google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsPager
    )

Lists all the DiscoveredAPIObservations in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_discovered_api_observations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_list_discovered_api_observations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_discovered_api_operations
    
    
    list_discovered_api_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsRequest,
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
        google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsPager
    )

Lists all the DiscoveredAPIOperations in a given project, location and ApiObservation.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_discovered_api_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_list_discovered_api_operations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_discovered_api_observation_path
    
    
    parse_discovered_api_observation_path(path: str) -> typing.Dict[str, str]

Parses a discovered_api_observation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_discovered_api_observation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_discovered_api_observation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_discovered_api_operation_path
    
    
    parse_discovered_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a discovered_api_operation path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_discovered_api_operation_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_discovered_api_operation_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.ApiHubDiscoveryClient#google_cloud_apihub_v1_services_api_hub_discovery_ApiHubDiscoveryClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsAsyncPager
    
    
    ListDiscoveredApiObservationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsRequest,
        response: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsAsyncPager#google_cloud_apihub_v1_services_api_hub_discovery_pagers_ListDiscoveredApiObservationsAsyncPager_ListDiscoveredApiObservationsAsyncPager)

### google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsPager
    
    
    ListDiscoveredApiObservationsPager(
        method: typing.Callable[
            [...],
            google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsResponse,
        ],
        request: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsRequest,
        response: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiObservationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiObservationsPager#google_cloud_apihub_v1_services_api_hub_discovery_pagers_ListDiscoveredApiObservationsPager_ListDiscoveredApiObservationsPager)

### google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsAsyncPager
    
    
    ListDiscoveredApiOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsRequest,
        response: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsAsyncPager#google_cloud_apihub_v1_services_api_hub_discovery_pagers_ListDiscoveredApiOperationsAsyncPager_ListDiscoveredApiOperationsAsyncPager)

### google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsPager
    
    
    ListDiscoveredApiOperationsPager(
        method: typing.Callable[
            [...],
            google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsResponse,
        ],
        request: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsRequest,
        response: google.cloud.apihub_v1.types.discovery_service.ListDiscoveredApiOperationsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_discovery.pagers.ListDiscoveredApiOperationsPager#google_cloud_apihub_v1_services_api_hub_discovery_pagers_ListDiscoveredApiOperationsPager_ListDiscoveredApiOperationsPager)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient
    
    
    ApiHubPluginAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub plugin async client.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_ApiHubPluginAsyncClient)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.create_plugin
    
    
    create_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin: typing.Optional[google.cloud.apihub_v1.types.plugin_service.Plugin] = None,
        plugin_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Create an API Hub plugin resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.create_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_create_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.create_plugin_instance
    
    
    create_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
        ] = None,
        plugin_instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a Plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.create_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_create_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_plugin
    
    
    delete_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginRequest, dict
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

Delete a Plugin in API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_delete_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_plugin_instance
    
    
    delete_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginInstanceRequest,
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

Deletes a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.delete_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_delete_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.disable_plugin
    
    
    disable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Disables a plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.disable_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_disable_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.disable_plugin_instance_action
    
    
    disable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Disables a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.disable_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_disable_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.enable_plugin
    
    
    enable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Enables a plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.enable_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_enable_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.enable_plugin_instance_action
    
    
    enable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Enables a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.enable_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_enable_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.execute_plugin_instance_action
    
    
    execute_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ExecutePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_execution_detail: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.ActionExecutionDetail
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

Executes a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.execute_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_execute_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_location)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_plugin
    
    
    get_plugin(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.plugin_service.GetPluginRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Get an API Hub plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_plugin_instance
    
    
    get_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.GetPluginInstanceRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Get an API Hub plugin instance.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_plugin_instances
    
    
    list_plugin_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest, dict
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
        google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager
    )

List all the plugins in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_plugin_instances](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_plugin_instances)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_plugins
    
    
    list_plugins(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager

List all the plugins in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.list_plugins](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_plugins)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_plugin_path
    
    
    parse_plugin_path(path: str) -> typing.Dict[str, str]

Parses a plugin path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_plugin_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_plugin_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_parse_service_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.plugin_path
    
    
    plugin_path(project: str, location: str, plugin: str) -> str

Returns a fully-qualified plugin string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.plugin_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_plugin_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.service_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_service_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.update_plugin_instance
    
    
    update_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.UpdatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
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
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Updates a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.update_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_update_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient
    
    
    ApiHubPluginClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub plugin client.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_ApiHubPluginClient)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient___exit__)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_attribute_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_cancel_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_common_location_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_common_project_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.create_plugin
    
    
    create_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin: typing.Optional[google.cloud.apihub_v1.types.plugin_service.Plugin] = None,
        plugin_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Create an API Hub plugin resource in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.create_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_create_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.create_plugin_instance
    
    
    create_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
        ] = None,
        plugin_instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a Plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.create_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_create_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_delete_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_plugin
    
    
    delete_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginRequest, dict
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

Delete a Plugin in API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_delete_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_plugin_instance
    
    
    delete_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginInstanceRequest,
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

Deletes a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.delete_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_delete_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.disable_plugin
    
    
    disable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Disables a plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.disable_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_disable_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.disable_plugin_instance_action
    
    
    disable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Disables a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.disable_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_disable_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.enable_plugin
    
    
    enable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Enables a plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.enable_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_enable_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.enable_plugin_instance_action
    
    
    enable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Enables a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.enable_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_enable_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.execute_plugin_instance_action
    
    
    execute_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ExecutePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_execution_detail: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.ActionExecutionDetail
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Executes a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.execute_plugin_instance_action](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_execute_plugin_instance_action)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_from_service_account_file)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_from_service_account_info)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_from_service_account_json)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_get_location)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_get_operation)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_plugin
    
    
    get_plugin(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.plugin_service.GetPluginRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Get an API Hub plugin.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_plugin](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_get_plugin)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_plugin_instance
    
    
    get_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.GetPluginInstanceRequest, dict
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
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Get an API Hub plugin instance.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.get_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_get_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_list_locations)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_list_operations)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_plugin_instances
    
    
    list_plugin_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesPager

List all the plugins in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_plugin_instances](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_list_plugin_instances)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_plugins
    
    
    list_plugins(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsPager

List all the plugins in a given project and location.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.list_plugins](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_list_plugins)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_attribute_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_attribute_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_common_location_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_common_project_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_plugin_path
    
    
    parse_plugin_path(path: str) -> typing.Dict[str, str]

Parses a plugin path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_plugin_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_plugin_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_parse_service_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.plugin_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_plugin_instance_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.plugin_path
    
    
    plugin_path(project: str, location: str, plugin: str) -> str

Returns a fully-qualified plugin string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.plugin_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_plugin_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.service_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_service_account_path)

### google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.update_plugin_instance
    
    
    update_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.UpdatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
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
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Updates a plugin instance in the API hub.

See more: [google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient.update_plugin_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginClient#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginClient_update_plugin_instance)

### google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager
    
    
    ListPluginInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager#google_cloud_apihub_v1_services_api_hub_plugin_pagers_ListPluginInstancesAsyncPager_ListPluginInstancesAsyncPager)

### google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesPager
    
    
    ListPluginInstancesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesPager#google_cloud_apihub_v1_services_api_hub_plugin_pagers_ListPluginInstancesPager_ListPluginInstancesPager)

### google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager
    
    
    ListPluginsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager#google_cloud_apihub_v1_services_api_hub_plugin_pagers_ListPluginsAsyncPager_ListPluginsAsyncPager)

### google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsPager
    
    
    ListPluginsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse,
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

See more: [google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsPager#google_cloud_apihub_v1_services_api_hub_plugin_pagers_ListPluginsPager_ListPluginsPager)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient
    
    
    HostProjectRegistrationServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.host_project_registration_service.transports.base.HostProjectRegistrationServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.host_project_registration_service.transports.base.HostProjectRegistrationServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the host project registration service async client.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_HostProjectRegistrationServiceAsyncClient)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.create_host_project_registration
    
    
    create_host_project_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.CreateHostProjectRegistrationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        host_project_registration: typing.Optional[
            google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
        ] = None,
        host_project_registration_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
    )

Create a host project registration.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.create_host_project_registration](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_create_host_project_registration)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_host_project_registration
    
    
    get_host_project_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.GetHostProjectRegistrationRequest,
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
        google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
    )

Get a host project registration.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_host_project_registration](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_get_host_project_registration)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_get_location)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_get_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.host_project_registration_service.transports.base.HostProjectRegistrationServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.host_project_registration_path
    
    
    host_project_registration_path(
        project: str, location: str, host_project_registration: str
    ) -> str

Returns a fully-qualified host_project_registration string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.host_project_registration_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_host_project_registration_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_host_project_registrations
    
    
    list_host_project_registrations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsRequest,
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
        google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsAsyncPager
    )

Lists host project registrations.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_host_project_registrations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_list_host_project_registrations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_list_locations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_list_operations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_host_project_registration_path
    
    
    parse_host_project_registration_path(path: str) -> typing.Dict[str, str]

Parses a host_project_registration path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient.parse_host_project_registration_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceAsyncClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceAsyncClient_parse_host_project_registration_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient
    
    
    HostProjectRegistrationServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.host_project_registration_service.transports.base.HostProjectRegistrationServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.host_project_registration_service.transports.base.HostProjectRegistrationServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the host project registration service client.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_HostProjectRegistrationServiceClient)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient___exit__)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_cancel_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_common_billing_account_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_common_folder_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_common_location_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_common_organization_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_common_project_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.create_host_project_registration
    
    
    create_host_project_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.CreateHostProjectRegistrationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        host_project_registration: typing.Optional[
            google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
        ] = None,
        host_project_registration_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
    )

Create a host project registration.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.create_host_project_registration](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_create_host_project_registration)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_delete_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_from_service_account_file)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_from_service_account_info)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_from_service_account_json)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_host_project_registration
    
    
    get_host_project_registration(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.GetHostProjectRegistrationRequest,
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
        google.cloud.apihub_v1.types.host_project_registration_service.HostProjectRegistration
    )

Get a host project registration.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_host_project_registration](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_get_host_project_registration)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_get_location)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_get_operation)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.host_project_registration_path
    
    
    host_project_registration_path(
        project: str, location: str, host_project_registration: str
    ) -> str

Returns a fully-qualified host_project_registration string.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.host_project_registration_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_host_project_registration_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_host_project_registrations
    
    
    list_host_project_registrations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsRequest,
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
        google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsPager
    )

Lists host project registrations.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_host_project_registrations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_list_host_project_registrations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_list_locations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_list_operations)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_common_location_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_common_project_path)

### google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_host_project_registration_path
    
    
    parse_host_project_registration_path(path: str) -> typing.Dict[str, str]

Parses a host_project_registration path into its component segments.

See more: [google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient.parse_host_project_registration_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.HostProjectRegistrationServiceClient#google_cloud_apihub_v1_services_host_project_registration_service_HostProjectRegistrationServiceClient_parse_host_project_registration_path)

### google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsAsyncPager
    
    
    ListHostProjectRegistrationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsRequest,
        response: google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsResponse,
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsAsyncPager#google_cloud_apihub_v1_services_host_project_registration_service_pagers_ListHostProjectRegistrationsAsyncPager_ListHostProjectRegistrationsAsyncPager)

### google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsPager
    
    
    ListHostProjectRegistrationsPager(
        method: typing.Callable[
            [...],
            google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsResponse,
        ],
        request: google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsRequest,
        response: google.cloud.apihub_v1.types.host_project_registration_service.ListHostProjectRegistrationsResponse,
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

See more: [google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.host_project_registration_service.pagers.ListHostProjectRegistrationsPager#google_cloud_apihub_v1_services_host_project_registration_service_pagers_ListHostProjectRegistrationsPager_ListHostProjectRegistrationsPager)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient
    
    
    LintingServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.linting_service.transports.base.LintingServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.linting_service.transports.base.LintingServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the linting service async client.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_LintingServiceAsyncClient)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_location)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_style_guide
    
    
    get_style_guide(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.GetStyleGuideRequest, dict
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuide

Get the style guide being used for linting.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_style_guide](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_style_guide)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_style_guide_contents
    
    
    get_style_guide_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.GetStyleGuideContentsRequest,
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuideContents

Get the contents of the style guide.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_style_guide_contents](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_style_guide_contents)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.linting_service.transports.base.LintingServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.lint_spec
    
    
    lint_spec(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.linting_service.LintSpecRequest, dict]
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

Lints the requested spec and updates the corresponding API Spec with the lint response.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.lint_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_lint_spec)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_list_locations)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_list_operations)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_spec_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_style_guide_path
    
    
    parse_style_guide_path(path: str) -> typing.Dict[str, str]

Parses a style_guide path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.parse_style_guide_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_parse_style_guide_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_spec_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.style_guide_path
    
    
    style_guide_path(project: str, location: str, plugin: str) -> str

Returns a fully-qualified style_guide string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.style_guide_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_style_guide_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.update_style_guide
    
    
    update_style_guide(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.UpdateStyleGuideRequest, dict
            ]
        ] = None,
        *,
        style_guide: typing.Optional[
            google.cloud.apihub_v1.types.linting_service.StyleGuide
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuide

Update the styleGuide to be used for liniting in by API hub.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient.update_style_guide](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceAsyncClient#google_cloud_apihub_v1_services_linting_service_LintingServiceAsyncClient_update_style_guide)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient
    
    
    LintingServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.linting_service.transports.base.LintingServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.linting_service.transports.base.LintingServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the linting service client.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_LintingServiceClient)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient___exit__)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_cancel_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_common_billing_account_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_common_folder_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_common_location_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_common_organization_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_common_project_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_delete_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_from_service_account_file)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_from_service_account_info)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_from_service_account_json)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_get_location)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_get_operation)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_style_guide
    
    
    get_style_guide(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.GetStyleGuideRequest, dict
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuide

Get the style guide being used for linting.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_style_guide](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_get_style_guide)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_style_guide_contents
    
    
    get_style_guide_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.GetStyleGuideContentsRequest,
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuideContents

Get the contents of the style guide.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.get_style_guide_contents](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_get_style_guide_contents)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.lint_spec
    
    
    lint_spec(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.linting_service.LintSpecRequest, dict]
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

Lints the requested spec and updates the corresponding API Spec with the lint response.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.lint_spec](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_lint_spec)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_list_locations)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_list_operations)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_common_location_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_common_project_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_spec_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_style_guide_path
    
    
    parse_style_guide_path(path: str) -> typing.Dict[str, str]

Parses a style_guide path into its component segments.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.parse_style_guide_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_parse_style_guide_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.spec_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_spec_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.style_guide_path
    
    
    style_guide_path(project: str, location: str, plugin: str) -> str

Returns a fully-qualified style_guide string.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.style_guide_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_style_guide_path)

### google.cloud.apihub_v1.services.linting_service.LintingServiceClient.update_style_guide
    
    
    update_style_guide(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.linting_service.UpdateStyleGuideRequest, dict
            ]
        ] = None,
        *,
        style_guide: typing.Optional[
            google.cloud.apihub_v1.types.linting_service.StyleGuide
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
    ) -> google.cloud.apihub_v1.types.linting_service.StyleGuide

Update the styleGuide to be used for liniting in by API hub.

See more: [google.cloud.apihub_v1.services.linting_service.LintingServiceClient.update_style_guide](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.linting_service.LintingServiceClient#google_cloud_apihub_v1_services_linting_service_LintingServiceClient_update_style_guide)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient
    
    
    ProvisioningAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.provisioning.transports.base.ProvisioningTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.provisioning.transports.base.ProvisioningTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the provisioning async client.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_ProvisioningAsyncClient)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.api_hub_instance_path
    
    
    api_hub_instance_path(project: str, location: str, api_hub_instance: str) -> str

Returns a fully-qualified api_hub_instance string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.api_hub_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_api_hub_instance_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.create_api_hub_instance
    
    
    create_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.CreateApiHubInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_hub_instance: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiHubInstance
        ] = None,
        api_hub_instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Provisions instance resources for the API Hub.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.create_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_create_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.delete_api_hub_instance
    
    
    delete_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.DeleteApiHubInstanceRequest,
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

Deletes the API hub instance.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.delete_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_delete_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_api_hub_instance
    
    
    get_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.GetApiHubInstanceRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiHubInstance

Gets details of a single API Hub instance.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_get_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_get_location)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_get_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.provisioning.transports.base.ProvisioningTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_list_locations)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_list_operations)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.lookup_api_hub_instance
    
    
    lookup_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.LookupApiHubInstanceRequest,
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
    ) -> google.cloud.apihub_v1.types.provisioning_service.LookupApiHubInstanceResponse

Looks up an Api Hub instance in a given GCP project.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.lookup_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_lookup_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_api_hub_instance_path
    
    
    parse_api_hub_instance_path(path: str) -> typing.Dict[str, str]

Parses a api_hub_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_api_hub_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_api_hub_instance_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apihub_v1_services_provisioning_ProvisioningAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient
    
    
    ProvisioningClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.provisioning.transports.base.ProvisioningTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.provisioning.transports.base.ProvisioningTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the provisioning client.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_ProvisioningClient)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient___exit__)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.api_hub_instance_path
    
    
    api_hub_instance_path(project: str, location: str, api_hub_instance: str) -> str

Returns a fully-qualified api_hub_instance string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.api_hub_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_api_hub_instance_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_cancel_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_common_billing_account_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_common_folder_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_common_location_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_common_organization_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_common_project_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.create_api_hub_instance
    
    
    create_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.CreateApiHubInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_hub_instance: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiHubInstance
        ] = None,
        api_hub_instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Provisions instance resources for the API Hub.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.create_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_create_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.delete_api_hub_instance
    
    
    delete_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.DeleteApiHubInstanceRequest,
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

Deletes the API hub instance.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.delete_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_delete_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_delete_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_from_service_account_file)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_from_service_account_info)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_from_service_account_json)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_api_hub_instance
    
    
    get_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.GetApiHubInstanceRequest,
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiHubInstance

Gets details of a single API Hub instance.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_get_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_get_location)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_get_operation)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_list_locations)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_list_operations)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.lookup_api_hub_instance
    
    
    lookup_api_hub_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.provisioning_service.LookupApiHubInstanceRequest,
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
    ) -> google.cloud.apihub_v1.types.provisioning_service.LookupApiHubInstanceResponse

Looks up an Api Hub instance in a given GCP project.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.lookup_api_hub_instance](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_lookup_api_hub_instance)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_api_hub_instance_path
    
    
    parse_api_hub_instance_path(path: str) -> typing.Dict[str, str]

Parses a api_hub_instance path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_api_hub_instance_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_api_hub_instance_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_common_location_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.provisioning.ProvisioningClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.provisioning.ProvisioningClient#google_cloud_apihub_v1_services_provisioning_ProvisioningClient_parse_common_project_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient
    
    
    RuntimeProjectAttachmentServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.runtime_project_attachment_service.transports.base.RuntimeProjectAttachmentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.runtime_project_attachment_service.transports.base.RuntimeProjectAttachmentServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the runtime project attachment service async client.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_RuntimeProjectAttachmentServiceAsyncClient)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_cancel_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_common_billing_account_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_common_folder_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_common_location_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_common_organization_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_common_project_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.create_runtime_project_attachment
    
    
    create_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        runtime_project_attachment: typing.Optional[
            google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
        ] = None,
        runtime_project_attachment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
    )

Attaches a runtime project to the host project.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.create_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_create_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_delete_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.delete_runtime_project_attachment
    
    
    delete_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest,
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

Delete a runtime project attachment in the API Hub.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.delete_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_delete_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_from_service_account_file)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_from_service_account_info)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_from_service_account_json)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_get_location)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_get_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_runtime_project_attachment
    
    
    get_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest,
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
        google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
    )

Gets a runtime project attachment.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_get_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.runtime_project_attachment_service.transports.base.RuntimeProjectAttachmentServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_get_transport_class)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_list_locations)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_list_operations)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_runtime_project_attachments
    
    
    list_runtime_project_attachments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
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
        google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsAsyncPager
    )

List runtime projects attached to the host project.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.list_runtime_project_attachments](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_list_runtime_project_attachments)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.lookup_runtime_project_attachment
    
    
    lookup_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest,
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
        google.cloud.apihub_v1.types.runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse
    )

Look up a runtime project attachment.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.lookup_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_lookup_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_common_location_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_common_project_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_runtime_project_attachment_path
    
    
    parse_runtime_project_attachment_path(path: str) -> typing.Dict[str, str]

Parses a runtime_project_attachment path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.parse_runtime_project_attachment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_parse_runtime_project_attachment_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.runtime_project_attachment_path
    
    
    runtime_project_attachment_path(
        project: str, location: str, runtime_project_attachment: str
    ) -> str

Returns a fully-qualified runtime_project_attachment string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient.runtime_project_attachment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceAsyncClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceAsyncClient_runtime_project_attachment_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient
    
    
    RuntimeProjectAttachmentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.runtime_project_attachment_service.transports.base.RuntimeProjectAttachmentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.runtime_project_attachment_service.transports.base.RuntimeProjectAttachmentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the runtime project attachment service client.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_RuntimeProjectAttachmentServiceClient)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient___exit__)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.cancel_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_cancel_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_common_billing_account_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_common_folder_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_common_location_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_common_organization_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_common_project_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.create_runtime_project_attachment
    
    
    create_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        runtime_project_attachment: typing.Optional[
            google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
        ] = None,
        runtime_project_attachment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
    )

Attaches a runtime project to the host project.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.create_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_create_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.delete_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_delete_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.delete_runtime_project_attachment
    
    
    delete_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest,
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

Delete a runtime project attachment in the API Hub.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.delete_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_delete_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_from_service_account_file)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_from_service_account_info)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_from_service_account_json)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_location
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_get_location)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_operation
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_get_operation)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_runtime_project_attachment
    
    
    get_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest,
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
        google.cloud.apihub_v1.types.runtime_project_attachment_service.RuntimeProjectAttachment
    )

Gets a runtime project attachment.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.get_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_get_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_locations
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_list_locations)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_operations
    
    
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_list_operations)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_runtime_project_attachments
    
    
    list_runtime_project_attachments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
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
        google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsPager
    )

List runtime projects attached to the host project.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.list_runtime_project_attachments](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_list_runtime_project_attachments)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.lookup_runtime_project_attachment
    
    
    lookup_runtime_project_attachment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest,
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
        google.cloud.apihub_v1.types.runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse
    )

Look up a runtime project attachment.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.lookup_runtime_project_attachment](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_lookup_runtime_project_attachment)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_common_billing_account_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_common_folder_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_common_location_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_common_organization_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_common_project_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_runtime_project_attachment_path
    
    
    parse_runtime_project_attachment_path(path: str) -> typing.Dict[str, str]

Parses a runtime_project_attachment path into its component segments.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.parse_runtime_project_attachment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_parse_runtime_project_attachment_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.runtime_project_attachment_path
    
    
    runtime_project_attachment_path(
        project: str, location: str, runtime_project_attachment: str
    ) -> str

Returns a fully-qualified runtime_project_attachment string.

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient.runtime_project_attachment_path](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.RuntimeProjectAttachmentServiceClient#google_cloud_apihub_v1_services_runtime_project_attachment_service_RuntimeProjectAttachmentServiceClient_runtime_project_attachment_path)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsAsyncPager
    
    
    ListRuntimeProjectAttachmentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
        response: google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsAsyncPager#google_cloud_apihub_v1_services_runtime_project_attachment_service_pagers_ListRuntimeProjectAttachmentsAsyncPager_ListRuntimeProjectAttachmentsAsyncPager)

### google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsPager
    
    
    ListRuntimeProjectAttachmentsPager(
        method: typing.Callable[
            [...],
            google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
        ],
        request: google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
        response: google.cloud.apihub_v1.types.runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
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

See more: [google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsPager](https://cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.runtime_project_attachment_service.pagers.ListRuntimeProjectAttachmentsPager#google_cloud_apihub_v1_services_runtime_project_attachment_service_pagers_ListRuntimeProjectAttachmentsPager_ListRuntimeProjectAttachmentsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
