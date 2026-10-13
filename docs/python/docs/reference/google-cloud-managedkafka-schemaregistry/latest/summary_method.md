---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/summary_method/
title: Package Methods (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:43.186420+00:00
---

# Package Methods (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.0 

Summary of entries of Methods for google-cloud-managedkafka-schemaregistry.

## 

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient
    
    
    ManagedSchemaRegistryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.transports.base.ManagedSchemaRegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.transports.base.ManagedSchemaRegistryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the managed schema registry async client.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_ManagedSchemaRegistryAsyncClient)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_cancel_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.check_compatibility
    
    
    check_compatibility(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CheckCompatibilityRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        schema: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CheckCompatibilityResponse
    )

Check compatibility of a schema with all versions or a specific version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.check_compatibility](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_check_compatibility)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_common_billing_account_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_common_folder_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_common_location_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_common_organization_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_common_project_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.create_schema_registry
    
    
    create_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateSchemaRegistryRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schema_registry: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
    )

Create a schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.create_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_create_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.create_version
    
    
    create_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        schema_type: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema.SchemaType
        ] = None,
        schema: typing.Optional[str] = None,
        references: typing.Optional[
            typing.MutableSequence[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema.SchemaReference
            ]
        ] = None,
        normalize: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateVersionResponse
    )

Register a new version under a given subject with the given schema.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.create_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_create_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_config
    
    
    delete_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaConfigRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Delete schema config for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_mode
    
    
    delete_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaModeRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Delete schema mode for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_schema_mode)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_registry
    
    
    delete_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaRegistryRequest,
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

Delete a schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_subject
    
    
    delete_subject(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSubjectRequest,
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

Delete a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_subject](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_subject)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_version
    
    
    delete_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteVersionRequest,
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

Delete a version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.delete_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_delete_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_from_service_account_file)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_from_service_account_info)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_from_service_account_json)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_context
    
    
    get_context(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetContextRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Context
    )

Get the context.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_context](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_context)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_location
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_location)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_raw_schema
    
    
    get_raw_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRequest,
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

Get the schema string for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_raw_schema](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_raw_schema)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_raw_schema_version
    
    
    get_raw_schema_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetVersionRequest,
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

Get the schema string only for a version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_raw_schema_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_raw_schema_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema
    
    
    get_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRequest,
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
    ) -> google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema

Get the schema for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_schema)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_config
    
    
    get_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaConfigRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Get schema config at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_mode
    
    
    get_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaModeRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Get mode at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_schema_mode)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_registry
    
    
    get_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRegistryRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
    )

Get the schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.transports.base.ManagedSchemaRegistryTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_transport_class)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_version
    
    
    get_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetVersionRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaVersion
    )

Get a versioned schema (schema with subject/version) of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.get_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_get_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_contexts
    
    
    list_contexts(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListContextsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List contexts for a schema registry.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_contexts](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_contexts)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_locations
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_locations)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_operations
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_operations)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_referenced_schemas
    
    
    list_referenced_schemas(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListReferencedSchemasRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get a list of IDs of schemas that reference the schema with the given subject and version.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_referenced_schemas](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_referenced_schemas)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_registries
    
    
    list_schema_registries(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaRegistriesRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaRegistriesResponse
    )

List schema registries.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_registries](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_schema_registries)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_types
    
    
    list_schema_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaTypesRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List the supported schema types.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_types](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_schema_types)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_versions
    
    
    list_schema_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaVersionsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List the schema versions for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_schema_versions](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_schema_versions)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_subjects
    
    
    list_subjects(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSubjectsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api.httpbody_pb2.HttpBody

List subjects in the schema registry.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_subjects](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_subjects)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_subjects_by_schema_id
    
    
    list_subjects_by_schema_id(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSubjectsBySchemaIdRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api.httpbody_pb2.HttpBody

List subjects which reference a particular schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_subjects_by_schema_id](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_subjects_by_schema_id)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_versions
    
    
    list_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListVersionsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get all versions of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.list_versions](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_list_versions)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.lookup_version
    
    
    lookup_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.LookupVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schema: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaVersion
    )

Lookup a schema under the specified subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.lookup_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_lookup_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_common_billing_account_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_common_folder_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_common_location_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_common_organization_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_common_project_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_config_path
    
    
    parse_schema_config_path(path: str) -> typing.Dict[str, str]

Parses a schema_config path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_config_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_config_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_context_path
    
    
    parse_schema_context_path(path: str) -> typing.Dict[str, str]

