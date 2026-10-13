---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient
title: Class InstanceGroupManagersClient (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:19:30.867677+00:00
---

# Class InstanceGroupManagersClient (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstanceGroupManagersClient (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    InstanceGroupManagersClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.instance_group_managers.transports.base.InstanceGroupManagersTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.instance_group_managers.transports.base.InstanceGroupManagersTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The InstanceGroupManagers API.

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
`InstanceGroupManagersTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### InstanceGroupManagersClient
    
    
    InstanceGroupManagersClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.instance_group_managers.transports.base.InstanceGroupManagersTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.instance_group_managers.transports.base.InstanceGroupManagersTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the instance group managers client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,InstanceGroupManagersTransport,Callable[..., InstanceGroupManagersTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the InstanceGroupManagersTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### abandon_instances
    
    
    abandon_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AbandonInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_abandon_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersAbandonInstancesRequest
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

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_abandon_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[abandon_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_abandon_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.AbandonInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_abandon_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersAbandonInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersAbandonInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_abandon_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### abandon_instances_unary
    
    
    abandon_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AbandonInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_abandon_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersAbandonInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_abandon_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[abandon_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_abandon_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AbandonInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.AbandonInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_abandon_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersAbandonInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersAbandonInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_abandon_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### aggregated_list
    
    
    aggregated_list(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AggregatedListInstanceGroupManagersRequest,
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
        google.cloud.compute_v1beta.services.instance_group_managers.pagers.AggregatedListPager
    )

Retrieves the list of managed instance groups and groups them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_aggregated_list():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AggregatedListInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListInstanceGroupManagersRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[aggregated_list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_aggregated_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AggregatedListInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListInstanceGroupManagersRequest), dict]`   
The request object. A request message for InstanceGroupManagers.AggregatedList. See the method description for details.  
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
`[google.cloud.compute_v1beta.services.instance_group_managers.pagers.AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.AggregatedListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### apply_updates_to_instances
    
    
    apply_updates_to_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_apply_updates_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersApplyUpdatesRequest
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

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_apply_updates_to_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[apply_updates_to_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_apply_updates_to_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ApplyUpdatesToInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. Should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group, should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_apply_updates_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersApplyUpdatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersApplyUpdatesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_apply_updates_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### apply_updates_to_instances_unary
    
    
    apply_updates_to_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_apply_updates_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersApplyUpdatesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_apply_updates_to_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[apply_updates_to_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_apply_updates_to_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ApplyUpdatesToInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ApplyUpdatesToInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. Should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group, should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_apply_updates_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersApplyUpdatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersApplyUpdatesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_apply_updates_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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

### configure_accelerator_topologies
    
    
    configure_accelerator_topologies(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_configure_accelerator_topologies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersConfigureAcceleratorTopologiesRequest
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

Updates the accelerator topologies configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_configure_accelerator_topologies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ConfigureAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[configure_accelerator_topologies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_configure_accelerator_topologies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ConfigureAcceleratorTopologies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_configure_accelerator_topologies_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersConfigureAcceleratorTopologiesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersConfigureAcceleratorTopologiesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_configure_accelerator_topologies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### configure_accelerator_topologies_unary
    
    
    configure_accelerator_topologies_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_configure_accelerator_topologies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersConfigureAcceleratorTopologiesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Updates the accelerator topologies configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_configure_accelerator_topologies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ConfigureAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[configure_accelerator_topologies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_configure_accelerator_topologies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ConfigureAcceleratorTopologiesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ConfigureAcceleratorTopologies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_configure_accelerator_topologies_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersConfigureAcceleratorTopologiesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersConfigureAcceleratorTopologiesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_configure_accelerator_topologies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### create_instances
    
    
    create_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CreateInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_create_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersCreateInstancesRequest
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

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_create_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[create_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_create_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.CreateInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_create_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersCreateInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersCreateInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_create_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### create_instances_unary
    
    
    create_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.CreateInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_create_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersCreateInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_create_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[create_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_create_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.CreateInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.CreateInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_create_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersCreateInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersCreateInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_create_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete
    
    
    delete(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group to delete. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_instances
    
    
    delete_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_delete_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersDeleteInstancesRequest
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

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.DeleteInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_delete_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersDeleteInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersDeleteInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_delete_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_instances_unary
    
    
    delete_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_delete_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersDeleteInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.DeleteInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_delete_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersDeleteInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersDeleteInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_delete_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_per_instance_configs
    
    
    delete_per_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_delete_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersDeletePerInstanceConfigsReq
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

Deletes selected per-instance configurations for the managed instance group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.DeletePerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_delete_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersDeletePerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersDeletePerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_delete_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_per_instance_configs_unary
    
    
    delete_per_instance_configs_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_delete_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersDeletePerInstanceConfigsReq
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes selected per-instance configurations for the managed instance group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeletePerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.DeletePerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_delete_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersDeletePerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersDeletePerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_delete_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.DeleteInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group to delete. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
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
`InstanceGroupManagersClient` | The constructed client.  
  
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
`InstanceGroupManagersClient` | The constructed client.  
  
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
`InstanceGroupManagersClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.InstanceGroupManager

Returns all of the details about the specified managed instance group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)` | Represents a Managed Instance Group resource. An instance group is a collection of VM instances that you can manage as a single entity. For more information, readInstance groups. For zonal Managed Instance Group, use the instanceGroupManagers resource. For regional Managed Instance Group, use theregionInstanceGroupManagers resource.  
  
### get_available_accelerator_topologies
    
    
    get_available_accelerator_topologies(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetAvailableAcceleratorTopologiesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.compute_v1beta.types.compute.InstanceGroupManagersGetAvailableAcceleratorTopologiesResponse
    )

Returns information about available accelerator topologies for a given MIG.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_available_accelerator_topologies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetAvailableAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetAvailableAcceleratorTopologiesInstanceGroupManagerRequest.html)(
            project="project_value",
            resource_id="resource_id_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_available_accelerator_topologies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_get_available_accelerator_topologies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetAvailableAcceleratorTopologiesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetAvailableAcceleratorTopologiesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.GetAvailableAcceleratorTopologies. See the method description for details.  
`project` |  `str`   
Required. Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
Required. The name of thezone where the managed instance group is located. Name should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource_id` |  `str`   
Required. The name of the managed instance group. It should conform to RFC1035. This corresponds to the `resource_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
                google.cloud.compute_v1beta.types.compute.InsertInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
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

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_insert():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.InsertInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_insert():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.ListInstanceGroupManagersRequest,
                dict,
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
    ) -> google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPager

Retrieves a list of managed instance groups that are contained within the specified project and zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListInstanceGroupManagersRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListInstanceGroupManagersRequest), dict]`   
The request object. A request message for InstanceGroupManagers.List. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPager)` | [Output Only] A list of managed instance groups. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_errors
    
    
    list_errors(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListErrorsInstanceGroupManagersRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListErrorsPager
    )

Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_errors():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListErrorsInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListErrorsInstanceGroupManagersRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_errors](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_list_errors)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListErrorsInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListErrorsInstanceGroupManagersRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ListErrors. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It must be a string that meets the requirements in RFC1035, or an unsigned long integer: must match regexp pattern: (?:`a-z <?:[-a-z0-9]{0,61}[a-z0-9]>`__?)|1-9{0,19}. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListErrorsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListErrorsPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_managed_instances
    
    
    list_managed_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListManagedInstancesInstanceGroupManagersRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListManagedInstancesPager
    )

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_managed_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListManagedInstancesInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListManagedInstancesInstanceGroupManagersRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_managed_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_list_managed_instances)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListManagedInstancesInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListManagedInstancesInstanceGroupManagersRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ListManagedInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListManagedInstancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListManagedInstancesPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_per_instance_configs
    
    
    list_per_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPerInstanceConfigsPager
    )

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListPerInstanceConfigsInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListPerInstanceConfigsInstanceGroupManagersRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_list_per_instance_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListPerInstanceConfigsInstanceGroupManagersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListPerInstanceConfigsInstanceGroupManagersRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ListPerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPerInstanceConfigsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPerInstanceConfigsPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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
                google.cloud.compute_v1beta.types.compute.PatchInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
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

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### patch_per_instance_configs
    
    
    patch_per_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_patch_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersPatchPerInstanceConfigsReq
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

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_patch_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.PatchPerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_patch_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersPatchPerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersPatchPerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_patch_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### patch_per_instance_configs_unary
    
    
    patch_per_instance_configs_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_patch_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersPatchPerInstanceConfigsReq
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_patch_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.PatchPerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_patch_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersPatchPerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersPatchPerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_patch_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.PatchInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### recreate_instances
    
    
    recreate_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.RecreateInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_recreate_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersRecreateInstancesRequest
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

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_recreate_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[recreate_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_recreate_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.RecreateInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_recreate_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersRecreateInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersRecreateInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_recreate_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### recreate_instances_unary
    
    
    recreate_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.RecreateInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_recreate_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersRecreateInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_recreate_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[recreate_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_recreate_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecreateInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.RecreateInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_recreate_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersRecreateInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersRecreateInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_recreate_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resize
    
    
    resize(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResizeInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

  * The status of the VM instance.
  * The health of the VM instance.
  * The instance template version the VM is based on.
  * For regional managed instance groups, the location of the VM instance.



This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resize():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            size=443,
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resize](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resize)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Resize. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`size` |  `int`   
The number of running instances that the managed instance group should maintain at any given time. The group automatically adds or removes instances to maintain the number of instances specified by this parameter. This corresponds to the `size` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resize_advanced
    
    
    resize_advanced(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResizeAdvancedInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_resize_advanced_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersResizeAdvancedRequest
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

Resizes the managed instance group with advanced configuration options like disabling creation retries. This is an extended version of theresize method.

If you increase the size of the instance group, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating,creatingWithoutRetries, or deleting actions with the get orlistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resize_advanced():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResizeAdvancedInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resize_advanced](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resize_advanced)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ResizeAdvanced. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_resize_advanced_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersResizeAdvancedRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersResizeAdvancedRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_resize_advanced_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resize_advanced_unary
    
    
    resize_advanced_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResizeAdvancedInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_resize_advanced_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersResizeAdvancedRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Resizes the managed instance group with advanced configuration options like disabling creation retries. This is an extended version of theresize method.

If you increase the size of the instance group, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating,creatingWithoutRetries, or deleting actions with the get orlistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resize_advanced():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResizeAdvancedInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resize_advanced](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resize_advanced)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeAdvancedInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ResizeAdvanced. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_resize_advanced_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersResizeAdvancedRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersResizeAdvancedRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_resize_advanced_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resize_unary
    
    
    resize_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResizeInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

  * The status of the VM instance.
  * The health of the VM instance.
  * The instance template version the VM is based on.
  * For regional managed instance groups, the location of the VM instance.



This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resize():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            size=443,
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resize](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resize)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResizeInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Resize. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`size` |  `int`   
The number of running instances that the managed instance group should maintain at any given time. The group automatically adds or removes instances to maintain the number of instances specified by this parameter. This corresponds to the `size` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resume_instances
    
    
    resume_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResumeInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_resume_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersResumeInstancesRequest
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

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resume_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resume_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resume_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ResumeInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_resume_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersResumeInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersResumeInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_resume_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resume_instances_unary
    
    
    resume_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResumeInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_resume_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersResumeInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resume_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resume_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_resume_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.ResumeInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_resume_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersResumeInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersResumeInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_resume_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_auto_healing_policies
    
    
    set_auto_healing_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetAutoHealingPoliciesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_auto_healing_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetAutoHealingRequest
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

Motifies the autohealing policy for the instances in this managed instance group. [Deprecated] This method is deprecated. UseinstanceGroupManagers.patch instead.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_auto_healing_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetAutoHealingPoliciesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_auto_healing_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_auto_healing_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetAutoHealingPolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_auto_healing_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetAutoHealingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetAutoHealingRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_auto_healing_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_auto_healing_policies_unary
    
    
    set_auto_healing_policies_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetAutoHealingPoliciesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_auto_healing_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetAutoHealingRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Motifies the autohealing policy for the instances in this managed instance group. [Deprecated] This method is deprecated. UseinstanceGroupManagers.patch instead.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_auto_healing_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetAutoHealingPoliciesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_auto_healing_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_auto_healing_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetAutoHealingPoliciesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetAutoHealingPolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_auto_healing_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetAutoHealingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetAutoHealingRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_auto_healing_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_instance_template
    
    
    set_instance_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetInstanceTemplateInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_instance_template_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetInstanceTemplateRequest
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

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_instance_template():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_instance_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_instance_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetInstanceTemplate. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_instance_template_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetInstanceTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetInstanceTemplateRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_instance_template_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_instance_template_unary
    
    
    set_instance_template_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetInstanceTemplateInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_instance_template_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetInstanceTemplateRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_instance_template():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_instance_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_instance_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetInstanceTemplateInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetInstanceTemplate. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_instance_template_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetInstanceTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetInstanceTemplateRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_instance_template_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_target_pools
    
    
    set_target_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetTargetPoolsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_target_pools_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetTargetPoolsRequest
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

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_target_pools():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_target_pools](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_target_pools)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetTargetPools. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_target_pools_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetTargetPoolsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetTargetPoolsRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_target_pools_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_target_pools_unary
    
    
    set_target_pools_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetTargetPoolsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_set_target_pools_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSetTargetPoolsRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_target_pools():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_target_pools](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_set_target_pools)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTargetPoolsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SetTargetPools. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_set_target_pools_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSetTargetPoolsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSetTargetPoolsRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_set_target_pools_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start_instances
    
    
    start_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_start_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersStartInstancesRequest
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

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_start_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.StartInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_start_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersStartInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersStartInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_start_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start_instances_unary
    
    
    start_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_start_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersStartInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_start_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.StartInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_start_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersStartInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersStartInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_start_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### stop_instances
    
    
    stop_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StopInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_stop_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersStopInstancesRequest
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

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_stop_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[stop_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_stop_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.StopInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_stop_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersStopInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersStopInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_stop_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### stop_instances_unary
    
    
    stop_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StopInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_stop_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersStopInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_stop_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[stop_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_stop_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.StopInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_stop_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersStopInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersStopInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_stop_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### suspend_instances
    
    
    suspend_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SuspendInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_suspend_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSuspendInstancesRequest
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

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_suspend_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[suspend_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_suspend_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SuspendInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_suspend_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSuspendInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSuspendInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_suspend_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### suspend_instances_unary
    
    
    suspend_instances_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SuspendInstancesInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_suspend_instances_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersSuspendInstancesRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_suspend_instances():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[suspend_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_suspend_instances)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstancesInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.SuspendInstances. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_suspend_instances_request_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersSuspendInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersSuspendInstancesRequest)`   
