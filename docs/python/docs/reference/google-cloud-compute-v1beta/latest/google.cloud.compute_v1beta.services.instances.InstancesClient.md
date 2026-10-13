---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient
title: Class InstancesClient (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:19:47.016765+00:00
---

# Class InstancesClient (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstancesClient (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    InstancesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.instances.transports.base.InstancesTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.instances.transports.base.InstancesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Instances API.

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
`InstancesTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### InstancesClient
    
    
    InstancesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.instances.transports.base.InstancesTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.instances.transports.base.InstancesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the instances client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,InstancesTransport,Callable[..., InstancesTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the InstancesTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### add_access_config
    
    
    add_access_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        access_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AccessConfig
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

Adds an access config to an instance's network interface.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.AddAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface to add to this instance. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config_resource` |  `[google.cloud.compute_v1beta.types.AccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AccessConfig)`   
The body resource for this request This corresponds to the `access_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_access_config_unary
    
    
    add_access_config_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        access_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AccessConfig
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

Adds an access config to an instance's network interface.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.AddAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface to add to this instance. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config_resource` |  `[google.cloud.compute_v1beta.types.AccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AccessConfig)`   
The body resource for this request This corresponds to the `access_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_network_interface
    
    
    add_network_interface(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.NetworkInterface
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

Adds one dynamic network interface to an active instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.AddNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_resource` |  `[google.cloud.compute_v1beta.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkInterface)`   
The body resource for this request This corresponds to the `network_interface_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_network_interface_unary
    
    
    add_network_interface_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.NetworkInterface
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

Adds one dynamic network interface to an active instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.AddNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_resource` |  `[google.cloud.compute_v1beta.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkInterface)`   
The body resource for this request This corresponds to the `network_interface_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_resource_policies
    
    
    add_resource_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddResourcePoliciesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_add_resource_policies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesAddResourcePoliciesRequest
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

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_resource_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_resource_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_resource_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest), dict]`   
The request object. A request message for Instances.AddResourcePolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_add_resource_policies_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesAddResourcePoliciesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesAddResourcePoliciesRequest)`   
The body resource for this request This corresponds to the `instances_add_resource_policies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_resource_policies_unary
    
    
    add_resource_policies_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddResourcePoliciesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_add_resource_policies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesAddResourcePoliciesRequest
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

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_resource_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[add_resource_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_add_resource_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddResourcePoliciesInstanceRequest), dict]`   
The request object. A request message for Instances.AddResourcePolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_add_resource_policies_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesAddResourcePoliciesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesAddResourcePoliciesRequest)`   
The body resource for this request This corresponds to the `instances_add_resource_policies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.AggregatedListInstancesRequest,
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
    ) -> google.cloud.compute_v1beta.services.instances.pagers.AggregatedListPager

Retrieves an aggregated list of all of the instances in your project across all regions and zones.

The performance of this method degrades when a filter is specified on a project that has a very large number of instances.

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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AggregatedListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListInstancesRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[aggregated_list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_aggregated_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AggregatedListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListInstancesRequest), dict]`   
The request object. A request message for Instances.AggregatedList. See the method description for details.  
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
`[google.cloud.compute_v1beta.services.instances.pagers.AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.pagers.AggregatedListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
### attach_disk
    
    
    attach_disk(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AttachDiskInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        attached_disk_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AttachedDisk
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

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_attach_disk():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AttachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachDiskInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[attach_disk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_attach_disk)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AttachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachDiskInstanceRequest), dict]`   
The request object. A request message for Instances.AttachDisk. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`attached_disk_resource` |  `[google.cloud.compute_v1beta.types.AttachedDisk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachedDisk)`   
The body resource for this request This corresponds to the `attached_disk_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### attach_disk_unary
    
    
    attach_disk_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AttachDiskInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        attached_disk_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AttachedDisk
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

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_attach_disk():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AttachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachDiskInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[attach_disk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_attach_disk)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AttachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachDiskInstanceRequest), dict]`   
The request object. A request message for Instances.AttachDisk. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`attached_disk_resource` |  `[google.cloud.compute_v1beta.types.AttachedDisk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AttachedDisk)`   
The body resource for this request This corresponds to the `attached_disk_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### bulk_insert
    
    
    bulk_insert(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.BulkInsertInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        bulk_insert_instance_resource_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BulkInsertInstanceResource
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

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_bulk_insert():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BulkInsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[bulk_insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_bulk_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.BulkInsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceRequest), dict]`   
The request object. A request message for Instances.BulkInsert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`bulk_insert_instance_resource_resource` |  `[google.cloud.compute_v1beta.types.BulkInsertInstanceResource](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceResource)`   
The body resource for this request This corresponds to the `bulk_insert_instance_resource_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### bulk_insert_unary
    
    
    bulk_insert_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.BulkInsertInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        bulk_insert_instance_resource_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BulkInsertInstanceResource
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

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_bulk_insert():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BulkInsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[bulk_insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_bulk_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.BulkInsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceRequest), dict]`   
The request object. A request message for Instances.BulkInsert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`bulk_insert_instance_resource_resource` |  `[google.cloud.compute_v1beta.types.BulkInsertInstanceResource](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BulkInsertInstanceResource)`   
The body resource for this request This corresponds to the `bulk_insert_instance_resource_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.DeleteInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified Instance resource. For more information, seeDeleting an instance.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceRequest), dict]`   
The request object. A request message for Instances.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to delete. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_access_config
    
    
    delete_access_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        access_config: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes an access config from an instance's network interface.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest.html)(
            access_config="access_config_value",
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.DeleteAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config` |  `str`   
The name of the access config to delete. This corresponds to the `access_config` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_access_config_unary
    
    
    delete_access_config_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        access_config: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes an access config from an instance's network interface.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest.html)(
            access_config="access_config_value",
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.DeleteAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config` |  `str`   
The name of the access config to delete. This corresponds to the `access_config` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_network_interface
    
    
    delete_network_interface(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates:

  * instance from which to delete, using project+zone+resource_id fields;
  * dynamic network interface to be deleted, using network_interface_name field;


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            network_interface_name="network_interface_name_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.DeleteNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_name` |  `str`   
The name of the dynamic network interface to be deleted from the instance. This corresponds to the `network_interface_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_network_interface_unary
    
    
    delete_network_interface_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates:

  * instance from which to delete, using project+zone+resource_id fields;
  * dynamic network interface to be deleted, using network_interface_name field;


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            network_interface_name="network_interface_name_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.DeleteNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_name` |  `str`   
The name of the dynamic network interface to be deleted from the instance. This corresponds to the `network_interface_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.DeleteInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes the specified Instance resource. For more information, seeDeleting an instance.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteInstanceRequest), dict]`   
The request object. A request message for Instances.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to delete. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### detach_disk
    
    
    detach_disk(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DetachDiskInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Detaches a disk from an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_detach_disk():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DetachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DetachDiskInstanceRequest.html)(
            device_name="device_name_value",
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[detach_disk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_detach_disk)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DetachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DetachDiskInstanceRequest), dict]`   
The request object. A request message for Instances.DetachDisk. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`device_name` |  `str`   
The device name of the disk to detach. Make a get() request on the instance to view currently attached disks and device names. This corresponds to the `device_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### detach_disk_unary
    
    
    detach_disk_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DetachDiskInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Detaches a disk from an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_detach_disk():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DetachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DetachDiskInstanceRequest.html)(
            device_name="device_name_value",
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[detach_disk](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_detach_disk)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DetachDiskInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DetachDiskInstanceRequest), dict]`   
The request object. A request message for Instances.DetachDisk. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`device_name` |  `str`   
The device name of the disk to detach. Make a get() request on the instance to view currently attached disks and device names. This corresponds to the `device_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`InstancesClient` | The constructed client.  
  
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
`InstancesClient` | The constructed client.  
  
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
`InstancesClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[google.cloud.compute_v1beta.types.compute.GetInstanceRequest, dict]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Instance

Returns the specified Instance resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetInstanceRequest), dict]`   
The request object. A request message for Instances.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to return. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Instance)` | Represents an Instance resource. An instance is a virtual machine that is hosted on Google Cloud Platform. For more information, readVirtual Machine Instances.  
  
### get_effective_firewalls
    
    
    get_effective_firewalls(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetEffectiveFirewallsInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.InstancesGetEffectiveFirewallsResponse

Returns effective firewalls applied to an interface of the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_effective_firewalls():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetEffectiveFirewallsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetEffectiveFirewallsInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_effective_firewalls](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_effective_firewalls)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetEffectiveFirewallsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetEffectiveFirewallsInstanceRequest), dict]`   
The request object. A request message for Instances.GetEffectiveFirewalls. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface to get the effective firewalls. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### get_guest_attributes
    
    
    get_guest_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetGuestAttributesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.GuestAttributes

