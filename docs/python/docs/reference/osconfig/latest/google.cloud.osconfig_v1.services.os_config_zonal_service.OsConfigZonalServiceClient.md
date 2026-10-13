---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient
title: Class OsConfigZonalServiceClient (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:39.184832+00:00
---

# Class OsConfigZonalServiceClient (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OsConfigZonalServiceClient (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    OsConfigZonalServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.osconfig_v1.services.os_config_zonal_service.transports.base.OsConfigZonalServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.osconfig_v1.services.os_config_zonal_service.transports.base.OsConfigZonalServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Zonal OS Config API

The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances.

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
`OsConfigZonalServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### OsConfigZonalServiceClient
    
    
    OsConfigZonalServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.osconfig_v1.services.os_config_zonal_service.transports.base.OsConfigZonalServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.osconfig_v1.services.os_config_zonal_service.transports.base.OsConfigZonalServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the os config zonal service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,OsConfigZonalServiceTransport,Callable[..., OsConfigZonalServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the OsConfigZonalServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_os_policy_assignment
    
    
    create_os_policy_assignment(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.CreateOSPolicyAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        os_policy_assignment: typing.Optional[
            google.cloud.osconfig_v1.types.os_policy_assignments.OSPolicyAssignment
        ] = None,
        os_policy_assignment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see `Method: projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_create_os_policy_assignment():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        os_policy_assignment = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment.html)()
        os_policy_assignment.os_policies.id = "id_value"
        os_policy_assignment.os_policies.mode = "ENFORCEMENT"
        os_policy_assignment.os_policies.resource_groups.resources.pkg.apt.name = "name_value"
        os_policy_assignment.os_policies.resource_groups.resources.pkg.desired_state = "REMOVED"
        os_policy_assignment.os_policies.resource_groups.resources.id = "id_value"
        os_policy_assignment.rollout.disruption_budget.fixed = 528
    
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest.html)(
            parent="parent_value",
            os_policy_assignment=os_policy_assignment,
            os_policy_assignment_id="os_policy_assignment_id_value",
        )
    
        # Make the request
        operation = client.[create_os_policy_assignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_create_os_policy_assignment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.CreateOSPolicyAssignmentRequest), dict]`   
The request object. A request message to create an OS policy assignment  
`parent` |  `str`   
Required. The parent resource name in the form: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`os_policy_assignment` |  `[google.cloud.osconfig_v1.types.OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment)`   
Required. The OS policy assignment to be created. This corresponds to the `os_policy_assignment` field on the `request` instance; if `request` is provided, this should not be set.  
`os_policy_assignment_id` |  `str`   
Required. The logical name of the OS policy assignment in the project with the following restrictions: - Must contain only lowercase letters, numbers, and hyphens. - Must start with a letter. - Must be between 1-63 characters. - Must end with a number or a letter. - Must be unique within the project. This corresponds to the `os_policy_assignment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment) OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances. An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).  
  
### delete_os_policy_assignment
    
    
    delete_os_policy_assignment(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.DeleteOSPolicyAssignmentRequest,
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
    ) -> google.api_core.operation.Operation

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see `Method: projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_delete_os_policy_assignment():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.DeleteOSPolicyAssignmentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_os_policy_assignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_delete_os_policy_assignment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.DeleteOSPolicyAssignmentRequest), dict]`   
The request object. A request message for deleting a OS policy assignment.  
`name` |  `str`   
Required. The name of the OS policy assignment to be deleted This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
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
`OsConfigZonalServiceClient` | The constructed client.  
  
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
`OsConfigZonalServiceClient` | The constructed client.  
  
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
`OsConfigZonalServiceClient` | The constructed client.  
  
### get_inventory
    
    
    get_inventory(
        request: typing.Optional[
            typing.Union[google.cloud.osconfig_v1.types.inventory.GetInventoryRequest, dict]
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
    ) -> google.cloud.osconfig_v1.types.inventory.Inventory

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_get_inventory():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[GetInventoryRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetInventoryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_inventory](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_get_inventory)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.GetInventoryRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetInventoryRequest), dict]`   
The request object. A request message for getting inventory data for the specified VM.  
`name` |  `str`   
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.types.Inventory](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory)` | This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time. You can use this API resource to determine the inventory data of your VM. For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).  
  
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
  
