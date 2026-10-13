---
url: https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient
title: Class AssuredWorkloadsServiceClient (2.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:21.057377+00:00
---

# Class AssuredWorkloadsServiceClient (2.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AssuredWorkloadsServiceClient (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.0 (latest)  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.15.2  1.14.0  1.13.1  1.12.5  1.11.0  1.10.3  1.9.1  1.8.1  1.7.0  1.6.1  1.5.0  1.4.2  1.3.0  1.2.3  1.1.0  1.0.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.2  0.3.1  0.2.1  0.1.0 
    
    
    AssuredWorkloadsServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.assuredworkloads_v1.services.assured_workloads_service.transports.base.AssuredWorkloadsServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.assuredworkloads_v1.services.assured_workloads_service.transports.base.AssuredWorkloadsServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service to manage AssuredWorkloads.

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
`AssuredWorkloadsServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AssuredWorkloadsServiceClient
    
    
    AssuredWorkloadsServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.assuredworkloads_v1.services.assured_workloads_service.transports.base.AssuredWorkloadsServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.assuredworkloads_v1.services.assured_workloads_service.transports.base.AssuredWorkloadsServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the assured workloads service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AssuredWorkloadsServiceTransport,Callable[..., AssuredWorkloadsServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the AssuredWorkloadsServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### acknowledge_violation
    
    
    acknowledge_violation(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.AcknowledgeViolationRequest,
                dict,
            ]
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
    ) -> (
        google.cloud.assuredworkloads_v1.types.assuredworkloads.AcknowledgeViolationResponse
    )

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_acknowledge_violation():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AcknowledgeViolationRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.AcknowledgeViolationRequest.html)(
            name="name_value",
            comment="comment_value",
        )
    
        # Make the request
        response = client.[acknowledge_violation](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_acknowledge_violation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.AcknowledgeViolationRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.AcknowledgeViolationRequest), dict]`   
The request object. Request for acknowledging the violation Next Id: 4  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.types.AcknowledgeViolationResponse](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.AcknowledgeViolationResponse)` | Response for violation acknowledgement  
  
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

### create_workload
    
    
    create_workload(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.CreateWorkloadRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        workload: typing.Optional[
            google.cloud.assuredworkloads_v1.types.assuredworkloads.Workload
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates Assured Workload.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_create_workload():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        workload = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload.html)()
        workload.display_name = "display_name_value"
        workload.compliance_regime = "ASSURED_WORKLOADS_FOR_PARTNERS"
    
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[CreateWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.CreateWorkloadRequest.html)(
            parent="parent_value",
            workload=workload,
        )
    
        # Make the request
        operation = client.[create_workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_create_workload)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.CreateWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.CreateWorkloadRequest), dict]`   
The request object. Request for creating a workload.  
`parent` |  `str`   
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`workload` |  `[google.cloud.assuredworkloads_v1.types.Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload)`   
Required. Assured Workload to create This corresponds to the `workload` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload) A Workload object for managing highly regulated workloads of cloud customers.  
  
### delete_workload
    
    
    delete_workload(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.DeleteWorkloadRequest,
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

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_delete_workload():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[DeleteWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.DeleteWorkloadRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_delete_workload)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.DeleteWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.DeleteWorkloadRequest), dict]`   
The request object. Request for deleting a Workload.  
`name` |  `str`   
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`AssuredWorkloadsServiceClient` | The constructed client.  
  
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
`AssuredWorkloadsServiceClient` | The constructed client.  
  
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
`AssuredWorkloadsServiceClient` | The constructed client.  
  
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
  
### get_violation
    
    
    get_violation(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.GetViolationRequest,
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
    ) -> google.cloud.assuredworkloads_v1.types.assuredworkloads.Violation

Retrieves Assured Workload Violation based on ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_get_violation():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[GetViolationRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.GetViolationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_violation](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_get_violation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.GetViolationRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.GetViolationRequest), dict]`   
The request object. Request for fetching a Workload Violation.  
`name` |  `str`   
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.types.Violation](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Violation)` | Workload monitoring Violation.  
  
### get_workload
    
    
    get_workload(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.GetWorkloadRequest,
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
    ) -> google.cloud.assuredworkloads_v1.types.assuredworkloads.Workload

Gets Assured Workload associated with a CRM Node
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_get_workload():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[GetWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.GetWorkloadRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_get_workload)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.GetWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.GetWorkloadRequest), dict]`   
The request object. Request for fetching a workload.  
`name` |  `str`   
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1". This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.types.Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload)` | A Workload object for managing highly regulated workloads of cloud customers.  
  
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
  
