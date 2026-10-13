---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient
title: Class ParticipantsAsyncClient (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:20.812453+00:00
---

# Class ParticipantsAsyncClient (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ParticipantsAsyncClient (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    ParticipantsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2beta1.services.participants.transports.base.ParticipantsTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2beta1.services.participants.transports.base.ParticipantsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing Participants.

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
`ParticipantsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ParticipantsAsyncClient
    
    
    ParticipantsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2beta1.services.participants.transports.base.ParticipantsTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2beta1.services.participants.transports.base.ParticipantsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the participants async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ParticipantsTransport,Callable[..., ParticipantsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ParticipantsTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### analyze_content
    
    
    analyze_content(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.AnalyzeContentRequest,
                dict,
            ]
        ] = None,
        *,
        participant: typing.Optional[str] = None,
        text_input: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.session.TextInput
        ] = None,
        audio_input: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.AudioInput
        ] = None,
        event_input: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.session.EventInput
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2beta1.types.participant.AnalyzeContentResponse

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See `Versions and environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_analyze_content():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[AnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest.html)(
            participant="participant_value",
        )
    
        # Make the request
        response = await client.[analyze_content](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_analyze_content)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest), dict]]`   
The request object. The request message for Participants.AnalyzeContent.  
`participant` |  ``str``   
Required. The name of the participant this text comes from. Format: `projects/`. This corresponds to the `participant` field on the `request` instance; if `request` is provided, this should not be set.  
`text_input` |  `[TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TextInput)`   
The natural language text to be processed. This corresponds to the `text_input` field on the `request` instance; if `request` is provided, this should not be set.  
`audio_input` |  `[AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AudioInput)`   
The natural language speech audio to be processed. This corresponds to the `audio_input` field on the `request` instance; if `request` is provided, this should not be set.  
`event_input` |  `[EventInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EventInput)`   
An input event to send to Dialogflow. This corresponds to the `event_input` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.AnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnalyzeContentResponse)` | The response message for Participants.AnalyzeContent.  
  
### answer_record_path
    
    
    answer_record_path(project: str, answer_record: str) -> str

Returns a fully-qualified answer_record string.

### app_path
    
    
    app_path(project: str, location: str, app: str) -> str

Returns a fully-qualified app string.

### bidi_streaming_analyze_content
    
    
    bidi_streaming_analyze_content(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.dialogflow_v2beta1.types.participant.BidiStreamingAnalyzeContentRequest
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
            google.cloud.dialogflow_v2beta1.types.participant.BidiStreamingAnalyzeContentResponse
        ]
    ]

Bidirectional endless streaming version of xref_StreamingAnalyzeContent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_bidi_streaming_analyze_content():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        config = dialogflow_v2beta1.[Config](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.Config.html)()
        config.voice_session_config.input_audio_encoding = "AUDIO_ENCODING_ALAW"
        config.voice_session_config.input_audio_sample_rate_hertz = 3097
        config.voice_session_config.output_audio_encoding = "OUTPUT_AUDIO_ENCODING_ALAW"
        config.voice_session_config.output_audio_sample_rate_hertz = 3226
        config.participant = "participant_value"
    
        request = dialogflow_v2beta1.[BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.html)(
            config=config,
        )
    
        # This method expects an iterator which contains
        # 'dialogflow_v2beta1.BidiStreamingAnalyzeContentRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = await client.[bidi_streaming_analyze_content](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_bidi_streaming_analyze_content)(requests=request_generator())
    
        # Handle the response
        async for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`requests` |  `AsyncIterator[`[google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest)`]`   
The request object AsyncIterator. The request message for Participants.BidiStreamingAnalyzeContent.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable[[google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse)]` | The response message for Participants.BidiStreamingAnalyzeContent.  
  
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
  
### ces_tool_path
    
    
    ces_tool_path(project: str, location: str, app: str, tool: str) -> str

Returns a fully-qualified ces_tool string.

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

### compile_suggestion
    
    
    compile_suggestion(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.CompileSuggestionRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.CompileSuggestionResponse

Deprecated. use xref_SuggestArticles and xref_SuggestFaqAnswers instead.

Gets suggestions for a participant based on specific historical messages.

Note that xref_ListSuggestions will only list the auto-generated suggestions, while xref_CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_compile_suggestion():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[CompileSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest.html)(
        )
    
        # Make the request
        response = await client.[compile_suggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_compile_suggestion)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest), dict]]`   