### get_os_policy_assignment
    
    
    get_os_policy_assignment(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.GetOSPolicyAssignmentRequest,
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
    ) -> google.cloud.osconfig_v1.types.os_policy_assignments.OSPolicyAssignment

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_get_os_policy_assignment():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetOSPolicyAssignmentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_os_policy_assignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_get_os_policy_assignment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetOSPolicyAssignmentRequest), dict]`   
The request object. A request message to get an OS policy assignment  
`name` |  `str`   
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.types.OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment)` | OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances. An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).  
  
### get_os_policy_assignment_report
    
    
    get_os_policy_assignment_report(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
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
    ) -> (
        google.cloud.osconfig_v1.types.os_policy_assignment_reports.OSPolicyAssignmentReport
    )

Get the OS policy asssignment report for the specified Compute Engine VM instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_get_os_policy_assignment_report():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetOSPolicyAssignmentReportRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_os_policy_assignment_report](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_get_os_policy_assignment_report)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetOSPolicyAssignmentReportRequest), dict]`   
The request object. Get a report of the OS policy assignment for a VM instance.  
`name` |  `str`   
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.types.OSPolicyAssignmentReport](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignmentReport)` | A report of the OS policy assignment status for a given instance.  
  
### get_vulnerability_report
    
    
    get_vulnerability_report(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.vulnerability.GetVulnerabilityReportRequest,
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
    ) -> google.cloud.osconfig_v1.types.vulnerability.VulnerabilityReport

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_get_vulnerability_report():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[GetVulnerabilityReportRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetVulnerabilityReportRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_vulnerability_report](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_get_vulnerability_report)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.GetVulnerabilityReportRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.GetVulnerabilityReportRequest), dict]`   
The request object. A request message for getting the vulnerability report for the specified VM.  
`name` |  `str`   
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.types.VulnerabilityReport](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.VulnerabilityReport)` | This API resource represents the vulnerability report for a specified Compute Engine virtual machine (VM) instance at a given point in time. For more information, see [Vulnerability reports](https://cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports).  
  
### instance_os_policy_assignment_path
    
    
    instance_os_policy_assignment_path(
        project: str, location: str, instance: str, assignment: str
    ) -> str

Returns a fully-qualified instance_os_policy_assignment string.

### instance_path
    
    
    instance_path(project: str, zone: str, instance: str) -> str

Returns a fully-qualified instance string.

### inventory_path
    
    
    inventory_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified inventory string.

### list_inventories
    
    
    list_inventories(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.inventory.ListInventoriesRequest, dict
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
        google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListInventoriesPager
    )

List inventory data for all VM instances in the specified zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_list_inventories():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[ListInventoriesRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListInventoriesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_inventories](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_list_inventories)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.ListInventoriesRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListInventoriesRequest), dict]`   
The request object. A request message for listing inventory data for all VMs in the specified location.  
`parent` |  `str`   
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListInventoriesPager](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListInventoriesPager)` | A response message for listing inventory data for all VMs in a specified location. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_os_policy_assignment_reports
    
    
    list_os_policy_assignment_reports(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
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
        google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentReportsPager
    )

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_list_os_policy_assignment_reports():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_os_policy_assignment_reports](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_list_os_policy_assignment_reports)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest), dict]`   
The request object. List the OS policy assignment reports for VM instances.  
`parent` |  `str`   
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentReportsPager](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentReportsPager)` | A response message for listing OS Policy assignment reports including the page of results and page token. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_os_policy_assignment_revisions
    
    
    list_os_policy_assignment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
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
    ) -> (
        google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentRevisionsPager
    )

List the OS policy assignment revisions for a given OS policy assignment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_list_os_policy_assignment_revisions():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_os_policy_assignment_revisions](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_list_os_policy_assignment_revisions)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest), dict]`   
The request object. A request message to list revisions for a OS policy assignment  
`name` |  `str`   
Required. The name of the OS policy assignment to list revisions for. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentRevisionsPager](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentRevisionsPager)` | A response message for listing all revisions for a OS policy assignment. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_os_policy_assignments
    
    
    list_os_policy_assignments(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.ListOSPolicyAssignmentsRequest,
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
        google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentsPager
    )

