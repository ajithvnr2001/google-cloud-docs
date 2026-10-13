---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient
title: Class AdviceClient (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:17:39.710822+00:00
---

# Class AdviceClient (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AdviceClient (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    AdviceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.advice.transports.base.AdviceTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.advice.transports.base.AdviceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Advice API.

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
`AdviceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AdviceClient
    
    
    AdviceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.advice.transports.base.AdviceTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.advice.transports.base.AdviceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the advice client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AdviceTransport,Callable[..., AdviceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the AdviceTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### calendar_mode
    
    
    calendar_mode(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CalendarModeAdviceRpcRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        calendar_mode_advice_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.CalendarModeAdviceRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.CalendarModeAdviceResponse

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_calendar_mode():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AdviceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeAdviceRpcRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[calendar_mode](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html#google_cloud_compute_v1beta_services_advice_AdviceClient_calendar_mode)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeAdviceRpcRequest), dict]`   
The request object. A request message for Advice.CalendarMode. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region for this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`calendar_mode_advice_request_resource` |  `[google.cloud.compute_v1beta.types.CalendarModeAdviceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeAdviceRequest)`   
The body resource for this request This corresponds to the `calendar_mode_advice_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.CalendarModeAdviceResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeAdviceResponse)` | A response containing the recommended way of creating the specified resources in the future. It contains (will contain) multiple recommendations that can be analyzed by the customer and the best one can be picked.  
  
### calendar_mode_extension
    
    
    calendar_mode_extension(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CalendarModeExtensionAdviceRpcRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        calendar_mode_extension_advice_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.CalendarModeExtensionAdviceRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.CalendarModeExtensionAdviceResponse

Advises on whether extending an existing future reservation is possible based on the desired extension end time. If capacity isn't available for the entire requested duration, the method recommends the longest possible extension.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_calendar_mode_extension():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AdviceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CalendarModeExtensionAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceRpcRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[calendar_mode_extension](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html#google_cloud_compute_v1beta_services_advice_AdviceClient_calendar_mode_extension)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceRpcRequest), dict]`   
The request object. A request message for Advice.CalendarModeExtension. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region for this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`calendar_mode_extension_advice_request_resource` |  `[google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceRequest)`   
The body resource for this request This corresponds to the `calendar_mode_extension_advice_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CalendarModeExtensionAdviceResponse)` | A response that contains the recommended duration for extending a future reservation in calendar mode based on available capacity during the extension period.  
  
### capacity
    
    
    capacity(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CapacityAdviceRpcRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        capacity_advice_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.CapacityAdviceRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.CapacityAdviceResponse

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_capacity():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AdviceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CapacityAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityAdviceRpcRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[capacity](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html#google_cloud_compute_v1beta_services_advice_AdviceClient_capacity)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CapacityAdviceRpcRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityAdviceRpcRequest), dict]`   
The request object. A request message for Advice.Capacity. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region for this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`capacity_advice_request_resource` |  `[google.cloud.compute_v1beta.types.CapacityAdviceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityAdviceRequest)`   
The body resource for this request This corresponds to the `capacity_advice_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.CapacityAdviceResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityAdviceResponse)` | A response contains scoring recommendations.  
  
### capacity_history
    
    
    capacity_history(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CapacityHistoryAdviceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        capacity_history_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.CapacityHistoryRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.CapacityHistoryResponse

Gets the capacity history.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_capacity_history():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AdviceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityHistoryAdviceRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[capacity_history](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.advice.AdviceClient.html#google_cloud_compute_v1beta_services_advice_AdviceClient_capacity_history)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CapacityHistoryAdviceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityHistoryAdviceRequest), dict]`   
The request object. A request message for Advice.CapacityHistory. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region for this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`capacity_history_request_resource` |  `[google.cloud.compute_v1beta.types.CapacityHistoryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityHistoryRequest)`   
The body resource for this request This corresponds to the `capacity_history_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.CapacityHistoryResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CapacityHistoryResponse)` | Contains the capacity history.  
  
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
`AdviceClient` | The constructed client.  
  
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
`AdviceClient` | The constructed client.  
  
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
`AdviceClient` | The constructed client.  
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
