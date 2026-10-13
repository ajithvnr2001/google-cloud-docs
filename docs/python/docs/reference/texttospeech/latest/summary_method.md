---
url: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/summary_method/
title: Package Methods (2.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:11.345458+00:00
---

# Package Methods (2.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.38.0 (latest)  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.0  2.19.0  2.18.0  2.17.2  2.16.5  2.15.1  2.14.2  2.13.0  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.5.0 

Summary of entries of Methods for texttospeech.

## 

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient
    
    
    TextToSpeechAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1.services.text_to_speech.transports.base.TextToSpeechTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1.services.text_to_speech.transports.base.TextToSpeechTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech async client.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_TextToSpeechAsyncClient)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_file)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_info)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_json)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_get_operation)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.texttospeech_v1.services.text_to_speech.transports.base.TextToSpeechTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_get_transport_class)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_list_operations)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.list_voices
    
    
    list_voices(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts.ListVoicesRequest, dict
            ]
        ] = None,
        *,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1.types.cloud_tts.ListVoicesResponse

Returns a list of Voice supported for synthesis.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.list_voices](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_list_voices)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_parse_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.streaming_synthesize
    
    
    streaming_synthesize(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.texttospeech_v1.types.cloud_tts.StreamingSynthesizeRequest
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.texttospeech_v1.types.cloud_tts.StreamingSynthesizeResponse
        ]
    ]

Performs bidirectional streaming speech synthesis: receives audio while sending text.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.streaming_synthesize](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_streaming_synthesize)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.synthesize_speech
    
    
    synthesize_speech(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts.SynthesizeSpeechRequest, dict
            ]
        ] = None,
        *,
        input: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.SynthesisInput
        ] = None,
        voice: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.VoiceSelectionParams
        ] = None,
        audio_config: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.AudioConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1.types.cloud_tts.SynthesizeSpeechResponse

Synthesizes speech synchronously: receive results after all text input has been processed.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient.synthesize_speech](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechAsyncClient_synthesize_speech)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient
    
    
    TextToSpeechClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1.services.text_to_speech.transports.base.TextToSpeechTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1.services.text_to_speech.transports.base.TextToSpeechTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech client.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_TextToSpeechClient)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.**exit**](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient___exit__)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_from_service_account_file)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_from_service_account_info)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_from_service_account_json)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_get_operation)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_list_operations)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.list_voices
    
    
    list_voices(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts.ListVoicesRequest, dict
            ]
        ] = None,
        *,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1.types.cloud_tts.ListVoicesResponse

Returns a list of Voice supported for synthesis.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.list_voices](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_list_voices)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_parse_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.streaming_synthesize
    
    
    streaming_synthesize(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.texttospeech_v1.types.cloud_tts.StreamingSynthesizeRequest
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
    ) -> typing.Iterable[
        google.cloud.texttospeech_v1.types.cloud_tts.StreamingSynthesizeResponse
    ]

Performs bidirectional streaming speech synthesis: receives audio while sending text.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.streaming_synthesize](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_streaming_synthesize)

### google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.synthesize_speech
    
    
    synthesize_speech(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts.SynthesizeSpeechRequest, dict
            ]
        ] = None,
        *,
        input: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.SynthesisInput
        ] = None,
        voice: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.VoiceSelectionParams
        ] = None,
        audio_config: typing.Optional[
            google.cloud.texttospeech_v1.types.cloud_tts.AudioConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1.types.cloud_tts.SynthesizeSpeechResponse

Synthesizes speech synchronously: receive results after all text input has been processed.

See more: [google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.synthesize_speech](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_synthesize_speech)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient
    
    
    TextToSpeechLongAudioSynthesizeAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech long audio synthesize async client.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_TextToSpeechLongAudioSynthesizeAsyncClient)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_file)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_info)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_json)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_operation)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_transport_class)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_list_operations)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.synthesize_long_audio
    
    
    synthesize_long_audio(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts_lrs.SynthesizeLongAudioRequest,
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

Synthesizes long form text asynchronously.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.synthesize_long_audio](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_synthesize_long_audio)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient
    
    
    TextToSpeechLongAudioSynthesizeClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech long audio synthesize client.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_TextToSpeechLongAudioSynthesizeClient)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.**exit**](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient___exit__)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_file)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_info)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_json)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_get_operation)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_list_operations)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_folder_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_location_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_organization_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_project_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_model_path)

### google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.synthesize_long_audio
    
    
    synthesize_long_audio(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1.types.cloud_tts_lrs.SynthesizeLongAudioRequest,
                dict,
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
    ) -> google.api_core.operation.Operation

Synthesizes long form text asynchronously.