List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_list_os_policy_assignments():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_os_policy_assignments](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_list_os_policy_assignments)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest), dict]`   
The request object. A request message to list OS policy assignments for a parent resource  
`parent` |  `str`   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentsPager](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListOSPolicyAssignmentsPager)` | A response message for listing all assignments under given parent. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_vulnerability_reports
    
    
    list_vulnerability_reports(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.vulnerability.ListVulnerabilityReportsRequest,
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
        google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListVulnerabilityReportsPager
    )

List vulnerability reports for all VM instances in the specified zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_list_vulnerability_reports():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_vulnerability_reports](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_list_vulnerability_reports)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest), dict]`   
The request object. A request message for listing vulnerability reports for all VM instances in the specified location.  
`parent` |  `str`   
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListVulnerabilityReportsPager](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.pagers.ListVulnerabilityReportsPager)` | A response message for listing vulnerability reports for all VM instances in the specified location. Iterating over this object will yield results and resolve additional pages automatically.  
  
### os_policy_assignment_path
    
    
    os_policy_assignment_path(
        project: str, location: str, os_policy_assignment: str
    ) -> str

Returns a fully-qualified os_policy_assignment string.

### os_policy_assignment_report_path
    
    
    os_policy_assignment_report_path(
        project: str, location: str, instance: str, assignment: str
    ) -> str

Returns a fully-qualified os_policy_assignment_report string.

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

### parse_instance_os_policy_assignment_path
    
    
    parse_instance_os_policy_assignment_path(path: str) -> typing.Dict[str, str]

Parses a instance_os_policy_assignment path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### parse_inventory_path
    
    
    parse_inventory_path(path: str) -> typing.Dict[str, str]

Parses a inventory path into its component segments.

### parse_os_policy_assignment_path
    
    
    parse_os_policy_assignment_path(path: str) -> typing.Dict[str, str]

Parses a os_policy_assignment path into its component segments.

### parse_os_policy_assignment_report_path
    
    
    parse_os_policy_assignment_report_path(path: str) -> typing.Dict[str, str]

Parses a os_policy_assignment_report path into its component segments.

### parse_vulnerability_report_path
    
    
    parse_vulnerability_report_path(path: str) -> typing.Dict[str, str]

Parses a vulnerability_report path into its component segments.

### update_os_policy_assignment
    
    
    update_os_policy_assignment(
        request: typing.Optional[
            typing.Union[
                google.cloud.osconfig_v1.types.os_policy_assignments.UpdateOSPolicyAssignmentRequest,
                dict,
            ]
        ] = None,
        *,
        os_policy_assignment: typing.Optional[
            google.cloud.osconfig_v1.types.os_policy_assignments.OSPolicyAssignment
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
    ) -> google.api_core.operation.Operation

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see `Method: projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest)
    
    def sample_update_os_policy_assignment():
        # Create a client
        client = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OsConfigZonalServiceClient](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html)()
    
        # Initialize request argument(s)
        os_policy_assignment = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment.html)()
        os_policy_assignment.os_policies.id = "id_value"
        os_policy_assignment.os_policies.mode = "ENFORCEMENT"
        os_policy_assignment.os_policies.resource_groups.resources.pkg.apt.name = "name_value"
        os_policy_assignment.os_policies.resource_groups.resources.pkg.desired_state = "REMOVED"
        os_policy_assignment.os_policies.resource_groups.resources.id = "id_value"
        os_policy_assignment.rollout.disruption_budget.fixed = 528
    
        request = [osconfig_v1](https://docs.cloud.google.com/python/docs/reference/osconfig/latest).[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.UpdateOSPolicyAssignmentRequest.html)(
            os_policy_assignment=os_policy_assignment,
        )
    
        # Make the request
        operation = client.[update_os_policy_assignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.services.os_config_zonal_service.OsConfigZonalServiceClient.html#google_cloud_osconfig_v1_services_os_config_zonal_service_OsConfigZonalServiceClient_update_os_policy_assignment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.osconfig_v1.types.UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.UpdateOSPolicyAssignmentRequest), dict]`   
The request object. A request message to update an OS policy assignment  
`os_policy_assignment` |  `[google.cloud.osconfig_v1.types.OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment)`   
Required. The updated OS policy assignment. This corresponds to the `os_policy_assignment` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask that controls which fields of the assignment should be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [OSPolicyAssignment](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicyAssignment) OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances. An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).  
  
### vulnerability_report_path
    
    
    vulnerability_report_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified vulnerability_report string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
