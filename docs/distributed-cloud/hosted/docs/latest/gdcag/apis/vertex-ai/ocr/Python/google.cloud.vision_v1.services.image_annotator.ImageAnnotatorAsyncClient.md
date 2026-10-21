---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient
title: Class ImageAnnotatorAsyncClient (3.4.4) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:44.127663+00:00
---

# Class ImageAnnotatorAsyncClient (3.4.4)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Class ImageAnnotatorAsyncClient (3.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    ImageAnnotatorAsyncClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Union[str, google.cloud.vision_v1.services.image_annotator.transports.base.ImageAnnotatorTransport] = 'grpc_asyncio', client_options: typing.Optional[google.api_core.client_options.ClientOptions] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Service that performs Google Cloud Vision API detection tasks over client images, such as face, landmark, logo, label, and text detection. The ImageAnnotator service returns detected entities from the images.

## Properties 

### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type**| **Description**  
`ImageAnnotatorTransport`| The transport used by the client instance.  
  
## Methods 

### ImageAnnotatorAsyncClient
    
    
    ImageAnnotatorAsyncClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Union[str, google.cloud.vision_v1.services.image_annotator.transports.base.ImageAnnotatorTransport] = 'grpc_asyncio', client_options: typing.Optional[google.api_core.client_options.ClientOptions] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Instantiates the image annotator client.

**Parameters**  
---  
**Name**| **Description**  
`credentials`|  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport`|  `Union[str, `.ImageAnnotatorTransport`]`   
The transport to use. If set to None, a transport is chosen automatically.  
`client_options`|  `ClientOptions`   
Custom options for the client. It won't take effect if a `transport` instance is provided. (1) The `api_endpoint` property can be used to override the default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT environment variable can also be used to override the endpoint: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto switch to the default mTLS endpoint if client certificate is present, this is the default value). However, the `api_endpoint` property takes precedence if provided. (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide client certificate for mutual TLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used.  
**Exceptions**  
---  
**Type**| **Description**  
`google.auth.exceptions.MutualTlsChannelError`| If mutual TLS transport creation failed for any reason.  
  
### async_batch_annotate_files
    
    
    async_batch_annotate_files(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1.types.image_annotator.AsyncBatchAnnotateFilesRequest,
                dict,
            ]
        ] = None,
        *,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vision_v1.types.image_annotator.AsyncAnnotateFileRequest
            ]
        ] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1
    
    async def sample_async_batch_annotate_files():
        # Create a client
        client = vision_v1.[ImageAnnotatorAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1.[AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.AsyncBatchAnnotateFilesRequest.html)(
        )
    
        # Make the request
        operation = client.[async_batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorAsyncClient_async_batch_annotate_files)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = (await operation).result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Optional[Union[[google.cloud.vision_v1.types.AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AsyncBatchAnnotateFilesRequest), dict]]`   
The request object. Multiple async file annotation requests are batched into a single service call.  
`requests`|  `:class:`MutableSequence[[google.cloud.vision_v1.types.AsyncAnnotateFileRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AsyncAnnotateFileRequest)]``   
Required. Individual async file annotation requests for this batch. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`google.api_core.operation_async.AsyncOperation`| An object representing a long-running operation. The result type for the operation will be [AsyncBatchAnnotateFilesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AsyncBatchAnnotateFilesResponse) Response to an async batch file annotation request.  
  
### async_batch_annotate_images
    
    
    async_batch_annotate_images(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1.types.image_annotator.AsyncBatchAnnotateImagesRequest,
                dict,
            ]
        ] = None,
        *,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vision_v1.types.image_annotator.AnnotateImageRequest
            ]
        ] = None,
        output_config: typing.Optional[
            google.cloud.vision_v1.types.image_annotator.OutputConfig
        ] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Run asynchronous image detection and annotation for a list of images.

Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results).

This service will write image annotation outputs to json files in customer GCS bucket, each json file containing BatchAnnotateImagesResponse proto.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1
    
    async def sample_async_batch_annotate_images():
        # Create a client
        client = vision_v1.[ImageAnnotatorAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1.[AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.AsyncBatchAnnotateImagesRequest.html)(
        )
    
        # Make the request
        operation = client.[async_batch_annotate_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorAsyncClient_async_batch_annotate_images)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = (await operation).result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Optional[Union[[google.cloud.vision_v1.types.AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AsyncBatchAnnotateImagesRequest), dict]]`   
The request object. Request for async image annotation for a list of images.  
`requests`|  `:class:`MutableSequence[[google.cloud.vision_v1.types.AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AnnotateImageRequest)]``   
Required. Individual image annotation requests for this batch. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config`|  `[OutputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.OutputConfig)`   
Required. The desired output location and metadata (e.g. format). This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`google.api_core.operation_async.AsyncOperation`| An object representing a long-running operation. The result type for the operation will be [AsyncBatchAnnotateImagesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AsyncBatchAnnotateImagesResponse) Response to an async batch image annotation request.  
  
### batch_annotate_files
    
    
    batch_annotate_files(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1.types.image_annotator.BatchAnnotateFilesRequest, dict
            ]
        ] = None,
        *,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vision_v1.types.image_annotator.AnnotateFileRequest
            ]
        ] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.vision_v1.types.image_annotator.BatchAnnotateFilesResponse