The request object. The request message for Participants.CompileSuggestion.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.CompileSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompileSuggestionResponse)` | The response message for Participants.CompileSuggestion.  
  
### context_path
    
    
    context_path(project: str, session: str, context: str) -> str

Returns a fully-qualified context string.

### create_participant
    
    
    create_participant(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.CreateParticipantRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        participant: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.Participant
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2beta1.types.participant.Participant

Creates a new participant in a conversation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_create_participant():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[CreateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_create_participant)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest), dict]]`   
The request object. The request message for Participants.CreateParticipant.  
`parent` |  ``str``   
Required. Resource identifier of the conversation adding the participant. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`participant` |  `[Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)`   
Required. The participant to create. This corresponds to the `participant` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)` | Represents a conversation participant (human agent, virtual agent, end-user).  
  
### document_path
    
    
    document_path(project: str, knowledge_base: str, document: str) -> str

Returns a fully-qualified document string.

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
`ParticipantsAsyncClient` | The constructed client.  
  
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
`ParticipantsAsyncClient` | The constructed client.  
  
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
`ParticipantsAsyncClient` | The constructed client.  
  
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
  
### get_participant
    
    
    get_participant(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.GetParticipantRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.Participant

Retrieves a conversation participant.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_get_participant():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[GetParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetParticipantRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_get_participant)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.GetParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetParticipantRequest), dict]]`   
The request object. The request message for Participants.GetParticipant.  
`name` |  ``str``   
Required. The name of the participant. Format: `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)` | Represents a conversation participant (human agent, virtual agent, end-user).  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.dialogflow_v2beta1.services.participants.transports.base.ParticipantsTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### intent_path
    
    
    intent_path(project: str, intent: str) -> str

Returns a fully-qualified intent string.

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
  
### list_participants
    
    
    list_participants(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.ListParticipantsRequest,
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
        google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsAsyncPager
    )

Returns the list of all participants in the specified conversation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_list_participants():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[ListParticipantsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_participants](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_list_participants)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest), dict]]`   
The request object. The request message for Participants.ListParticipants.  
`parent` |  ``str``   
Required. The conversation to list all participants from. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsAsyncPager)` | The response message for Participants.ListParticipants. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_suggestions
    
    
    list_suggestions(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.ListSuggestionsRequest,
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
    ) -> (
        google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsAsyncPager
    )

Deprecated: Use inline suggestion, event based suggestion or Suggestion* API instead. See xref_HumanAgentAssistantConfig.name for more details. Removal Date: 2020-09-01.

Retrieves suggestions for live agents.

This method should be used by human agent client software to fetch auto generated suggestions in real-time, while the conversation with an end user is in progress. The functionality is implemented in terms of the `list pagination <https://cloud.google.com/apis/design/design_patterns#list_pagination>`__ design pattern. The client app should use the `next_page_token` field to fetch the next batch of suggestions. `suggestions` are sorted by `create_time` in descending order. To fetch latest suggestion, just set `page_size` to 1. To fetch new suggestions without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_list_suggestions():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[ListSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest.html)(
        )
    
        # Make the request
        page_result = client.[list_suggestions](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_list_suggestions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest), dict]]`   
The request object. The request message for Participants.ListSuggestions.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsAsyncPager)` | The response message for Participants.ListSuggestions. Iterating over this object will yield results and resolve additional pages automatically.  
  
### message_path
    
    
    message_path(project: str, conversation: str, message: str) -> str

Returns a fully-qualified message string.

### parse_answer_record_path
    
    
    parse_answer_record_path(path: str) -> typing.Dict[str, str]

Parses a answer_record path into its component segments.

### parse_app_path
    
    
    parse_app_path(path: str) -> typing.Dict[str, str]

Parses a app path into its component segments.

### parse_ces_tool_path
    
    
    parse_ces_tool_path(path: str) -> typing.Dict[str, str]

Parses a ces_tool path into its component segments.

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

### parse_context_path
    
    
    parse_context_path(path: str) -> typing.Dict[str, str]

