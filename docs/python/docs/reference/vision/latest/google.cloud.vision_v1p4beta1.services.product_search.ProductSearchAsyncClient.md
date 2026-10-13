---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient
title: Class ProductSearchAsyncClient (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:07.557984+00:00
---

# Class ProductSearchAsyncClient (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ProductSearchAsyncClient (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    ProductSearchAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.vision_v1p4beta1.services.product_search.transports.base.ProductSearchTransport,
                typing.Callable[
                    [...],
                    google.cloud.vision_v1p4beta1.services.product_search.transports.base.ProductSearchTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Manages Products and ProductSets of reference images for use in product search. It uses the following resource model:

  * The API has a collection of ProductSet resources, named `projects/*/locations/*/productSets/*`, which acts as a way to put different products into groups to limit identification.



In parallel,

  * The API has a collection of Product resources, named `projects/*/locations/*/products/*`

  * Each Product has a collection of ReferenceImage resources, named `projects/*/locations/*/products/*/referenceImages/*`




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
`ProductSearchTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ProductSearchAsyncClient
    
    
    ProductSearchAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.vision_v1p4beta1.services.product_search.transports.base.ProductSearchTransport,
                typing.Callable[
                    [...],
                    google.cloud.vision_v1p4beta1.services.product_search.transports.base.ProductSearchTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the product search async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ProductSearchTransport,Callable[..., ProductSearchTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ProductSearchTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### add_product_to_product_set
    
    
    add_product_to_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.AddProductToProductSetRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        product: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_add_product_to_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[AddProductToProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.AddProductToProductSetRequest.html)(
            name="name_value",
            product="product_value",
        )
    
        # Make the request
        await client.[add_product_to_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_add_product_to_product_set)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.AddProductToProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.AddProductToProductSetRequest), dict]]`   
The request object. Request message for the `AddProductToProductSet` method.  
`name` |  ``str``   
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`product` |  ``str``   
Required. The resource name for the Product to be added to this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID` This corresponds to the `product` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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

### create_product
    
    
    create_product(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.CreateProductRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        product: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.Product
        ] = None,
        product_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.Product

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is missing or invalid.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_create_product():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[CreateProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateProductRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_create_product)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.CreateProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateProductRequest), dict]]`   
The request object. Request message for the `CreateProduct` method.  
`parent` |  ``str``   
Required. The project in which the Product should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`product` |  `[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product)`   
Required. The product to create. This corresponds to the `product` field on the `request` instance; if `request` is provided, this should not be set.  
`product_id` |  ``str``   
A user-supplied resource id for this Product. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`. This corresponds to the `product_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product)` | A Product contains ReferenceImages.  
  
### create_product_set
    
    
    create_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.CreateProductSetRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        product_set: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.ProductSet
        ] = None,
        product_set_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.ProductSet

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_create_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[CreateProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateProductSetRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_create_product_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.CreateProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateProductSetRequest), dict]]`   
The request object. Request message for the `CreateProductSet` method.  
`parent` |  ``str``   
Required. The project in which the ProductSet should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`product_set` |  `[ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSet)`   
Required. The ProductSet to create. This corresponds to the `product_set` field on the `request` instance; if `request` is provided, this should not be set.  
`product_set_id` |  ``str``   
A user-supplied resource id for this ProductSet. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`. This corresponds to the `product_set_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSet)` | A ProductSet contains Products. A ProductSet can contain a maximum of 1 million reference images. If the limit is exceeded, periodic indexing will fail.  
  
### create_reference_image
    
    
    create_reference_image(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.CreateReferenceImageRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        reference_image: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.ReferenceImage
        ] = None,
        reference_image_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.ReferenceImage

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if the product does not exist.
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected.
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_create_reference_image():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        reference_image = vision_v1p4beta1.[ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ReferenceImage.html)()
        reference_image.uri = "uri_value"
    
        request = vision_v1p4beta1.[CreateReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateReferenceImageRequest.html)(
            parent="parent_value",
            reference_image=reference_image,
        )
    
        # Make the request
        response = await client.[create_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_create_reference_image)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.CreateReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CreateReferenceImageRequest), dict]]`   
