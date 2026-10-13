---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/summary_method/
title: Package Methods (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:59.523616+00:00
---

# Package Methods (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 

Summary of entries of Methods for cloudfunctions.

## 

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient
    
    
    CloudFunctionsServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.functions_v1.services.cloud_functions_service.transports.base.CloudFunctionsServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.functions_v1.services.cloud_functions_service.transports.base.CloudFunctionsServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud functions service async client.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_CloudFunctionsServiceAsyncClient)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.call_function
    
    
    call_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.CallFunctionRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        data: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.functions_v1.types.functions.CallFunctionResponse

Synchronously invokes a deployed Cloud Function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.call_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_call_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.cloud_function_path
    
    
    cloud_function_path(project: str, location: str, function: str) -> str

Returns a fully-qualified cloud_function string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.cloud_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_cloud_function_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_common_billing_account_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_common_folder_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_common_location_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_common_organization_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_common_project_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.create_function
    
    
    create_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.CreateFunctionRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        function: typing.Optional[
            google.cloud.functions_v1.types.functions.CloudFunction
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

Creates a new function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.create_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_create_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_crypto_key_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.delete_function
    
    
    delete_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.DeleteFunctionRequest, dict
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

Deletes a function with the given name from the specified project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.delete_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_delete_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_from_service_account_file)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_from_service_account_info)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_from_service_account_json)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.generate_download_url
    
    
    generate_download_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.GenerateDownloadUrlRequest, dict
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
    ) -> google.cloud.functions_v1.types.functions.GenerateDownloadUrlResponse

Returns a signed URL for downloading deployed function source code.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.generate_download_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_generate_download_url)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.generate_upload_url
    
    
    generate_upload_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.GenerateUploadUrlRequest, dict
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
    ) -> google.cloud.functions_v1.types.functions.GenerateUploadUrlResponse

Returns a signed URL for uploading a function source code.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.generate_upload_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_generate_upload_url)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_function
    
    
    get_function(
        request: typing.Optional[
            typing.Union[google.cloud.functions_v1.types.functions.GetFunctionRequest, dict]
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
    ) -> google.cloud.functions_v1.types.functions.CloudFunction

Returns a function with the given name from the requested project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_get_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_get_iam_policy)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_get_operation)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.functions_v1.services.cloud_functions_service.transports.base.CloudFunctionsServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_get_transport_class)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_functions
    
    
    list_functions(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.ListFunctionsRequest, dict
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
        google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsAsyncPager
    )

Returns a list of functions that belong to the requested project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_functions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_list_functions)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_list_locations)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_list_operations)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_cloud_function_path
    
    
    parse_cloud_function_path(path: str) -> typing.Dict[str, str]

Parses a cloud_function path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_cloud_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_cloud_function_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_common_folder_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_common_location_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_common_organization_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_common_project_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_crypto_key_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.parse_repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_parse_repository_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.repository_path
    
    
    repository_path(project: str, location: str, repository: str) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_repository_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_set_iam_policy)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.test_iam_permissions
    
    
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

Tests the specified permissions against the IAM access control policy for a function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_test_iam_permissions)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.update_function
    
    
    update_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.UpdateFunctionRequest, dict
            ]
        ] = None,
        *,
        function: typing.Optional[
            google.cloud.functions_v1.types.functions.CloudFunction
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

Updates existing function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient.update_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceAsyncClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceAsyncClient_update_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient
    
    
    CloudFunctionsServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.functions_v1.services.cloud_functions_service.transports.base.CloudFunctionsServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.functions_v1.services.cloud_functions_service.transports.base.CloudFunctionsServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud functions service client.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_CloudFunctionsServiceClient)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient___exit__)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.call_function
    
    
    call_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.CallFunctionRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        data: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.functions_v1.types.functions.CallFunctionResponse

Synchronously invokes a deployed Cloud Function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.call_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_call_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.cloud_function_path
    
    
    cloud_function_path(project: str, location: str, function: str) -> str

Returns a fully-qualified cloud_function string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.cloud_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_cloud_function_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_common_billing_account_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_common_folder_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_common_location_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_common_organization_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_common_project_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.create_function
    
    
    create_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.CreateFunctionRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        function: typing.Optional[
            google.cloud.functions_v1.types.functions.CloudFunction
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

Creates a new function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.create_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_create_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_crypto_key_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.delete_function
    
    
    delete_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.DeleteFunctionRequest, dict
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

Deletes a function with the given name from the specified project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.delete_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_delete_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_from_service_account_file)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_from_service_account_info)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_from_service_account_json)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.generate_download_url
    
    
    generate_download_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.GenerateDownloadUrlRequest, dict
            ]
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
    ) -> google.cloud.functions_v1.types.functions.GenerateDownloadUrlResponse

