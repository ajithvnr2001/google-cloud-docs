---
url: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient
title: Class DocumentProcessorServiceAsyncClient (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:04.768837+00:00
---

# Class DocumentProcessorServiceAsyncClient (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentProcessorServiceAsyncClient (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.1  2.35.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.3  2.28.0  2.27.1  2.26.0  2.25.0  2.24.2  2.23.0  2.22.0  2.21.1  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.3  1.5.1  1.4.2  1.3.0  1.2.1  1.1.0  1.0.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DocumentProcessorServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.documentai_v1beta3.services.document_processor_service.transports.base.DocumentProcessorServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.documentai_v1beta3.services.document_processor_service.transports.base.DocumentProcessorServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service to call Document AI to process documents according to the processor's definition. Processors are built using state-of-the-art Google AI such as natural language, computer vision, and translation to extract structured information from unstructured or semi-structured documents.

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
`DocumentProcessorServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DocumentProcessorServiceAsyncClient
    
    
    DocumentProcessorServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.documentai_v1beta3.services.document_processor_service.transports.base.DocumentProcessorServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.documentai_v1beta3.services.document_processor_service.transports.base.DocumentProcessorServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the document processor service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DocumentProcessorServiceTransport,Callable[..., DocumentProcessorServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DocumentProcessorServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### batch_process_documents
    
    
    batch_process_documents(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.BatchProcessRequest,
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

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_batch_process_documents():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[BatchProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.BatchProcessRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[batch_process_documents](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_batch_process_documents)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.BatchProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.BatchProcessRequest), dict]]`   
The request object. Request message for BatchProcessDocuments.  
`name` |  ``str``   
Required. The resource name of Processor or ProcessorVersion. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [BatchProcessResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.BatchProcessResponse) Response message for BatchProcessDocuments.  
  
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

### create_processor
    
    
    create_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.CreateProcessorRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        processor: typing.Optional[
            google.cloud.documentai_v1beta3.types.processor.Processor
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.documentai_v1beta3.types.processor.Processor

Creates a processor from the xref_ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_create_processor():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[CreateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.CreateProcessorRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_create_processor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.CreateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.CreateProcessorRequest), dict]]`   
The request object. Request message for the CreateProcessor method. Notice this request is sent to a regionalized backend service. If the ProcessorType isn't available in that region, the creation fails.  
`parent` |  ``str``   
Required. The parent (project and location) under which to create the processor. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`processor` |  `[Processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor)`   
Required. The processor to be created, requires Processor.type and Processor.display_name to be set. Also, the Processor.kms_key_name field must be set if the processor is under CMEK. This corresponds to the `processor` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.Processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor)` | The first-class citizen for Document AI. Each processor defines how to extract structural information from a document.  
  
### delete_processor
    
    
    delete_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.DeleteProcessorRequest,
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

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_delete_processor():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[DeleteProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeleteProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_delete_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.DeleteProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeleteProcessorRequest), dict]]`   
The request object. Request message for the DeleteProcessor method.  
`name` |  ``str``   
Required. The processor resource name to be deleted. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_processor_version
    
    
    delete_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.DeleteProcessorVersionRequest,
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

Deletes the processor version, all artifacts under the processor version will be deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_delete_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[DeleteProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeleteProcessorVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_delete_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.DeleteProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeleteProcessorVersionRequest), dict]]`   
The request object. Request message for the DeleteProcessorVersion method.  
`name` |  ``str``   
Required. The processor version resource name to be deleted. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### deploy_processor_version
    
    
    deploy_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.DeployProcessorVersionRequest,
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

Deploys the processor version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_deploy_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[DeployProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeployProcessorVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[deploy_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_deploy_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.DeployProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DeployProcessorVersionRequest), dict]]`   
The request object. Request message for the DeployProcessorVersion method.  
`name` |  ``str``   
Required. The processor version resource name to be deployed. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DeployProcessorVersionResponse Response message for the DeployProcessorVersion method.  
  
### disable_processor
    
    
    disable_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.DisableProcessorRequest,
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

Disables a processor
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_disable_processor():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[DisableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DisableProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[disable_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_disable_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.DisableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DisableProcessorRequest), dict]]`   
The request object. Request message for the DisableProcessor method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DisableProcessorResponse Response message for the DisableProcessor method. Intentionally empty proto for adding fields in future.  
  
