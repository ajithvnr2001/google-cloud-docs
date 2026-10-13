---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient
title: Class GroupServiceAsyncClient (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:07.296777+00:00
---

# Class GroupServiceAsyncClient (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GroupServiceAsyncClient (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    GroupServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.monitoring_v3.services.group_service.transports.base.GroupServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.monitoring_v3.services.group_service.transports.base.GroupServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Group API lets you inspect and manage your `groups <#google.monitoring.v3.Group>`__.

A group is a named filter that is used to identify a collection of monitored resources. Groups are typically used to mirror the physical and/or logical topology of the environment. Because group membership is computed dynamically, monitored resources that are started in the future are automatically placed in matching groups. By using a group to name monitored resources in, for example, an alert policy, the target of that alert policy is updated automatically as monitored resources are added and removed from the infrastructure.

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
`GroupServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### GroupServiceAsyncClient
    
    
    GroupServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.monitoring_v3.services.group_service.transports.base.GroupServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.monitoring_v3.services.group_service.transports.base.GroupServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the group service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,GroupServiceTransport,Callable[..., GroupServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the GroupServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_group
    
    
    create_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.CreateGroupRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        group: typing.Optional[google.cloud.monitoring_v3.types.group.Group] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.monitoring_v3.types.group.Group

Creates a new group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_create_group():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[CreateGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[create_group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_create_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.CreateGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateGroupRequest), dict]]`   
The request object. The `CreateGroup` request.  
`name` |  ``str``   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ in which to create the group. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`group` |  `[Group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Group)`   
Required. A group definition. It is an error to define the `name` field because the system assigns the name. This corresponds to the `group` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.types.Group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Group)` | The description of a dynamic collection of monitored resources. Each group has a filter that is matched against monitored resources and their associated metadata. If a group's filter matches an available monitored resource, then that resource is a member of that group. Groups can contain any number of monitored resources, and each monitored resource can be a member of any number of groups. Groups can be nested in parent-child hierarchies. The parentName field identifies an optional parent for each group. If a group has a parent, then the only monitored resources available to be matched by the group's filter are the resources contained in the parent group. In other words, a group contains the monitored resources that match its filter and the filters of all the group's ancestors. A group without a parent can contain any monitored resource. For example, consider an infrastructure running a set of instances with two user-defined tags: "environment" and "role". A parent group has a filter, environment="production". A child of that parent group has a filter, role="transcoder". The parent group contains all instances in the production environment, regardless of their roles. The child group contains instances that have the transcoder role *and* are in the production environment. The monitored resources contained in a group can change at any moment, depending on what resources exist and what filters are associated with the group and its ancestors.  
  
### delete_group
    
    
    delete_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.DeleteGroupRequest, dict
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
    ) -> None

Deletes an existing group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_delete_group():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[DeleteGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.DeleteGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_delete_group)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.DeleteGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.DeleteGroupRequest), dict]]`   
The request object. The `DeleteGroup` request. The default behavior is to be able to delete a single group without any descendants.  
`name` |  ``str``   
Required. The group to delete. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
`GroupServiceAsyncClient` | The constructed client.  
  
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
`GroupServiceAsyncClient` | The constructed client.  
  
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
`GroupServiceAsyncClient` | The constructed client.  
  
### get_group
    
    
    get_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.GetGroupRequest, dict
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
    ) -> google.cloud.monitoring_v3.types.group.Group

