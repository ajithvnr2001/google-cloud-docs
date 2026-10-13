---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient
title: Class GlobalNetworkEndpointGroupsClient (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:08.396931+00:00
---

# Class GlobalNetworkEndpointGroupsClient (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GlobalNetworkEndpointGroupsClient (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    GlobalNetworkEndpointGroupsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.global_network_endpoint_groups.transports.base.GlobalNetworkEndpointGroupsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.global_network_endpoint_groups.transports.base.GlobalNetworkEndpointGroupsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The GlobalNetworkEndpointGroups API. This class implements API version 2026-10-01-preview.

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
`GlobalNetworkEndpointGroupsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### GlobalNetworkEndpointGroupsClient
    
    
    GlobalNetworkEndpointGroupsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.global_network_endpoint_groups.transports.base.GlobalNetworkEndpointGroupsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.global_network_endpoint_groups.transports.base.GlobalNetworkEndpointGroupsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the global network endpoint groups client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,GlobalNetworkEndpointGroupsTransport,Callable[..., GlobalNetworkEndpointGroupsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the GlobalNetworkEndpointGroupsTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### attach_network_endpoints
    
    
    attach_network_endpoints(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        global_network_endpoint_groups_attach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.GlobalNetworkEndpointGroupsAttachEndpointsRequest
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

Attach a network endpoint to the specified network endpoint group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_attach_network_endpoints():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[attach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_attach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.AttachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`global_network_endpoint_groups_attach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsAttachEndpointsRequest)`   
The body resource for this request This corresponds to the `global_network_endpoint_groups_attach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### attach_network_endpoints_unary
    
    
    attach_network_endpoints_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        global_network_endpoint_groups_attach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.GlobalNetworkEndpointGroupsAttachEndpointsRequest
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

Attach a network endpoint to the specified network endpoint group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_attach_network_endpoints():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[attach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_attach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.AttachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`global_network_endpoint_groups_attach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsAttachEndpointsRequest)`   
The body resource for this request This corresponds to the `global_network_endpoint_groups_attach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DeleteGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group to delete. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DeleteGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.Operation

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group to delete. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### detach_network_endpoints
    
    
    detach_network_endpoints(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        global_network_endpoint_groups_detach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.GlobalNetworkEndpointGroupsDetachEndpointsRequest
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

Detach the network endpoint from the specified network endpoint group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_detach_network_endpoints():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[detach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_detach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.DetachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`global_network_endpoint_groups_detach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsDetachEndpointsRequest)`   
The body resource for this request This corresponds to the `global_network_endpoint_groups_detach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### detach_network_endpoints_unary
    
    
    detach_network_endpoints_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        global_network_endpoint_groups_detach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.GlobalNetworkEndpointGroupsDetachEndpointsRequest
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

Detach the network endpoint from the specified network endpoint group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_detach_network_endpoints():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[detach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_detach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.DetachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`global_network_endpoint_groups_detach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GlobalNetworkEndpointGroupsDetachEndpointsRequest)`   
The body resource for this request This corresponds to the `global_network_endpoint_groups_detach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
`GlobalNetworkEndpointGroupsClient` | The constructed client.  
  
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
`GlobalNetworkEndpointGroupsClient` | The constructed client.  
  
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
`GlobalNetworkEndpointGroupsClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.GetGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.types.compute.NetworkEndpointGroup

Returns the specified network endpoint group.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetGlobalNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.types.NetworkEndpointGroup](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroup)` | Represents a collection of network endpoints. A network endpoint group (NEG) defines how a set of endpoints should be reached, whether they are reachable, and where they are located. For more information about using NEGs for different use cases, seeNetwork endpoint groups overview. Note: Use the following APIs to manage network endpoint groups: - To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API - To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API  
  
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
                google.cloud.compute_v1.types.compute.InsertGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroup
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

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API \- To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API \- To manage NEGs with global scope (such as global internet NEGs):global API
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroup](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroup)`   
The body resource for this request This corresponds to the `network_endpoint_group_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.InsertGlobalNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroup
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

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API \- To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API \- To manage NEGs with global scope (such as global internet NEGs):global API
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertGlobalNetworkEndpointGroupRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroup](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroup)`   
The body resource for this request This corresponds to the `network_endpoint_group_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.ListGlobalNetworkEndpointGroupsRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListPager

Retrieves the list of network endpoint groups that are located in the specified project.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListGlobalNetworkEndpointGroupsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListGlobalNetworkEndpointGroupsRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.List. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_network_endpoints
    
    
    list_network_endpoints(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListNetworkEndpointsPager
    )

Lists the network endpoints in the specified network endpoint group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_list_network_endpoints():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
        )
    
        # Make the request
        page_result = client.[list_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.GlobalNetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_global_network_endpoint_groups_GlobalNetworkEndpointGroupsClient_list_network_endpoints)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest), dict]`   
The request object. A request message for GlobalNetworkEndpointGroups.ListNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListNetworkEndpointsPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_network_endpoint_groups.pagers.ListNetworkEndpointsPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
