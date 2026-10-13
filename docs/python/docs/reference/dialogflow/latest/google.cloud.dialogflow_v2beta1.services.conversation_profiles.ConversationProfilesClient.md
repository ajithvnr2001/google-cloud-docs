---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient
title: Class ConversationProfilesClient (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:29.557137+00:00
---

# Class ConversationProfilesClient (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConversationProfilesClient (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    ConversationProfilesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2beta1.services.conversation_profiles.transports.base.ConversationProfilesTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2beta1.services.conversation_profiles.transports.base.ConversationProfilesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing ConversationProfiles.

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
`ConversationProfilesTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ConversationProfilesClient
    
    
    ConversationProfilesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dialogflow_v2beta1.services.conversation_profiles.transports.base.ConversationProfilesTransport,
                typing.Callable[
                    [...],
                    google.cloud.dialogflow_v2beta1.services.conversation_profiles.transports.base.ConversationProfilesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the conversation profiles client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ConversationProfilesTransport,Callable[..., ConversationProfilesTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the ConversationProfilesTransport constructor. If set to None, a transport is chosen automatically.  
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

### agent_path
    
    
    agent_path(project: str) -> str

Returns a fully-qualified agent string.

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
  
### clear_suggestion_feature_config
    
    
    clear_suggestion_feature_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.ClearSuggestionFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        conversation_profile: typing.Optional[str] = None,
        participant_role: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.Participant.Role
        ] = None,
        suggestion_feature_type: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.SuggestionFeature.Type
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

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: xref_ClearSuggestionFeatureConfigOperationMetadata
  * `response`: xref_ConversationProfile


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_clear_suggestion_feature_config():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ClearSuggestionFeatureConfigRequest.html)(
            conversation_profile="conversation_profile_value",
            participant_role="END_USER",
            suggestion_feature_type="KNOWLEDGE_ASSIST",
        )
    
        # Make the request
        operation = client.[clear_suggestion_feature_config](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_clear_suggestion_feature_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ClearSuggestionFeatureConfigRequest), dict]`   
The request object. The request message for [ConversationProfiles.ClearFeature][].  
`conversation_profile` |  `str`   
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/`. This corresponds to the `conversation_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`participant_role` |  `[google.cloud.dialogflow_v2beta1.types.Participant.Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant.Role)`   
Required. The participant role to remove the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. This corresponds to the `participant_role` field on the `request` instance; if `request` is provided, this should not be set.  
`suggestion_feature_type` |  `[google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type)`   
Required. The type of the suggestion feature to remove. This corresponds to the `suggestion_feature_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be ConversationProfile Defines the services to connect to incoming Dialogflow conversations.  
  
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

### conversation_profile_path
    
    
    conversation_profile_path(project: str, conversation_profile: str) -> str

Returns a fully-qualified conversation_profile string.

### create_conversation_profile
    
    
    create_conversation_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.CreateConversationProfileRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation_profile: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.conversation_profile.ConversationProfile
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dialogflow_v2beta1.types.conversation_profile.ConversationProfile

Creates a conversation profile in the specified project.

[ConversationProfile.CreateTime][] and [ConversationProfile.UpdateTime][] aren't populated in the response. You can retrieve them via xref_GetConversationProfile API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_create_conversation_profile():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        conversation_profile = dialogflow_v2beta1.[ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile.html)()
        conversation_profile.display_name = "display_name_value"
    
        request = dialogflow_v2beta1.[CreateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateConversationProfileRequest.html)(
            parent="parent_value",
            conversation_profile=conversation_profile,
        )
    
        # Make the request
        response = client.[create_conversation_profile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_create_conversation_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.CreateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateConversationProfileRequest), dict]`   
The request object. The request message for ConversationProfiles.CreateConversationProfile.  
`parent` |  `str`   
Required. The project to create a conversation profile for. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`conversation_profile` |  `[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)`   
Required. The conversation profile to create. This corresponds to the `conversation_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)` | Defines the services to connect to incoming Dialogflow conversations.  
  
### cx_security_settings_path
    
    
    cx_security_settings_path(
        project: str, location: str, security_settings: str
    ) -> str

Returns a fully-qualified cx_security_settings string.

### delete_conversation_profile
    
    
    delete_conversation_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.DeleteConversationProfileRequest,
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

Deletes the specified conversation profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_delete_conversation_profile():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[DeleteConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteConversationProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_conversation_profile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_delete_conversation_profile)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.DeleteConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteConversationProfileRequest), dict]`   
The request object. The request message for ConversationProfiles.DeleteConversationProfile. This operation fails if the conversation profile is still referenced from a phone number.  
`name` |  `str`   
Required. The name of the conversation profile to delete. Format: `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
`ConversationProfilesClient` | The constructed client.  
  
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
`ConversationProfilesClient` | The constructed client.  
  
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
`ConversationProfilesClient` | The constructed client.  
  
### generator_path
    
    
    generator_path(project: str, location: str, generator: str) -> str

Returns a fully-qualified generator string.

### get_conversation_profile
    
    
    get_conversation_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.GetConversationProfileRequest,
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
    ) -> google.cloud.dialogflow_v2beta1.types.conversation_profile.ConversationProfile

