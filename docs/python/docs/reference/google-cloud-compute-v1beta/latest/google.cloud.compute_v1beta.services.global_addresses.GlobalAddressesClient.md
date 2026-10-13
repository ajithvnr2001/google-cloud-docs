---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient
title: Class GlobalAddressesClient (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:18:48.567283+00:00
---

# Class GlobalAddressesClient (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GlobalAddressesClient (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    GlobalAddressesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.global_addresses.transports.base.GlobalAddressesTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.global_addresses.transports.base.GlobalAddressesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The GlobalAddresses API.

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
`GlobalAddressesTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### GlobalAddressesClient
    
    
    GlobalAddressesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.global_addresses.transports.base.GlobalAddressesTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.global_addresses.transports.base.GlobalAddressesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the global addresses client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,GlobalAddressesTransport,Callable[..., GlobalAddressesTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the GlobalAddressesTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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
                google.cloud.compute_v1beta.types.compute.DeleteGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified address resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest.html)(
            address="address_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address` |  `str`   
Name of the address resource to delete. This corresponds to the `address` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.DeleteGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes the specified address resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest.html)(
            address="address_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address` |  `str`   
Name of the address resource to delete. This corresponds to the `address` field on the `request` instance; if `request` is provided, this should not be set.  
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
`GlobalAddressesClient` | The constructed client.  
  
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
`GlobalAddressesClient` | The constructed client.  
  
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
`GlobalAddressesClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Address

Returns the specified address resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetGlobalAddressRequest.html)(
            address="address_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address` |  `str`   
Name of the address resource to return. This corresponds to the `address` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Address](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Address)` | Represents an IP Address resource. Google Compute Engine has two IP Address resources: \\* [Global (external and internal)](https://cloud.google.com/compute/docs/reference/rest/beta/globalAddresses) \\* [Regional (external and internal)](https://cloud.google.com/compute/docs/reference/rest/beta/addresses) For more information, see Reserving a static external IP address.  
  
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
                google.cloud.compute_v1beta.types.compute.InsertGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Address
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

Creates an address resource in the specified project by using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertGlobalAddressRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address_resource` |  `[google.cloud.compute_v1beta.types.Address](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Address)`   
The body resource for this request This corresponds to the `address_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.InsertGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.Address
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

Creates an address resource in the specified project by using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertGlobalAddressRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address_resource` |  `[google.cloud.compute_v1beta.types.Address](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Address)`   
The body resource for this request This corresponds to the `address_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.ListGlobalAddressesRequest, dict
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
    ) -> google.cloud.compute_v1beta.services.global_addresses.pagers.ListPager

Retrieves a list of global addresses.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListGlobalAddressesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListGlobalAddressesRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListGlobalAddressesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListGlobalAddressesRequest), dict]`   
The request object. A request message for GlobalAddresses.List. See the method description for details.  
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
`[google.cloud.compute_v1beta.services.global_addresses.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.pagers.ListPager)` | Contains a list of addresses. Iterating over this object will yield results and resolve additional pages automatically.  
  
### move
    
    
    move(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.MoveGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        global_addresses_move_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.GlobalAddressesMoveRequest
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

Moves the specified address resource from one project to another project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_move():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[MoveGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MoveGlobalAddressRequest.html)(
            address="address_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[move](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_move)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.MoveGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MoveGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Move. See the method description for details.  
`project` |  `str`   
Source project ID which the Address is moved from. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address` |  `str`   
Name of the address resource to move. This corresponds to the `address` field on the `request` instance; if `request` is provided, this should not be set.  
`global_addresses_move_request_resource` |  `[google.cloud.compute_v1beta.types.GlobalAddressesMoveRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GlobalAddressesMoveRequest)`   
The body resource for this request This corresponds to the `global_addresses_move_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### move_unary
    
    
    move_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.MoveGlobalAddressRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        global_addresses_move_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.GlobalAddressesMoveRequest
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

Moves the specified address resource from one project to another project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_move():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[MoveGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MoveGlobalAddressRequest.html)(
            address="address_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[move](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_move)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.MoveGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MoveGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.Move. See the method description for details.  
`project` |  `str`   
Source project ID which the Address is moved from. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`address` |  `str`   
Name of the address resource to move. This corresponds to the `address` field on the `request` instance; if `request` is provided, this should not be set.  
`global_addresses_move_request_resource` |  `[google.cloud.compute_v1beta.types.GlobalAddressesMoveRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GlobalAddressesMoveRequest)`   
The body resource for this request This corresponds to the `global_addresses_move_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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

### set_labels
    
    
    set_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetLabelsGlobalAddressRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        global_set_labels_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.GlobalSetLabelsRequest
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

Sets the labels on a GlobalAddress. To learn more about labels, read theLabeling Resources documentation.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetLabelsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_labels](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_set_labels)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.SetLabels. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`global_set_labels_request_resource` |  `[google.cloud.compute_v1beta.types.GlobalSetLabelsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GlobalSetLabelsRequest)`   
The body resource for this request This corresponds to the `global_set_labels_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.SetLabelsGlobalAddressRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        global_set_labels_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.GlobalSetLabelsRequest
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

Sets the labels on a GlobalAddress. To learn more about labels, read theLabeling Resources documentation.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetLabelsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_labels](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_set_labels)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetLabelsGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.SetLabels. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`global_set_labels_request_resource` |  `[google.cloud.compute_v1beta.types.GlobalSetLabelsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GlobalSetLabelsRequest)`   
The body resource for this request This corresponds to the `global_set_labels_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.TestIamPermissionsGlobalAddressRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GlobalAddressesClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[TestIamPermissionsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsGlobalAddressRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.global_addresses.GlobalAddressesClient.html#google_cloud_compute_v1beta_services_global_addresses_GlobalAddressesClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.TestIamPermissionsGlobalAddressRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsGlobalAddressRequest), dict]`   
The request object. A request message for GlobalAddresses.TestIamPermissions. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