The request object. Request message for the `CreateReferenceImage` method.  
`parent` |  ``str``   
Required. Resource name of the product in which to create the reference image. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`reference_image` |  `[ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ReferenceImage)`   
Required. The reference image to create. If an image ID is specified, it is ignored. This corresponds to the `reference_image` field on the `request` instance; if `request` is provided, this should not be set.  
`reference_image_id` |  ``str``   
A user-supplied resource id for the ReferenceImage to be added. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`. This corresponds to the `reference_image_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ReferenceImage)` | A ReferenceImage represents a product image and its associated metadata, such as bounding boxes.  
  
### delete_product
    
    
    delete_product(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.DeleteProductRequest,
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

Permanently deletes a product and its reference images. Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_delete_product():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[DeleteProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteProductRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_delete_product)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.DeleteProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteProductRequest), dict]]`   
The request object. Request message for the `DeleteProduct` method.  
`name` |  ``str``   
Required. Resource name of product to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_product_set
    
    
    delete_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.DeleteProductSetRequest,
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

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_delete_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[DeleteProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteProductSetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_delete_product_set)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.DeleteProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteProductSetRequest), dict]]`   
The request object. Request message for the `DeleteProductSet` method.  
`name` |  ``str``   
Required. Resource name of the ProductSet to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_reference_image
    
    
    delete_reference_image(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.DeleteReferenceImageRequest,
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

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_delete_reference_image():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[DeleteReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteReferenceImageRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_delete_reference_image)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.DeleteReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.DeleteReferenceImageRequest), dict]]`   
The request object. Request message for the `DeleteReferenceImage` method.  
`name` |  ``str``   
Required. The resource name of the reference image to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`ProductSearchAsyncClient` | The constructed client.  
  
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
`ProductSearchAsyncClient` | The constructed client.  
  
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
`ProductSearchAsyncClient` | The constructed client.  
  
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
  
### get_product
    
    
    get_product(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.GetProductRequest,
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
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.Product

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_get_product():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[GetProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetProductRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_get_product)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.GetProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetProductRequest), dict]]`   
The request object. Request message for the `GetProduct` method.  
`name` |  ``str``   
Required. Resource name of the Product to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product)` | A Product contains ReferenceImages.  
  
### get_product_set
    
    
    get_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.GetProductSetRequest,
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
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.ProductSet

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_get_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[GetProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetProductSetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_get_product_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.GetProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetProductSetRequest), dict]]`   
The request object. Request message for the `GetProductSet` method.  
`name` |  ``str``   
Required. Resource name of the ProductSet to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSet)` | A ProductSet contains Products. A ProductSet can contain a maximum of 1 million reference images. If the limit is exceeded, periodic indexing will fail.  
  
### get_reference_image
    
    
    get_reference_image(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.GetReferenceImageRequest,
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
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.ReferenceImage

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_get_reference_image():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[GetReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetReferenceImageRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_get_reference_image)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.GetReferenceImageRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.GetReferenceImageRequest), dict]]`   
The request object. Request message for the `GetReferenceImage` method.  
`name` |  ``str``   
Required. The resource name of the ReferenceImage to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ReferenceImage)` | A ReferenceImage represents a product image and its associated metadata, such as bounding boxes.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.vision_v1p4beta1.services.product_search.transports.base.ProductSearchTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### import_product_sets
    
    
    import_product_sets(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.ImportProductSetsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.ImportProductSetsInputConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The `google.longrunning.Operation][google.longrunning.Operation]` API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see xref_ImportProductSetsGcsSource.csv_file_uri.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_import_product_sets():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[ImportProductSetsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImportProductSetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[import_product_sets](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_import_product_sets)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.ImportProductSetsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImportProductSetsRequest), dict]]`   
The request object. Request message for the `ImportProductSets` method.  
`parent` |  ``str``   
Required. The project in which the ProductSets should be imported. Format is `projects/PROJECT_ID/locations/LOC_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`input_config` |  `[ImportProductSetsInputConfig](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImportProductSetsInputConfig)`   
Required. The input content for the list of requests. This corresponds to the `input_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ImportProductSetsResponse](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImportProductSetsResponse) Response message for the ImportProductSets method. This message is returned by the `google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]` method in the returned `google.longrunning.Operation.response][google.longrunning.Operation.response]` field.  
  
### list_product_sets
    
    
    list_product_sets(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.ListProductSetsRequest,
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
        google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductSetsAsyncPager
    )

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_list_product_sets():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[ListProductSetsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductSetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_product_sets](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_list_product_sets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.ListProductSetsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductSetsRequest), dict]]`   
The request object. Request message for the `ListProductSets` method.  
`parent` |  ``str``   
Required. The project from which ProductSets should be listed. Format is `projects/PROJECT_ID/locations/LOC_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductSetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductSetsAsyncPager)` | Response message for the ListProductSets method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_products
    
    
    list_products(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.ListProductsRequest,
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
        google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsAsyncPager
    )

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_list_products():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[ListProductsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_list_products)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.ListProductsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductsRequest), dict]]`   
The request object. Request message for the `ListProducts` method.  
`parent` |  ``str``   
Required. The project OR ProductSet from which Products should be listed. Format: `projects/PROJECT_ID/locations/LOC_ID` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsAsyncPager](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsAsyncPager)` | Response message for the ListProducts method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_products_in_product_set
    
    
    list_products_in_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.ListProductsInProductSetRequest,
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
        google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsInProductSetAsyncPager
    )

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_list_products_in_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[ListProductsInProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductsInProductSetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_products_in_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_list_products_in_product_set)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.ListProductsInProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListProductsInProductSetRequest), dict]]`   
The request object. Request message for the `ListProductsInProductSet` method.  
`name` |  ``str``   
Required. The ProductSet resource for which to retrieve Products. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsInProductSetAsyncPager](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.pagers.ListProductsInProductSetAsyncPager)` | Response message for the ListProductsInProductSet method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_reference_images
    
    
    list_reference_images(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.ListReferenceImagesRequest,
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
        google.cloud.vision_v1p4beta1.services.product_search.pagers.ListReferenceImagesAsyncPager
    )

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_list_reference_images():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[ListReferenceImagesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListReferenceImagesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_reference_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_list_reference_images)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.ListReferenceImagesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ListReferenceImagesRequest), dict]]`   
The request object. Request message for the `ListReferenceImages` method.  
`parent` |  ``str``   
Required. Resource name of the product containing the reference images. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.services.product_search.pagers.ListReferenceImagesAsyncPager](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.pagers.ListReferenceImagesAsyncPager)` | Response message for the ListReferenceImages method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_product_path
    
    
    parse_product_path(path: str) -> typing.Dict[str, str]