Retrieves the specified conversation profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_get_conversation_profile():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[GetConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetConversationProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_conversation_profile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_get_conversation_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.GetConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetConversationProfileRequest), dict]`   
The request object. The request message for ConversationProfiles.GetConversationProfile.  
`name` |  `str`   
Required. The resource name of the conversation profile. Format: `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)` | Defines the services to connect to incoming Dialogflow conversations.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
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
  
### knowledge_base_path
    
    
    knowledge_base_path(project: str, knowledge_base: str) -> str

Returns a fully-qualified knowledge_base string.

### list_conversation_profiles
    
    
    list_conversation_profiles(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.ListConversationProfilesRequest,
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
        google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers.ListConversationProfilesPager
    )

Returns the list of all conversation profiles in the specified project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_list_conversation_profiles():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[ListConversationProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_conversation_profiles](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_list_conversation_profiles)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.ListConversationProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesRequest), dict]`   
The request object. The request message for ConversationProfiles.ListConversationProfiles.  
`parent` |  `str`   
Required. The project to list all conversation profiles from. Format: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers.ListConversationProfilesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers.ListConversationProfilesPager)` | The response message for ConversationProfiles.ListConversationProfiles. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_agent_path
    
    
    parse_agent_path(path: str) -> typing.Dict[str, str]

Parses a agent path into its component segments.

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

### parse_conversation_profile_path
    
    
    parse_conversation_profile_path(path: str) -> typing.Dict[str, str]

Parses a conversation_profile path into its component segments.

### parse_cx_security_settings_path
    
    
    parse_cx_security_settings_path(path: str) -> typing.Dict[str, str]

Parses a cx_security_settings path into its component segments.

### parse_document_path
    
    
    parse_document_path(path: str) -> typing.Dict[str, str]

Parses a document path into its component segments.

### parse_generator_path
    
    
    parse_generator_path(path: str) -> typing.Dict[str, str]

Parses a generator path into its component segments.

### parse_knowledge_base_path
    
    
    parse_knowledge_base_path(path: str) -> typing.Dict[str, str]

Parses a knowledge_base path into its component segments.

### parse_phrase_set_path
    
    
    parse_phrase_set_path(path: str) -> typing.Dict[str, str]

Parses a phrase_set path into its component segments.

### phrase_set_path
    
    
    phrase_set_path(project: str, location: str, phrase_set: str) -> str

Returns a fully-qualified phrase_set string.

### set_suggestion_feature_config
    
    
    set_suggestion_feature_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.SetSuggestionFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        conversation_profile: typing.Optional[str] = None,
        participant_role: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.participant.Participant.Role
        ] = None,
        suggestion_feature_config: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.conversation_profile.HumanAgentAssistantConfig.SuggestionFeatureConfig
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

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a `long-running operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__. The returned `Operation` type has the following method-specific fields:

  * `metadata`: xref_SetSuggestionFeatureConfigOperationMetadata
  * `response`: xref_ConversationProfile



If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_set_suggestion_feature_config():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        request = dialogflow_v2beta1.[SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SetSuggestionFeatureConfigRequest.html)(
            conversation_profile="conversation_profile_value",
            participant_role="END_USER",
        )
    
        # Make the request
        operation = client.[set_suggestion_feature_config](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_set_suggestion_feature_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SetSuggestionFeatureConfigRequest), dict]`   
The request object. The request message for [ConversationProfiles.SetSuggestionFeature][].  
`conversation_profile` |  `str`   
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/`. This corresponds to the `conversation_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`participant_role` |  `[google.cloud.dialogflow_v2beta1.types.Participant.Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant.Role)`   
Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. This corresponds to the `participant_role` field on the `request` instance; if `request` is provided, this should not be set.  
`suggestion_feature_config` |  `[google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionFeatureConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionFeatureConfig)`   
Required. The suggestion feature config to add or update. This corresponds to the `suggestion_feature_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be ConversationProfile Defines the services to connect to incoming Dialogflow conversations.  
  
### update_conversation_profile
    
    
    update_conversation_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.dialogflow_v2beta1.types.conversation_profile.UpdateConversationProfileRequest,
                dict,
            ]
        ] = None,
        *,
        conversation_profile: typing.Optional[
            google.cloud.dialogflow_v2beta1.types.conversation_profile.ConversationProfile
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
    ) -> google.cloud.dialogflow_v2beta1.types.conversation_profile.ConversationProfile

Updates the specified conversation profile.

[ConversationProfile.CreateTime][] and [ConversationProfile.UpdateTime][] aren't populated in the response. You can retrieve them via xref_GetConversationProfile API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import dialogflow_v2beta1
    
    def sample_update_conversation_profile():
        # Create a client
        client = dialogflow_v2beta1.[ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html)()
    
        # Initialize request argument(s)
        conversation_profile = dialogflow_v2beta1.[ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile.html)()
        conversation_profile.display_name = "display_name_value"
    
        request = dialogflow_v2beta1.[UpdateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateConversationProfileRequest.html)(
            conversation_profile=conversation_profile,
        )
    
        # Make the request
        response = client.[update_conversation_profile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient.html#google_cloud_dialogflow_v2beta1_services_conversation_profiles_ConversationProfilesClient_update_conversation_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.dialogflow_v2beta1.types.UpdateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateConversationProfileRequest), dict]`   
The request object. The request message for ConversationProfiles.UpdateConversationProfile.  
`conversation_profile` |  `[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)`   
Required. The conversation profile to update. This corresponds to the `conversation_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. The mask to control which fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)` | Defines the services to connect to incoming Dialogflow conversations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