The body resource for this request This corresponds to the `instance_group_managers_suspend_instances_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.TestIamPermissionsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        test_permissions_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.TestPermissionsRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.TestPermissionsResponse

Returns permissions that a caller has on the specified resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_test_iam_permissions():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[TestIamPermissionsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsInstanceGroupManagerRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.TestIamPermissionsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.TestIamPermissions. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`test_permissions_request_resource` |  `[google.cloud.compute_v1beta.types.TestPermissionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestPermissionsRequest)`   
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
                google.cloud.compute_v1beta.types.compute.UpdateInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
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

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is updated even if the instances in the group have not yet been updated. You must separately verify the status of the individual instances with thelistManagedInstances method.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_per_instance_configs
    
    
    update_per_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_update_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersUpdatePerInstanceConfigsReq
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

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_update_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.UpdatePerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_update_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersUpdatePerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersUpdatePerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_update_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_per_instance_configs_unary
    
    
    update_per_instance_configs_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_managers_update_per_instance_configs_req_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersUpdatePerInstanceConfigsReq
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_per_instance_configs():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_per_instance_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_update_per_instance_configs)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdatePerInstanceConfigsInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.UpdatePerInstanceConfigs. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of thezone where the managed instance group is located. It should conform to RFC1035. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the managed instance group. It should conform to RFC1035. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_managers_update_per_instance_configs_req_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManagersUpdatePerInstanceConfigsReq](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersUpdatePerInstanceConfigsReq)`   
The body resource for this request This corresponds to the `instance_group_managers_update_per_instance_configs_req_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.UpdateInstanceGroupManagerRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_group_manager: typing.Optional[str] = None,
        instance_group_manager_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstanceGroupManager
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is updated even if the instances in the group have not yet been updated. You must separately verify the status of the individual instances with thelistManagedInstances method.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstanceGroupManagersClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest.html)(
            instance_group_manager="instance_group_manager_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.InstanceGroupManagersClient.html#google_cloud_compute_v1beta_services_instance_group_managers_InstanceGroupManagersClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceGroupManagerRequest), dict]`   
The request object. A request message for InstanceGroupManagers.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone where you want to create the managed instance group. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager` |  `str`   
The name of the instance group manager. This corresponds to the `instance_group_manager` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_group_manager_resource` |  `[google.cloud.compute_v1beta.types.InstanceGroupManager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManager)`   
The body resource for this request This corresponds to the `instance_group_manager_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
