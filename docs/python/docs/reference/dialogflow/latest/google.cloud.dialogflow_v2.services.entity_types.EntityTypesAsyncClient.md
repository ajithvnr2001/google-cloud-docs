---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient
title: Class EntityTypesAsyncClient (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:46:57.311364+00:00
---

# Class EntityTypesAsyncClient (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EntityTypesAsyncClient (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    EntityTypesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2.services.entity_types.transports.base.EntityTypesTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2.services.entity_types.transports.base.EntityTypesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing EntityTypes.

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
`EntityTypesTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### EntityTypesAsyncClient
    
    
    EntityTypesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2.services.entity_types.transports.base.EntityTypesTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2.services.entity_types.transports.base.EntityTypesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the entity types async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,EntityTypesTransport,Callable[..., EntityTypesTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the EntityTypesTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### batch_create_entities
    
    
    batch_create_entities(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.BatchCreateEntitiesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        entities: typing.Optional[
            typing.MutableSequence[
                google.cloud.dialogflow_v2.types.entity_type.EntityType.Entity
            ]
        ] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates multiple new entities in the specified entity type.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty `Struct message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
  * `response`: An `Empty message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__



Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_batch_create_entities():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        entities = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).Entity()
        entities.value = "value_value"
        entities.synonyms = ['synonyms_value1', 'synonyms_value2']
    
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).[BatchCreateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchCreateEntitiesRequest.html)(
            parent="parent_value",
            entities=entities,
        )
    
        # Make the request
        operation = await client.[batch_create_entities](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_batch_create_entities)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.BatchCreateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchCreateEntitiesRequest), dict]]`   
The request object. The request message for EntityTypes.BatchCreateEntities.  
`parent` |  ``str``   
Required. The name of the entity type to create entities in. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`entities` |  `:class:`MutableSequence[[google.cloud.dialogflow_v2.types.EntityType.Entity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType.Entity)]``   
Required. The entities to create. This corresponds to the `entities` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### batch_delete_entities
    
    
    batch_delete_entities(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.BatchDeleteEntitiesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        entity_values: typing.Optional[typing.MutableSequence[str]] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deletes entities in the specified entity type.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty `Struct message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
  * `response`: An `Empty message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__



Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_batch_delete_entities():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).[BatchDeleteEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntitiesRequest.html)(
            parent="parent_value",
            entity_values=['entity_values_value1', 'entity_values_value2'],
        )
    
        # Make the request
        operation = await client.[batch_delete_entities](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_batch_delete_entities)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.BatchDeleteEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntitiesRequest), dict]]`   
The request object. The request message for EntityTypes.BatchDeleteEntities.  
`parent` |  ``str``   
Required. The name of the entity type to delete entries for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`entity_values` |  `:class:`MutableSequence[str]``   
Required. The reference `values` of the entities to delete. Note that these are not fully-qualified names, i.e. they don't start with `projects/`. This corresponds to the `entity_values` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### batch_delete_entity_types
    
    
    batch_delete_entity_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.BatchDeleteEntityTypesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        entity_type_names: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deletes entity types in the specified agent.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty `Struct message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
  * `response`: An `Empty message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__



Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_batch_delete_entity_types():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).[BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntityTypesRequest.html)(
            parent="parent_value",
            entity_type_names=['entity_type_names_value1', 'entity_type_names_value2'],
        )
    
        # Make the request
        operation = await client.[batch_delete_entity_types](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_batch_delete_entity_types)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntityTypesRequest), dict]]`   
