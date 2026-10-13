---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient
title: Class CloudControlsPartnerCoreAsyncClient (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:45.314917+00:00
---

# Class CloudControlsPartnerCoreAsyncClient (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudControlsPartnerCoreAsyncClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7  0.1.3 
    
    
    CloudControlsPartnerCoreAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.transports.base.CloudControlsPartnerCoreTransport,
                typing.Callable[
                    [...],
                    google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.transports.base.CloudControlsPartnerCoreTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
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
`CloudControlsPartnerCoreTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudControlsPartnerCoreAsyncClient
    
    
    CloudControlsPartnerCoreAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.transports.base.CloudControlsPartnerCoreTransport,
                typing.Callable[
                    [...],
                    google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.transports.base.CloudControlsPartnerCoreTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud controls partner core async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudControlsPartnerCoreTransport,Callable[..., CloudControlsPartnerCoreTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudControlsPartnerCoreTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### access_approval_request_path
    
    
    access_approval_request_path(
        organization: str,
        location: str,
        customer: str,
        workload: str,
        access_approval_request: str,
    ) -> str

Returns a fully-qualified access_approval_request string.

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

### create_customer
    
    
    create_customer(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customers.CreateCustomerRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        customer: typing.Optional[
            google.cloud.cloudcontrolspartner_v1.types.customers.Customer
        ] = None,
        customer_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.cloudcontrolspartner_v1.types.customers.Customer

Creates a new customer.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_create_customer():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        customer = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer.html)()
        customer.display_name = "display_name_value"
    
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CreateCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.CreateCustomerRequest.html)(
            parent="parent_value",
            customer=customer,
            customer_id="customer_id_value",
        )
    
        # Make the request
        response = await client.[create_customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_create_customer)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.CreateCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.CreateCustomerRequest), dict]]`   
The request object. Request to create a customer  
`parent` |  ``str``   
Required. Parent resource Format: `organizations/{organization}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`customer` |  `[Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)`   
Required. The customer to create. This corresponds to the `customer` field on the `request` instance; if `request` is provided, this should not be set.  
`customer_id` |  ``str``   
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id. This corresponds to the `customer_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)` | Contains metadata around a Cloud Controls Partner Customer  
  
### customer_path
    
    
    customer_path(organization: str, location: str, customer: str) -> str

Returns a fully-qualified customer string.

### delete_customer
    
    
    delete_customer(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customers.DeleteCustomerRequest,
                dict,
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

Delete details of a single customer
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_delete_customer():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[DeleteCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.DeleteCustomerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_delete_customer)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.DeleteCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.DeleteCustomerRequest), dict]]`   
The request object. Message for deleting customer  
`name` |  ``str``   
Required. name of the resource to be deleted format: name=organizations/_/locations/_ /customers/* This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### ekm_connections_path
    
    
    ekm_connections_path(
        organization: str, location: str, customer: str, workload: str
    ) -> str

Returns a fully-qualified ekm_connections string.

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
`CloudControlsPartnerCoreAsyncClient` | The constructed client.  
  
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
`CloudControlsPartnerCoreAsyncClient` | The constructed client.  
  
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
`CloudControlsPartnerCoreAsyncClient` | The constructed client.  
  
### get_customer
    
    
    get_customer(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customers.GetCustomerRequest,
                dict,
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
    ) -> google.cloud.cloudcontrolspartner_v1.types.customers.Customer

Gets details of a single customer
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_get_customer():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[GetCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetCustomerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_get_customer)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.GetCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetCustomerRequest), dict]]`   
The request object. Message for getting a customer  
`name` |  ``str``   
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)` | Contains metadata around a Cloud Controls Partner Customer  
  
### get_ekm_connections
    
    
    get_ekm_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.ekm_connections.GetEkmConnectionsRequest,
                dict,
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
    ) -> google.cloud.cloudcontrolspartner_v1.types.ekm_connections.EkmConnections

Gets the EKM connections associated with a workload
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_get_ekm_connections():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[GetEkmConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetEkmConnectionsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_ekm_connections](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_get_ekm_connections)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.GetEkmConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetEkmConnectionsRequest), dict]]`   
The request object. Request for getting the EKM connections associated with a workload  
`name` |  ``str``   
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.EkmConnections](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.EkmConnections)` | The EKM connections associated with a workload  
  
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
  
### get_partner
    
    
    get_partner(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.partners.GetPartnerRequest, dict
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
    ) -> google.cloud.cloudcontrolspartner_v1.types.partners.Partner

Get details of a Partner.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_get_partner():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[GetPartnerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetPartnerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_partner](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_get_partner)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.GetPartnerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetPartnerRequest), dict]]`   
The request object. Message for getting a Partner  
`name` |  ``str``   
Required. Format: `organizations/{organization}/locations/{location}/partner` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.Partner](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Partner)` | Message describing Partner resource  
  
### get_partner_permissions
    
    
    get_partner_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.partner_permissions.GetPartnerPermissionsRequest,
                dict,
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
    ) -> google.cloud.cloudcontrolspartner_v1.types.partner_permissions.PartnerPermissions

Gets the partner permissions granted for a workload
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_get_partner_permissions():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[GetPartnerPermissionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetPartnerPermissionsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_partner_permissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_get_partner_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.GetPartnerPermissionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetPartnerPermissionsRequest), dict]]`   
The request object. Request for getting the partner permissions granted for a workload  
`name` |  ``str``   
Required. Name of the resource to get in the format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.PartnerPermissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.PartnerPermissions)` | The permissions granted to the partner for a workload  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.transports.base.CloudControlsPartnerCoreTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### get_workload
    
    
    get_workload(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customer_workloads.GetWorkloadRequest,
                dict,
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
    ) -> google.cloud.cloudcontrolspartner_v1.types.customer_workloads.Workload

Gets details of a single workload
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_get_workload():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[GetWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetWorkloadRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_workload](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_get_workload)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.GetWorkloadRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.GetWorkloadRequest), dict]]`   
The request object. Message for getting a customer workload.  
`name` |  ``str``   
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.Workload](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Workload)` | Contains metadata around the [Workload resource](https://cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload) in the Assured Workloads API.  
  
### list_access_approval_requests
    
    
    list_access_approval_requests(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.access_approval_requests.ListAccessApprovalRequestsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListAccessApprovalRequestsAsyncPager
    )

Deprecated: Only returns access approval requests directly associated with an assured workload folder.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_list_access_approval_requests():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListAccessApprovalRequestsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_access_approval_requests](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_list_access_approval_requests)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListAccessApprovalRequestsRequest), dict]]`   
The request object. Request for getting the access requests associated with a workload.  
`parent` |  ``str``   
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListAccessApprovalRequestsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListAccessApprovalRequestsAsyncPager)` | Response message for list access requests. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_customers
    
    
    list_customers(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customers.ListCustomersRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListCustomersAsyncPager
    )

Lists customers of a partner identified by its Google Cloud organization ID
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_list_customers():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[ListCustomersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListCustomersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_customers](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_list_customers)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.ListCustomersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListCustomersRequest), dict]]`   
The request object. Request to list customers  
`parent` |  ``str``   
Required. Parent resource Format: `organizations/{organization}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListCustomersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListCustomersAsyncPager)` | Response message for list customer Customers requests Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_workloads
    
    
    list_workloads(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customer_workloads.ListWorkloadsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListWorkloadsAsyncPager
    )

Lists customer workloads for a given customer org id
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_list_workloads():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[ListWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListWorkloadsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_workloads](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_list_workloads)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.ListWorkloadsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.ListWorkloadsRequest), dict]]`   
The request object. Request to list customer workloads.  
`parent` |  ``str``   
Required. Parent resource Format: `organizations/{organization}/locations/{location}/customers/{customer}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListWorkloadsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.pagers.ListWorkloadsAsyncPager)` | Response message for list customer workloads requests. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_access_approval_request_path
    
    
    parse_access_approval_request_path(path: str) -> typing.Dict[str, str]

Parses a access_approval_request path into its component segments.

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

### parse_customer_path
    
    
    parse_customer_path(path: str) -> typing.Dict[str, str]

Parses a customer path into its component segments.

### parse_ekm_connections_path
    
    
    parse_ekm_connections_path(path: str) -> typing.Dict[str, str]

Parses a ekm_connections path into its component segments.

### parse_partner_path
    
    
    parse_partner_path(path: str) -> typing.Dict[str, str]

Parses a partner path into its component segments.

### parse_partner_permissions_path
    
    
    parse_partner_permissions_path(path: str) -> typing.Dict[str, str]

Parses a partner_permissions path into its component segments.

### parse_workload_path
    
    
    parse_workload_path(path: str) -> typing.Dict[str, str]

Parses a workload path into its component segments.

### partner_path
    
    
    partner_path(organization: str, location: str) -> str

Returns a fully-qualified partner string.

### partner_permissions_path
    
    
    partner_permissions_path(
        organization: str, location: str, customer: str, workload: str
    ) -> str

Returns a fully-qualified partner_permissions string.

### update_customer
    
    
    update_customer(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudcontrolspartner_v1.types.customers.UpdateCustomerRequest,
                dict,
            ]
        ] = None,
        *,
        customer: typing.Optional[
            google.cloud.cloudcontrolspartner_v1.types.customers.Customer
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.cloudcontrolspartner_v1.types.customers.Customer

Update details of a single customer
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest)
    
    async def sample_update_customer():
        # Create a client
        client = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[CloudControlsPartnerCoreAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html)()
    
        # Initialize request argument(s)
        customer = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer.html)()
        customer.display_name = "display_name_value"
    
        request = [cloudcontrolspartner_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest).[UpdateCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.UpdateCustomerRequest.html)(
            customer=customer,
        )
    
        # Make the request
        response = await client.[update_customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_core.CloudControlsPartnerCoreAsyncClient.html#google_cloud_cloudcontrolspartner_v1_services_cloud_controls_partner_core_CloudControlsPartnerCoreAsyncClient_update_customer)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.cloudcontrolspartner_v1.types.UpdateCustomerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.UpdateCustomerRequest), dict]]`   
The request object. Request to update a customer  
`customer` |  `[Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)`   
Required. The customer to update Format: `organizations/{organization}/locations/{location}/customers/{customer}` This corresponds to the `customer` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. The list of fields to update This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudcontrolspartner_v1.types.Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)` | Contains metadata around a Cloud Controls Partner Customer  
  
### workload_path
    
    
    workload_path(
        organization: str, location: str, customer: str, workload: str
    ) -> str

Returns a fully-qualified workload string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
