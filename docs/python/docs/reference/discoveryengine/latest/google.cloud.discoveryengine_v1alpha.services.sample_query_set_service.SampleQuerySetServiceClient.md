---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient
title: Class SampleQuerySetServiceClient (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:37.194130+00:00
---

# Class SampleQuerySetServiceClient (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SampleQuerySetServiceClient (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SampleQuerySetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.transports.base.SampleQuerySetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.transports.base.SampleQuerySetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing SampleQuerySets,

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
`SampleQuerySetServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### SampleQuerySetServiceClient
    
    
    SampleQuerySetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.transports.base.SampleQuerySetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.transports.base.SampleQuerySetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the sample query set service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SampleQuerySetServiceTransport,Callable[..., SampleQuerySetServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the SampleQuerySetServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_sample_query_set
    
    
    create_sample_query_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1alpha.types.sample_query_set_service.CreateSampleQuerySetRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        sample_query_set: typing.Optional[
            google.cloud.discoveryengine_v1alpha.types.sample_query_set.SampleQuerySet
        ] = None,
        sample_query_set_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.discoveryengine_v1alpha.types.sample_query_set.SampleQuerySet

Creates a xref_SampleQuerySet
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1alpha
    
    def sample_create_sample_query_set():
        # Create a client
        client = discoveryengine_v1alpha.[SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html)()
    
        # Initialize request argument(s)
        sample_query_set = discoveryengine_v1alpha.[SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet.html)()
        sample_query_set.display_name = "display_name_value"
    
        request = discoveryengine_v1alpha.[CreateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSampleQuerySetRequest.html)(
            parent="parent_value",
            sample_query_set=sample_query_set,
            sample_query_set_id="sample_query_set_id_value",
        )
    
        # Make the request
        response = client.[create_sample_query_set](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html#google_cloud_discoveryengine_v1alpha_services_sample_query_set_service_SampleQuerySetServiceClient_create_sample_query_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1alpha.types.CreateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSampleQuerySetRequest), dict]`   
The request object. Request message for SampleQuerySetService.CreateSampleQuerySet method.  
`parent` |  `str`   
Required. The parent resource name, such as `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`sample_query_set` |  `[google.cloud.discoveryengine_v1alpha.types.SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)`   
Required. The SampleQuerySet to create. This corresponds to the `sample_query_set` field on the `request` instance; if `request` is provided, this should not be set.  
`sample_query_set_id` |  `str`   
Required. The ID to use for the SampleQuerySet, which will become the final component of the SampleQuerySet.name. If the caller does not have permission to create the SampleQuerySet, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all SampleQuerySets with the same parent. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__ standard with a length limit of 63 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. This corresponds to the `sample_query_set_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1alpha.types.SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)` | A SampleQuerySet is the parent resource of SampleQuery, and contains the configurations shared by all SampleQuery under it.  
  
### delete_sample_query_set
    
    
    delete_sample_query_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1alpha.types.sample_query_set_service.DeleteSampleQuerySetRequest,
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

Deletes a xref_SampleQuerySet.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1alpha
    
    def sample_delete_sample_query_set():
        # Create a client
        client = discoveryengine_v1alpha.[SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1alpha.[DeleteSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSampleQuerySetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_sample_query_set](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html#google_cloud_discoveryengine_v1alpha_services_sample_query_set_service_SampleQuerySetServiceClient_delete_sample_query_set)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1alpha.types.DeleteSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSampleQuerySetRequest), dict]`   
The request object. Request message for SampleQuerySetService.DeleteSampleQuerySet method.  
`name` |  `str`   
Required. Full resource name of SampleQuerySet, such as `projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}`. If the caller does not have permission to delete the SampleQuerySet, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the SampleQuerySet to delete does not exist, a `NOT_FOUND` error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
`SampleQuerySetServiceClient` | The constructed client.  
  
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
`SampleQuerySetServiceClient` | The constructed client.  
  
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
`SampleQuerySetServiceClient` | The constructed client.  
  
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
  
### get_sample_query_set
    
    
    get_sample_query_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1alpha.types.sample_query_set_service.GetSampleQuerySetRequest,
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
    ) -> google.cloud.discoveryengine_v1alpha.types.sample_query_set.SampleQuerySet