Returns the specified guest attributes entry.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_guest_attributes():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetGuestAttributesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetGuestAttributesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_guest_attributes](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_guest_attributes)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetGuestAttributesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetGuestAttributesInstanceRequest), dict]`   
The request object. A request message for Instances.GetGuestAttributes. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.GuestAttributes](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GuestAttributes)` | A guest attributes entry.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetIamPolicyInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Policy

Gets the access control policy for a resource. May be empty if no such policy or resource exists.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_iam_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetIamPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetIamPolicyInstanceRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetIamPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetIamPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.GetIamPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Policy)` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
  
### get_partner_metadata
    
    
    get_partner_metadata(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetPartnerMetadataInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.PartnerMetadata

Gets partner metadata of the specified instance and namespaces.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_partner_metadata():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetPartnerMetadataInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_partner_metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_partner_metadata)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetPartnerMetadataInstanceRequest), dict]`   
The request object. A request message for Instances.GetPartnerMetadata. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.PartnerMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PartnerMetadata)` | Model definition of partner_metadata field. To be used in dedicated Partner Metadata methods and to be inlined in the Instance and InstanceTemplate resources.  
  
### get_screenshot
    
    
    get_screenshot(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetScreenshotInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Screenshot

Returns the screenshot from the specified instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_screenshot():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetScreenshotInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetScreenshotInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_screenshot](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_screenshot)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetScreenshotInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetScreenshotInstanceRequest), dict]`   
The request object. A request message for Instances.GetScreenshot. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Screenshot](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Screenshot)` | An instance's screenshot.  
  
### get_serial_port_output
    
    
    get_serial_port_output(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetSerialPortOutputInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.SerialPortOutput

Returns the last 1 MB of serial port output from the specified instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_serial_port_output():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetSerialPortOutputInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetSerialPortOutputInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_serial_port_output](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_serial_port_output)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetSerialPortOutputInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetSerialPortOutputInstanceRequest), dict]`   
The request object. A request message for Instances.GetSerialPortOutput. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.SerialPortOutput](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SerialPortOutput)` | An instance serial console output.  
  
### get_shielded_instance_identity
    
    
    get_shielded_instance_identity(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetShieldedInstanceIdentityInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.ShieldedInstanceIdentity

Returns the Shielded Instance Identity of an instance
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_shielded_instance_identity():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetShieldedInstanceIdentityInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetShieldedInstanceIdentityInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_shielded_instance_identity](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_shielded_instance_identity)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetShieldedInstanceIdentityInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetShieldedInstanceIdentityInstanceRequest), dict]`   
The request object. A request message for Instances.GetShieldedInstanceIdentity. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.ShieldedInstanceIdentity](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedInstanceIdentity)` | A Shielded Instance Identity.  
  
### get_shielded_vm_identity
    
    
    get_shielded_vm_identity(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetShieldedVmIdentityInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.ShieldedVmIdentity

Returns the Shielded VM Identity of an instance
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_shielded_vm_identity():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetShieldedVmIdentityInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetShieldedVmIdentityInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_shielded_vm_identity](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_shielded_vm_identity)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetShieldedVmIdentityInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetShieldedVmIdentityInstanceRequest), dict]`   
The request object. A request message for Instances.GetShieldedVmIdentity. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.ShieldedVmIdentity](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedVmIdentity)` | A Shielded VM Identity.  
  
### get_vm_extension_state
    
    
    get_vm_extension_state(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetVmExtensionStateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        extension_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.VmExtensionState

Retrieves details of a specific VM extension state. This is a read-only API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_vm_extension_state():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetVmExtensionStateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetVmExtensionStateInstanceRequest.html)(
            extension_name="extension_name_value",
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[get_vm_extension_state](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_get_vm_extension_state)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetVmExtensionStateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetVmExtensionStateInstanceRequest), dict]`   
The request object. A request message for Instances.GetVmExtensionState. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
Name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance resource. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`extension_name` |  `str`   
The name of the extension to get the state for. This corresponds to the `extension_name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.VmExtensionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.VmExtensionState)` | State of an extension on an instance.  
  
