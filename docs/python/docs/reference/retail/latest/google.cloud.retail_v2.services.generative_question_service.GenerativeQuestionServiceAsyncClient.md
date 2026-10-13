---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient
title: Class GenerativeQuestionServiceAsyncClient (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:24.043467+00:00
---

# Class GenerativeQuestionServiceAsyncClient (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerativeQuestionServiceAsyncClient (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    GenerativeQuestionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2.services.generative_question_service.transports.base.GenerativeQuestionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2.services.generative_question_service.transports.base.GenerativeQuestionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing LLM generated questions in search serving.

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
`GenerativeQuestionServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### GenerativeQuestionServiceAsyncClient
    
    
    GenerativeQuestionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2.services.generative_question_service.transports.base.GenerativeQuestionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2.services.generative_question_service.transports.base.GenerativeQuestionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the generative question service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,GenerativeQuestionServiceTransport,Callable[..., GenerativeQuestionServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the GenerativeQuestionServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### batch_update_generative_question_configs
    
    
    batch_update_generative_question_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.generative_question_service.BatchUpdateGenerativeQuestionConfigsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.retail_v2.types.generative_question_service.UpdateGenerativeQuestionConfigRequest
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.retail_v2.types.generative_question_service.BatchUpdateGenerativeQuestionConfigsResponse
    )

Allows management of multiple questions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    async def sample_batch_update_generative_question_configs():
        # Create a client
        client = retail_v2.[GenerativeQuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        requests = retail_v2.[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest.html)()
        requests.generative_question_config.catalog = "catalog_value"
        requests.generative_question_config.facet = "facet_value"
    
        request = retail_v2.[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.BatchUpdateGenerativeQuestionConfigsRequest.html)(
            requests=requests,
        )
    
        # Make the request
        response = await client.[batch_update_generative_question_configs](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html#google_cloud_retail_v2_services_generative_question_service_GenerativeQuestionServiceAsyncClient_batch_update_generative_question_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.retail_v2.types.BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.BatchUpdateGenerativeQuestionConfigsRequest), dict]]`   
The request object. Request for BatchUpdateGenerativeQuestionConfig method.  
`parent` |  ``str``   
Optional. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`requests` |  `:class:`MutableSequence[[google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest)]``   
Required. The updates question configs. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.BatchUpdateGenerativeQuestionConfigsResponse)` | Aggregated response for UpdateGenerativeQuestionConfig method.  
  
### catalog_path
    
    
    catalog_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified catalog string.

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
`GenerativeQuestionServiceAsyncClient` | The constructed client.  
  
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
`GenerativeQuestionServiceAsyncClient` | The constructed client.  
  
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
`GenerativeQuestionServiceAsyncClient` | The constructed client.  
  
### get_generative_questions_feature_config
    
    
    get_generative_questions_feature_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.generative_question_service.GetGenerativeQuestionsFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        catalog: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2.types.generative_question.GenerativeQuestionsFeatureConfig

Manages overal generative question feature state -- enables toggling feature on and off.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    async def sample_get_generative_questions_feature_config():
        # Create a client
        client = retail_v2.[GenerativeQuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[GetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GetGenerativeQuestionsFeatureConfigRequest.html)(
            catalog="catalog_value",
        )
    
        # Make the request
        response = await client.[get_generative_questions_feature_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html#google_cloud_retail_v2_services_generative_question_service_GenerativeQuestionServiceAsyncClient_get_generative_questions_feature_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.retail_v2.types.GetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GetGenerativeQuestionsFeatureConfigRequest), dict]]`   