See more: [google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.synthesize_long_audio](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_synthesize_long_audio)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient
    
    
    TextToSpeechAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.base.TextToSpeechTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.base.TextToSpeechTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech async client.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_TextToSpeechAsyncClient)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_file)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_info)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_from_service_account_json)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_get_operation)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.base.TextToSpeechTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_get_transport_class)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_list_operations)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.list_voices
    
    
    list_voices(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.ListVoicesRequest, dict
            ]
        ] = None,
        *,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1beta1.types.cloud_tts.ListVoicesResponse

Returns a list of Voice supported for synthesis.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.list_voices](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_list_voices)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_parse_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.streaming_synthesize
    
    
    streaming_synthesize(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.StreamingSynthesizeRequest
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.StreamingSynthesizeResponse
        ]
    ]

Performs bidirectional streaming speech synthesis: receives audio while sending text.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.streaming_synthesize](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_streaming_synthesize)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.synthesize_speech
    
    
    synthesize_speech(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesizeSpeechRequest,
                dict,
            ]
        ] = None,
        *,
        input: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesisInput
        ] = None,
        voice: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.VoiceSelectionParams
        ] = None,
        audio_config: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.AudioConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesizeSpeechResponse

Synthesizes speech synchronously: receive results after all text input has been processed.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient.synthesize_speech](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechAsyncClient_synthesize_speech)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient
    
    
    TextToSpeechClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.base.TextToSpeechTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1beta1.services.text_to_speech.transports.base.TextToSpeechTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech client.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_TextToSpeechClient)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.**exit**](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient___exit__)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_from_service_account_file)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_from_service_account_info)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_from_service_account_json)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_get_operation)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_list_operations)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.list_voices
    
    
    list_voices(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.ListVoicesRequest, dict
            ]
        ] = None,
        *,
        language_code: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1beta1.types.cloud_tts.ListVoicesResponse

Returns a list of Voice supported for synthesis.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.list_voices](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_list_voices)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_parse_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.streaming_synthesize
    
    
    streaming_synthesize(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.StreamingSynthesizeRequest
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
    ) -> typing.Iterable[
        google.cloud.texttospeech_v1beta1.types.cloud_tts.StreamingSynthesizeResponse
    ]

Performs bidirectional streaming speech synthesis: receives audio while sending text.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.streaming_synthesize](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_streaming_synthesize)

### google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.synthesize_speech
    
    
    synthesize_speech(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesizeSpeechRequest,
                dict,
            ]
        ] = None,
        *,
        input: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesisInput
        ] = None,
        voice: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.VoiceSelectionParams
        ] = None,
        audio_config: typing.Optional[
            google.cloud.texttospeech_v1beta1.types.cloud_tts.AudioConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.texttospeech_v1beta1.types.cloud_tts.SynthesizeSpeechResponse

Synthesizes speech synchronously: receive results after all text input has been processed.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient.synthesize_speech](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_TextToSpeechClient_synthesize_speech)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient
    
    
    TextToSpeechLongAudioSynthesizeAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech long audio synthesize async client.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_TextToSpeechLongAudioSynthesizeAsyncClient)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_file)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_info)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_from_service_account_json)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_operation)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_get_transport_class)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_list_operations)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_parse_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.synthesize_long_audio
    
    
    synthesize_long_audio(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts_lrs.SynthesizeLongAudioRequest,
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

Synthesizes long form text asynchronously.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient.synthesize_long_audio](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeAsyncClient_synthesize_long_audio)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient
    
    
    TextToSpeechLongAudioSynthesizeClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                typing.Callable[
                    [...],
                    google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.transports.base.TextToSpeechLongAudioSynthesizeTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the text to speech long audio synthesize client.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_TextToSpeechLongAudioSynthesizeClient)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.**exit**](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient___exit__)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_file](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_file)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_info](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_info)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.from_service_account_json](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_from_service_account_json)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_get_mtls_endpoint_and_cert_source)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_operation
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.get_operation](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_get_operation)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.list_operations
    
    
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

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.list_operations](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_list_operations)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_billing_account_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_folder_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_location_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_organization_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_common_project_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.parse_model_path](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_parse_model_path)

### google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.synthesize_long_audio
    
    
    synthesize_long_audio(
        request: typing.Optional[
            typing.Union[
                google.cloud.texttospeech_v1beta1.types.cloud_tts_lrs.SynthesizeLongAudioRequest,
                dict,
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
    ) -> google.api_core.operation.Operation

Synthesizes long form text asynchronously.

See more: [google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient.synthesize_long_audio](https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient#google_cloud_texttospeech_v1beta1_services_text_to_speech_long_audio_synthesize_TextToSpeechLongAudioSynthesizeClient_synthesize_long_audio)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
