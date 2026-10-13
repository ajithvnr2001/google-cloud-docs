---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient
title: Class PredictionServiceAsyncClient (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:41.405813+00:00
---

# Class PredictionServiceAsyncClient (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PredictionServiceAsyncClient (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    PredictionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

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
`PredictionServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### PredictionServiceAsyncClient
    
    
    PredictionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the prediction service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,PredictionServiceTransport,Callable[..., PredictionServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the PredictionServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### batch_predict
    
    
    batch_predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.BatchPredictRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictInputConfig
        ] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictOutputConfig
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Perform a batch prediction. Unlike the online xref_Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via `GetOperation][google.longrunning.Operations.GetOperation]` method. Once the operation is done, xref_BatchPredictResult is returned in the `response][google.longrunning.Operation.response]` field. Available for following ML problems:

  * Image Classification
  * Image Object Detection
  * Video Classification
  * Video Object Tracking * Text Extraction
  * Tables


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_batch_predict():
        # Create a client
        client = automl_v1beta1.[PredictionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[BatchPredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[batch_predict](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.html#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_batch_predict)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.BatchPredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictRequest), dict]]`   
The request object. Request message for PredictionService.BatchPredict.  
`name` |  ``str``   
Required. Name of the model requested to serve the batch prediction. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`input_config` |  `[BatchPredictInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictInputConfig)`   
Required. The input configuration for batch prediction. This corresponds to the `input_config` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config` |  `[BatchPredictOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BatchPredictOutputConfig)`   
Required. The Configuration specifying where output predictions should be written. This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`params` |  `:class:`MutableMapping[str, str]``   
Required. Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long. - For Text Classification: `score_threshold` \- (float) A value from 0.0 to 1.0. When the model makes predictions for a text snippet, it will only produce results that have at least this confidence score. The default is 0.5. - For Image Classification: `score_threshold` \- (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. - For Image Object Detection: `score_threshold` \- (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` \- (int64) No more than this number of bounding boxes will be produced per image. Default is 100, the requested value may be limited by server. - For Video Classification : `score_threshold` \- (float) A value from 0.0 to 1.0. When the model makes predictions for a video, it will only produce results that have at least this confidence score. The default is 0.5. `segment_classification` \- (boolean) Set to true to request segment-level classification. AutoML Video Intelligence returns labels and their confidence scores for the entire segment of the video that user specified in the request configuration. The default is "true". `shot_classification` \- (boolean) Set to true to request shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. The default is "false". `1s_interval_classification` \- (boolean) Set to true to request classification for a video at one-second intervals. AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. The default is "false". - For Tables: feature_importance - (boolean) Whether feature importance should be populated in the returned TablesAnnotations. The default is false. - For Video Object Tracking: `score_threshold` \- (float) When Model detects objects on video frames, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` \- (int64) No more than this number of bounding boxes will be returned per frame. Default is 100, the requested value may be limited by server. `min_bounding_box_size` \- (float) Only bounding boxes with shortest edge at least that long as a relative value of video frame size will be returned. Value in 0 to 1 range. Default is 0. This corresponds to the `params` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be BatchPredictResult Result of the Batch Predict. This message is returned in `response][google.longrunning.Operation.response]` of the operation returned by the PredictionService.BatchPredict.  
  
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
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`PredictionServiceAsyncClient` | The constructed client.  
  
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
`PredictionServiceAsyncClient` | The constructed client.  
  
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
`PredictionServiceAsyncClient` | The constructed client.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

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

### parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

### predict
    
    
    predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.PredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[
            google.cloud.automl_v1beta1.types.data_items.ExamplePayload
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.prediction_service.PredictResponse

Perform an online prediction. The prediction result will be directly returned in the response. Available for following ML problems, and their expected request payloads:

  * Image Classification - Image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.
  * Image Object Detection - Image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.
  * Text Classification - TextSnippet, content up to 60,000 characters, UTF-8 encoded.
  * Text Extraction - TextSnippet, content up to 30,000 characters, UTF-8 NFC encoded.
  * Translation - TextSnippet, content up to 25,000 characters, UTF-8 encoded.
  * Tables - Row, with column values matching the columns of the model, up to 5MB. Not available for FORECASTING



xref_prediction_type.

  * Text Sentiment - TextSnippet, content up 500 characters, UTF-8 encoded.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_predict():
        # Create a client
        client = automl_v1beta1.[PredictionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        payload = automl_v1beta1.[ExamplePayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExamplePayload.html)()
        payload.image.image_bytes = b'image_bytes_blob'
    
        request = automl_v1beta1.[PredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictRequest.html)(
            name="name_value",
            payload=payload,
        )
    
        # Make the request
        response = await client.[predict](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.html)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.PredictRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictRequest), dict]]`   
The request object. Request message for PredictionService.Predict.  
`name` |  ``str``   
Required. Name of the model requested to serve the prediction. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`payload` |  `[ExamplePayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExamplePayload)`   
Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve. This corresponds to the `payload` field on the `request` instance; if `request` is provided, this should not be set.  
`params` |  `:class:`MutableMapping[str, str]``   
Additional domain-specific parameters, any string must be up to 25000 characters long. - For Image Classification: `score_threshold` \- (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. - For Image Object Detection: `score_threshold` \- (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` \- (int64) No more than this number of bounding boxes will be returned in the response. Default is 100, the requested value may be limited by server. - For Tables: feature_importance - (boolean) Whether feature importance should be populated in the returned TablesAnnotation. The default is false. This corresponds to the `params` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.PredictResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.PredictResponse)` | Response message for PredictionService.Predict.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