Returns a signed URL for downloading deployed function source code.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.generate_download_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_generate_download_url)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.generate_upload_url
    
    
    generate_upload_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.GenerateUploadUrlRequest, dict
            ]
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
    ) -> google.cloud.functions_v1.types.functions.GenerateUploadUrlResponse

Returns a signed URL for uploading a function source code.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.generate_upload_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_generate_upload_url)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_function
    
    
    get_function(
        request: typing.Optional[
            typing.Union[google.cloud.functions_v1.types.functions.GetFunctionRequest, dict]
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
    ) -> google.cloud.functions_v1.types.functions.CloudFunction

Returns a function with the given name from the requested project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_function)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_iam_policy)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_operation
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.get_operation](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_operation)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_functions
    
    
    list_functions(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.ListFunctionsRequest, dict
            ]
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
    ) -> (
        google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager
    )

Returns a list of functions that belong to the requested project.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_functions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_list_functions)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_locations
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_locations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_list_locations)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_operations
    
    
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.list_operations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_list_operations)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_cloud_function_path
    
    
    parse_cloud_function_path(path: str) -> typing.Dict[str, str]

Parses a cloud_function path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_cloud_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_cloud_function_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_common_billing_account_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_common_folder_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_common_location_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_common_organization_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_common_project_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_crypto_key_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.parse_repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_parse_repository_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.repository_path
    
    
    repository_path(project: str, location: str, repository: str) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_repository_path)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_set_iam_policy)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified permissions against the IAM access control policy for a function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_test_iam_permissions)

### google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.update_function
    
    
    update_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v1.types.functions.UpdateFunctionRequest, dict
            ]
        ] = None,
        *,
        function: typing.Optional[
            google.cloud.functions_v1.types.functions.CloudFunction
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

Updates existing function.

See more: [google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.update_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_update_function)

### google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsAsyncPager
    
    
    ListFunctionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.functions_v1.types.functions.ListFunctionsResponse
            ],
        ],
        request: google.cloud.functions_v1.types.functions.ListFunctionsRequest,
        response: google.cloud.functions_v1.types.functions.ListFunctionsResponse,
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsAsyncPager](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsAsyncPager#google_cloud_functions_v1_services_cloud_functions_service_pagers_ListFunctionsAsyncPager_ListFunctionsAsyncPager)

### google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager
    
    
    ListFunctionsPager(
        method: typing.Callable[
            [...], google.cloud.functions_v1.types.functions.ListFunctionsResponse
        ],
        request: google.cloud.functions_v1.types.functions.ListFunctionsRequest,
        response: google.cloud.functions_v1.types.functions.ListFunctionsResponse,
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

See more: [google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager#google_cloud_functions_v1_services_cloud_functions_service_pagers_ListFunctionsPager_ListFunctionsPager)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient
    
    
    FunctionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.functions_v2.services.function_service.transports.base.FunctionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.functions_v2.services.function_service.transports.base.FunctionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the function service async client.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_FunctionServiceAsyncClient)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.build_path
    
    
    build_path(project: str, location: str, build: str) -> str

Returns a fully-qualified build string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.build_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_build_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.channel_path
    
    
    channel_path(project: str, location: str, channel: str) -> str

Returns a fully-qualified channel string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.channel_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_channel_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_common_billing_account_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_common_folder_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_common_location_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_common_organization_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_common_project_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.connector_path
    
    
    connector_path(project: str, location: str, connector: str) -> str

Returns a fully-qualified connector string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.connector_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_connector_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.create_function
    
    
    create_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.CreateFunctionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        function: typing.Optional[
            google.cloud.functions_v2.types.functions.Function
        ] = None,
        function_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.create_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_create_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_crypto_key_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.delete_function
    
    
    delete_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.DeleteFunctionRequest, dict
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

Deletes a function with the given name from the specified project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.delete_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_delete_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_from_service_account_file)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_from_service_account_info)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_from_service_account_json)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.function_path
    
    
    function_path(project: str, location: str, function: str) -> str

Returns a fully-qualified function string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_function_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.generate_download_url
    
    
    generate_download_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.GenerateDownloadUrlRequest, dict
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
    ) -> google.cloud.functions_v2.types.functions.GenerateDownloadUrlResponse