### insert
    
    
    insert(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.InsertInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Instance
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

Creates an instance resource in the specified project using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceRequest), dict]`   
The request object. A request message for Instances.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_resource` |  `[google.cloud.compute_v1beta.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Instance)`   
The body resource for this request This corresponds to the `instance_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.InsertInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Instance
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

Creates an instance resource in the specified project using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertInstanceRequest), dict]`   
The request object. A request message for Instances.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_resource` |  `[google.cloud.compute_v1beta.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Instance)`   
The body resource for this request This corresponds to the `instance_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.ListInstancesRequest, dict
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
    ) -> google.cloud.compute_v1beta.services.instances.pagers.ListPager

Retrieves the list of instances contained within the specified zone.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListInstancesRequest.html)(
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListInstancesRequest), dict]`   
The request object. A request message for Instances.List. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instances.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.pagers.ListPager)` | Contains a list of instances. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_referrers
    
    
    list_referrers(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListReferrersInstancesRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.services.instances.pagers.ListReferrersPager

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_referrers():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListReferrersInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListReferrersInstancesRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_referrers](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_list_referrers)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListReferrersInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListReferrersInstancesRequest), dict]`   
The request object. A request message for Instances.ListReferrers. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the target instance scoping this request, or '-' if the request should span over all instances in the container. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instances.pagers.ListReferrersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.pagers.ListReferrersPager)` | Contains a list of instance referrers. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_vm_extension_states
    
    
    list_vm_extension_states(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListVmExtensionStatesInstancesRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.services.instances.pagers.ListVmExtensionStatesPager

Lists all VM extensions states for a specific instance. This is a read-only API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_vm_extension_states():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListVmExtensionStatesInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListVmExtensionStatesInstancesRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        page_result = client.[list_vm_extension_states](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_list_vm_extension_states)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListVmExtensionStatesInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListVmExtensionStatesInstancesRequest), dict]`   
The request object. A request message for Instances.ListVmExtensionStates. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
Required. Name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the target instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.instances.pagers.ListVmExtensionStatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.pagers.ListVmExtensionStatesPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### patch_partner_metadata
    
    
    patch_partner_metadata(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchPartnerMetadataInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        partner_metadata_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.PartnerMetadata
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

Patches partner metadata of the specified instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch_partner_metadata():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch_partner_metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_patch_partner_metadata)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest), dict]`   
The request object. A request message for Instances.PatchPartnerMetadata. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`partner_metadata_resource` |  `[google.cloud.compute_v1beta.types.PartnerMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PartnerMetadata)`   
The body resource for this request This corresponds to the `partner_metadata_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### patch_partner_metadata_unary
    
    
    patch_partner_metadata_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchPartnerMetadataInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        partner_metadata_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.PartnerMetadata
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

Patches partner metadata of the specified instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch_partner_metadata():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[patch_partner_metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_patch_partner_metadata)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchPartnerMetadataInstanceRequest), dict]`   
The request object. A request message for Instances.PatchPartnerMetadata. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`partner_metadata_resource` |  `[google.cloud.compute_v1beta.types.PartnerMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PartnerMetadata)`   
The body resource for this request This corresponds to the `partner_metadata_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### perform_maintenance
    
    
    perform_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PerformMaintenanceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Perform a manual maintenance on the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_perform_maintenance():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[perform_maintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_perform_maintenance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest), dict]`   