Parses a schema_context path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_context_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_context_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_mode_path
    
    
    parse_schema_mode_path(path: str) -> typing.Dict[str, str]

Parses a schema_mode path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_mode_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_mode_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_path
    
    
    parse_schema_path(path: str) -> typing.Dict[str, str]

Parses a schema path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_registry_path
    
    
    parse_schema_registry_path(path: str) -> typing.Dict[str, str]

Parses a schema_registry path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_registry_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_registry_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_subject_path
    
    
    parse_schema_subject_path(path: str) -> typing.Dict[str, str]

Parses a schema_subject path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_subject_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_subject_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_version_path
    
    
    parse_schema_version_path(path: str) -> typing.Dict[str, str]

Parses a schema_version path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.parse_schema_version_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_parse_schema_version_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_config_path
    
    
    schema_config_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_config string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_config_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_config_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_context_path
    
    
    schema_context_path(
        project: str, location: str, schema_registry: str, context: str
    ) -> str

Returns a fully-qualified schema_context string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_context_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_context_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_mode_path
    
    
    schema_mode_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_mode string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_mode_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_mode_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_path
    
    
    schema_path(project: str, location: str, schema_registry: str, schema: str) -> str

Returns a fully-qualified schema string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_registry_path
    
    
    schema_registry_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_registry string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_registry_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_registry_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_subject_path
    
    
    schema_subject_path(
        project: str, location: str, schema_registry: str, subject: str
    ) -> str

Returns a fully-qualified schema_subject string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_subject_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_subject_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_version_path
    
    
    schema_version_path(
        project: str, location: str, schema_registry: str, subject: str, version: str
    ) -> str

Returns a fully-qualified schema_version string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.schema_version_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_schema_version_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.update_schema_config
    
    
    update_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.UpdateSchemaConfigRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        compatibility: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig.CompatibilityType
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Update config at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.update_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_update_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.update_schema_mode
    
    
    update_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.UpdateSchemaModeRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        mode: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode.ModeType
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Update mode at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient.update_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryAsyncClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryAsyncClient_update_schema_mode)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient
    
    
    ManagedSchemaRegistryClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.transports.base.ManagedSchemaRegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.transports.base.ManagedSchemaRegistryTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the managed schema registry client.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_ManagedSchemaRegistryClient)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient___exit__)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.cancel_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_cancel_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.check_compatibility
    
    
    check_compatibility(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CheckCompatibilityRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        schema: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CheckCompatibilityResponse
    )

Check compatibility of a schema with all versions or a specific version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.check_compatibility](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_check_compatibility)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_common_billing_account_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_common_folder_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_common_location_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_common_organization_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_common_project_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.create_schema_registry
    
    
    create_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateSchemaRegistryRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schema_registry: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
    )

Create a schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.create_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_create_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.create_version
    
    
    create_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        schema_type: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema.SchemaType
        ] = None,
        schema: typing.Optional[str] = None,
        references: typing.Optional[
            typing.MutableSequence[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema.SchemaReference
            ]
        ] = None,
        normalize: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.CreateVersionResponse
    )

Register a new version under a given subject with the given schema.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.create_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_create_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_config
    
    
    delete_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaConfigRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Delete schema config for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_mode
    
    
    delete_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaModeRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Delete schema mode for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_schema_mode)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_registry
    
    
    delete_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSchemaRegistryRequest,
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

Delete a schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_subject
    
    
    delete_subject(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteSubjectRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Delete a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_subject](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_subject)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_version
    
    
    delete_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.DeleteVersionRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Delete a version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.delete_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_delete_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_from_service_account_file)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_from_service_account_info)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_from_service_account_json)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_context
    
    
    get_context(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetContextRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Context
    )

Get the context.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_context](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_context)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_location
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_location)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_mtls_endpoint_and_cert_source)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_operation
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_operation)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_raw_schema
    
    
    get_raw_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get the schema string for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_raw_schema](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_raw_schema)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_raw_schema_version
    
    
    get_raw_schema_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetVersionRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get the schema string only for a version of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_raw_schema_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_raw_schema_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema
    
    
    get_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRequest,
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
    ) -> google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.Schema

Get the schema for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_schema)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_config
    
    
    get_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaConfigRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Get schema config at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_mode
    
    
    get_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaModeRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Get mode at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_schema_mode)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_registry
    
    
    get_schema_registry(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetSchemaRegistryRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaRegistry
    )

Get the schema registry instance.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_schema_registry](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_schema_registry)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_version
    
    
    get_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.GetVersionRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaVersion
    )

