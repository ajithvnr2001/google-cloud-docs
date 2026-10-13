---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient
title: Class ConversationalSearchServiceClient (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:55.486136+00:00
---

# Class ConversationalSearchServiceClient (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConversationalSearchServiceClient (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ConversationalSearchServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.conversational_search_service.transports.base.ConversationalSearchServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.conversational_search_service.transports.base.ConversationalSearchServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for conversational search.

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
`ConversationalSearchServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ConversationalSearchServiceClient
    
    
    ConversationalSearchServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.conversational_search_service.transports.base.ConversationalSearchServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.conversational_search_service.transports.base.ConversationalSearchServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the conversational search service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ConversationalSearchServiceTransport,Callable[..., ConversationalSearchServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the ConversationalSearchServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### answer_path
    
    
    answer_path(
        project: str, location: str, data_store: str, session: str, answer: str
    ) -> str

Returns a fully-qualified answer string.

### answer_query
    
    
    answer_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.AnswerQueryRequest,
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
    ) -> (
        google.cloud.discoveryengine_v1.types.conversational_search_service.AnswerQueryResponse
    )

Answer query method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_answer_query():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        query = discoveryengine_v1.[Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Query.html)()
        query.text = "text_value"
    
        request = discoveryengine_v1.[AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.html)(
            serving_config="serving_config_value",
            query=query,
        )
    
        # Make the request
        response = client.[answer_query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_answer_query)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest), dict]`   
The request object. Request message for ConversationalSearchService.AnswerQuery method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryResponse)` | Response message for ConversationalSearchService.AnswerQuery method.  
  
### assist_answer_path
    
    
    assist_answer_path(
        project: str,
        location: str,
        collection: str,
        engine: str,
        session: str,
        assist_answer: str,
    ) -> str

Returns a fully-qualified assist_answer string.

### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
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
    ) -> None

Starts asynchronous cancellation on a long-running operation.

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### chunk_path
    
    
    chunk_path(
        project: str, location: str, data_store: str, branch: str, document: str, chunk: str
    ) -> str

Returns a fully-qualified chunk string.

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

### conversation_path
    
    
    conversation_path(
        project: str, location: str, data_store: str, conversation: str
    ) -> str

Returns a fully-qualified conversation string.

### converse_conversation
    
    
    converse_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.ConverseConversationRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        query: typing.Optional[
            google.cloud.discoveryengine_v1.types.conversation.TextInput
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.discoveryengine_v1.types.conversational_search_service.ConverseConversationResponse
    )

Converses a conversation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_converse_conversation():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[converse_conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_converse_conversation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationRequest), dict]`   
The request object. Request message for ConversationalSearchService.ConverseConversation method.  
`name` |  `str`   
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`query` |  `[google.cloud.discoveryengine_v1.types.TextInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TextInput)`   
Required. Current user input. This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.ConverseConversationResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationResponse)` | Response message for ConversationalSearchService.ConverseConversation method.  
  
### create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.discoveryengine_v1.types.conversation.Conversation
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.discoveryengine_v1.types.conversation.Conversation

Creates a Conversation.

If the xref_Conversation to create already exists, an ALREADY_EXISTS error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_create_conversation():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateConversationRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_create_conversation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateConversationRequest), dict]`   
The request object. Request for CreateConversation method.  
`parent` |  `str`   
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`conversation` |  `[google.cloud.discoveryengine_v1.types.Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)`   
Required. The conversation to create. This corresponds to the `conversation` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)` | External conversation proto definition.  
  
### create_session
    
    
    create_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.CreateSessionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        session: typing.Optional[
            google.cloud.discoveryengine_v1.types.session.Session
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.discoveryengine_v1.types.session.Session

Creates a Session.

If the xref_Session to create already exists, an ALREADY_EXISTS error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_create_session():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSessionRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_create_session)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSessionRequest), dict]`   
The request object. Request for CreateSession method.  
`parent` |  `str`   
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`session` |  `[google.cloud.discoveryengine_v1.types.Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)`   
Required. The session to create. This corresponds to the `session` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)` | External session proto definition.  
  
### data_store_path
    
    
    data_store_path(project: str, location: str, data_store: str) -> str

Returns a fully-qualified data_store string.

### delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.DeleteConversationRequest,
                dict,
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
    ) -> None

Deletes a Conversation.

If the xref_Conversation to delete does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_delete_conversation():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteConversationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_delete_conversation)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteConversationRequest), dict]`   
The request object. Request for DeleteConversation method.  
`name` |  `str`   
Required. The resource name of the Conversation to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_session
    
    
    delete_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.DeleteSessionRequest,
                dict,
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
    ) -> None

Deletes a Session.