The request object. A request message for Instances.PerformMaintenance. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### perform_maintenance_unary
    
    
    perform_maintenance_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PerformMaintenanceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Perform a manual maintenance on the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_perform_maintenance():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[perform_maintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_perform_maintenance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PerformMaintenanceInstanceRequest), dict]`   
The request object. A request message for Instances.PerformMaintenance. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### remove_resource_policies
    
    
    remove_resource_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.RemoveResourcePoliciesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_remove_resource_policies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesRemoveResourcePoliciesRequest
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

Removes resource policies from an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_remove_resource_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[remove_resource_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_remove_resource_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest), dict]`   
The request object. A request message for Instances.RemoveResourcePolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_remove_resource_policies_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesRemoveResourcePoliciesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesRemoveResourcePoliciesRequest)`   
The body resource for this request This corresponds to the `instances_remove_resource_policies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### remove_resource_policies_unary
    
    
    remove_resource_policies_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.RemoveResourcePoliciesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_remove_resource_policies_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesRemoveResourcePoliciesRequest
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

Removes resource policies from an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_remove_resource_policies():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[remove_resource_policies](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_remove_resource_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RemoveResourcePoliciesInstanceRequest), dict]`   
The request object. A request message for Instances.RemoveResourcePolicies. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_remove_resource_policies_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesRemoveResourcePoliciesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesRemoveResourcePoliciesRequest)`   
The body resource for this request This corresponds to the `instances_remove_resource_policies_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### report_host_as_faulty
    
    
    report_host_as_faulty(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ReportHostAsFaultyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_report_host_as_faulty_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesReportHostAsFaultyRequest
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

Mark the host as faulty and try to restart the instance on a new host.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_report_host_as_faulty():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[report_host_as_faulty](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_report_host_as_faulty)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest), dict]`   
The request object. A request message for Instances.ReportHostAsFaulty. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_report_host_as_faulty_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesReportHostAsFaultyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesReportHostAsFaultyRequest)`   
The body resource for this request This corresponds to the `instances_report_host_as_faulty_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### report_host_as_faulty_unary
    
    
    report_host_as_faulty_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ReportHostAsFaultyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_report_host_as_faulty_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesReportHostAsFaultyRequest
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

Mark the host as faulty and try to restart the instance on a new host.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_report_host_as_faulty():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[report_host_as_faulty](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_report_host_as_faulty)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ReportHostAsFaultyInstanceRequest), dict]`   
The request object. A request message for Instances.ReportHostAsFaulty. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_report_host_as_faulty_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesReportHostAsFaultyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesReportHostAsFaultyRequest)`   
The body resource for this request This corresponds to the `instances_report_host_as_faulty_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### reset
    
    
    reset(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResetInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_reset():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResetInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[reset](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_reset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResetInstanceRequest), dict]`   
The request object. A request message for Instances.Reset. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### reset_unary
    
    
    reset_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResetInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_reset():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResetInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[reset](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_reset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResetInstanceRequest), dict]`   
The request object. A request message for Instances.Reset. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resume
    
    
    resume(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResumeInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Resumes an instance that was suspended using theinstances().suspend method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resume():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResumeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resume](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_resume)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResumeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstanceRequest), dict]`   
The request object. A request message for Instances.Resume. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to resume. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### resume_unary
    
    
    resume_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ResumeInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Resumes an instance that was suspended using theinstances().suspend method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_resume():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ResumeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[resume](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_resume)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ResumeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ResumeInstanceRequest), dict]`   
The request object. A request message for Instances.Resume. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to resume. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### send_diagnostic_interrupt
    
    
    send_diagnostic_interrupt(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SendDiagnosticInterruptInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.SendDiagnosticInterruptInstanceResponse

Sends diagnostic interrupt to the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_send_diagnostic_interrupt():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SendDiagnosticInterruptInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SendDiagnosticInterruptInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[send_diagnostic_interrupt](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_send_diagnostic_interrupt)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SendDiagnosticInterruptInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SendDiagnosticInterruptInstanceRequest), dict]`   
The request object. A request message for Instances.SendDiagnosticInterrupt. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.SendDiagnosticInterruptInstanceResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SendDiagnosticInterruptInstanceResponse)` | A response message for Instances.SendDiagnosticInterrupt. See the method description for details.  
  
### set_deletion_protection
    
    
    set_deletion_protection(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetDeletionProtectionInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Sets deletion protection on the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_deletion_protection():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_deletion_protection](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_deletion_protection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest), dict]`   