Returns a signed URL for downloading deployed function source code.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.generate_download_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_generate_download_url)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.generate_upload_url
    
    
    generate_upload_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.GenerateUploadUrlRequest, dict
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
    ) -> google.cloud.functions_v2.types.functions.GenerateUploadUrlResponse

Returns a signed URL for uploading a function source code.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.generate_upload_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_generate_upload_url)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_function
    
    
    get_function(
        request: typing.Optional[
            typing.Union[google.cloud.functions_v2.types.functions.GetFunctionRequest, dict]
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
    ) -> google.cloud.functions_v2.types.functions.Function

Returns a function with the given name from the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_get_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_get_iam_policy)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_get_operation)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.functions_v2.services.function_service.transports.base.FunctionServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_get_transport_class)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_functions
    
    
    list_functions(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.ListFunctionsRequest, dict
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
    ) -> google.cloud.functions_v2.services.function_service.pagers.ListFunctionsAsyncPager

Returns a list of functions that belong to the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_functions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_list_functions)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_list_locations)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_list_operations)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_runtimes
    
    
    list_runtimes(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.ListRuntimesRequest, dict
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
    ) -> google.cloud.functions_v2.types.functions.ListRuntimesResponse

Returns a list of runtimes that are supported for the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.list_runtimes](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_list_runtimes)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_build_path
    
    
    parse_build_path(path: str) -> typing.Dict[str, str]

Parses a build path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_build_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_build_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_channel_path
    
    
    parse_channel_path(path: str) -> typing.Dict[str, str]

Parses a channel path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_channel_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_channel_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_common_folder_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_common_location_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_common_organization_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_common_project_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_connector_path
    
    
    parse_connector_path(path: str) -> typing.Dict[str, str]

Parses a connector path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_connector_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_connector_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_crypto_key_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_function_path
    
    
    parse_function_path(path: str) -> typing.Dict[str, str]

Parses a function path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_function_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_repository_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_service_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_service_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_topic_path
    
    
    parse_topic_path(path: str) -> typing.Dict[str, str]

Parses a topic path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_topic_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_topic_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_trigger_path
    
    
    parse_trigger_path(path: str) -> typing.Dict[str, str]

Parses a trigger path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_trigger_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_trigger_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_parse_worker_pool_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.repository_path
    
    
    repository_path(project: str, location: str, repository: str) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_repository_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.service_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_service_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_set_iam_policy)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_test_iam_permissions)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.topic_path
    
    
    topic_path(project: str, topic: str) -> str

Returns a fully-qualified topic string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.topic_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_topic_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.trigger_path
    
    
    trigger_path(project: str, location: str, trigger: str) -> str

Returns a fully-qualified trigger string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.trigger_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_trigger_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.update_function
    
    
    update_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.UpdateFunctionRequest, dict
            ]
        ] = None,
        *,
        function: typing.Optional[
            google.cloud.functions_v2.types.functions.Function
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

Updates existing function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.update_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_update_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient.worker_pool_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceAsyncClient#google_cloud_functions_v2_services_function_service_FunctionServiceAsyncClient_worker_pool_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient
    
    
    FunctionServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.functions_v2.services.function_service.transports.base.FunctionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.functions_v2.services.function_service.transports.base.FunctionServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the function service client.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_FunctionServiceClient)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient___exit__)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.build_path
    
    
    build_path(project: str, location: str, build: str) -> str

Returns a fully-qualified build string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.build_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_build_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.channel_path
    
    
    channel_path(project: str, location: str, channel: str) -> str

Returns a fully-qualified channel string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.channel_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_channel_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_common_billing_account_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_common_folder_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_common_location_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_common_organization_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_common_project_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.connector_path
    
    
    connector_path(project: str, location: str, connector: str) -> str

Returns a fully-qualified connector string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.connector_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_connector_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.create_function
    
    
    create_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.CreateFunctionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        function: typing.Optional[
            google.cloud.functions_v2.types.functions.Function
        ] = None,
        function_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.create_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_create_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_crypto_key_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.delete_function
    
    
    delete_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.DeleteFunctionRequest, dict
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

Deletes a function with the given name from the specified project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.delete_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_delete_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_from_service_account_file)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_from_service_account_info)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_from_service_account_json)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.function_path
    
    
    function_path(project: str, location: str, function: str) -> str

Returns a fully-qualified function string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_function_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.generate_download_url
    
    
    generate_download_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.GenerateDownloadUrlRequest, dict
            ]
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
    ) -> google.cloud.functions_v2.types.functions.GenerateDownloadUrlResponse

