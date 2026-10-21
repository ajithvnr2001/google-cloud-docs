---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/Python/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient
title: Class SpeechAsyncClient (2.15.0) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:13.402475+00:00
---

# Class SpeechAsyncClient (2.15.0)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/Python/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Class SpeechAsyncClient (2.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    SpeechAsyncClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Union[str, google.cloud.speech_v1p1beta1.services.speech.transports.base.SpeechTransport] = 'grpc_asyncio', client_options: typing.Optional[google.api_core.client_options.ClientOptions] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Service that implements Google Cloud Speech API.

## Properties 

### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type**| **Description**  
`SpeechTransport`| The transport used by the client instance.  
  
## Methods 

### SpeechAsyncClient
    
    
    SpeechAsyncClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Union[str, google.cloud.speech_v1p1beta1.services.speech.transports.base.SpeechTransport] = 'grpc_asyncio', client_options: typing.Optional[google.api_core.client_options.ClientOptions] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Instantiates the speech client.

**Parameters**  
---  
**Name**| **Description**  
`credentials`|  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport`|  `Union[str, `.SpeechTransport`]`   
The transport to use. If set to None, a transport is chosen automatically.  
`client_options`|  `ClientOptions`   
Custom options for the client. It won't take effect if a `transport` instance is provided. (1) The `api_endpoint` property can be used to override the default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT environment variable can also be used to override the endpoint: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto switch to the default mTLS endpoint if client certificate is present, this is the default value). However, the `api_endpoint` property takes precedence if provided. (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide client certificate for mutual TLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used.  
**Exceptions**  
---  
**Type**| **Description**  
`google.auth.exceptions.MutualTlsChannelError`| If mutual TLS transport creation failed for any reason.  
  
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

### custom_class_path
    
    
    custom_class_path(project: str, location: str, custom_class: str) -> str

Returns a fully-qualified custom_class string.

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
`SpeechAsyncClient`| The constructed client.  
  
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
`SpeechAsyncClient`| The constructed client.  
  
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
`SpeechAsyncClient`| The constructed client.  
  
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

### parse_custom_class_path
    
    
    parse_custom_class_path(path: str) -> typing.Dict[str, str]

Parses a custom_class path into its component segments.

### parse_phrase_set_path
    
    
    parse_phrase_set_path(path: str) -> typing.Dict[str, str]

Parses a phrase_set path into its component segments.

### phrase_set_path
    
    
    phrase_set_path(project: str, location: str, phrase_set: str) -> str

Returns a fully-qualified phrase_set string.

### recognize
    
    
    recognize(
        request: typing.Optional[
            typing.Union[google.cloud.speech_v1p1beta1.types.cloud_speech.RecognizeRequest, dict]
        ] = None,
        *,
        config: typing.Optional[
            google.cloud.speech_v1p1beta1.types.cloud_speech.RecognitionConfig
        ] = None,
        audio: typing.Optional[
            google.cloud.speech_v1p1beta1.types.cloud_speech.RecognitionAudio
        ] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.speech_v1p1beta1.types.cloud_speech.RecognizeResponse

Performs synchronous speech recognition: receive results after all audio has been sent and processed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import speech_v1p1beta1
    
    async def sample_recognize():
        # Create a client
        client = speech_v1p1beta1.[SpeechAsyncClient](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient.html)()
    
        # Initialize request argument(s)
        config = speech_v1p1beta1.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionConfig.html)()
        config.language_code = "language_code_value"
    
        audio = speech_v1p1beta1.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionAudio.html)()
        audio.content = b'content_blob'
    
        request = speech_v1p1beta1.[RecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognizeRequest.html)(
            config=config,
            audio=audio,
        )
    
        # Make the request
        response = await client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient.html#google_cloud_speech_v1p1beta1_services_speech_SpeechAsyncClient_recognize)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Optional[Union[google.cloud.speech_v1p1beta1.types.RecognizeRequest, dict]]`   