The request object. A request message for Instances.SetDeletionProtection. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_deletion_protection_unary
    
    
    set_deletion_protection_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetDeletionProtectionInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Sets deletion protection on the instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_deletion_protection():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_deletion_protection](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_deletion_protection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDeletionProtectionInstanceRequest), dict]`   
The request object. A request message for Instances.SetDeletionProtection. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_disk_auto_delete
    
    
    set_disk_auto_delete(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetDiskAutoDeleteInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        auto_delete: typing.Optional[bool] = None,
        device_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Sets the auto-delete flag for a disk attached to an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_disk_auto_delete():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest.html)(
            auto_delete=True,
            device_name="device_name_value",
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_disk_auto_delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_disk_auto_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest), dict]`   
The request object. A request message for Instances.SetDiskAutoDelete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`auto_delete` |  `bool`   
Whether to auto-delete the disk when the instance is deleted. This corresponds to the `auto_delete` field on the `request` instance; if `request` is provided, this should not be set.  
`device_name` |  `str`   
The device name of the disk to modify. Make a get() request on the instance to view currently attached disks and device names. This corresponds to the `device_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_disk_auto_delete_unary
    
    
    set_disk_auto_delete_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetDiskAutoDeleteInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        auto_delete: typing.Optional[bool] = None,
        device_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Sets the auto-delete flag for a disk attached to an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_disk_auto_delete():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest.html)(
            auto_delete=True,
            device_name="device_name_value",
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_disk_auto_delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_disk_auto_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetDiskAutoDeleteInstanceRequest), dict]`   
The request object. A request message for Instances.SetDiskAutoDelete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`auto_delete` |  `bool`   
Whether to auto-delete the disk when the instance is deleted. This corresponds to the `auto_delete` field on the `request` instance; if `request` is provided, this should not be set.  
`device_name` |  `str`   
The device name of the disk to modify. Make a get() request on the instance to view currently attached disks and device names. This corresponds to the `device_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetIamPolicyInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        zone_set_policy_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ZoneSetPolicyRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Policy

Sets the access control policy on the specified resource. Replaces any existing policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_iam_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetIamPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetIamPolicyInstanceRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetIamPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetIamPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetIamPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`zone_set_policy_request_resource` |  `[google.cloud.compute_v1beta.types.ZoneSetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ZoneSetPolicyRequest)`   
The body resource for this request This corresponds to the `zone_set_policy_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Policy)` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### set_labels
    
    
    set_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetLabelsInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_labels_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetLabelsRequest
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

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_labels():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetLabelsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_labels](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_labels)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetLabelsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsInstanceRequest), dict]`   
The request object. A request message for Instances.SetLabels. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_labels_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetLabelsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetLabelsRequest)`   
The body resource for this request This corresponds to the `instances_set_labels_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_labels_unary
    
    
    set_labels_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetLabelsInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_labels_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetLabelsRequest
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

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_labels():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetLabelsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_labels](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_labels)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetLabelsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsInstanceRequest), dict]`   
The request object. A request message for Instances.SetLabels. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_labels_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetLabelsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetLabelsRequest)`   
The body resource for this request This corresponds to the `instances_set_labels_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_machine_resources
    
    
    set_machine_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMachineResourcesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_machine_resources_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMachineResourcesRequest
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

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_machine_resources():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_machine_resources](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_machine_resources)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest), dict]`   
The request object. A request message for Instances.SetMachineResources. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_machine_resources_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMachineResourcesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMachineResourcesRequest)`   
The body resource for this request This corresponds to the `instances_set_machine_resources_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_machine_resources_unary
    
    
    set_machine_resources_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMachineResourcesInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_machine_resources_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMachineResourcesRequest
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

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_machine_resources():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_machine_resources](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_machine_resources)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineResourcesInstanceRequest), dict]`   
The request object. A request message for Instances.SetMachineResources. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_machine_resources_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMachineResourcesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMachineResourcesRequest)`   
The body resource for this request This corresponds to the `instances_set_machine_resources_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_machine_type
    
    
    set_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMachineTypeInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_machine_type_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMachineTypeRequest
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

Changes the machine type for a stopped instance to the machine type specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_machine_type():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_machine_type](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_machine_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest), dict]`   
The request object. A request message for Instances.SetMachineType. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_machine_type_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMachineTypeRequest)`   
The body resource for this request This corresponds to the `instances_set_machine_type_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_machine_type_unary
    
    
    set_machine_type_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMachineTypeInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_machine_type_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMachineTypeRequest
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

