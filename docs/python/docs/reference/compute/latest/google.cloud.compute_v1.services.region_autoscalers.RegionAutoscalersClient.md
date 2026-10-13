---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient
title: Class RegionAutoscalersClient (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:15.940893+00:00
---

# Class RegionAutoscalersClient (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RegionAutoscalersClient (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    RegionAutoscalersClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.region_autoscalers.transports.base.RegionAutoscalersTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.region_autoscalers.transports.base.RegionAutoscalersTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The RegionAutoscalers API. This class implements API version 2026-10-01-preview.

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
`RegionAutoscalersTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### RegionAutoscalersClient
    
    
    RegionAutoscalersClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.region_autoscalers.transports.base.RegionAutoscalersTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.region_autoscalers.transports.base.RegionAutoscalersTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the region autoscalers client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,RegionAutoscalersTransport,Callable[..., RegionAutoscalersTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the RegionAutoscalersTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### delete
    
    
    delete(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.DeleteRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified autoscaler.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_delete():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest.html)(
            autoscaler="autoscaler_value",
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler` |  `str`   
Name of the autoscaler to delete. This corresponds to the `autoscaler` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### delete_unary
    
    
    delete_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.DeleteRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Operation

Deletes the specified autoscaler.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_delete():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest.html)(
            autoscaler="autoscaler_value",
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler` |  `str`   
Name of the autoscaler to delete. This corresponds to the `autoscaler` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
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
`RegionAutoscalersClient` | The constructed client.  
  
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
`RegionAutoscalersClient` | The constructed client.  
  
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
`RegionAutoscalersClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.GetRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Autoscaler

Returns the specified autoscaler.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_get():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GetRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetRegionAutoscalerRequest.html)(
            autoscaler="autoscaler_value",
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.GetRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler` |  `str`   
Name of the autoscaler to return. This corresponds to the `autoscaler` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)` | Represents an Autoscaler resource. Google Compute Engine has two Autoscaler resources: - [Zonal](/compute/docs/reference/rest/v1/autoscalers) - [Regional](/compute/docs/reference/rest/v1/regionAutoscalers) Use autoscalers to automatically add or delete instances from a managed instance group according to your defined autoscaling policy. For more information, read Autoscaling Groups of Instances. For zonal managed instance groups resource, use the autoscaler resource. For regional managed instance groups, use theregionAutoscalers resource.  
  
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
  
### insert
    
    
    insert(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.InsertRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Creates an autoscaler in the specified project using the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_insert():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### insert_unary
    
    
    insert_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.InsertRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Operation

Creates an autoscaler in the specified project using the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_insert():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### list
    
    
    list(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.ListRegionAutoscalersRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.services.region_autoscalers.pagers.ListPager

Retrieves a list of autoscalers contained within the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_list():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ListRegionAutoscalersRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListRegionAutoscalersRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.ListRegionAutoscalersRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListRegionAutoscalersRequest), dict]`   
The request object. A request message for RegionAutoscalers.List. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.services.region_autoscalers.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.pagers.ListPager)` | Contains a list of autoscalers. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### patch
    
    
    patch(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.PatchRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[PatchRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.PatchRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.PatchRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.PatchRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### patch_unary
    
    
    patch_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.PatchRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Operation

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[PatchRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.PatchRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.PatchRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.PatchRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.TestIamPermissionsRegionAutoscalerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        test_permissions_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.TestPermissionsRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.TestPermissionsResponse

Returns permissions that a caller has on the specified resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_test_iam_permissions():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[TestIamPermissionsRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.TestIamPermissionsRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.TestIamPermissionsRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.TestIamPermissionsRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.TestIamPermissions. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
The name of the region for this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`test_permissions_request_resource` |  `[google.cloud.compute_v1.types.TestPermissionsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.TestPermissionsRequest)`   
The body resource for this request This corresponds to the `test_permissions_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### update
    
    
    update(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.UpdateRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Updates an autoscaler in the specified project using the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
### update_unary
    
    
    update_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.UpdateRegionAutoscalerRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        autoscaler_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.Autoscaler
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Operation

Updates an autoscaler in the specified project using the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionAutoscalersClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest.html)(
            project="project_value",
            region="region_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_autoscalers.RegionAutoscalersClient.html#google_cloud_compute_v1_services_region_autoscalers_RegionAutoscalersClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UpdateRegionAutoscalerRequest), dict]`   
The request object. A request message for RegionAutoscalers.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`region` |  `str`   
Name of the region scoping this request. This corresponds to the `region` field on the `request` instance; if `request` is provided, this should not be set.  
`autoscaler_resource` |  `[google.cloud.compute_v1.types.Autoscaler](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Autoscaler)`   
The body resource for this request This corresponds to the `autoscaler_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.extended_operation.ExtendedOperation` | An object representing a extended long-running operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