Gets a single group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_get_group():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GetGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_get_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.GetGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetGroupRequest), dict]]`   
The request object. The `GetGroup` request.  
`name` |  ``str``   
Required. The group to retrieve. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.types.Group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Group)` | The description of a dynamic collection of monitored resources. Each group has a filter that is matched against monitored resources and their associated metadata. If a group's filter matches an available monitored resource, then that resource is a member of that group. Groups can contain any number of monitored resources, and each monitored resource can be a member of any number of groups. Groups can be nested in parent-child hierarchies. The parentName field identifies an optional parent for each group. If a group has a parent, then the only monitored resources available to be matched by the group's filter are the resources contained in the parent group. In other words, a group contains the monitored resources that match its filter and the filters of all the group's ancestors. A group without a parent can contain any monitored resource. For example, consider an infrastructure running a set of instances with two user-defined tags: "environment" and "role". A parent group has a filter, environment="production". A child of that parent group has a filter, role="transcoder". The parent group contains all instances in the production environment, regardless of their roles. The child group contains instances that have the transcoder role *and* are in the production environment. The monitored resources contained in a group can change at any moment, depending on what resources exist and what filters are associated with the group and its ancestors.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.monitoring_v3.services.group_service.transports.base.GroupServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### group_path
    
    
    group_path(project: str, group: str) -> str

Returns a fully-qualified group string.

### list_group_members
    
    
    list_group_members(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.ListGroupMembersRequest, dict
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
    ) -> (
        google.cloud.monitoring_v3.services.group_service.pagers.ListGroupMembersAsyncPager
    )

Lists the monitored resources that are members of a group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_list_group_members():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListGroupMembersRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListGroupMembersRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_group_members](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_list_group_members)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.ListGroupMembersRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListGroupMembersRequest), dict]]`   
The request object. The `ListGroupMembers` request.  
`name` |  ``str``   
Required. The group whose members are listed. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.services.group_service.pagers.ListGroupMembersAsyncPager](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.pagers.ListGroupMembersAsyncPager)` | The ListGroupMembers response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_groups
    
    
    list_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.ListGroupsRequest, dict
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
    ) -> google.cloud.monitoring_v3.services.group_service.pagers.ListGroupsAsyncPager

Lists the existing groups.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_list_groups():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListGroupsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListGroupsRequest.html)(
            children_of_group="children_of_group_value",
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_groups](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_list_groups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.ListGroupsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListGroupsRequest), dict]]`   
The request object. The `ListGroup` request.  
`name` |  ``str``   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ whose groups are to be listed. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.services.group_service.pagers.ListGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.pagers.ListGroupsAsyncPager)` | The ListGroups response. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_group_path
    
    
    parse_group_path(path: str) -> typing.Dict[str, str]

Parses a group path into its component segments.

### update_group
    
    
    update_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.group_service.UpdateGroupRequest, dict
            ]
        ] = None,
        *,
        group: typing.Optional[google.cloud.monitoring_v3.types.group.Group] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.monitoring_v3.types.group.Group

Updates an existing group. You can change any group attributes except `name`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    async def sample_update_group():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GroupServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[UpdateGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UpdateGroupRequest.html)(
        )
    
        # Make the request
        response = await client.[update_group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.group_service.GroupServiceAsyncClient.html#google_cloud_monitoring_v3_services_group_service_GroupServiceAsyncClient_update_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.monitoring_v3.types.UpdateGroupRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UpdateGroupRequest), dict]]`   
The request object. The `UpdateGroup` request.  
`group` |  `[Group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Group)`   
Required. The new definition of the group. All fields of the existing group, excepting `name`, are replaced with the corresponding fields of this group. This corresponds to the `group` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.types.Group](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Group)` | The description of a dynamic collection of monitored resources. Each group has a filter that is matched against monitored resources and their associated metadata. If a group's filter matches an available monitored resource, then that resource is a member of that group. Groups can contain any number of monitored resources, and each monitored resource can be a member of any number of groups. Groups can be nested in parent-child hierarchies. The parentName field identifies an optional parent for each group. If a group has a parent, then the only monitored resources available to be matched by the group's filter are the resources contained in the parent group. In other words, a group contains the monitored resources that match its filter and the filters of all the group's ancestors. A group without a parent can contain any monitored resource. For example, consider an infrastructure running a set of instances with two user-defined tags: "environment" and "role". A parent group has a filter, environment="production". A child of that parent group has a filter, role="transcoder". The parent group contains all instances in the production environment, regardless of their roles. The child group contains instances that have the transcoder role *and* are in the production environment. The monitored resources contained in a group can change at any moment, depending on what resources exist and what filters are associated with the group and its ancestors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