### list_violations
    
    
    list_violations(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.ListViolationsRequest,
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
        google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListViolationsPager
    )

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per `AIP-159 <https://google.aip.dev/159>`__ by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_list_violations():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[ListViolationsRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.ListViolationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_violations](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_list_violations)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.ListViolationsRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.ListViolationsRequest), dict]`   
The request object. Request for fetching violations in an organization.  
`parent` |  `str`   
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListViolationsPager](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListViolationsPager)` | Response of ListViolations endpoint. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_workloads
    
    
    list_workloads(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.ListWorkloadsRequest,
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
        google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListWorkloadsPager
    )

Lists Assured Workloads under a CRM Node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_list_workloads():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[ListWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.ListWorkloadsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_workloads](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_list_workloads)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.ListWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.ListWorkloadsRequest), dict]`   
The request object. Request for fetching workloads in an organization.  
`parent` |  `str`   
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListWorkloadsPager](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.pagers.ListWorkloadsPager)` | Response of ListWorkloads endpoint. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_violation_path
    
    
    parse_violation_path(path: str) -> typing.Dict[str, str]

Parses a violation path into its component segments.

### parse_workload_path
    
    
    parse_workload_path(path: str) -> typing.Dict[str, str]

Parses a workload path into its component segments.

### restrict_allowed_resources
    
    
    restrict_allowed_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.RestrictAllowedResourcesRequest,
                dict,
            ]
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
    ) -> (
        google.cloud.assuredworkloads_v1.types.assuredworkloads.RestrictAllowedResourcesResponse
    )

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_restrict_allowed_resources():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.RestrictAllowedResourcesRequest.html)(
            name="name_value",
            restriction_type="ALLOW_COMPLIANT_RESOURCES",
        )
    
        # Make the request
        response = client.[restrict_allowed_resources](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_restrict_allowed_resources)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.RestrictAllowedResourcesRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.RestrictAllowedResourcesRequest), dict]`   
The request object. Request for restricting list of available resources in Workload environment.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.types.RestrictAllowedResourcesResponse](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.RestrictAllowedResourcesResponse)` | Response for restricting the list of allowed resources.  
  
### update_workload
    
    
    update_workload(
        request: typing.Optional[
            typing.Union[
                google.cloud.assuredworkloads_v1.types.assuredworkloads.UpdateWorkloadRequest,
                dict,
            ]
        ] = None,
        *,
        workload: typing.Optional[
            google.cloud.assuredworkloads_v1.types.assuredworkloads.Workload
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
    ) -> google.cloud.assuredworkloads_v1.types.assuredworkloads.Workload

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest)
    
    def sample_update_workload():
        # Create a client
        client = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html)()
    
        # Initialize request argument(s)
        workload = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload.html)()
        workload.display_name = "display_name_value"
        workload.compliance_regime = "ASSURED_WORKLOADS_FOR_PARTNERS"
    
        request = [assuredworkloads_v1](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest).[UpdateWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.UpdateWorkloadRequest.html)(
            workload=workload,
        )
    
        # Make the request
        response = client.[update_workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.services.assured_workloads_service.AssuredWorkloadsServiceClient.html#google_cloud_assuredworkloads_v1_services_assured_workloads_service_AssuredWorkloadsServiceClient_update_workload)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.assuredworkloads_v1.types.UpdateWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.UpdateWorkloadRequest), dict]`   
The request object. Request for Updating a workload.  
`workload` |  `[google.cloud.assuredworkloads_v1.types.Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload)`   
Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id} This corresponds to the `workload` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. The list of fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.assuredworkloads_v1.types.Workload](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload)` | A Workload object for managing highly regulated workloads of cloud customers.  
  
### violation_path
    
    
    violation_path(
        organization: str, location: str, workload: str, violation: str
    ) -> str

Returns a fully-qualified violation string.

### workload_path
    
    
    workload_path(organization: str, location: str, workload: str) -> str

Returns a fully-qualified workload string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