### enable_processor
    
    
    enable_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.EnableProcessorRequest,
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

Enables a processor
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_enable_processor():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[EnableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EnableProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[enable_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_enable_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.EnableProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EnableProcessorRequest), dict]]`   
The request object. Request message for the EnableProcessor method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be EnableProcessorResponse Response message for the EnableProcessor method. Intentionally empty proto for adding fields in future.  
  
### evaluate_processor_version
    
    
    evaluate_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.EvaluateProcessorVersionRequest,
                dict,
            ]
        ] = None,
        *,
        processor_version: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_evaluate_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[EvaluateProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionRequest.html)(
            processor_version="processor_version_value",
        )
    
        # Make the request
        operation = await client.[evaluate_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_evaluate_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionRequest), dict]]`   
The request object. Evaluates the given ProcessorVersion against the supplied documents.  
`processor_version` |  ``str``   
Required. The resource name of the ProcessorVersion to evaluate. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}` This corresponds to the `processor_version` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [EvaluateProcessorVersionResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionResponse) Response of the EvaluateProcessorVersion method.  
  
### evaluation_path
    
    
    evaluation_path(
        project: str, location: str, processor: str, processor_version: str, evaluation: str
    ) -> str

Returns a fully-qualified evaluation string.

### fetch_processor_types
    
    
    fetch_processor_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.FetchProcessorTypesRequest,
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
        google.cloud.documentai_v1beta3.types.document_processor_service.FetchProcessorTypesResponse
    )

Fetches processor types. Note that we don't use xref_ListProcessorTypes here, because it isn't paginated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_fetch_processor_types():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[FetchProcessorTypesRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.FetchProcessorTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[fetch_processor_types](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_fetch_processor_types)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.FetchProcessorTypesRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.FetchProcessorTypesRequest), dict]]`   
The request object. Request message for the FetchProcessorTypes method. Some processor types may require the project be added to an allowlist.  
`parent` |  ``str``   
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.FetchProcessorTypesResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.FetchProcessorTypesResponse)` | Response message for the FetchProcessorTypes method.  
  
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
`DocumentProcessorServiceAsyncClient` | The constructed client.  
  
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
`DocumentProcessorServiceAsyncClient` | The constructed client.  
  
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
`DocumentProcessorServiceAsyncClient` | The constructed client.  
  
### get_evaluation
    
    
    get_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.GetEvaluationRequest,
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
    ) -> google.cloud.documentai_v1beta3.types.evaluation.Evaluation

Retrieves a specific evaluation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_get_evaluation():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[GetEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetEvaluationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_evaluation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_get_evaluation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.GetEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetEvaluationRequest), dict]]`   
The request object. Retrieves a specific Evaluation.  
`name` |  ``str``   
Required. The resource name of the Evaluation to get. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.Evaluation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Evaluation)` | An evaluation of a ProcessorVersion's performance.  
  
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
  
### get_processor
    
    
    get_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.GetProcessorRequest,
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
    ) -> google.cloud.documentai_v1beta3.types.processor.Processor

Gets a processor detail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_get_processor():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[GetProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_get_processor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.GetProcessorRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorRequest), dict]]`   
The request object. Request message for the GetProcessor method.  
`name` |  ``str``   
Required. The processor resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.Processor](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Processor)` | The first-class citizen for Document AI. Each processor defines how to extract structural information from a document.  
  
### get_processor_type
    
    
    get_processor_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.GetProcessorTypeRequest,
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
    ) -> google.cloud.documentai_v1beta3.types.processor_type.ProcessorType

Gets a processor type detail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_get_processor_type():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[GetProcessorTypeRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_processor_type](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_get_processor_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.GetProcessorTypeRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorTypeRequest), dict]]`   
The request object. Request message for the GetProcessorType method.  
`name` |  ``str``   
Required. The processor type resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.ProcessorType](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorType)` | A processor type is responsible for performing a certain document understanding task on a certain type of document.  
  
### get_processor_version
    
    
    get_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.GetProcessorVersionRequest,
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
    ) -> google.cloud.documentai_v1beta3.types.processor.ProcessorVersion

Gets a processor version detail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_get_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[GetProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_get_processor_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.GetProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.GetProcessorVersionRequest), dict]]`   
The request object. Request message for the GetProcessorVersion method.  
`name` |  ``str``   
Required. The processor resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.ProcessorVersion](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion)` | A processor version is an implementation of a processor. Each processor can have multiple versions, pretrained by Google internally or uptrained by the customer. A processor can only have one default version at a time. Its document-processing behavior is defined by that version.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.documentai_v1beta3.services.document_processor_service.transports.base.DocumentProcessorServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### human_review_config_path
    
    
    human_review_config_path(project: str, location: str, processor: str) -> str

Returns a fully-qualified human_review_config string.

### import_processor_version
    
    
    import_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ImportProcessorVersionRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Imports a processor version from source processor version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_import_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[ImportProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ImportProcessorVersionRequest.html)(
            processor_version_source="processor_version_source_value",
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[import_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_import_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ImportProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ImportProcessorVersionRequest), dict]]`   
The request object. The request message for the ImportProcessorVersion method. The Document AI `Service Agent <https://cloud.google.com/iam/docs/service-agents>`**of the destination project must have`Document AI Editor role <https://cloud.google.com/document-ai/docs/access-control/iam-roles>`** on the source project. The destination project is specified as part of the parent field. The source project is specified as part of the source or external_processor_version_source field.  
`parent` |  ``str``   
Required. The destination processor name to create the processor version in. Format: `projects/{project}/locations/{location}/processors/{processor}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be ImportProcessorVersionResponse The response message for the ImportProcessorVersion method.  
  
### list_evaluations
    
    
    list_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ListEvaluationsRequest,
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
        google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListEvaluationsAsyncPager
    )

Retrieves a set of evaluations for a given processor version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_list_evaluations():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[ListEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListEvaluationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_evaluations](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_list_evaluations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ListEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListEvaluationsRequest), dict]]`   
The request object. Retrieves a list of evaluations for a given ProcessorVersion.  
`parent` |  ``str``   
Required. The resource name of the ProcessorVersion to list evaluations for. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListEvaluationsAsyncPager)` | The response from ListEvaluations. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_processor_types
    
    
    list_processor_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesRequest,
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
        google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesAsyncPager
    )

Lists the processor types that exist.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_list_processor_types():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[ListProcessorTypesRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_processor_types](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_list_processor_types)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest), dict]]`   
The request object. Request message for the ListProcessorTypes method. Some processor types may require the project be added to an allowlist.  
`parent` |  ``str``   
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesAsyncPager)` | Response message for the ListProcessorTypes method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_processor_versions
    
    
    list_processor_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorVersionsRequest,
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
        google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorVersionsAsyncPager
    )

Lists all versions of a processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_list_processor_versions():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[ListProcessorVersionsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_processor_versions](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_list_processor_versions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest), dict]]`   
The request object. Request message for list all processor versions belongs to a processor.  
`parent` |  ``str``   
Required. The parent (project, location and processor) to list all versions. Format: `projects/{project}/locations/{location}/processors/{processor}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorVersionsAsyncPager)` | Response message for the ListProcessorVersions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_processors
    
    
    list_processors(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorsRequest,
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
        google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsAsyncPager
    )

