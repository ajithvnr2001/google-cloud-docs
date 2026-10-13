---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient
title: Class AppTopologyClient (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:04.471440+00:00
---

# Class AppTopologyClient (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AppTopologyClient (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    AppTopologyClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apptopology_v1.services.app_topology.transports.base.AppTopologyTransport,
                typing.Callable[
                    [...],
                    google.cloud.apptopology_v1.services.app_topology.transports.base.AppTopologyTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service describing handlers for resources

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
`AppTopologyTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AppTopologyClient
    
    
    AppTopologyClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apptopology_v1.services.app_topology.transports.base.AppTopologyTransport,
                typing.Callable[
                    [...],
                    google.cloud.apptopology_v1.services.app_topology.transports.base.AppTopologyTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the app topology client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AppTopologyTransport,Callable[..., AppTopologyTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the AppTopologyTransport constructor. If set to None, a transport is chosen automatically.  
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

### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
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

Deletes a long-running operation.

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### discovered_resources_topology_path
    
    
    discovered_resources_topology_path(project: str, location: str) -> str

Returns a fully-qualified discovered_resources_topology string.

### domain_path
    
    
    domain_path(project: str, location: str, domain: str) -> str

Returns a fully-qualified domain string.

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
`AppTopologyClient` | The constructed client.  
  
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
`AppTopologyClient` | The constructed client.  
  
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
`AppTopologyClient` | The constructed client.  
  
### generate_discovered_resources_topology
    
    
    generate_discovered_resources_topology(
        request: typing.Optional[
            typing.Union[
                google.cloud.apptopology_v1.types.service.GenerateDiscoveredResourcesTopologyRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        topology_domains: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apptopology_v1.types.service.GenerateDiscoveredResourcesTopologyResponse
    )

Generate the topology for all resources in the given project. If the project represents an `app boundary <https://cloud.google.com/app-hub/docs/reference/rest/v1/Boundary>`__, the topology is generated for all resources in the boundary.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest)
    
    def sample_generate_discovered_resources_topology():
        # Create a client
        client = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[AppTopologyClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html)()
    
        # Initialize request argument(s)
        request = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[GenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GenerateDiscoveredResourcesTopologyRequest.html)(
            name="name_value",
            topology_domains=['topology_domains_value1', 'topology_domains_value2'],
        )
    
        # Make the request
        response = client.[generate_discovered_resources_topology](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html#google_cloud_apptopology_v1_services_app_topology_AppTopologyClient_generate_discovered_resources_topology)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.apptopology_v1.types.GenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GenerateDiscoveredResourcesTopologyRequest), dict]`   
The request object. Request for GenerateDiscoveredResourcesTopology.  
`name` |  `str`   
Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`topology_domains` |  `MutableSequence[str]`   
Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains. This corresponds to the `topology_domains` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apptopology_v1.types.GenerateDiscoveredResourcesTopologyResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GenerateDiscoveredResourcesTopologyResponse)` | Response for GenerateDiscoveredResourcesTopology.  
  
### get_domain
    
    
    get_domain(
        request: typing.Optional[
            typing.Union[google.cloud.apptopology_v1.types.service.GetDomainRequest, dict]
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
    ) -> google.cloud.apptopology_v1.types.schema.Domain

Retrieves the specified topology domain.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest)
    
    def sample_get_domain():
        # Create a client
        client = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[AppTopologyClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html)()
    
        # Initialize request argument(s)
        request = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[GetDomainRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GetDomainRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_domain](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html#google_cloud_apptopology_v1_services_app_topology_AppTopologyClient_get_domain)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.apptopology_v1.types.GetDomainRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GetDomainRequest), dict]`   
The request object. Request for GetDomain.  
`name` |  `str`   
Required. The name of the domain to retrieve. Format: `projects/{project}/locations/{location}/domains/{domain}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apptopology_v1.types.Domain](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Domain)` | Domain is a pre-defined topology query domain. Each topology domain contains a set of nodes and edges.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
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
  
### get_schema
    
    
    get_schema(
        request: typing.Optional[
            typing.Union[google.cloud.apptopology_v1.types.service.GetSchemaRequest, dict]
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
    ) -> google.cloud.apptopology_v1.types.schema.Schema

Retrieves the schema for the specified topology domain. The schema defines the NodeTypes and EdgeTypes that are supported in GenerateDiscoveredResourcesTopology requests and responses for a given domain.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest)
    
    def sample_get_schema():
        # Create a client
        client = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[AppTopologyClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html)()
    
        # Initialize request argument(s)
        request = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GetSchemaRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_schema](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html#google_cloud_apptopology_v1_services_app_topology_AppTopologyClient_get_schema)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.apptopology_v1.types.GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.GetSchemaRequest), dict]`   
The request object. Request for GetSchema.  
`name` |  `str`   
Required. The name of the singleton domain schema resource. Format: `projects/{project}/locations/{location}/domains/{domain}/schema` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apptopology_v1.types.Schema](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.Schema)` | Schema is a collection of supported node & edge labels and properties for an overlay.  
  
### list_domains
    
    
    list_domains(
        request: typing.Optional[
            typing.Union[google.cloud.apptopology_v1.types.service.ListDomainsRequest, dict]
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
    ) -> google.cloud.apptopology_v1.services.app_topology.pagers.ListDomainsPager

Lists the topology domains available in a specific location. Only `global` location is supported.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest)
    
    def sample_list_domains():
        # Create a client
        client = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[AppTopologyClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html)()
    
        # Initialize request argument(s)
        request = [apptopology_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest).[ListDomainsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.ListDomainsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_domains](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.AppTopologyClient.html#google_cloud_apptopology_v1_services_app_topology_AppTopologyClient_list_domains)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.apptopology_v1.types.ListDomainsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.types.ListDomainsRequest), dict]`   
The request object. Request for ListDomains.  
`parent` |  `str`   
Required. The parent location to list domains for. Format: `projects/{project}/locations/{location}` Only `global` location is supported. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apptopology_v1.services.app_topology.pagers.ListDomainsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apptopology/latest/google.cloud.apptopology_v1.services.app_topology.pagers.ListDomainsPager)` | Response for ListDomains. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
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

### parse_discovered_resources_topology_path
    
    
    parse_discovered_resources_topology_path(path: str) -> typing.Dict[str, str]

Parses a discovered_resources_topology path into its component segments.

### parse_domain_path
    
    
    parse_domain_path(path: str) -> typing.Dict[str, str]

Parses a domain path into its component segments.

### parse_schema_path
    
    
    parse_schema_path(path: str) -> typing.Dict[str, str]

Parses a schema path into its component segments.

### schema_path
    
    
    schema_path(project: str, location: str, domain: str) -> str

Returns a fully-qualified schema string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
