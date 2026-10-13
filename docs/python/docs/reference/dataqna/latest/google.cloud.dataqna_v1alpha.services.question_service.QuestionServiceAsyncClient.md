---
url: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient
title: Class QuestionServiceAsyncClient (0.14.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:41.591522+00:00
---

# Class QuestionServiceAsyncClient (0.14.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QuestionServiceAsyncClient (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.17  0.9.0  0.8.2  0.7.1  0.6.3  0.5.1  0.4.0  0.3.3  0.2.1  0.1.1 
    
    
    QuestionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dataqna_v1alpha.services.question_service.transports.base.QuestionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.dataqna_v1alpha.services.question_service.transports.base.QuestionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service to interpret natural language queries. The service allows to create `Question` resources that are interpreted and are filled with one or more interpretations if the question could be interpreted. Once a `Question` resource is created and has at least one interpretation, an interpretation can be chosen for execution, which triggers a query to the backend (for BigQuery, it will create a job). Upon successful execution of that interpretation, backend specific information will be returned so that the client can retrieve the results from the backend.

The `Question` resources are named `projects/*/locations/*/questions/*`.

The `Question` resource has a singletion sub-resource `UserFeedback` named `projects/*/locations/*/questions/*/userFeedback`, which allows access to user feedback.

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
`QuestionServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### QuestionServiceAsyncClient
    
    
    QuestionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dataqna_v1alpha.services.question_service.transports.base.QuestionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.dataqna_v1alpha.services.question_service.transports.base.QuestionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the question service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,QuestionServiceTransport,Callable[..., QuestionServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the QuestionServiceTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
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

### create_question
    
    
    create_question(
        request: typing.Optional[
            typing.Union[
                google.cloud.dataqna_v1alpha.types.question_service.CreateQuestionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        question: typing.Optional[
            google.cloud.dataqna_v1alpha.types.question.Question
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dataqna_v1alpha.types.question.Question

Creates a question.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest)
    
    async def sample_create_question():
        # Create a client
        client = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        question = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question.html)()
        question.scopes = ['scopes_value1', 'scopes_value2']
        question.query = "query_value"
    
        request = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[CreateQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.CreateQuestionRequest.html)(
            parent="parent_value",
            question=question,
        )
    
        # Make the request
        response = await client.[create_question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html#google_cloud_dataqna_v1alpha_services_question_service_QuestionServiceAsyncClient_create_question)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dataqna_v1alpha.types.CreateQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.CreateQuestionRequest), dict]]`   
The request object. Request to create a question resource.  
`parent` |  ``str``   
Required. The name of the project this data source reference belongs to. Example: `projects/foo/locations/bar` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`question` |  `[Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question)`   
Required. The question to create. This corresponds to the `question` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dataqna_v1alpha.types.Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question)` | The question resource represents a natural language query, its settings, understanding generated by the system, and answer retrieval status. A question cannot be modified.  
  
### execute_question
    
    
    execute_question(
        request: typing.Optional[
            typing.Union[
                google.cloud.dataqna_v1alpha.types.question_service.ExecuteQuestionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        interpretation_index: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dataqna_v1alpha.types.question.Question

Executes an interpretation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest)
    
    async def sample_execute_question():
        # Create a client
        client = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[ExecuteQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecuteQuestionRequest.html)(
            name="name_value",
            interpretation_index=2159,
        )
    
        # Make the request
        response = await client.[execute_question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html#google_cloud_dataqna_v1alpha_services_question_service_QuestionServiceAsyncClient_execute_question)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dataqna_v1alpha.types.ExecuteQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecuteQuestionRequest), dict]]`   