The request object. Request for GetGenerativeQuestionsFeatureConfig method.  
`catalog` |  ``str``   
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog} This corresponds to the `catalog` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig)` | Configuration for overall generative question feature state.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.retail_v2.services.generative_question_service.transports.base.GenerativeQuestionServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_generative_question_configs
    
    
    list_generative_question_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.generative_question_service.ListGenerativeQuestionConfigsRequest,
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
        google.cloud.retail_v2.types.generative_question_service.ListGenerativeQuestionConfigsResponse
    )

Returns all questions for a given catalog.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    async def sample_list_generative_question_configs():
        # Create a client
        client = retail_v2.[GenerativeQuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[ListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ListGenerativeQuestionConfigsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[list_generative_question_configs](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html#google_cloud_retail_v2_services_generative_question_service_GenerativeQuestionServiceAsyncClient_list_generative_question_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.retail_v2.types.ListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ListGenerativeQuestionConfigsRequest), dict]]`   
The request object. Request for ListQuestions method.  
`parent` |  ``str``   
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ListGenerativeQuestionConfigsResponse)` | Response for ListQuestions method.  
  
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
  
### parse_catalog_path
    
    
    parse_catalog_path(path: str) -> typing.Dict[str, str]

Parses a catalog path into its component segments.

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

### update_generative_question_config
    
    
    update_generative_question_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.generative_question_service.UpdateGenerativeQuestionConfigRequest,
                dict,
            ]
        ] = None,
        *,
        generative_question_config: typing.Optional[
            google.cloud.retail_v2.types.generative_question.GenerativeQuestionConfig
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
    ) -> google.cloud.retail_v2.types.generative_question.GenerativeQuestionConfig

Allows management of individual questions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    async def sample_update_generative_question_config():
        # Create a client
        client = retail_v2.[GenerativeQuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        generative_question_config = retail_v2.[GenerativeQuestionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionConfig.html)()
        generative_question_config.catalog = "catalog_value"
        generative_question_config.facet = "facet_value"
    
        request = retail_v2.[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest.html)(
            generative_question_config=generative_question_config,
        )
    
        # Make the request
        response = await client.[update_generative_question_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html#google_cloud_retail_v2_services_generative_question_service_GenerativeQuestionServiceAsyncClient_update_generative_question_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionConfigRequest), dict]]`   
The request object. Request for UpdateGenerativeQuestionConfig method.  
`generative_question_config` |  `[GenerativeQuestionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionConfig)`   
Required. The question to update. This corresponds to the `generative_question_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Indicates which fields in the provided [GenerativeQuestionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionConfig) to update. The following are NOT supported: - [GenerativeQuestionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionConfig).frequency If not set or empty, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.GenerativeQuestionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionConfig)` | Configuration for a single generated question.  
  
### update_generative_questions_feature_config
    
    
    update_generative_questions_feature_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.generative_question_service.UpdateGenerativeQuestionsFeatureConfigRequest,
                dict,
            ]
        ] = None,
        *,
        generative_questions_feature_config: typing.Optional[
            google.cloud.retail_v2.types.generative_question.GenerativeQuestionsFeatureConfig
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
    ) -> google.cloud.retail_v2.types.generative_question.GenerativeQuestionsFeatureConfig

Manages overal generative question feature state -- enables toggling feature on and off.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    async def sample_update_generative_questions_feature_config():
        # Create a client
        client = retail_v2.[GenerativeQuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        generative_questions_feature_config = retail_v2.[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig.html)()
        generative_questions_feature_config.catalog = "catalog_value"
    
        request = retail_v2.[UpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionsFeatureConfigRequest.html)(
            generative_questions_feature_config=generative_questions_feature_config,
        )
    
        # Make the request
        response = await client.[update_generative_questions_feature_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.generative_question_service.GenerativeQuestionServiceAsyncClient.html#google_cloud_retail_v2_services_generative_question_service_GenerativeQuestionServiceAsyncClient_update_generative_questions_feature_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.retail_v2.types.UpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateGenerativeQuestionsFeatureConfigRequest), dict]]`   
The request object. Request for UpdateGenerativeQuestionsFeatureConfig method.  
`generative_questions_feature_config` |  `[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig)`   
Required. The configuration managing the feature state. This corresponds to the `generative_questions_feature_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Indicates which fields in the provided [GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig) to update. If not set or empty, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GenerativeQuestionsFeatureConfig)` | Configuration for overall generative question feature state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