Lists all processors which belong to this project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_list_processors():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[ListProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_processors](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_list_processors)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ListProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorsRequest), dict]]`   
The request object. Request message for list all processors belongs to a project.  
`parent` |  ``str``   
Required. The parent (project and location) which owns this collection of Processors. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsAsyncPager)` | Response message for the ListProcessors method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_evaluation_path
    
    
    parse_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a evaluation path into its component segments.

### parse_human_review_config_path
    
    
    parse_human_review_config_path(path: str) -> typing.Dict[str, str]

Parses a human_review_config path into its component segments.

### parse_processor_path
    
    
    parse_processor_path(path: str) -> typing.Dict[str, str]

Parses a processor path into its component segments.

### parse_processor_type_path
    
    
    parse_processor_type_path(path: str) -> typing.Dict[str, str]

Parses a processor_type path into its component segments.

### parse_processor_version_path
    
    
    parse_processor_version_path(path: str) -> typing.Dict[str, str]

Parses a processor_version path into its component segments.

### process_document
    
    
    process_document(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ProcessRequest,
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
    ) -> google.cloud.documentai_v1beta3.types.document_processor_service.ProcessResponse

Processes a single document.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_process_document():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        inline_document = documentai_v1beta3.[Document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Document.html)()
        inline_document.uri = "uri_value"
    
        request = documentai_v1beta3.[ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessRequest.html)(
            inline_document=inline_document,
            name="name_value",
        )
    
        # Make the request
        response = await client.[process_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_process_document)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessRequest), dict]]`   
The request object. Request message for the ProcessDocument method.  
`name` |  ``str``   
Required. The resource name of the Processor or ProcessorVersion to use for processing. If a Processor is specified, the server will use its [default version][google.cloud.documentai.v1beta3.Processor.default_processor_version]. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.documentai_v1beta3.types.ProcessResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessResponse)` | Response message for the ProcessDocument method.  
  