Changes the machine type for a stopped instance to the machine type specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_machine_type():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_machine_type](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_machine_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMachineTypeInstanceRequest), dict]`   
The request object. A request message for Instances.SetMachineType. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_machine_type_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMachineTypeRequest)`   
The body resource for this request This corresponds to the `instances_set_machine_type_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_metadata
    
    
    set_metadata(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMetadataInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        metadata_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Metadata
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

Sets metadata for the specified instance to the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_metadata():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMetadataInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_metadata)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMetadataInstanceRequest), dict]`   
The request object. A request message for Instances.SetMetadata. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`metadata_resource` |  `[google.cloud.compute_v1beta.types.Metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Metadata)`   
The body resource for this request This corresponds to the `metadata_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_metadata_unary
    
    
    set_metadata_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMetadataInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        metadata_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Metadata
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

Sets metadata for the specified instance to the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_metadata():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMetadataInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_metadata)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMetadataInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMetadataInstanceRequest), dict]`   
The request object. A request message for Instances.SetMetadata. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`metadata_resource` |  `[google.cloud.compute_v1beta.types.Metadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Metadata)`   
The body resource for this request This corresponds to the `metadata_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_min_cpu_platform
    
    
    set_min_cpu_platform(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMinCpuPlatformInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_min_cpu_platform_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMinCpuPlatformRequest
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

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_min_cpu_platform():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_min_cpu_platform](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_min_cpu_platform)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest), dict]`   
The request object. A request message for Instances.SetMinCpuPlatform. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_min_cpu_platform_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMinCpuPlatformRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMinCpuPlatformRequest)`   
The body resource for this request This corresponds to the `instances_set_min_cpu_platform_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_min_cpu_platform_unary
    
    
    set_min_cpu_platform_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetMinCpuPlatformInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_min_cpu_platform_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetMinCpuPlatformRequest
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

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_min_cpu_platform():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_min_cpu_platform](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_min_cpu_platform)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetMinCpuPlatformInstanceRequest), dict]`   
The request object. A request message for Instances.SetMinCpuPlatform. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_min_cpu_platform_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetMinCpuPlatformRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetMinCpuPlatformRequest)`   
The body resource for this request This corresponds to the `instances_set_min_cpu_platform_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_name
    
    
    set_name(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetNameInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_name_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetNameRequest
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

Sets name of an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_name():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetNameInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetNameInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_name](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_name)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetNameInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetNameInstanceRequest), dict]`   
The request object. A request message for Instances.SetName. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_name_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetNameRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetNameRequest)`   
The body resource for this request This corresponds to the `instances_set_name_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_name_unary
    
    
    set_name_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetNameInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_name_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetNameRequest
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

Sets name of an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_name():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetNameInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetNameInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_name](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_name)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetNameInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetNameInstanceRequest), dict]`   
The request object. A request message for Instances.SetName. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_name_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetNameRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetNameRequest)`   
The body resource for this request This corresponds to the `instances_set_name_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_scheduling
    
    
    set_scheduling(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetSchedulingInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        scheduling_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Scheduling
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

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_scheduling():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetSchedulingInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_scheduling](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_scheduling)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest), dict]`   
The request object. A request message for Instances.SetScheduling. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`scheduling_resource` |  `[google.cloud.compute_v1beta.types.Scheduling](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Scheduling)`   
The body resource for this request This corresponds to the `scheduling_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_scheduling_unary
    
    
    set_scheduling_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetSchedulingInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        scheduling_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Scheduling
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

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_scheduling():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetSchedulingInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_scheduling](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_scheduling)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSchedulingInstanceRequest), dict]`   
The request object. A request message for Instances.SetScheduling. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`scheduling_resource` |  `[google.cloud.compute_v1beta.types.Scheduling](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Scheduling)`   
The body resource for this request This corresponds to the `scheduling_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_security_policy
    
    
    set_security_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetSecurityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_security_policy_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetSecurityPolicyRequest
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

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_security_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_security_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_security_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetSecurityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
Name of the zone scoping this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the Instance resource to which the security policy should be set. The name should conform to RFC1035. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_security_policy_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetSecurityPolicyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetSecurityPolicyRequest)`   
The body resource for this request This corresponds to the `instances_set_security_policy_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_security_policy_unary
    
    
    set_security_policy_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetSecurityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_security_policy_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetSecurityPolicyRequest
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

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_security_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_security_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_security_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetSecurityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetSecurityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
Name of the zone scoping this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the Instance resource to which the security policy should be set. The name should conform to RFC1035. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_security_policy_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetSecurityPolicyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetSecurityPolicyRequest)`   
The body resource for this request This corresponds to the `instances_set_security_policy_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_service_account
    
    
    set_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetServiceAccountInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_service_account_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetServiceAccountRequest
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

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_service_account():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_service_account](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest), dict]`   
The request object. A request message for Instances.SetServiceAccount. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_service_account_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetServiceAccountRequest)`   
The body resource for this request This corresponds to the `instances_set_service_account_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_service_account_unary
    
    
    set_service_account_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetServiceAccountInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_set_service_account_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesSetServiceAccountRequest
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

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_service_account():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_service_account](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetServiceAccountInstanceRequest), dict]`   
The request object. A request message for Instances.SetServiceAccount. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_set_service_account_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesSetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesSetServiceAccountRequest)`   
The body resource for this request This corresponds to the `instances_set_service_account_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_shielded_instance_integrity_policy
    
    
    set_shielded_instance_integrity_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetShieldedInstanceIntegrityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_instance_integrity_policy_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedInstanceIntegrityPolicy
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

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_shielded_instance_integrity_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_shielded_instance_integrity_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_shielded_instance_integrity_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetShieldedInstanceIntegrityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_instance_integrity_policy_resource` |  `[google.cloud.compute_v1beta.types.ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedInstanceIntegrityPolicy)`   
The body resource for this request This corresponds to the `shielded_instance_integrity_policy_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_shielded_instance_integrity_policy_unary
    
    
    set_shielded_instance_integrity_policy_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetShieldedInstanceIntegrityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_instance_integrity_policy_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedInstanceIntegrityPolicy
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

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_shielded_instance_integrity_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_shielded_instance_integrity_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_shielded_instance_integrity_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedInstanceIntegrityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetShieldedInstanceIntegrityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_instance_integrity_policy_resource` |  `[google.cloud.compute_v1beta.types.ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedInstanceIntegrityPolicy)`   
The body resource for this request This corresponds to the `shielded_instance_integrity_policy_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_shielded_vm_integrity_policy
    
    
    set_shielded_vm_integrity_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetShieldedVmIntegrityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_vm_integrity_policy_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedVmIntegrityPolicy
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

Sets the Shielded VM integrity policy for a VM instance. You can only use this method on a running VM instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_shielded_vm_integrity_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetShieldedVmIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_shielded_vm_integrity_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_shielded_vm_integrity_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetShieldedVmIntegrityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_vm_integrity_policy_resource` |  `[google.cloud.compute_v1beta.types.ShieldedVmIntegrityPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedVmIntegrityPolicy)`   
The body resource for this request This corresponds to the `shielded_vm_integrity_policy_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_shielded_vm_integrity_policy_unary
    
    
    set_shielded_vm_integrity_policy_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetShieldedVmIntegrityPolicyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_vm_integrity_policy_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedVmIntegrityPolicy
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

Sets the Shielded VM integrity policy for a VM instance. You can only use this method on a running VM instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_shielded_vm_integrity_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetShieldedVmIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_shielded_vm_integrity_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_shielded_vm_integrity_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetShieldedVmIntegrityPolicyInstanceRequest), dict]`   
The request object. A request message for Instances.SetShieldedVmIntegrityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_vm_integrity_policy_resource` |  `[google.cloud.compute_v1beta.types.ShieldedVmIntegrityPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedVmIntegrityPolicy)`   
The body resource for this request This corresponds to the `shielded_vm_integrity_policy_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_tags
    
    
    set_tags(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetTagsInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        tags_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Tags
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

Sets network tags for the specified instance to the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_tags():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetTagsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTagsInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_tags](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_tags)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetTagsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTagsInstanceRequest), dict]`   
The request object. A request message for Instances.SetTags. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`tags_resource` |  `[google.cloud.compute_v1beta.types.Tags](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Tags)`   
The body resource for this request This corresponds to the `tags_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_tags_unary
    
    
    set_tags_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetTagsInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        tags_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Tags
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

