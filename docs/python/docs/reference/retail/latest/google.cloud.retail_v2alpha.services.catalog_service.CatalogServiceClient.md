---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient
title: Class CatalogServiceClient (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:58.304758+00:00
---

# Class CatalogServiceClient (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CatalogServiceClient (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    CatalogServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2alpha.services.catalog_service.transports.base.CatalogServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2alpha.services.catalog_service.transports.base.CatalogServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing catalog configuration.

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
`CatalogServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CatalogServiceClient
    
    
    CatalogServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2alpha.services.catalog_service.transports.base.CatalogServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2alpha.services.catalog_service.transports.base.CatalogServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the catalog service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CatalogServiceTransport,Callable[..., CatalogServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the CatalogServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### add_catalog_attribute
    
    
    add_catalog_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.AddCatalogAttributeRequest,
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
    ) -> google.cloud.retail_v2alpha.types.catalog.AttributesConfig

Adds the specified xref_CatalogAttribute to the xref_AttributesConfig.

If the xref_CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_add_catalog_attribute():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        catalog_attribute = retail_v2alpha.[CatalogAttribute](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CatalogAttribute.html)()
        catalog_attribute.key = "key_value"
    
        request = retail_v2alpha.[AddCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AddCatalogAttributeRequest.html)(
            attributes_config="attributes_config_value",
            catalog_attribute=catalog_attribute,
        )
    
        # Make the request
        response = client.[add_catalog_attribute](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_add_catalog_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.AddCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AddCatalogAttributeRequest), dict]`   
The request object. Request for CatalogService.AddCatalogAttribute method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)` | Catalog level attribute config.  
  
### attributes_config_path
    
    
    attributes_config_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified attributes_config string.

### batch_remove_catalog_attributes
    
    
    batch_remove_catalog_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.BatchRemoveCatalogAttributesRequest,
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
        google.cloud.retail_v2alpha.types.catalog_service.BatchRemoveCatalogAttributesResponse
    )

Removes all specified xref_CatalogAttributes from the xref_AttributesConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_batch_remove_catalog_attributes():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.BatchRemoveCatalogAttributesRequest.html)(
            attributes_config="attributes_config_value",
            attribute_keys=['attribute_keys_value1', 'attribute_keys_value2'],
        )
    
        # Make the request
        response = client.[batch_remove_catalog_attributes](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_batch_remove_catalog_attributes)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.BatchRemoveCatalogAttributesRequest), dict]`   
The request object. Request for CatalogService.BatchRemoveCatalogAttributes method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.BatchRemoveCatalogAttributesResponse](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.BatchRemoveCatalogAttributesResponse)` | Response of the CatalogService.BatchRemoveCatalogAttributes.  
  
### branch_path
    
    
    branch_path(project: str, location: str, catalog: str, branch: str) -> str

Returns a fully-qualified branch string.

### catalog_path
    
    
    catalog_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified catalog string.

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

### completion_config_path
    
    
    completion_config_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified completion_config string.

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
`CatalogServiceClient` | The constructed client.  
  
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
`CatalogServiceClient` | The constructed client.  
  
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
`CatalogServiceClient` | The constructed client.  
  
### get_attributes_config
    
    
    get_attributes_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.GetAttributesConfigRequest,
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
    ) -> google.cloud.retail_v2alpha.types.catalog.AttributesConfig

Gets an xref_AttributesConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_get_attributes_config():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[GetAttributesConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetAttributesConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_attributes_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_get_attributes_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.GetAttributesConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetAttributesConfigRequest), dict]`   
The request object. Request for CatalogService.GetAttributesConfig method.  
`name` |  `str`   
Required. Full AttributesConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)` | Catalog level attribute config.  
  
### get_completion_config
    
    
    get_completion_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.GetCompletionConfigRequest,
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
    ) -> google.cloud.retail_v2alpha.types.catalog.CompletionConfig

Gets a xref_CompletionConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_get_completion_config():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[GetCompletionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetCompletionConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_completion_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_get_completion_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.GetCompletionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetCompletionConfigRequest), dict]`   
The request object. Request for CatalogService.GetCompletionConfig method.  
`name` |  `str`   
Required. Full CompletionConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/completionConfig` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.CompletionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CompletionConfig)` | Catalog level autocomplete config for customers to customize autocomplete feature's settings.  
  
### get_default_branch
    
    
    get_default_branch(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.GetDefaultBranchRequest,
                dict,
            ]
        ] = None,
        *,
        catalog: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2alpha.types.catalog_service.GetDefaultBranchResponse