### processor_path
    
    
    processor_path(project: str, location: str, processor: str) -> str

Returns a fully-qualified processor string.

### processor_type_path
    
    
    processor_type_path(project: str, location: str, processor_type: str) -> str

Returns a fully-qualified processor_type string.

### processor_version_path
    
    
    processor_version_path(
        project: str, location: str, processor: str, processor_version: str
    ) -> str

Returns a fully-qualified processor_version string.

### review_document
    
    
    review_document(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.ReviewDocumentRequest,
                dict,
            ]
        ] = None,
        *,
        human_review_config: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Send a document for Human Review. The input document should be processed by the specified processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_review_document():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        inline_document = documentai_v1beta3.[Document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.Document.html)()
        inline_document.uri = "uri_value"
    
        request = documentai_v1beta3.[ReviewDocumentRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ReviewDocumentRequest.html)(
            inline_document=inline_document,
            human_review_config="human_review_config_value",
        )
    
        # Make the request
        operation = await client.[review_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_review_document)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.ReviewDocumentRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ReviewDocumentRequest), dict]]`   
The request object. Request message for the ReviewDocument method.  
`human_review_config` |  ``str``   
Required. The resource name of the HumanReviewConfig that the document will be reviewed with. This corresponds to the `human_review_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be ReviewDocumentResponse Response message for the ReviewDocument method.  
  
### set_default_processor_version
    
    
    set_default_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.SetDefaultProcessorVersionRequest,
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

Set the default (active) version of a xref_Processor that will be used in xref_ProcessDocument and xref_BatchProcessDocuments.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_set_default_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.SetDefaultProcessorVersionRequest.html)(
            processor="processor_value",
            default_processor_version="default_processor_version_value",
        )
    
        # Make the request
        operation = await client.[set_default_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_set_default_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.SetDefaultProcessorVersionRequest), dict]]`   
The request object. Request message for the SetDefaultProcessorVersion method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be SetDefaultProcessorVersionResponse Response message for the SetDefaultProcessorVersion method.  
  
### train_processor_version
    
    
    train_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.TrainProcessorVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        processor_version: typing.Optional[
            google.cloud.documentai_v1beta3.types.processor.ProcessorVersion
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

Trains a new processor version. Operation metadata is returned as xref_TrainProcessorVersionMetadata.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_train_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[TrainProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.TrainProcessorVersionRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[train_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_train_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.TrainProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.TrainProcessorVersionRequest), dict]]`   
The request object. Request message for the TrainProcessorVersion method.  
`parent` |  ``str``   
Required. The parent (project, location and processor) to create the new version for. Format: `projects/{project}/locations/{location}/processors/{processor}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`processor_version` |  `[ProcessorVersion](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion)`   
Required. The processor version to be created. This corresponds to the `processor_version` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be TrainProcessorVersionResponse The response for TrainProcessorVersion.  
  
### undeploy_processor_version
    
    
    undeploy_processor_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.documentai_v1beta3.types.document_processor_service.UndeployProcessorVersionRequest,
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

Undeploys the processor version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import documentai_v1beta3
    
    async def sample_undeploy_processor_version():
        # Create a client
        client = documentai_v1beta3.[DocumentProcessorServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = documentai_v1beta3.[UndeployProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.UndeployProcessorVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[undeploy_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.DocumentProcessorServiceAsyncClient.html#google_cloud_documentai_v1beta3_services_document_processor_service_DocumentProcessorServiceAsyncClient_undeploy_processor_version)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.documentai_v1beta3.types.UndeployProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.UndeployProcessorVersionRequest), dict]]`   
The request object. Request message for the UndeployProcessorVersion method.  
`name` |  ``str``   
Required. The processor version resource name to be undeployed. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be UndeployProcessorVersionResponse Response message for the UndeployProcessorVersion method.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