Parses a product path into its component segments.

### parse_product_set_path
    
    
    parse_product_set_path(path: str) -> typing.Dict[str, str]

Parses a product_set path into its component segments.

### parse_reference_image_path
    
    
    parse_reference_image_path(path: str) -> typing.Dict[str, str]

Parses a reference_image path into its component segments.

### product_path
    
    
    product_path(project: str, location: str, product: str) -> str

Returns a fully-qualified product string.

### product_set_path
    
    
    product_set_path(project: str, location: str, product_set: str) -> str

Returns a fully-qualified product_set string.

### purge_products
    
    
    purge_products(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.PurgeProductsRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The `google.longrunning.Operation][google.longrunning.Operation]` API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_purge_products():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[PurgeProductsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.PurgeProductsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[purge_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_purge_products)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.PurgeProductsRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.PurgeProductsRequest), dict]]`   
The request object. Request message for the `PurgeProducts` method.  
`parent` |  ``str``   
Required. The project and location in which the Products should be deleted. Format is `projects/PROJECT_ID/locations/LOC_ID`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### reference_image_path
    
    
    reference_image_path(
        project: str, location: str, product: str, reference_image: str
    ) -> str

Returns a fully-qualified reference_image string.

### remove_product_from_product_set
    
    
    remove_product_from_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.RemoveProductFromProductSetRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        product: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Removes a Product from the specified ProductSet.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_remove_product_from_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.RemoveProductFromProductSetRequest.html)(
            name="name_value",
            product="product_value",
        )
    
        # Make the request
        await client.[remove_product_from_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_remove_product_from_product_set)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.RemoveProductFromProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.RemoveProductFromProductSetRequest), dict]]`   
The request object. Request message for the `RemoveProductFromProductSet` method.  
`name` |  ``str``   
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`product` |  ``str``   
Required. The resource name for the Product to be removed from this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID` This corresponds to the `product` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### update_product
    
    
    update_product(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.UpdateProductRequest,
                dict,
            ]
        ] = None,
        *,
        product: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.Product
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
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.Product

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is present in update_mask.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_update_product():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[UpdateProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.UpdateProductRequest.html)(
        )
    
        # Make the request
        response = await client.[update_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_update_product)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.UpdateProductRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.UpdateProductRequest), dict]]`   
The request object. Request message for the `UpdateProduct` method.  
`product` |  `[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product)`   
Required. The Product resource which replaces the one on the server. product.name is immutable. This corresponds to the `product` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The `FieldMask][google.protobuf.FieldMask]` that specifies which fields to update. If update_mask isn't specified, all mutable fields are to be updated. Valid mask paths include `product_labels`, `display_name`, and `description`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.Product)` | A Product contains ReferenceImages.  
  
### update_product_set
    
    
    update_product_set(
        request: typing.Optional[
            typing.Union[
                google.cloud.vision_v1p4beta1.types.product_search_service.UpdateProductSetRequest,
                dict,
            ]
        ] = None,
        *,
        product_set: typing.Optional[
            google.cloud.vision_v1p4beta1.types.product_search_service.ProductSet
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
    ) -> google.cloud.vision_v1p4beta1.types.product_search_service.ProductSet

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import vision_v1p4beta1
    
    async def sample_update_product_set():
        # Create a client
        client = vision_v1p4beta1.[ProductSearchAsyncClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html)()
    
        # Initialize request argument(s)
        request = vision_v1p4beta1.[UpdateProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.UpdateProductSetRequest.html)(
        )
    
        # Make the request
        response = await client.[update_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.services.product_search.ProductSearchAsyncClient.html#google_cloud_vision_v1p4beta1_services_product_search_ProductSearchAsyncClient_update_product_set)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vision_v1p4beta1.types.UpdateProductSetRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.UpdateProductSetRequest), dict]]`   
The request object. Request message for the `UpdateProductSet` method.  
`product_set` |  `[ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSet)`   
Required. The ProductSet resource which replaces the one on the server. This corresponds to the `product_set` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The `FieldMask][google.protobuf.FieldMask]` that specifies which fields to update. If update_mask isn't specified, all mutable fields are to be updated. Valid mask path is `display_name`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vision_v1p4beta1.types.ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSet)` | A ProductSet contains Products. A ProductSet can contain a maximum of 1 million reference images. If the limit is exceeded, periodic indexing will fail.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