Sets network tags for the specified instance to the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_tags():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetTagsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTagsInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[set_tags](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_set_tags)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetTagsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetTagsInstanceRequest), dict]`   
The request object. A request message for Instances.SetTags. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`tags_resource` |  `[google.cloud.compute_v1beta.types.Tags](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Tags)`   
The body resource for this request This corresponds to the `tags_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### simulate_maintenance_event
    
    
    simulate_maintenance_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SimulateMaintenanceEventInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_simulate_maintenance_event():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[simulate_maintenance_event](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_simulate_maintenance_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest), dict]`   
The request object. A request message for Instances.SimulateMaintenanceEvent. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### simulate_maintenance_event_unary
    
    
    simulate_maintenance_event_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SimulateMaintenanceEventInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_simulate_maintenance_event():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[simulate_maintenance_event](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_simulate_maintenance_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SimulateMaintenanceEventInstanceRequest), dict]`   
The request object. A request message for Instances.SimulateMaintenanceEvent. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start
    
    
    start(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_start)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstanceRequest), dict]`   
The request object. A request message for Instances.Start. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start_unary
    
    
    start_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_start)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartInstanceRequest), dict]`   
The request object. A request message for Instances.Start. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start_with_encryption_key
    
    
    start_with_encryption_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartWithEncryptionKeyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_start_with_encryption_key_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesStartWithEncryptionKeyRequest
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

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start_with_encryption_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start_with_encryption_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_start_with_encryption_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest), dict]`   
The request object. A request message for Instances.StartWithEncryptionKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_start_with_encryption_key_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesStartWithEncryptionKeyRequest)`   
The body resource for this request This corresponds to the `instances_start_with_encryption_key_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### start_with_encryption_key_unary
    
    
    start_with_encryption_key_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StartWithEncryptionKeyInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instances_start_with_encryption_key_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.InstancesStartWithEncryptionKeyRequest
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

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_start_with_encryption_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[start_with_encryption_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_start_with_encryption_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StartWithEncryptionKeyInstanceRequest), dict]`   
The request object. A request message for Instances.StartWithEncryptionKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to start. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instances_start_with_encryption_key_request_resource` |  `[google.cloud.compute_v1beta.types.InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstancesStartWithEncryptionKeyRequest)`   
The body resource for this request This corresponds to the `instances_start_with_encryption_key_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### stop
    
    
    stop(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StopInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_stop():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[stop](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_stop)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstanceRequest), dict]`   
The request object. A request message for Instances.Stop. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to stop. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### stop_unary
    
    
    stop_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.StopInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_stop():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[stop](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_stop)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.StopInstanceRequest), dict]`   
The request object. A request message for Instances.Stop. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to stop. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### suspend
    
    
    suspend(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SuspendInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_suspend():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SuspendInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[suspend](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_suspend)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SuspendInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstanceRequest), dict]`   
The request object. A request message for Instances.Suspend. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to suspend. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### suspend_unary
    
    
    suspend_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SuspendInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_suspend():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SuspendInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[suspend](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_suspend)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SuspendInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SuspendInstanceRequest), dict]`   
