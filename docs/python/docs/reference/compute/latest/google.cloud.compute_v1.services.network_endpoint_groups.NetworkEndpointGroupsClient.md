---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient
title: Class NetworkEndpointGroupsClient (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:22.747626+00:00
---

# Class NetworkEndpointGroupsClient (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NetworkEndpointGroupsClient (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    NetworkEndpointGroupsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.network_endpoint_groups.transports.base.NetworkEndpointGroupsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.network_endpoint_groups.transports.base.NetworkEndpointGroupsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The NetworkEndpointGroups API. This class implements API version 2026-10-01-preview.

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
`NetworkEndpointGroupsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### NetworkEndpointGroupsClient
    
    
    NetworkEndpointGroupsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1.services.network_endpoint_groups.transports.base.NetworkEndpointGroupsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1.services.network_endpoint_groups.transports.base.NetworkEndpointGroupsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the network endpoint groups client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,NetworkEndpointGroupsTransport,Callable[..., NetworkEndpointGroupsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the NetworkEndpointGroupsTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### aggregated_list
    
    
    aggregated_list(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.AggregatedListNetworkEndpointGroupsRequest,
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
    ) -> (
        google.cloud.compute_v1.services.network_endpoint_groups.pagers.AggregatedListPager
    )

Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    def sample_aggregated_list():
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AggregatedListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AggregatedListNetworkEndpointGroupsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[aggregated_list](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_aggregated_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.AggregatedListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AggregatedListNetworkEndpointGroupsRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.AggregatedList. See the method description for details.  
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
`[google.cloud.compute_v1.services.network_endpoint_groups.pagers.AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.pagers.AggregatedListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### attach_network_endpoints
    
    
    attach_network_endpoints(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.AttachNetworkEndpointsNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        network_endpoint_groups_attach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroupsAttachEndpointsRequest
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

Attach a list of network endpoints to the specified network endpoint group.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[attach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_attach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.AttachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_groups_attach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroupsAttachEndpointsRequest)`   
The body resource for this request This corresponds to the `network_endpoint_groups_attach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.AttachNetworkEndpointsNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        network_endpoint_groups_attach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroupsAttachEndpointsRequest
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

Attach a list of network endpoints to the specified network endpoint group.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[attach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_attach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachNetworkEndpointsNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.AttachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_groups_attach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroupsAttachEndpointsRequest)`   
The body resource for this request This corresponds to the `network_endpoint_groups_attach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DeleteNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DeleteNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DetachNetworkEndpointsNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        network_endpoint_groups_detach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroupsDetachEndpointsRequest
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

Detach a list of network endpoints from the specified network endpoint group.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[detach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_detach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.DetachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_groups_detach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroupsDetachEndpointsRequest)`   
The body resource for this request This corresponds to the `network_endpoint_groups_detach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.DetachNetworkEndpointsNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        network_endpoint_groups_detach_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroupsDetachEndpointsRequest
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

Detach a list of network endpoints from the specified network endpoint group.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[detach_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_detach_network_endpoints)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DetachNetworkEndpointsNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.DetachNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_groups_detach_endpoints_request_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroupsDetachEndpointsRequest)`   
The body resource for this request This corresponds to the `network_endpoint_groups_detach_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
`NetworkEndpointGroupsClient` | The constructed client.  
  
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
`NetworkEndpointGroupsClient` | The constructed client.  
  
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
`NetworkEndpointGroupsClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.GetNetworkEndpointGroupRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GetNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetNetworkEndpointGroupRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.GetNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GetNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.InsertNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the network endpoint group. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.InsertNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the network endpoint group. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1.types.compute.ListNetworkEndpointGroupsRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListPager

Retrieves the list of network endpoint groups that are located in the specified project and zone.
    
    
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointGroupsRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.ListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointGroupsRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.List. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_network_endpoints
    
    
    list_network_endpoints(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.ListNetworkEndpointsNetworkEndpointGroupsRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        network_endpoint_group: typing.Optional[str] = None,
        network_endpoint_groups_list_endpoints_request_resource: typing.Optional[
            google.cloud.compute_v1.types.compute.NetworkEndpointGroupsListEndpointsRequest
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
        google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListNetworkEndpointsPager
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ListNetworkEndpointsNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointsNetworkEndpointGroupsRequest.html)(
            network_endpoint_group="network_endpoint_group_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_network_endpoints](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_list_network_endpoints)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.ListNetworkEndpointsNetworkEndpointGroupsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListNetworkEndpointsNetworkEndpointGroupsRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.ListNetworkEndpoints. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where the network endpoint group is located. It should comply with RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_group` |  `str`   
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035. This corresponds to the `network_endpoint_group` field on the `request` instance; if `request` is provided, this should not be set.  
`network_endpoint_groups_list_endpoints_request_resource` |  `[google.cloud.compute_v1.types.NetworkEndpointGroupsListEndpointsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkEndpointGroupsListEndpointsRequest)`   
The body resource for this request This corresponds to the `network_endpoint_groups_list_endpoints_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListNetworkEndpointsPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.pagers.ListNetworkEndpointsPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1.types.compute.TestIamPermissionsNetworkEndpointGroupRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
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
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkEndpointGroupsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[TestIamPermissionsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.TestIamPermissionsNetworkEndpointGroupRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.network_endpoint_groups.NetworkEndpointGroupsClient.html#google_cloud_compute_v1_services_network_endpoint_groups_NetworkEndpointGroupsClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1.types.TestIamPermissionsNetworkEndpointGroupRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.TestIamPermissionsNetworkEndpointGroupRequest), dict]`   
The request object. A request message for NetworkEndpointGroups.TestIamPermissions. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