The request object. The top-level message sent by the client for the `Recognize` method.  
`config`|  `RecognitionConfig`   
Required. Provides information to the recognizer that specifies how to process the request. This corresponds to the `config` field on the `request` instance; if `request` is provided, this should not be set.  
`audio`|  `RecognitionAudio`   
Required. The audio data to be recognized. This corresponds to the `audio` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`google.cloud.speech_v1p1beta1.types.RecognizeResponse`| The only message returned to the client by the Recognize method. It contains the result as zero or more sequential SpeechRecognitionResult messages.  
  
### streaming_recognize
    
    
    streaming_recognize(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.speech_v1p1beta1.types.cloud_speech.StreamingRecognizeRequest
            ]
        ] = None,
        *,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.speech_v1p1beta1.types.cloud_speech.StreamingRecognizeResponse
        ]
    ]

Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import speech_v1p1beta1
    
    async def sample_streaming_recognize():
        # Create a client
        client = speech_v1p1beta1.[SpeechAsyncClient](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient.html)()
    
        # Initialize request argument(s)
        streaming_config = speech_v1p1beta1.[StreamingRecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.StreamingRecognitionConfig.html)()
        streaming_config.config.language_code = "language_code_value"
    
        request = speech_v1p1beta1.[StreamingRecognizeRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.StreamingRecognizeRequest.html)(
            streaming_config=streaming_config,
        )
    
        # This method expects an iterator which contains
        # 'speech_v1p1beta1.StreamingRecognizeRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = await client.[streaming_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.speech.SpeechAsyncClient.html#google_cloud_speech_v1p1beta1_services_speech_SpeechAsyncClient_streaming_recognize)(requests=request_generator())
    
        # Handle the response
        async for response in stream:
            print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`requests`|  `AsyncIterator[`google.cloud.speech_v1p1beta1.types.StreamingRecognizeRequest`]`   
The request object AsyncIterator. The top-level message sent by the client for the `StreamingRecognize` method. Multiple `StreamingRecognizeRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain `audio_content`. All subsequent messages must contain `audio_content` and must not contain a `streaming_config` message.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`AsyncIterable[google.cloud.speech_v1p1beta1.types.StreamingRecognizeResponse]`| StreamingRecognizeResponse is the only message returned to the client by StreamingRecognize. A series of zero or more StreamingRecognizeResponse messages are streamed back to the client. If there is no recognizable audio, and single_utterance is set to false, then no messages are streamed back to the client. Here's an example of a series of StreamingRecognizeResponses that might be returned while processing audio: 1. results { alternatives { transcript: "tube" } stability: 0.01 } 2. results { alternatives { transcript: "to be a" } stability: 0.01 } 3. results { alternatives { transcript: "to be" } stability: 0.9 } results { alternatives { transcript: " or not to be" } stability: 0.01 } 4. results { alternatives { transcript: "to be or not to be" confidence: 0.92 } alternatives { transcript: "to bee or not to bee" } is_final: true } 5. results { alternatives { transcript: " that's" } stability: 0.01 } 6. results { alternatives { transcript: " that is" } stability: 0.9 } results { alternatives { transcript: " the question" } stability: 0.01 } 7. results { alternatives { transcript: " that is the question" confidence: 0.98 } alternatives { transcript: " that was the question" } is_final: true } Notes: - Only two of the above responses #4 and #7 contain final results; they are indicated by is_final: true. Concatenating these together generates the full transcript: "to be or not to be that is the question". - The others contain interim results. #3 and #6 contain two interim \`results`: the first portion has a high stability and is less likely to change; the second portion has a low stability and is very likely to change. A UI designer might choose to show only high stability results. - The specific stability and confidence values shown above are only for illustrative purposes. Actual values may vary. - In each response, only one of these fields will be set: error, speech_event_type, or one or more (repeated) results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