The request object. A request message for Instances.Suspend. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to suspend. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.TestIamPermissionsInstanceRequest,
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[TestIamPermissionsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsInstanceRequest.html)(
            project="project_value",
            resource="resource_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.TestIamPermissionsInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsInstanceRequest), dict]`   
The request object. A request message for Instances.TestIamPermissions. See the method description for details.  
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
                google.cloud.compute_v1beta.types.compute.UpdateInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instance_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Instance
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

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceRequest), dict]`   
The request object. A request message for Instances.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to update. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_resource` |  `[google.cloud.compute_v1beta.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Instance)`   
The body resource for this request This corresponds to the `instance_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_access_config
    
    
    update_access_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        access_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AccessConfig
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

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface where the access config is attached. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config_resource` |  `[google.cloud.compute_v1beta.types.AccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AccessConfig)`   
The body resource for this request This corresponds to the `access_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_access_config_unary
    
    
    update_access_config_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateAccessConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        access_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.AccessConfig
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

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_access_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_access_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_access_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateAccessConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateAccessConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface where the access config is attached. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`access_config_resource` |  `[google.cloud.compute_v1beta.types.AccessConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AccessConfig)`   
The body resource for this request This corresponds to the `access_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_display_device
    
    
    update_display_device(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateDisplayDeviceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        display_device_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.DisplayDevice
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

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_display_device():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_display_device](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_display_device)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateDisplayDevice. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`display_device_resource` |  `[google.cloud.compute_v1beta.types.DisplayDevice](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DisplayDevice)`   
The body resource for this request This corresponds to the `display_device_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_display_device_unary
    
    
    update_display_device_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateDisplayDeviceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        display_device_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.DisplayDevice
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

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_display_device():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_display_device](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_display_device)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateDisplayDeviceInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateDisplayDevice. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`display_device_resource` |  `[google.cloud.compute_v1beta.types.DisplayDevice](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DisplayDevice)`   
The body resource for this request This corresponds to the `display_device_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_network_interface
    
    
    update_network_interface(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        network_interface_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.NetworkInterface
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

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface to update. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_resource` |  `[google.cloud.compute_v1beta.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkInterface)`   
The body resource for this request This corresponds to the `network_interface_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_network_interface_unary
    
    
    update_network_interface_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateNetworkInterfaceInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        network_interface: typing.Optional[str] = None,
        network_interface_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.NetworkInterface
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

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_network_interface():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest.html)(
            instance="instance_value",
            network_interface="network_interface_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_network_interface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_network_interface)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateNetworkInterfaceInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateNetworkInterface. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
The instance name for this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface` |  `str`   
The name of the network interface to update. This corresponds to the `network_interface` field on the `request` instance; if `request` is provided, this should not be set.  
`network_interface_resource` |  `[google.cloud.compute_v1beta.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkInterface)`   
The body resource for this request This corresponds to the `network_interface_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_shielded_instance_config
    
    
    update_shielded_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateShieldedInstanceConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_instance_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedInstanceConfig
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

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_shielded_instance_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_shielded_instance_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_shielded_instance_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateShieldedInstanceConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_instance_config_resource` |  `[google.cloud.compute_v1beta.types.ShieldedInstanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedInstanceConfig)`   
The body resource for this request This corresponds to the `shielded_instance_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_shielded_instance_config_unary
    
    
    update_shielded_instance_config_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateShieldedInstanceConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_instance_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedInstanceConfig
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

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_shielded_instance_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_shielded_instance_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_shielded_instance_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedInstanceConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateShieldedInstanceConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name or id of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_instance_config_resource` |  `[google.cloud.compute_v1beta.types.ShieldedInstanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedInstanceConfig)`   
The body resource for this request This corresponds to the `shielded_instance_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_shielded_vm_config
    
    
    update_shielded_vm_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateShieldedVmConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_vm_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedVmConfig
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

Updates the Shielded VM config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_shielded_vm_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateShieldedVmConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_shielded_vm_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_shielded_vm_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateShieldedVmConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_vm_config_resource` |  `[google.cloud.compute_v1beta.types.ShieldedVmConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedVmConfig)`   
The body resource for this request This corresponds to the `shielded_vm_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_shielded_vm_config_unary
    
    
    update_shielded_vm_config_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateShieldedVmConfigInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        shielded_vm_config_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.ShieldedVmConfig
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

Updates the Shielded VM config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update_shielded_vm_config():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateShieldedVmConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update_shielded_vm_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update_shielded_vm_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateShieldedVmConfigInstanceRequest), dict]`   
The request object. A request message for Instances.UpdateShieldedVmConfig. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance scoping this request. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`shielded_vm_config_resource` |  `[google.cloud.compute_v1beta.types.ShieldedVmConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ShieldedVmConfig)`   
The body resource for this request This corresponds to the `shielded_vm_config_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.UpdateInstanceRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        zone: typing.Optional[str] = None,
        instance: typing.Optional[str] = None,
        instance_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Instance
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

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceRequest.html)(
            instance="instance_value",
            project="project_value",
            zone="zone_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instances.InstancesClient.html#google_cloud_compute_v1beta_services_instances_InstancesClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateInstanceRequest), dict]`   
The request object. A request message for Instances.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `str`   
The name of the zone for this request. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `str`   
Name of the instance resource to update. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_resource` |  `[google.cloud.compute_v1beta.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Instance)`   
The body resource for this request This corresponds to the `instance_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
