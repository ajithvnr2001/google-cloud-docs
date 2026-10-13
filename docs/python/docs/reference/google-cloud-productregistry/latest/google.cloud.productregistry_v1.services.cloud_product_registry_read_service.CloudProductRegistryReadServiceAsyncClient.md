---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient
title: Class CloudProductRegistryReadServiceAsyncClient (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:03.769848+00:00
---

# Class CloudProductRegistryReadServiceAsyncClient (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudProductRegistryReadServiceAsyncClient (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    CloudProductRegistryReadServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.productregistry_v1.services.cloud_product_registry_read_service.transports.base.CloudProductRegistryReadServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.productregistry_v1.services.cloud_product_registry_read_service.transports.base.CloudProductRegistryReadServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Cloud Product Registry Read Service provides capabilities to access all first and third party Google Cloud products.

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
`CloudProductRegistryReadServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudProductRegistryReadServiceAsyncClient
    
    
    CloudProductRegistryReadServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.productregistry_v1.services.cloud_product_registry_read_service.transports.base.CloudProductRegistryReadServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.productregistry_v1.services.cloud_product_registry_read_service.transports.base.CloudProductRegistryReadServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud product registry read service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudProductRegistryReadServiceTransport,Callable[..., CloudProductRegistryReadServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudProductRegistryReadServiceTransport constructor. If set to None, a transport is chosen automatically.  
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
`CloudProductRegistryReadServiceAsyncClient` | The constructed client.  
  
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
`CloudProductRegistryReadServiceAsyncClient` | The constructed client.  
  
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
`CloudProductRegistryReadServiceAsyncClient` | The constructed client.  
  
### get_logical_product
    
    
    get_logical_product(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.GetLogicalProductRequest,
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
    ) -> google.cloud.productregistry_v1.types.logical_product.LogicalProduct

Gets details of a LogicalProduct.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_get_logical_product():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[GetLogicalProductRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetLogicalProductRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_logical_product](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_get_logical_product)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.GetLogicalProductRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetLogicalProductRequest), dict]]`   
The request object. Request message for GetLogicalProduct.  
`name` |  ``str``   
Required. The name of the LogicalProduct to retrieve. Format: logicalProducts/{logical_product} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.types.LogicalProduct](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.LogicalProduct)` | Represents an independent service offering that can be provisioned by a customer.  
  
### get_logical_product_variant
    
    
    get_logical_product_variant(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.GetLogicalProductVariantRequest,
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
    ) -> (
        google.cloud.productregistry_v1.types.logical_product_variant.LogicalProductVariant
    )

Get details of a LogicalProductVariant.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_get_logical_product_variant():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[GetLogicalProductVariantRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetLogicalProductVariantRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_logical_product_variant](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_get_logical_product_variant)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.GetLogicalProductVariantRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetLogicalProductVariantRequest), dict]]`   
The request object. Request message for GetLogicalProductVariant.  
`name` |  ``str``   
Required. The name of the LogicalProductVariant to retrieve. Format: logicalProducts/{logical_product}/variants/{variant} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.types.LogicalProductVariant](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.LogicalProductVariant)` | Represents a distinct offering derived from a primary product that retains core functionalities but offers specialized features for a specific market segment.  
  
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
  
### get_product_suite
    
    
    get_product_suite(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.GetProductSuiteRequest,
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
    ) -> google.cloud.productregistry_v1.types.product_suite.ProductSuite

Get details of a ProductSuite.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_get_product_suite():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[GetProductSuiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetProductSuiteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_product_suite](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_get_product_suite)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.GetProductSuiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.GetProductSuiteRequest), dict]]`   
The request object. Request message for GetProductSuite.  
`name` |  ``str``   
Required. The name of the ProductSuite to retrieve. Format: productSuites/{product_suite} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.types.ProductSuite](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ProductSuite)` | Represents a unified grouping of products sharing a common brand and market positioning.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.productregistry_v1.services.cloud_product_registry_read_service.transports.base.CloudProductRegistryReadServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_logical_product_variants
    
    
    list_logical_product_variants(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
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
        google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductVariantsAsyncPager
    )

Lists LogicalProductVariants matching given criteria.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_list_logical_product_variants():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[ListLogicalProductVariantsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_logical_product_variants](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_list_logical_product_variants)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest), dict]]`   
The request object. Request message for ListLogicalProductVariants.  
`parent` |  ``str``   
Required. Parent logical product id. Format: logicalProducts/{logical_product} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductVariantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductVariantsAsyncPager)` | Response message for ListLogicalProductVariants. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_logical_products
    
    
    list_logical_products(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.ListLogicalProductsRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductsAsyncPager
    )

Lists LogicalProducts matching given criteria.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_list_logical_products():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[ListLogicalProductsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListLogicalProductsRequest.html)(
        )
    
        # Make the request
        page_result = client.[list_logical_products](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_list_logical_products)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.ListLogicalProductsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListLogicalProductsRequest), dict]]`   
The request object. Request message for ListLogicalProducts.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductsAsyncPager)` | Response message for ListLogicalProducts. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_product_suites
    
    
    list_product_suites(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.ListProductSuitesRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListProductSuitesAsyncPager
    )

Lists ProductSuites.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_list_product_suites():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[ListProductSuitesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListProductSuitesRequest.html)(
        )
    
        # Make the request
        page_result = client.[list_product_suites](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_list_product_suites)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.ListProductSuitesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.ListProductSuitesRequest), dict]]`   
The request object. Request message for ListProductSuites.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListProductSuitesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListProductSuitesAsyncPager)` | Response message for ListProductSuites. Iterating over this object will yield results and resolve additional pages automatically.  
  
### logical_product_path
    
    
    logical_product_path(logical_product: str) -> str

Returns a fully-qualified logical_product string.

### logical_product_variant_path
    
    
    logical_product_variant_path(logical_product: str, variant: str) -> str

Returns a fully-qualified logical_product_variant string.

### lookup_entity
    
    
    lookup_entity(
        request: typing.Optional[
            typing.Union[
                google.cloud.productregistry_v1.types.cloud_product_registry_read_service.LookupEntityRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.productregistry_v1.types.cloud_product_registry_read_service.LookupEntityResponse
    )

Look up entities.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest)
    
    async def sample_lookup_entity():
        # Create a client
        client = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[CloudProductRegistryReadServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [productregistry_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest).[LookupEntityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.LookupEntityRequest.html)(
            lookup_uri="lookup_uri_value",
        )
    
        # Make the request
        response = await client.[lookup_entity](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.services.cloud_product_registry_read_service.CloudProductRegistryReadServiceAsyncClient.html#google_cloud_productregistry_v1_services_cloud_product_registry_read_service_CloudProductRegistryReadServiceAsyncClient_lookup_entity)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.productregistry_v1.types.LookupEntityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.LookupEntityRequest), dict]]`   
The request object. Request message for LookupEntity.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.productregistry_v1.types.LookupEntityResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-productregistry/latest/google.cloud.productregistry_v1.types.LookupEntityResponse)` | Response message for LookupEntity.  
  
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

### parse_logical_product_path
    
    
    parse_logical_product_path(path: str) -> typing.Dict[str, str]

Parses a logical_product path into its component segments.

### parse_logical_product_variant_path
    
    
    parse_logical_product_variant_path(path: str) -> typing.Dict[str, str]

Parses a logical_product_variant path into its component segments.

### parse_product_suite_path
    
    
    parse_product_suite_path(path: str) -> typing.Dict[str, str]

Parses a product_suite path into its component segments.

### product_suite_path
    
    
    product_suite_path(product_suite: str) -> str

Returns a fully-qualified product_suite string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