The request object. The request message for EntityTypes.BatchDeleteEntityTypes.  
`parent` |  ``str``   
Required. The name of the agent to delete all entities types for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`entity_type_names` |  `:class:`MutableSequence[str]``   
Required. The names entity types to delete. All names must point to the same agent as `parent`. This corresponds to the `entity_type_names` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### batch_update_entities
    
    
    batch_update_entities(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.BatchUpdateEntitiesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        entities: typing.Optional[
            typing.MutableSequence[
                google.cloud.dialogflow_v2.types.entity_type.EntityType.Entity
            ]
        ] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates or creates multiple entities in the specified entity type. This method does not affect entities in the entity type that aren't explicitly specified in the request.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty `Struct message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
  * `response`: An `Empty message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__



Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_batch_update_entities():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        entities = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).Entity()
        entities.value = "value_value"
        entities.synonyms = ['synonyms_value1', 'synonyms_value2']
    
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).[BatchUpdateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntitiesRequest.html)(
            parent="parent_value",
            entities=entities,
        )
    
        # Make the request
        operation = await client.[batch_update_entities](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_batch_update_entities)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.BatchUpdateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntitiesRequest), dict]]`   
The request object. The request message for EntityTypes.BatchUpdateEntities.  
`parent` |  ``str``   
Required. The name of the entity type to update or create entities in. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`entities` |  `:class:`MutableSequence[[google.cloud.dialogflow_v2.types.EntityType.Entity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType.Entity)]``   
Required. The entities to update or create. This corresponds to the `entities` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### batch_update_entity_types
    
    
    batch_update_entity_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.BatchUpdateEntityTypesRequest,
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

Updates/Creates multiple entity types in the specified agent.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty `Struct message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
  * `response`: xref_BatchUpdateEntityTypesResponse



Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_batch_update_entity_types():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesRequest.html)(
            entity_type_batch_uri="entity_type_batch_uri_value",
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[batch_update_entity_types](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_batch_update_entity_types)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesRequest), dict]]`   
The request object. The request message for EntityTypes.BatchUpdateEntityTypes.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be BatchUpdateEntityTypesResponse The response message for EntityTypes.BatchUpdateEntityTypes.  
  
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

### create_entity_type
    
    
    create_entity_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.CreateEntityTypeRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        entity_type: typing.Optional[
            google.cloud.dialogflow_v2.types.entity_type.EntityType
        ] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2.types.entity_type.EntityType

Creates an entity type in the specified agent.

Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_create_entity_type():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        entity_type = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityType()
        entity_type.display_name = "display_name_value"
        entity_type.kind = "KIND_REGEXP"
    
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).CreateEntityTypeRequest(
            parent="parent_value",
            entity_type=entity_type,
        )
    
        # Make the request
        response = await client.[create_entity_type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_create_entity_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.CreateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateEntityTypeRequest), dict]]`   
The request object. The request message for EntityTypes.CreateEntityType.  
`parent` |  ``str``   
Required. The agent to create a entity type for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`entity_type` |  `[EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)`   
Required. The entity type to create. This corresponds to the `entity_type` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2.types.EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)` | Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted. Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent. For more information, see the [Entity guide](https://cloud.google.com/dialogflow/docs/entities-overview).  
  
### delete_entity_type
    
    
    delete_entity_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.DeleteEntityTypeRequest, dict
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

Deletes the specified entity type.

Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_delete_entity_type():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).DeleteEntityTypeRequest(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_entity_type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_delete_entity_type)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.DeleteEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteEntityTypeRequest), dict]]`   
The request object. The request message for EntityTypes.DeleteEntityType.  
`name` |  ``str``   
Required. The name of the entity type to delete. Format: `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### entity_type_path
    
    
    entity_type_path(project: str, entity_type: str) -> str

Returns a fully-qualified entity_type string.

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
`EntityTypesAsyncClient` | The constructed client.  
  
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
`EntityTypesAsyncClient` | The constructed client.  
  
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
`EntityTypesAsyncClient` | The constructed client.  
  
### get_entity_type
    
    
    get_entity_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.GetEntityTypeRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2.types.entity_type.EntityType

Retrieves the specified entity type.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_get_entity_type():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).GetEntityTypeRequest(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_entity_type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_get_entity_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.GetEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetEntityTypeRequest), dict]]`   
The request object. The request message for EntityTypes.GetEntityType.  
`name` |  ``str``   
Required. The name of the entity type. Format: `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2.types.EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)` | Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted. Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent. For more information, see the [Entity guide](https://cloud.google.com/dialogflow/docs/entities-overview).  
  
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
        google.cloud.dialogflow_v2.services.entity_types.transports.base.EntityTypesTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_entity_types
    
    
    list_entity_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.ListEntityTypesRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesAsyncPager

Returns the list of all entity types in the specified agent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_list_entity_types():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).ListEntityTypesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_entity_types](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_list_entity_types)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.ListEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesRequest), dict]]`   
The request object. The request message for EntityTypes.ListEntityTypes.  
`parent` |  ``str``   
Required. The agent to list all entity types from. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesAsyncPager)` | The response message for EntityTypes.ListEntityTypes. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_entity_type_path
    
    
    parse_entity_type_path(path: str) -> typing.Dict[str, str]

Parses a entity_type path into its component segments.

### update_entity_type
    
    
    update_entity_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2.types.entity_type.UpdateEntityTypeRequest, dict
            ]
        ] = None,
        *,
        entity_type: typing.Optional[
            google.cloud.dialogflow_v2.types.entity_type.EntityType
        ] = None,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2.types.entity_type.EntityType

Updates the specified entity type.

Note: You should always train an agent prior to sending it queries. See the `training documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest)
    
    async def sample_update_entity_type():
        # Create a client
        client = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityTypesAsyncClient()
    
        # Initialize request argument(s)
        entity_type = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).EntityType()
        entity_type.display_name = "display_name_value"
        entity_type.kind = "KIND_REGEXP"
    
        request = [dialogflow_v2](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest).UpdateEntityTypeRequest(
            entity_type=entity_type,
        )
    
        # Make the request
        response = await client.[update_entity_type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient.html#google_cloud_dialogflow_v2_services_entity_types_EntityTypesAsyncClient_update_entity_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2.types.UpdateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateEntityTypeRequest), dict]]`   
The request object. The request message for EntityTypes.UpdateEntityType.  
`entity_type` |  `[EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)`   
Required. The entity type to update. This corresponds to the `entity_type` field on the `request` instance; if `request` is provided, this should not be set.  
`language_code` |  ``str``   
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see `Multilingual intent and entity data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__. This corresponds to the `language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2.types.EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)` | Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted. Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent. For more information, see the [Entity guide](https://cloud.google.com/dialogflow/docs/entities-overview).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
