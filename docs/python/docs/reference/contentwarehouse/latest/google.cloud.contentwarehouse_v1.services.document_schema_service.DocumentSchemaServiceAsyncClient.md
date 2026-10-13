---
url: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient
title: Class DocumentSchemaServiceAsyncClient (0.11.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:41.149434+00:00
---

# Class DocumentSchemaServiceAsyncClient (0.11.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentSchemaServiceAsyncClient (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.11.0  0.10.0  0.9.0  0.8.0  0.7.16  0.6.0  0.5.1  0.4.1  0.3.1  0.2.1  0.1.0 
    
    
    DocumentSchemaServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.contentwarehouse_v1.services.document_schema_service.transports.base.DocumentSchemaServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.contentwarehouse_v1.services.document_schema_service.transports.base.DocumentSchemaServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

This service lets you manage document schema.

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
`DocumentSchemaServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DocumentSchemaServiceAsyncClient
    
    
    DocumentSchemaServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.contentwarehouse_v1.services.document_schema_service.transports.base.DocumentSchemaServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.contentwarehouse_v1.services.document_schema_service.transports.base.DocumentSchemaServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the document schema service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DocumentSchemaServiceTransport,Callable[..., DocumentSchemaServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DocumentSchemaServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_document_schema
    
    
    create_document_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.contentwarehouse_v1.types.document_schema_service.CreateDocumentSchemaRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        document_schema: typing.Optional[
            google.cloud.contentwarehouse_v1.types.document_schema.DocumentSchema
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.contentwarehouse_v1.types.document_schema.DocumentSchema

Creates a document schema.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest)
    
    async def sample_create_document_schema():
        # Create a client
        client = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        document_schema = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema.html)()
        document_schema.display_name = "display_name_value"
    
        request = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[CreateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest.html)(
            parent="parent_value",
            document_schema=document_schema,
        )
    
        # Make the request
        response = await client.[create_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceAsyncClient_create_document_schema)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest), dict]]`   
The request object. Request message for DocumentSchemaService.CreateDocumentSchema.  
`parent` |  ``str``   
Required. The parent name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`document_schema` |  `[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema)`   
Required. The document schema to create. This corresponds to the `document_schema` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.contentwarehouse_v1.types.DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema)` | A document schema used to define document structure.  
  
### delete_document_schema
    
    
    delete_document_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.contentwarehouse_v1.types.document_schema_service.DeleteDocumentSchemaRequest,
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

Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest)
    
    async def sample_delete_document_schema():
        # Create a client
        client = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DeleteDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DeleteDocumentSchemaRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceAsyncClient_delete_document_schema)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.contentwarehouse_v1.types.DeleteDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DeleteDocumentSchemaRequest), dict]]`   
The request object. Request message for DocumentSchemaService.DeleteDocumentSchema.  
`name` |  ``str``   
Required. The name of the document schema to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### document_schema_path
    
    
    document_schema_path(project: str, location: str, document_schema: str) -> str

Returns a fully-qualified document_schema string.

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
`DocumentSchemaServiceAsyncClient` | The constructed client.  
  
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
`DocumentSchemaServiceAsyncClient` | The constructed client.  
  
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
`DocumentSchemaServiceAsyncClient` | The constructed client.  
  
### get_document_schema
    
    
    get_document_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.contentwarehouse_v1.types.document_schema_service.GetDocumentSchemaRequest,
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
    ) -> google.cloud.contentwarehouse_v1.types.document_schema.DocumentSchema

Gets a document schema. Returns NOT_FOUND if the document schema does not exist.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest)
    
    async def sample_get_document_schema():
        # Create a client
        client = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[GetDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.GetDocumentSchemaRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceAsyncClient_get_document_schema)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.contentwarehouse_v1.types.GetDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.GetDocumentSchemaRequest), dict]]`   
The request object. Request message for DocumentSchemaService.GetDocumentSchema.  
`name` |  ``str``   
Required. The name of the document schema to retrieve. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.contentwarehouse_v1.types.DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema)` | A document schema used to define document structure.  
  
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
        google.cloud.contentwarehouse_v1.services.document_schema_service.transports.base.DocumentSchemaServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_document_schemas
    
    
    list_document_schemas(
        request: typing.Optional[
            typing.Union[
                google.cloud.contentwarehouse_v1.types.document_schema_service.ListDocumentSchemasRequest,
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
        google.cloud.contentwarehouse_v1.services.document_schema_service.pagers.ListDocumentSchemasAsyncPager
    )

Lists document schemas.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest)
    
    async def sample_list_document_schemas():
        # Create a client
        client = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[ListDocumentSchemasRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.ListDocumentSchemasRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_document_schemas](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceAsyncClient_list_document_schemas)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.contentwarehouse_v1.types.ListDocumentSchemasRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.ListDocumentSchemasRequest), dict]]`   
The request object. Request message for DocumentSchemaService.ListDocumentSchemas.  
`parent` |  ``str``   
Required. The parent, which owns this collection of document schemas. Format: projects/{project_number}/locations/{location}. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.contentwarehouse_v1.services.document_schema_service.pagers.ListDocumentSchemasAsyncPager](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.pagers.ListDocumentSchemasAsyncPager)` | Response message for DocumentSchemaService.ListDocumentSchemas. Iterating over this object will yield results and resolve additional pages automatically.  
  
### location_path
    
    
    location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

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

### parse_document_schema_path
    
    
    parse_document_schema_path(path: str) -> typing.Dict[str, str]

Parses a document_schema path into its component segments.

### parse_location_path
    
    
    parse_location_path(path: str) -> typing.Dict[str, str]

Parses a location path into its component segments.

### update_document_schema
    
    
    update_document_schema(
        request: typing.Optional[
            typing.Union[
                google.cloud.contentwarehouse_v1.types.document_schema_service.UpdateDocumentSchemaRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        document_schema: typing.Optional[
            google.cloud.contentwarehouse_v1.types.document_schema.DocumentSchema
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.contentwarehouse_v1.types.document_schema.DocumentSchema

Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the xref_EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest)
    
    async def sample_update_document_schema():
        # Create a client
        client = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        document_schema = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema.html)()
        document_schema.display_name = "display_name_value"
    
        request = [contentwarehouse_v1](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest).[UpdateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UpdateDocumentSchemaRequest.html)(
            name="name_value",
            document_schema=document_schema,
        )
    
        # Make the request
        response = await client.[update_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceAsyncClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceAsyncClient_update_document_schema)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.contentwarehouse_v1.types.UpdateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UpdateDocumentSchemaRequest), dict]]`   
The request object. Request message for DocumentSchemaService.UpdateDocumentSchema.  
`name` |  ``str``   
Required. The name of the document schema to update. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`document_schema` |  `[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema)`   
Required. The document schema to update with. This corresponds to the `document_schema` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.contentwarehouse_v1.types.DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema)` | A document schema used to define document structure.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