Get which branch is currently default branch set by xref_CatalogService.SetDefaultBranch method under a specified parent catalog.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_get_default_branch():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[GetDefaultBranchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetDefaultBranchRequest.html)(
        )
    
        # Make the request
        response = client.[get_default_branch](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_get_default_branch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.GetDefaultBranchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetDefaultBranchRequest), dict]`   
The request object. Request message to show which branch is currently the default branch.  
`catalog` |  `str`   
The parent catalog resource name, such as `projects/*/locations/global/catalogs/default_catalog`. This corresponds to the `catalog` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.GetDefaultBranchResponse](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.GetDefaultBranchResponse)` | Response message of CatalogService.GetDefaultBranch.  
  
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
  
### list_catalogs
    
    
    list_catalogs(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.ListCatalogsRequest, dict
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
    ) -> google.cloud.retail_v2alpha.services.catalog_service.pagers.ListCatalogsPager

Lists all the xref_Catalogs associated with the project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_list_catalogs():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[ListCatalogsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ListCatalogsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_catalogs](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_list_catalogs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.ListCatalogsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ListCatalogsRequest), dict]`   
The request object. Request for CatalogService.ListCatalogs method.  
`parent` |  `str`   
Required. The account resource name with an associated location. If the caller does not have permission to list Catalogs under this location, regardless of whether or not this location exists, a PERMISSION_DENIED error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.services.catalog_service.pagers.ListCatalogsPager](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.pagers.ListCatalogsPager)` | Response for CatalogService.ListCatalogs method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_attributes_config_path
    
    
    parse_attributes_config_path(path: str) -> typing.Dict[str, str]

Parses a attributes_config path into its component segments.

### parse_branch_path
    
    
    parse_branch_path(path: str) -> typing.Dict[str, str]

Parses a branch path into its component segments.

### parse_catalog_path
    
    
    parse_catalog_path(path: str) -> typing.Dict[str, str]

Parses a catalog path into its component segments.

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

### parse_completion_config_path
    
    
    parse_completion_config_path(path: str) -> typing.Dict[str, str]

Parses a completion_config path into its component segments.

### remove_catalog_attribute
    
    
    remove_catalog_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.RemoveCatalogAttributeRequest,
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
    ) -> google.cloud.retail_v2alpha.types.catalog.AttributesConfig

Removes the specified xref_CatalogAttribute from the xref_AttributesConfig.

If the xref_CatalogAttribute to remove does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_remove_catalog_attribute():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.RemoveCatalogAttributeRequest.html)(
            attributes_config="attributes_config_value",
            key="key_value",
        )
    
        # Make the request
        response = client.[remove_catalog_attribute](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_remove_catalog_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.RemoveCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.RemoveCatalogAttributeRequest), dict]`   
The request object. Request for CatalogService.RemoveCatalogAttribute method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)` | Catalog level attribute config.  
  
### replace_catalog_attribute
    
    
    replace_catalog_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.ReplaceCatalogAttributeRequest,
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
    ) -> google.cloud.retail_v2alpha.types.catalog.AttributesConfig

Replaces the specified xref_CatalogAttribute in the xref_AttributesConfig by updating the catalog attribute with the same xref_CatalogAttribute.key.

If the xref_CatalogAttribute to replace does not exist, a NOT_FOUND error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_replace_catalog_attribute():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        catalog_attribute = retail_v2alpha.[CatalogAttribute](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CatalogAttribute.html)()
        catalog_attribute.key = "key_value"
    
        request = retail_v2alpha.[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ReplaceCatalogAttributeRequest.html)(
            attributes_config="attributes_config_value",
            catalog_attribute=catalog_attribute,
        )
    
        # Make the request
        response = client.[replace_catalog_attribute](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_replace_catalog_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.ReplaceCatalogAttributeRequest), dict]`   
The request object. Request for CatalogService.ReplaceCatalogAttribute method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)` | Catalog level attribute config.  
  
### set_default_branch
    
    
    set_default_branch(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.SetDefaultBranchRequest,
                dict,
            ]
        ] = None,
        *,
        catalog: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Set a specified branch id as default branch. API methods such as xref_SearchService.Search, xref_ProductService.GetProduct, xref_ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting xref_SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting xref_SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as xref_SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}.
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set).
  * UserEventService will only join events with products from branch {newBranch}.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_set_default_branch():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2alpha.[SetDefaultBranchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.SetDefaultBranchRequest.html)(
        )
    
        # Make the request
        client.[set_default_branch](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_set_default_branch)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.SetDefaultBranchRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.SetDefaultBranchRequest), dict]`   
The request object. Request message to set a specified branch as new default_branch.  
`catalog` |  `str`   
Full resource name of the catalog, such as `projects/*/locations/global/catalogs/default_catalog`. This corresponds to the `catalog` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### update_attributes_config
    
    
    update_attributes_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.UpdateAttributesConfigRequest,
                dict,
            ]
        ] = None,
        *,
        attributes_config: typing.Optional[
            google.cloud.retail_v2alpha.types.catalog.AttributesConfig
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
    ) -> google.cloud.retail_v2alpha.types.catalog.AttributesConfig

Updates the xref_AttributesConfig.

The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_update_attributes_config():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        attributes_config = retail_v2alpha.[AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig.html)()
        attributes_config.name = "name_value"
    
        request = retail_v2alpha.[UpdateAttributesConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateAttributesConfigRequest.html)(
            attributes_config=attributes_config,
        )
    
        # Make the request
        response = client.[update_attributes_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_update_attributes_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.UpdateAttributesConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateAttributesConfigRequest), dict]`   