Service that performs image detection and annotation for a batch of files. Now only "application/pdf", "image/tiff" and "image/gif" are supported. This service will extract at most 5 (customers can specify which 5 in AnnotateFileRequest.pages) frames (gif) or pages (pdf or tiff) from each file provided and perform detection and annotation for each image extracted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1
    
    async def sample_batch_annotate_files():
        # Create a client
        client = vision_v1.[ImageAnnotatorAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1.[BatchAnnotateFilesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.BatchAnnotateFilesRequest.html)(
        )
    
        # Make the request
        response = await client.[batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorAsyncClient_batch_annotate_files)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Optional[Union[[google.cloud.vision_v1.types.BatchAnnotateFilesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.BatchAnnotateFilesRequest), dict]]`   
The request object. A list of requests to annotate files using the BatchAnnotateFiles API.  
`requests`|  `:class:`MutableSequence[[google.cloud.vision_v1.types.AnnotateFileRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AnnotateFileRequest)]``   
Required. The list of file annotation requests. Right now we support only one AnnotateFileRequest in BatchAnnotateFilesRequest. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`[google.cloud.vision_v1.types.BatchAnnotateFilesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.BatchAnnotateFilesResponse)`| A list of file annotation responses.  
  
### batch_annotate_images
    
    
    batch_annotate_images(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1.types.image_annotator.BatchAnnotateImagesRequest,
                dict,
            ]
        ] = None,
        *,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vision_v1.types.image_annotator.AnnotateImageRequest
            ]
        ] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.vision_v1.types.image_annotator.BatchAnnotateImagesResponse

Run image detection and annotation for a batch of images.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1
    
    async def sample_batch_annotate_images():
        # Create a client
        client = vision_v1.[ImageAnnotatorAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1.[BatchAnnotateImagesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.BatchAnnotateImagesRequest.html)(
        )
    
        # Make the request
        response = await client.[batch_annotate_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorAsyncClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorAsyncClient_batch_annotate_images)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Optional[Union[[google.cloud.vision_v1.types.BatchAnnotateImagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.BatchAnnotateImagesRequest), dict]]`   
The request object. Multiple image annotation requests are batched into a single service call.  
`requests`|  `:class:`MutableSequence[[google.cloud.vision_v1.types.AnnotateImageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.AnnotateImageRequest)]``   
Required. Individual image annotation requests for this batch. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`[google.cloud.vision_v1.types.BatchAnnotateImagesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/Python/google.cloud.vision_v1.types.BatchAnnotateImagesResponse)`| Response to a batch image annotation request.  
  
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

### from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name**| **Description**  
`filename`|  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type**| **Description**  
`ImageAnnotatorAsyncClient`| The constructed client.  
  
### from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

**Parameter**  
---  
**Name**| **Description**  
`info`|  `dict`   
The service account private key info.  
**Returns**  
---  
**Type**| **Description**  
`ImageAnnotatorAsyncClient`| The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name**| **Description**  
`filename`|  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type**| **Description**  
`ImageAnnotatorAsyncClient`| The constructed client.  
  
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
**Name**| **Description**  
`client_options`|  `google.api_core.client_options.ClientOptions`   
Custom options for the client. Only the `api_endpoint` and `client_cert_source` properties may be used in this method.  
**Exceptions**  
---  
**Type**| **Description**  
`google.auth.exceptions.MutualTLSChannelError`| If any errors happen.  
**Returns**  
---  
**Type**| **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]`| returns the API endpoint and the client cert source to use.  
  
### get_transport_class
    
    
    get_transport_class() -> (
        typing.Type[
            google.cloud.vision_v1.services.image_annotator.transports.base.ImageAnnotatorTransport
        ]
    )

Returns an appropriate transport class.

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

### parse_product_path
    
    
    parse_product_path(path: str) -> typing.Dict[str, str]

Parses a product path into its component segments.

### parse_product_set_path
    
    
    parse_product_set_path(path: str) -> typing.Dict[str, str]

Parses a product_set path into its component segments.

### product_path
    
    
    product_path(project: str, location: str, product: str) -> str

Returns a fully-qualified product string.

### product_set_path
    
    
    product_set_path(project: str, location: str, product_set: str) -> str

Returns a fully-qualified product_set string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