If the xref_Session to delete does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_delete_session():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSessionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_delete_session)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSessionRequest), dict]`   
The request object. Request for DeleteSession method.  
`name` |  `str`   
Required. The resource name of the Session to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### document_path
    
    
    document_path(
        project: str, location: str, data_store: str, branch: str, document: str
    ) -> str

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
`ConversationalSearchServiceClient` | The constructed client.  
  
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
`ConversationalSearchServiceClient` | The constructed client.  
  
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
`ConversationalSearchServiceClient` | The constructed client.  
  
### get_answer
    
    
    get_answer(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.GetAnswerRequest,
                dict,
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
    ) -> google.cloud.discoveryengine_v1.types.answer.Answer

Gets a Answer.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_get_answer():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetAnswerRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetAnswerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_get_answer)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.GetAnswerRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetAnswerRequest), dict]`   
The request object. Request for GetAnswer method.  
`name` |  `str`   
Required. The resource name of the Answer to get. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine_id}/sessions/{session_id}/answers/{answer_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer)` | Defines an answer.  
  
### get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.GetConversationRequest,
                dict,
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
    ) -> google.cloud.discoveryengine_v1.types.conversation.Conversation

Gets a Conversation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_get_conversation():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetConversationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_get_conversation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetConversationRequest), dict]`   
The request object. Request for GetConversation method.  
`name` |  `str`   
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)` | External conversation proto definition.  
  
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
  
### get_session
    
    
    get_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.GetSessionRequest,
                dict,
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
    ) -> google.cloud.discoveryengine_v1.types.session.Session

Gets a Session.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_get_session():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSessionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_get_session)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSessionRequest), dict]`   
The request object. Request for GetSession method.  
`name` |  `str`   
Required. The resource name of the Session to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)` | External session proto definition.  
  
### list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.ListConversationsRequest,
                dict,
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
    ) -> (
        google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListConversationsPager
    )

Lists all Conversations by their parent xref_DataStore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_list_conversations():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_conversations](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_list_conversations)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsRequest), dict]`   
The request object. Request for ListConversations method.  
`parent` |  `str`   
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListConversationsPager)` | Response for ListConversations method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_sessions
    
    
    list_sessions(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.ListSessionsRequest,
                dict,
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
    ) -> (
        google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListSessionsPager
    )

Lists all Sessions by their parent xref_DataStore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_list_sessions():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_sessions](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_list_sessions)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsRequest), dict]`   
The request object. Request for ListSessions method.  
`parent` |  `str`   
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListSessionsPager)` | Response for ListSessions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_answer_path
    
    
    parse_answer_path(path: str) -> typing.Dict[str, str]

Parses a answer path into its component segments.

### parse_assist_answer_path
    
    
    parse_assist_answer_path(path: str) -> typing.Dict[str, str]

Parses a assist_answer path into its component segments.

### parse_chunk_path
    
    
    parse_chunk_path(path: str) -> typing.Dict[str, str]

Parses a chunk path into its component segments.

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

### parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

### parse_data_store_path
    
    
    parse_data_store_path(path: str) -> typing.Dict[str, str]

Parses a data_store path into its component segments.

### parse_document_path
    
    
    parse_document_path(path: str) -> typing.Dict[str, str]

Parses a document path into its component segments.

### parse_serving_config_path
    
    
    parse_serving_config_path(path: str) -> typing.Dict[str, str]

Parses a serving_config path into its component segments.

### parse_session_path
    
    
    parse_session_path(path: str) -> typing.Dict[str, str]

Parses a session path into its component segments.

### serving_config_path
    
    
    serving_config_path(
        project: str, location: str, data_store: str, serving_config: str
    ) -> str

Returns a fully-qualified serving_config string.

### session_path
    
    
    session_path(project: str, location: str, data_store: str, session: str) -> str

Returns a fully-qualified session string.

### stream_answer_query
    
    
    stream_answer_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.AnswerQueryRequest,
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
    ) -> typing.Iterable[
        google.cloud.discoveryengine_v1.types.conversational_search_service.AnswerQueryResponse
    ]

Answer query method (streaming).

It takes one xref_AnswerQueryRequest and returns multiple xref_AnswerQueryResponse messages in a stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_stream_answer_query():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        query = discoveryengine_v1.[Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Query.html)()
        query.text = "text_value"
    
        request = discoveryengine_v1.[AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.html)(
            serving_config="serving_config_value",
            query=query,
        )
    
        # Make the request
        stream = client.[stream_answer_query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_stream_answer_query)(request=request)
    
        # Handle the response
        for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest), dict]`   
The request object. Request message for ConversationalSearchService.AnswerQuery method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[[google.cloud.discoveryengine_v1.types.AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryResponse)]` | Response message for ConversationalSearchService.AnswerQuery method.  
  
### update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.discoveryengine_v1.types.conversation.Conversation
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
    ) -> google.cloud.discoveryengine_v1.types.conversation.Conversation

Updates a Conversation.

xref_Conversation action type cannot be changed. If the xref_Conversation to update does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_update_conversation():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateConversationRequest.html)(
        )
    
        # Make the request
        response = client.[update_conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_update_conversation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateConversationRequest), dict]`   
The request object. Request for UpdateConversation method.  
`conversation` |  `[google.cloud.discoveryengine_v1.types.Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)`   
Required. The Conversation to update. This corresponds to the `conversation` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided Conversation to update. The following are NOT supported: - Conversation.name If not set or empty, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)` | External conversation proto definition.  
  
### update_session
    
    
    update_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.conversational_search_service.UpdateSessionRequest,
                dict,
            ]
        ] = None,
        *,
        session: typing.Optional[
            google.cloud.discoveryengine_v1.types.session.Session
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
    ) -> google.cloud.discoveryengine_v1.types.session.Session

Updates a Session.

xref_Session action type cannot be changed. If the xref_Session to update does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_update_session():
        # Create a client
        client = discoveryengine_v1.[ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[UpdateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSessionRequest.html)(
        )
    
        # Make the request
        response = client.[update_session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient.html#google_cloud_discoveryengine_v1_services_conversational_search_service_ConversationalSearchServiceClient_update_session)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.UpdateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSessionRequest), dict]`   
The request object. Request for UpdateSession method.  
`session` |  `[google.cloud.discoveryengine_v1.types.Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)`   
Required. The Session to update. This corresponds to the `session` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided Session to update. The following are NOT supported: - Session.name If not set or empty, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)` | External session proto definition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