Gets a xref_SampleQuerySet.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1alpha
    
    def sample_get_sample_query_set():
        # Create a client
        client = discoveryengine_v1alpha.[SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1alpha.[GetSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSampleQuerySetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_sample_query_set](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html#google_cloud_discoveryengine_v1alpha_services_sample_query_set_service_SampleQuerySetServiceClient_get_sample_query_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1alpha.types.GetSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSampleQuerySetRequest), dict]`   
The request object. Request message for SampleQuerySetService.GetSampleQuerySet method.  
`name` |  `str`   
Required. Full resource name of SampleQuerySet, such as `projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}`. If the caller does not have permission to access the SampleQuerySet, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested SampleQuerySet does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1alpha.types.SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)` | A SampleQuerySet is the parent resource of SampleQuery, and contains the configurations shared by all SampleQuery under it.  
  
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
  
### list_sample_query_sets
    
    
    list_sample_query_sets(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1alpha.types.sample_query_set_service.ListSampleQuerySetsRequest,
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
        google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers.ListSampleQuerySetsPager
    )

Gets a list of xref_SampleQuerySets.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1alpha
    
    def sample_list_sample_query_sets():
        # Create a client
        client = discoveryengine_v1alpha.[SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1alpha.[ListSampleQuerySetsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_sample_query_sets](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html#google_cloud_discoveryengine_v1alpha_services_sample_query_set_service_SampleQuerySetServiceClient_list_sample_query_sets)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsRequest), dict]`   
The request object. Request message for SampleQuerySetService.ListSampleQuerySets method.  
`parent` |  `str`   
Required. The parent location resource name, such as `projects/{project}/locations/{location}`. If the caller does not have permission to list SampleQuerySets under this location, regardless of whether or not this location exists, a `PERMISSION_DENIED` error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers.ListSampleQuerySetsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers.ListSampleQuerySetsPager)` | Response message for SampleQuerySetService.ListSampleQuerySets method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### location_path
    
    
    location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

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

### parse_location_path
    
    
    parse_location_path(path: str) -> typing.Dict[str, str]

Parses a location path into its component segments.

### parse_sample_query_set_path
    
    
    parse_sample_query_set_path(path: str) -> typing.Dict[str, str]

Parses a sample_query_set path into its component segments.

### sample_query_set_path
    
    
    sample_query_set_path(project: str, location: str, sample_query_set: str) -> str

Returns a fully-qualified sample_query_set string.

### update_sample_query_set
    
    
    update_sample_query_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1alpha.types.sample_query_set_service.UpdateSampleQuerySetRequest,
                dict,
            ]
        ] = None,
        *,
        sample_query_set: typing.Optional[
            google.cloud.discoveryengine_v1alpha.types.sample_query_set.SampleQuerySet
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
    ) -> google.cloud.discoveryengine_v1alpha.types.sample_query_set.SampleQuerySet

Updates a xref_SampleQuerySet.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1alpha
    
    def sample_update_sample_query_set():
        # Create a client
        client = discoveryengine_v1alpha.[SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html)()
    
        # Initialize request argument(s)
        sample_query_set = discoveryengine_v1alpha.[SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet.html)()
        sample_query_set.display_name = "display_name_value"
    
        request = discoveryengine_v1alpha.[UpdateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSampleQuerySetRequest.html)(
            sample_query_set=sample_query_set,
        )
    
        # Make the request
        response = client.[update_sample_query_set](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient.html#google_cloud_discoveryengine_v1alpha_services_sample_query_set_service_SampleQuerySetServiceClient_update_sample_query_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1alpha.types.UpdateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSampleQuerySetRequest), dict]`   
The request object. Request message for SampleQuerySetService.UpdateSampleQuerySet method.  
`sample_query_set` |  `[google.cloud.discoveryengine_v1alpha.types.SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)`   
Required. The sample query set to update. If the caller does not have permission to update the SampleQuerySet, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the SampleQuerySet to update does not exist a `NOT_FOUND` error is returned. This corresponds to the `sample_query_set` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided imported 'sample query set' to update. If not set, will by default update all fields. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1alpha.types.SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)` | A SampleQuerySet is the parent resource of SampleQuery, and contains the configurations shared by all SampleQuery under it.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