Returns a signed URL for downloading deployed function source code.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.generate_download_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_generate_download_url)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.generate_upload_url
    
    
    generate_upload_url(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.GenerateUploadUrlRequest, dict
            ]
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
    ) -> google.cloud.functions_v2.types.functions.GenerateUploadUrlResponse

Returns a signed URL for uploading a function source code.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.generate_upload_url](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_generate_upload_url)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_function
    
    
    get_function(
        request: typing.Optional[
            typing.Union[google.cloud.functions_v2.types.functions.GetFunctionRequest, dict]
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
    ) -> google.cloud.functions_v2.types.functions.Function

Returns a function with the given name from the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_get_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_get_iam_policy)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_operation
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.get_operation](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_get_operation)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_functions
    
    
    list_functions(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.ListFunctionsRequest, dict
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
    ) -> google.cloud.functions_v2.services.function_service.pagers.ListFunctionsPager

Returns a list of functions that belong to the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_functions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_list_functions)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_locations
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_locations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_list_locations)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_operations
    
    
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

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_operations](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_list_operations)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_runtimes
    
    
    list_runtimes(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.ListRuntimesRequest, dict
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
    ) -> google.cloud.functions_v2.types.functions.ListRuntimesResponse

Returns a list of runtimes that are supported for the requested project.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.list_runtimes](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_list_runtimes)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_build_path
    
    
    parse_build_path(path: str) -> typing.Dict[str, str]

Parses a build path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_build_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_build_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_channel_path
    
    
    parse_channel_path(path: str) -> typing.Dict[str, str]

Parses a channel path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_channel_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_channel_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_common_billing_account_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_common_folder_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_common_location_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_common_organization_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_common_project_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_connector_path
    
    
    parse_connector_path(path: str) -> typing.Dict[str, str]

Parses a connector path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_connector_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_connector_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_crypto_key_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_function_path
    
    
    parse_function_path(path: str) -> typing.Dict[str, str]

Parses a function path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_function_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_function_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_repository_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_service_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_service_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_topic_path
    
    
    parse_topic_path(path: str) -> typing.Dict[str, str]

Parses a topic path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_topic_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_topic_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_trigger_path
    
    
    parse_trigger_path(path: str) -> typing.Dict[str, str]

Parses a trigger path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_trigger_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_trigger_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_parse_worker_pool_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.repository_path
    
    
    repository_path(project: str, location: str, repository: str) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.repository_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_repository_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.service_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_service_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_set_iam_policy)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_test_iam_permissions)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.topic_path
    
    
    topic_path(project: str, topic: str) -> str

Returns a fully-qualified topic string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.topic_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_topic_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.trigger_path
    
    
    trigger_path(project: str, location: str, trigger: str) -> str

Returns a fully-qualified trigger string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.trigger_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_trigger_path)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.update_function
    
    
    update_function(
        request: typing.Optional[
            typing.Union[
                google.cloud.functions_v2.types.functions.UpdateFunctionRequest, dict
            ]
        ] = None,
        *,
        function: typing.Optional[
            google.cloud.functions_v2.types.functions.Function
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
    ) -> google.api_core.operation.Operation

Updates existing function.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.update_function](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_update_function)

### google.cloud.functions_v2.services.function_service.FunctionServiceClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.functions_v2.services.function_service.FunctionServiceClient.worker_pool_path](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient#google_cloud_functions_v2_services_function_service_FunctionServiceClient_worker_pool_path)

### google.cloud.functions_v2.services.function_service.pagers.ListFunctionsAsyncPager
    
    
    ListFunctionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.functions_v2.types.functions.ListFunctionsResponse
            ],
        ],
        request: google.cloud.functions_v2.types.functions.ListFunctionsRequest,
        response: google.cloud.functions_v2.types.functions.ListFunctionsResponse,
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

See more: [google.cloud.functions_v2.services.function_service.pagers.ListFunctionsAsyncPager](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.pagers.ListFunctionsAsyncPager#google_cloud_functions_v2_services_function_service_pagers_ListFunctionsAsyncPager_ListFunctionsAsyncPager)

### google.cloud.functions_v2.services.function_service.pagers.ListFunctionsPager
    
    
    ListFunctionsPager(
        method: typing.Callable[
            [...], google.cloud.functions_v2.types.functions.ListFunctionsResponse
        ],
        request: google.cloud.functions_v2.types.functions.ListFunctionsRequest,
        response: google.cloud.functions_v2.types.functions.ListFunctionsResponse,
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

See more: [google.cloud.functions_v2.services.function_service.pagers.ListFunctionsPager](https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.pagers.ListFunctionsPager#google_cloud_functions_v2_services_function_service_pagers_ListFunctionsPager_ListFunctionsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