Get a versioned schema (schema with subject/version) of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.get_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_get_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_contexts
    
    
    list_contexts(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListContextsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List contexts for a schema registry.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_contexts](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_contexts)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_locations
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_locations)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_operations
    
    
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

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_operations)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_referenced_schemas
    
    
    list_referenced_schemas(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListReferencedSchemasRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get a list of IDs of schemas that reference the schema with the given subject and version.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_referenced_schemas](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_referenced_schemas)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_registries
    
    
    list_schema_registries(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaRegistriesRequest,
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaRegistriesResponse
    )

List schema registries.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_registries](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_schema_registries)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_types
    
    
    list_schema_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaTypesRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List the supported schema types.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_types](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_schema_types)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_versions
    
    
    list_schema_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSchemaVersionsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

List the schema versions for the given schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_schema_versions](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_schema_versions)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_subjects
    
    
    list_subjects(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSubjectsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        subject_prefix: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api.httpbody_pb2.HttpBody

List subjects in the schema registry.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_subjects](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_subjects)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_subjects_by_schema_id
    
    
    list_subjects_by_schema_id(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListSubjectsBySchemaIdRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api.httpbody_pb2.HttpBody

List subjects which reference a particular schema id.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_subjects_by_schema_id](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_subjects_by_schema_id)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_versions
    
    
    list_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.ListVersionsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Get all versions of a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.list_versions](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_list_versions)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.lookup_version
    
    
    lookup_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.LookupVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schema: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaVersion
    )

Lookup a schema under the specified subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.lookup_version](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_lookup_version)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_common_billing_account_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_common_folder_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_common_location_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_common_organization_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_common_project_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_config_path
    
    
    parse_schema_config_path(path: str) -> typing.Dict[str, str]

Parses a schema_config path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_config_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_config_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_context_path
    
    
    parse_schema_context_path(path: str) -> typing.Dict[str, str]

Parses a schema_context path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_context_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_context_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_mode_path
    
    
    parse_schema_mode_path(path: str) -> typing.Dict[str, str]

Parses a schema_mode path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_mode_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_mode_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_path
    
    
    parse_schema_path(path: str) -> typing.Dict[str, str]

Parses a schema path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_registry_path
    
    
    parse_schema_registry_path(path: str) -> typing.Dict[str, str]

Parses a schema_registry path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_registry_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_registry_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_subject_path
    
    
    parse_schema_subject_path(path: str) -> typing.Dict[str, str]

Parses a schema_subject path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_subject_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_subject_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_version_path
    
    
    parse_schema_version_path(path: str) -> typing.Dict[str, str]

Parses a schema_version path into its component segments.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.parse_schema_version_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_parse_schema_version_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_config_path
    
    
    schema_config_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_config string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_config_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_config_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_context_path
    
    
    schema_context_path(
        project: str, location: str, schema_registry: str, context: str
    ) -> str

Returns a fully-qualified schema_context string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_context_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_context_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_mode_path
    
    
    schema_mode_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_mode string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_mode_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_mode_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_path
    
    
    schema_path(project: str, location: str, schema_registry: str, schema: str) -> str

Returns a fully-qualified schema string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_registry_path
    
    
    schema_registry_path(project: str, location: str, schema_registry: str) -> str

Returns a fully-qualified schema_registry string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_registry_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_registry_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_subject_path
    
    
    schema_subject_path(
        project: str, location: str, schema_registry: str, subject: str
    ) -> str

Returns a fully-qualified schema_subject string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_subject_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_subject_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_version_path
    
    
    schema_version_path(
        project: str, location: str, schema_registry: str, subject: str, version: str
    ) -> str

Returns a fully-qualified schema_version string.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.schema_version_path](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_schema_version_path)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.update_schema_config
    
    
    update_schema_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.UpdateSchemaConfigRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        compatibility: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig.CompatibilityType
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaConfig
    )

Update config at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.update_schema_config](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_update_schema_config)

### google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.update_schema_mode
    
    
    update_schema_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.managedkafka_schemaregistry_v1.types.schema_registry.UpdateSchemaModeRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        mode: typing.Optional[
            google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode.ModeType
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
        google.cloud.managedkafka_schemaregistry_v1.types.schema_registry_resources.SchemaMode
    )

Update mode at global level or for a subject.

See more: [google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient.update_schema_mode](https://cloud.google.com/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest/google.cloud.managedkafka_schemaregistry_v1.services.managed_schema_registry.ManagedSchemaRegistryClient#google_cloud_managedkafka_schemaregistry_v1_services_managed_schema_registry_ManagedSchemaRegistryClient_update_schema_mode)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