The request object. Request to execute an interpretation.  
`name` |  ``str``   
Required. The unique identifier for the question. Example: `projects/foo/locations/bar/questions/1234` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`interpretation_index` |  ``int``   
Required. Index of the interpretation to execute. This corresponds to the `interpretation_index` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dataqna_v1alpha.types.Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question)` | The question resource represents a natural language query, its settings, understanding generated by the system, and answer retrieval status. A question cannot be modified.  
  
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
`QuestionServiceAsyncClient` | The constructed client.  
  
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
`QuestionServiceAsyncClient` | The constructed client.  
  
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
`QuestionServiceAsyncClient` | The constructed client.  
  
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
  
### get_question
    
    
    get_question(
        request: typing.Optional[
            typing.Union[
                google.cloud.dataqna_v1alpha.types.question_service.GetQuestionRequest, dict
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
    ) -> google.cloud.dataqna_v1alpha.types.question.Question

Gets a previously created question.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest)
    
    async def sample_get_question():
        # Create a client
        client = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[GetQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetQuestionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html#google_cloud_dataqna_v1alpha_services_question_service_QuestionServiceAsyncClient_get_question)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dataqna_v1alpha.types.GetQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetQuestionRequest), dict]]`   
The request object. A request to get a previously created question.  
`name` |  ``str``   
Required. The unique identifier for the question. Example: `projects/foo/locations/bar/questions/1234` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dataqna_v1alpha.types.Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question)` | The question resource represents a natural language query, its settings, understanding generated by the system, and answer retrieval status. A question cannot be modified.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.dataqna_v1alpha.services.question_service.transports.base.QuestionServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### get_user_feedback
    
    
    get_user_feedback(
        request: typing.Optional[
            typing.Union[
                google.cloud.dataqna_v1alpha.types.question_service.GetUserFeedbackRequest,
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
    ) -> google.cloud.dataqna_v1alpha.types.user_feedback.UserFeedback

Gets previously created user feedback.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest)
    
    async def sample_get_user_feedback():
        # Create a client
        client = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[GetUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetUserFeedbackRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_user_feedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html#google_cloud_dataqna_v1alpha_services_question_service_QuestionServiceAsyncClient_get_user_feedback)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dataqna_v1alpha.types.GetUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetUserFeedbackRequest), dict]]`   
The request object. Request to get user feedback.  
`name` |  ``str``   
Required. The unique identifier for the user feedback. User feedback is a singleton resource on a Question. Example: `projects/foo/locations/bar/questions/1234/userFeedback` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dataqna_v1alpha.types.UserFeedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback)` | Feedback provided by a user.  
  
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

### parse_question_path
    
    
    parse_question_path(path: str) -> typing.Dict[str, str]

Parses a question path into its component segments.

### parse_user_feedback_path
    
    
    parse_user_feedback_path(path: str) -> typing.Dict[str, str]

Parses a user_feedback path into its component segments.

### question_path
    
    
    question_path(project: str, location: str, question: str) -> str

Returns a fully-qualified question string.

### update_user_feedback
    
    
    update_user_feedback(
        request: typing.Optional[
            typing.Union[
                google.cloud.dataqna_v1alpha.types.question_service.UpdateUserFeedbackRequest,
                dict,
            ]
        ] = None,
        *,
        user_feedback: typing.Optional[
            google.cloud.dataqna_v1alpha.types.user_feedback.UserFeedback
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
    ) -> google.cloud.dataqna_v1alpha.types.user_feedback.UserFeedback

Updates user feedback. This creates user feedback if there was none before (upsert).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest)
    
    async def sample_update_user_feedback():
        # Create a client
        client = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        user_feedback = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[UserFeedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback.html)()
        user_feedback.name = "name_value"
    
        request = [dataqna_v1alpha](https://docs.cloud.google.com/python/docs/reference/dataqna/latest).[UpdateUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UpdateUserFeedbackRequest.html)(
            user_feedback=user_feedback,
        )
    
        # Make the request
        response = await client.[update_user_feedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient.html#google_cloud_dataqna_v1alpha_services_question_service_QuestionServiceAsyncClient_update_user_feedback)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dataqna_v1alpha.types.UpdateUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UpdateUserFeedbackRequest), dict]]`   
The request object. Request to updates user feedback.  
`user_feedback` |  `[UserFeedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback)`   
Required. The user feedback to update. This can be called even if there is no user feedback so far. The feedback's name field is used to identify the user feedback (and the corresponding question) to update. This corresponds to the `user_feedback` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dataqna_v1alpha.types.UserFeedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback)` | Feedback provided by a user.  
  
### user_feedback_path
    
    
    user_feedback_path(project: str, location: str, question: str) -> str

Returns a fully-qualified user_feedback string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