Parses a context path into its component segments.

### parse_document_path
    
    
    parse_document_path(path: str) -> typing.Dict[str, str]

Parses a document path into its component segments.

### parse_intent_path
    
    
    parse_intent_path(path: str) -> typing.Dict[str, str]

Parses a intent path into its component segments.

### parse_message_path
    
    
    parse_message_path(path: str) -> typing.Dict[str, str]

Parses a message path into its component segments.

### parse_participant_path
    
    
    parse_participant_path(path: str) -> typing.Dict[str, str]

Parses a participant path into its component segments.

### parse_phrase_set_path
    
    
    parse_phrase_set_path(path: str) -> typing.Dict[str, str]

Parses a phrase_set path into its component segments.

### parse_session_entity_type_path
    
    
    parse_session_entity_type_path(path: str) -> typing.Dict[str, str]

Parses a session_entity_type path into its component segments.

### parse_tool_path
    
    
    parse_tool_path(path: str) -> typing.Dict[str, str]

Parses a tool path into its component segments.

### parse_toolset_path
    
    
    parse_toolset_path(path: str) -> typing.Dict[str, str]

Parses a toolset path into its component segments.

### participant_path
    
    
    participant_path(project: str, conversation: str, participant: str) -> str

Returns a fully-qualified participant string.

### phrase_set_path
    
    
    phrase_set_path(project: str, location: str, phrase_set: str) -> str

Returns a fully-qualified phrase_set string.

### session_entity_type_path
    
    
    session_entity_type_path(project: str, session: str, entity_type: str) -> str

Returns a fully-qualified session_entity_type string.

### streaming_analyze_content
    
    
    streaming_analyze_content(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.dialogflow_v2beta1.types.participant.StreamingAnalyzeContentRequest
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
            google.cloud.dialogflow_v2beta1.types.participant.StreamingAnalyzeContentResponse
        ]
    ]

Adds a text (e.g., chat) or audio (e.g., phone recording) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST).

The top-level message sent to the client by the server is `StreamingAnalyzeContentResponse`. Multiple response messages can be returned in order. The first one or more messages contain the `recognition_result` field. Each result represents a more complete transcript of what the user said. The next message contains the `reply_text` field, and potentially the `reply_audio` and/or the `automated_agent_reply` fields.