The request object. Request for CatalogService.UpdateAttributesConfig method.  
`attributes_config` |  `[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)`   
Required. The AttributesConfig to update. This corresponds to the `attributes_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided AttributesConfig to update. The following is the only supported field: - AttributesConfig.catalog_attributes If not set, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.AttributesConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.AttributesConfig)` | Catalog level attribute config.  
  
### update_catalog
    
    
    update_catalog(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.UpdateCatalogRequest, dict
            ]
        ] = None,
        *,
        catalog: typing.Optional[google.cloud.retail_v2alpha.types.catalog.Catalog] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2alpha.types.catalog.Catalog

Updates the xref_Catalogs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_update_catalog():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        catalog = retail_v2alpha.[Catalog](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.Catalog.html)()
        catalog.name = "name_value"
        catalog.display_name = "display_name_value"
    
        request = retail_v2alpha.[UpdateCatalogRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateCatalogRequest.html)(
            catalog=catalog,
        )
    
        # Make the request
        response = client.[update_catalog](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_update_catalog)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.UpdateCatalogRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateCatalogRequest), dict]`   
The request object. Request for CatalogService.UpdateCatalog method.  
`catalog` |  `[google.cloud.retail_v2alpha.types.Catalog](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.Catalog)`   
Required. The Catalog to update. If the caller does not have permission to update the Catalog, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Catalog to update does not exist, a NOT_FOUND error is returned. This corresponds to the `catalog` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided Catalog to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.Catalog](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.Catalog)` | The catalog configuration.  
  
### update_completion_config
    
    
    update_completion_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2alpha.types.catalog_service.UpdateCompletionConfigRequest,
                dict,
            ]
        ] = None,
        *,
        completion_config: typing.Optional[
            google.cloud.retail_v2alpha.types.catalog.CompletionConfig
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
    ) -> google.cloud.retail_v2alpha.types.catalog.CompletionConfig

Updates the xref_CompletionConfigs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2alpha
    
    def sample_update_completion_config():
        # Create a client
        client = retail_v2alpha.[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        completion_config = retail_v2alpha.[CompletionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CompletionConfig.html)()
        completion_config.name = "name_value"
    
        request = retail_v2alpha.[UpdateCompletionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateCompletionConfigRequest.html)(
            completion_config=completion_config,
        )
    
        # Make the request
        response = client.[update_completion_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.services.catalog_service.CatalogServiceClient.html#google_cloud_retail_v2alpha_services_catalog_service_CatalogServiceClient_update_completion_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2alpha.types.UpdateCompletionConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.UpdateCompletionConfigRequest), dict]`   
The request object. Request for CatalogService.UpdateCompletionConfig method.  
`completion_config` |  `[google.cloud.retail_v2alpha.types.CompletionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CompletionConfig)`   
Required. The CompletionConfig to update. If the caller does not have permission to update the CompletionConfig, then a PERMISSION_DENIED error is returned. If the CompletionConfig to update does not exist, a NOT_FOUND error is returned. This corresponds to the `completion_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided CompletionConfig to update. The following are the only supported fields: - CompletionConfig.matching_order - CompletionConfig.max_suggestions - CompletionConfig.min_prefix_length - CompletionConfig.auto_learning If not set, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2alpha.types.CompletionConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2alpha.types.CompletionConfig)` | Catalog level autocomplete config for customers to customize autocomplete feature's settings.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
