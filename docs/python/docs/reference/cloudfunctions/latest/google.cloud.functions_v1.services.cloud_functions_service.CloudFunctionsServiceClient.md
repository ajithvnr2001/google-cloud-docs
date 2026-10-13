---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient
title: Class CloudFunctionsServiceClient (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:00.381206+00:00
---

# Class CloudFunctionsServiceClient (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudFunctionsServiceClient (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
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

A service that application uses to manipulate triggers and functions.

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
`CloudFunctionsServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudFunctionsServiceClient
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudFunctionsServiceTransport,Callable[..., CloudFunctionsServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudFunctionsServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### call_function
    
    
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

Synchronously invokes a deployed Cloud Function. To be used for testing purposes as very limited traffic is allowed. For more information on the actual limits, refer to `Rate Limits <https://cloud.google.com/functions/quotas#rate_limits>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_call_function():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.[CallFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionRequest.html)(
            name="name_value",
            data="data_value",
        )
    
        # Make the request
        response = client.[call_function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_call_function)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.CallFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionRequest), dict]`   
The request object. Request for the `CallFunction` method.  
`name` |  `str`   
Required. The name of the function to be called. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`data` |  `str`   
Required. Input to be passed to the function. This corresponds to the `data` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.functions_v1.types.CallFunctionResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CallFunctionResponse)` | Response of CallFunction method.  
  
### cloud_function_path
    
    
    cloud_function_path(project: str, location: str, function: str) -> str

Returns a fully-qualified cloud_function string.

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

### create_function
    
    
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

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_create_function():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        function = functions_v1.[CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.html)()
        function.source_archive_url = "source_archive_url_value"
    
        request = functions_v1.CreateFunctionRequest(
            location="location_value",
            function=function,
        )
    
        # Make the request
        operation = client.[create_function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_create_function)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.CreateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CreateFunctionRequest), dict]`   
The request object. Request for the `CreateFunction` method.  
`location` |  `str`   
Required. The project and location in which the function should be created, specified in the format `projects/_/locations/_` This corresponds to the `location` field on the `request` instance; if `request` is provided, this should not be set.  
`function` |  `[google.cloud.functions_v1.types.CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction)`   
Required. Function to be created. This corresponds to the `function` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction) Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### delete_function
    
    
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

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_delete_function():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.DeleteFunctionRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_delete_function)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.DeleteFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.DeleteFunctionRequest), dict]`   
The request object. Request for the `DeleteFunction` method.  
`name` |  `str`   
Required. The name of the function which should be deleted. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
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
`CloudFunctionsServiceClient` | The constructed client.  
  
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
`CloudFunctionsServiceClient` | The constructed client.  
  
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
`CloudFunctionsServiceClient` | The constructed client.  
  
### generate_download_url
    
    
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

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within minutes after generation. For more information about the signed URL usage see:

<https://cloud.google.com/storage/docs/access-control/signed-urls>
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_generate_download_url():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.GenerateDownloadUrlRequest(
        )
    
        # Make the request
        response = client.[generate_download_url](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_generate_download_url)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.GenerateDownloadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateDownloadUrlRequest), dict]`   
The request object. Request of `GenerateDownloadUrl` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.functions_v1.types.GenerateDownloadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateDownloadUrlResponse)` | Response of GenerateDownloadUrl method.  
  
### generate_upload_url
    
    
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

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * Source file size should not exceed 100MB limit.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, these two headers need to be specified:

  * `content-type: application/zip`
  * `x-goog-content-length-range: 0,104857600`



And this header SHOULD NOT be specified:

  * `Authorization: Bearer YOUR_TOKEN`


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_generate_upload_url():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.GenerateUploadUrlRequest(
        )
    
        # Make the request
        response = client.[generate_upload_url](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_generate_upload_url)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.GenerateUploadUrlRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateUploadUrlRequest), dict]`   
The request object. Request of `GenerateSourceUploadUrl` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.functions_v1.types.GenerateUploadUrlResponse](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GenerateUploadUrlResponse)` | Response of GenerateSourceUploadUrl method.  
  
### get_function
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_get_function():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.GetFunctionRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_function)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.GetFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.GetFunctionRequest), dict]`   
The request object. Request for the `GetFunction` method.  
`name` |  `str`   
Required. The name of the function which details should be obtained. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.functions_v1.types.CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction)` | Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.  
  
### get_iam_policy
    
    
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

Gets the IAM access control policy for a function. Returns an empty policy if the function exists and does not have a policy set.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_get_iam_policy():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]`   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated. Return the API endpoint and client cert source for mutual TLS.

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
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### list_functions
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_list_functions():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = functions_v1.ListFunctionsRequest(
        )
    
        # Make the request
        page_result = client.[list_functions](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_list_functions)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.ListFunctionsRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.ListFunctionsRequest), dict]`   
The request object. Request for the `ListFunctions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.pagers.ListFunctionsPager)` | Response for the ListFunctions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
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
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### parse_cloud_function_path
    
    
    parse_cloud_function_path(path: str) -> typing.Dict[str, str]

Parses a cloud_function path into its component segments.

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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

### repository_path
    
    
    repository_path(project: str, location: str, repository: str) -> str

Returns a fully-qualified repository string.

### set_iam_policy
    
    
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

Sets the IAM access control policy on the specified function. Replaces any existing policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_set_iam_policy():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]`   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### test_iam_permissions
    
    
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

Tests the specified permissions against the IAM access control policy for a function. If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_test_iam_permissions():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]`   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### update_function
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import functions_v1
    
    def sample_update_function():
        # Create a client
        client = functions_v1.[CloudFunctionsServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html)()
    
        # Initialize request argument(s)
        function = functions_v1.[CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction.html)()
        function.source_archive_url = "source_archive_url_value"
    
        request = functions_v1.UpdateFunctionRequest(
            function=function,
        )
    
        # Make the request
        operation = client.[update_function](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.services.cloud_functions_service.CloudFunctionsServiceClient.html#google_cloud_functions_v1_services_cloud_functions_service_CloudFunctionsServiceClient_update_function)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.functions_v1.types.UpdateFunctionRequest](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.UpdateFunctionRequest), dict]`   
The request object. Request for the `UpdateFunction` method.  
`function` |  `[google.cloud.functions_v1.types.CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction)`   
Required. New version of the function. This corresponds to the `function` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [CloudFunction](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v1.types.CloudFunction) Describes a Cloud Function that contains user computation executed in response to an event. It encapsulate function and triggers configurations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