Note: Always use agent versions for production traffic sent to virtual agents. See `Versions and environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_streaming_analyze_content():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        audio_config = dialogflow_v2beta1.[InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InputAudioConfig.html)()
        audio_config.audio_encoding = "AUDIO_ENCODING_ALAW"
        audio_config.sample_rate_hertz = 1817
        audio_config.language_code = "language_code_value"
    
        request = dialogflow_v2beta1.[StreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentRequest.html)(
            audio_config=audio_config,
            input_audio=b'input_audio_blob',
            participant="participant_value",
        )
    
        # This method expects an iterator which contains
        # 'dialogflow_v2beta1.StreamingAnalyzeContentRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = await client.[streaming_analyze_content](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_streaming_analyze_content)(requests=request_generator())
    
        # Handle the response
        async for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`requests` |  `AsyncIterator[`[google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentRequest)`]`   
The request object AsyncIterator. The top-level message sent by the client to the Participants.StreamingAnalyzeContent method. Multiple request messages should be sent in order: 1. The first message must contain participant, config and optionally query_params. If you want to receive an audio response, it should also contain reply_audio_config. The message must not contain input. 2. If config in the first message was set to audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. If you decide to rather analyze text input after you already started Speech recognition, please send a message with StreamingAnalyzeContentRequest.input_text. However, note that: - Dialogflow will bill you for the audio so far. - Dialogflow discards all Speech recognition results in favor of the text input. 3. If StreamingAnalyzeContentRequest.config in the first message was set to StreamingAnalyzeContentRequest.text_config, then the second message must contain only input_text. Moreover, you must not send more than two messages. After you sent all input, you must half-close or abort the request stream.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable[[google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentResponse)]` | The top-level message returned from the StreamingAnalyzeContent method. Multiple response messages can be returned in order: 1. If the input was set to streaming audio, the first one or more messages contain recognition_result. Each recognition_result represents a more complete transcript of what the user said. When a user speaks multiple sentences, the API will emit multiple messages where is_final = true. Each time the system detects a distinct pause or completed thought, it locks in that segment, marks it is_final = true, and then immediately starts a new recognition cycle for the next sentence on the same stream. 2. In virtual agent stage: if enable_partial_automated_agent_reply is true, the following N (currently 1 <= n=""><= 4)="" messages="" contain="" automated_agent_reply="" and="" optionally="" reply_audio="" returned="" by="" the="" virtual="" agent.="" the="" first="" (n-1)="">`s will have \`automated_agent_reply_type set to PARTIAL. The last automated_agent_reply has automated_agent_reply_type set to FINAL. If enable_partial_automated_agent_reply is not enabled, response stream only contains the final reply. In human assist stage: the following N (N >= 1) messages contain human_agent_suggestion_results, end_user_suggestion_results or message.  
  
### suggest_articles
    
    
    suggest_articles(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.SuggestArticlesRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.SuggestArticlesResponse

Gets suggested articles for a participant based on specific historical messages.

Note that xref_ListSuggestions will only list the auto-generated suggestions, while xref_CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_suggest_articles():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[SuggestArticlesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[suggest_articles](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_suggest_articles)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest), dict]]`   
The request object. The request message for Participants.SuggestArticles.  
`parent` |  ``str``   
Required. The name of the participant to fetch suggestion for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.SuggestArticlesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestArticlesResponse)` | The response message for Participants.SuggestArticles.  
  
### suggest_faq_answers
    
    
    suggest_faq_answers(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.SuggestFaqAnswersRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.SuggestFaqAnswersResponse

Gets suggested faq answers for a participant based on specific historical messages.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_suggest_faq_answers():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[SuggestFaqAnswersRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[suggest_faq_answers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_suggest_faq_answers)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest), dict]]`   
The request object. The request message for Participants.SuggestFaqAnswers.  
`parent` |  ``str``   
Required. The name of the participant to fetch suggestion for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersResponse)` | The request message for Participants.SuggestFaqAnswers.  
  
### suggest_knowledge_assist
    
    
    suggest_knowledge_assist(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.SuggestKnowledgeAssistRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.SuggestKnowledgeAssistResponse

Gets knowledge assist suggestions based on historical messages.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_suggest_knowledge_assist():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[suggest_knowledge_assist](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_suggest_knowledge_assist)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistRequest), dict]]`   
The request object. The request message for Participants.SuggestKnowledgeAssist.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistResponse)` | The response message for Participants.SuggestKnowledgeAssist.  
  
### suggest_smart_replies
    
    
    suggest_smart_replies(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.SuggestSmartRepliesRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.SuggestSmartRepliesResponse

Gets smart replies for a participant based on specific historical messages.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_suggest_smart_replies():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[SuggestSmartRepliesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[suggest_smart_replies](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_suggest_smart_replies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest), dict]]`   
The request object. The request message for Participants.SuggestSmartReplies.  
`parent` |  ``str``   
Required. The name of the participant to fetch suggestion for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesResponse)` | The response message for Participants.SuggestSmartReplies.  
  
### tool_path
    
    
    tool_path(project: str, location: str, tool: str) -> str

Returns a fully-qualified tool string.

### toolset_path
    
    
    toolset_path(project: str, location: str, app: str, toolset: str) -> str

Returns a fully-qualified toolset string.

### update_participant
    
    
    update_participant(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.participant.UpdateParticipantRequest,
                dict,
            ]
        ] = None,
        *,
        participant: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.Participant
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
    ) -> google.cloud.dialogflow_v2beta1.types.participant.Participant

Updates the specified participant.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    async def sample_update_participant():
        # Create a client
        client = dialogflow_v2beta1.[ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[UpdateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest.html)(
        )
    
        # Make the request
        response = await client.[update_participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient.html#google_cloud_dialogflow_v2beta1_services_participants_ParticipantsAsyncClient_update_participant)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest), dict]]`   
The request object. The request message for Participants.UpdateParticipant.  
`participant` |  `[Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)`   
Required. The participant to update. This corresponds to the `participant` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The mask to specify which fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)` | Represents a conversation participant (human agent, virtual agent, end-user).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
