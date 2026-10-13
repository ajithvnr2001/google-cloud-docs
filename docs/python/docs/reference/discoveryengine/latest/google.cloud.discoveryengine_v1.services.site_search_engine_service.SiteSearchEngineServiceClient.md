---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient
title: Class SiteSearchEngineServiceClient (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:30.679318+00:00
---

# Class SiteSearchEngineServiceClient (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SiteSearchEngineServiceClient (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SiteSearchEngineServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.site_search_engine_service.transports.base.SiteSearchEngineServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.site_search_engine_service.transports.base.SiteSearchEngineServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing site search related resources.

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
`SiteSearchEngineServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### SiteSearchEngineServiceClient
    
    
    SiteSearchEngineServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.site_search_engine_service.transports.base.SiteSearchEngineServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.site_search_engine_service.transports.base.SiteSearchEngineServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the site search engine service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SiteSearchEngineServiceTransport,Callable[..., SiteSearchEngineServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the SiteSearchEngineServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### batch_create_target_sites
    
    
    batch_create_target_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.BatchCreateTargetSitesRequest,
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
    ) -> google.api_core.operation.Operation

Creates xref_TargetSite in a batch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_batch_create_target_sites():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        requests = discoveryengine_v1.[CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateTargetSiteRequest.html)()
        requests.parent = "parent_value"
        requests.target_site.provided_uri_pattern = "provided_uri_pattern_value"
    
        request = discoveryengine_v1.[BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesRequest.html)(
            parent="parent_value",
            requests=requests,
        )
    
        # Make the request
        operation = client.[batch_create_target_sites](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_batch_create_target_sites)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesRequest), dict]`   
The request object. Request message for SiteSearchEngineService.BatchCreateTargetSites method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BatchCreateTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesResponse) Response message for SiteSearchEngineService.BatchCreateTargetSites method.  
  
### batch_verify_target_sites
    
    
    batch_verify_target_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.BatchVerifyTargetSitesRequest,
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
    ) -> google.api_core.operation.Operation

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_batch_verify_target_sites():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = client.[batch_verify_target_sites](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_batch_verify_target_sites)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesRequest), dict]`   
The request object. Request message for SiteSearchEngineService.BatchVerifyTargetSites method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesResponse) Response message for SiteSearchEngineService.BatchVerifyTargetSites method.  
  
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

### create_sitemap
    
    
    create_sitemap(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.CreateSitemapRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        sitemap: typing.Optional[
            google.cloud.discoveryengine_v1.types.site_search_engine.Sitemap
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

Creates a xref_Sitemap.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_create_sitemap():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        sitemap = discoveryengine_v1.[Sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Sitemap.html)()
        sitemap.uri = "uri_value"
    
        request = discoveryengine_v1.[CreateSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSitemapRequest.html)(
            parent="parent_value",
            sitemap=sitemap,
        )
    
        # Make the request
        operation = client.[create_sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_create_sitemap)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.CreateSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSitemapRequest), dict]`   
The request object. Request message for SiteSearchEngineService.CreateSitemap method.  
`parent` |  `str`   
Required. Parent resource name of the SiteSearchEngine, such as `projects/_/locations/_ /collections/_/dataStores/_ /siteSearchEngine`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`sitemap` |  `[google.cloud.discoveryengine_v1.types.Sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Sitemap)`   
Required. The Sitemap to create. This corresponds to the `sitemap` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Sitemap A sitemap for the SiteSearchEngine.  
  
### create_target_site
    
    
    create_target_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.CreateTargetSiteRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target_site: typing.Optional[
            google.cloud.discoveryengine_v1.types.site_search_engine.TargetSite
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

Creates a xref_TargetSite.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_create_target_site():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        target_site = discoveryengine_v1.[TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.html)()
        target_site.provided_uri_pattern = "provided_uri_pattern_value"
    
        request = discoveryengine_v1.[CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateTargetSiteRequest.html)(
            parent="parent_value",
            target_site=target_site,
        )
    
        # Make the request
        operation = client.[create_target_site](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_create_target_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateTargetSiteRequest), dict]`   
The request object. Request message for SiteSearchEngineService.CreateTargetSite method.  
`parent` |  `str`   
Required. Parent resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`target_site` |  `[google.cloud.discoveryengine_v1.types.TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite)`   
Required. The TargetSite to create. This corresponds to the `target_site` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be TargetSite A target site for the SiteSearchEngine.  
  
### delete_sitemap
    
    
    delete_sitemap(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.DeleteSitemapRequest,
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

Deletes a xref_Sitemap.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_delete_sitemap():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSitemapRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_delete_sitemap)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.DeleteSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSitemapRequest), dict]`   
The request object. Request message for SiteSearchEngineService.DeleteSitemap method.  
`name` |  `str`   
Required. Full resource name of Sitemap, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/sitemaps/{sitemap}`. If the caller does not have permission to access the Sitemap, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested Sitemap does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_target_site
    
    
    delete_target_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.DeleteTargetSiteRequest,
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

Deletes a xref_TargetSite.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_delete_target_site():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteTargetSiteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_target_site](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_delete_target_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.DeleteTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteTargetSiteRequest), dict]`   
The request object. Request message for SiteSearchEngineService.DeleteTargetSite method.  
`name` |  `str`   
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### disable_advanced_site_search
    
    
    disable_advanced_site_search(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.DisableAdvancedSiteSearchRequest,
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
    ) -> google.api_core.operation.Operation

Downgrade from advanced site search to basic site search.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_disable_advanced_site_search():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchRequest.html)(
            site_search_engine="site_search_engine_value",
        )
    
        # Make the request
        operation = client.[disable_advanced_site_search](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_disable_advanced_site_search)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchRequest), dict]`   
The request object. Request message for SiteSearchEngineService.DisableAdvancedSiteSearch method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchResponse) Response message for SiteSearchEngineService.DisableAdvancedSiteSearch method.  
  
### enable_advanced_site_search
    
    
    enable_advanced_site_search(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.EnableAdvancedSiteSearchRequest,
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
    ) -> google.api_core.operation.Operation

Upgrade from basic site search to advanced site search.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_enable_advanced_site_search():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchRequest.html)(
            site_search_engine="site_search_engine_value",
        )
    
        # Make the request
        operation = client.[enable_advanced_site_search](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_enable_advanced_site_search)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchRequest), dict]`   
The request object. Request message for SiteSearchEngineService.EnableAdvancedSiteSearch method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchResponse) Response message for SiteSearchEngineService.EnableAdvancedSiteSearch method.  
  
### fetch_domain_verification_status
    
    
    fetch_domain_verification_status(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.FetchDomainVerificationStatusRequest,
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
        google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager
    )

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_fetch_domain_verification_status():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusRequest.html)(
            site_search_engine="site_search_engine_value",
        )
    
        # Make the request
        page_result = client.[fetch_domain_verification_status](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_fetch_domain_verification_status)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusRequest), dict]`   
The request object. Request message for SiteSearchEngineService.FetchDomainVerificationStatus method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager)` | Response message for SiteSearchEngineService.FetchDomainVerificationStatus method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### fetch_sitemaps
    
    
    fetch_sitemaps(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.FetchSitemapsRequest,
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
        google.cloud.discoveryengine_v1.types.site_search_engine_service.FetchSitemapsResponse
    )

Fetch xref_Sitemaps in a xref_DataStore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_fetch_sitemaps():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[FetchSitemapsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[fetch_sitemaps](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_fetch_sitemaps)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.FetchSitemapsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest), dict]`   
The request object. Request message for SiteSearchEngineService.FetchSitemaps method.  
`parent` |  `str`   
Required. Parent resource name of the SiteSearchEngine, such as `projects/_/locations/_ /collections/_/dataStores/_ /siteSearchEngine`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.FetchSitemapsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsResponse)` | Response message for SiteSearchEngineService.FetchSitemaps method.  
  
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
`SiteSearchEngineServiceClient` | The constructed client.  
  
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
`SiteSearchEngineServiceClient` | The constructed client.  
  
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
`SiteSearchEngineServiceClient` | The constructed client.  
  
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
  
### get_site_search_engine
    
    
    get_site_search_engine(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.GetSiteSearchEngineRequest,
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
    ) -> google.cloud.discoveryengine_v1.types.site_search_engine.SiteSearchEngine

Gets the xref_SiteSearchEngine.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_get_site_search_engine():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetSiteSearchEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSiteSearchEngineRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_site_search_engine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_get_site_search_engine)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.GetSiteSearchEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSiteSearchEngineRequest), dict]`   
The request object. Request message for SiteSearchEngineService.GetSiteSearchEngine method.  
`name` |  `str`   
Required. Resource name of SiteSearchEngine, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to access the [SiteSearchEngine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.SiteSearchEngine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteSearchEngine)` | SiteSearchEngine captures DataStore level site search persisting configurations. It is a singleton value per data store.  
  
### get_target_site
    
    
    get_target_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.GetTargetSiteRequest,
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
    ) -> google.cloud.discoveryengine_v1.types.site_search_engine.TargetSite

Gets a xref_TargetSite.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_get_target_site():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetTargetSiteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_target_site](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_get_target_site)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.GetTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetTargetSiteRequest), dict]`   
The request object. Request message for SiteSearchEngineService.GetTargetSite method.  
`name` |  `str`   
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite)` | A target site for the SiteSearchEngine.  
  
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
  
### list_target_sites
    
    
    list_target_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesRequest,
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
        google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager
    )

Gets a list of xref_TargetSites.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_list_target_sites():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_target_sites](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_list_target_sites)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesRequest), dict]`   
The request object. Request message for SiteSearchEngineService.ListTargetSites method.  
`parent` |  `str`   
Required. The parent site search engine resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to list TargetSites under this site search engine, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager)` | Response message for SiteSearchEngineService.ListTargetSites method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_site_search_engine_path
    
    
    parse_site_search_engine_path(path: str) -> typing.Dict[str, str]

Parses a site_search_engine path into its component segments.

### parse_sitemap_path
    
    
    parse_sitemap_path(path: str) -> typing.Dict[str, str]

Parses a sitemap path into its component segments.

### parse_target_site_path
    
    
    parse_target_site_path(path: str) -> typing.Dict[str, str]

Parses a target_site path into its component segments.

### recrawl_uris
    
    
    recrawl_uris(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.RecrawlUrisRequest,
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
    ) -> google.api_core.operation.Operation

Request on-demand recrawl for a list of URIs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_recrawl_uris():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisRequest.html)(
            site_search_engine="site_search_engine_value",
            uris=['uris_value1', 'uris_value2'],
        )
    
        # Make the request
        operation = client.[recrawl_uris](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_recrawl_uris)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisRequest), dict]`   
The request object. Request message for SiteSearchEngineService.RecrawlUris method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [RecrawlUrisResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse) Response message for SiteSearchEngineService.RecrawlUris method.  
  
### site_search_engine_path
    
    
    site_search_engine_path(project: str, location: str, data_store: str) -> str

Returns a fully-qualified site_search_engine string.

### sitemap_path
    
    
    sitemap_path(project: str, location: str, data_store: str, sitemap: str) -> str

Returns a fully-qualified sitemap string.

### target_site_path
    
    
    target_site_path(
        project: str, location: str, data_store: str, target_site: str
    ) -> str

Returns a fully-qualified target_site string.

### update_target_site
    
    
    update_target_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.site_search_engine_service.UpdateTargetSiteRequest,
                dict,
            ]
        ] = None,
        *,
        target_site: typing.Optional[
            google.cloud.discoveryengine_v1.types.site_search_engine.TargetSite
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

Updates a xref_TargetSite.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    def sample_update_target_site():
        # Create a client
        client = discoveryengine_v1.[SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html)()
    
        # Initialize request argument(s)
        target_site = discoveryengine_v1.[TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.html)()
        target_site.provided_uri_pattern = "provided_uri_pattern_value"
    
        request = discoveryengine_v1.[UpdateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateTargetSiteRequest.html)(
            target_site=target_site,
        )
    
        # Make the request
        operation = client.[update_target_site](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient.html#google_cloud_discoveryengine_v1_services_site_search_engine_service_SiteSearchEngineServiceClient_update_target_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.discoveryengine_v1.types.UpdateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateTargetSiteRequest), dict]`   
The request object. Request message for SiteSearchEngineService.UpdateTargetSite method.  
`target_site` |  `[google.cloud.discoveryengine_v1.types.TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite)`   
Required. The target site to update. If the caller does not have permission to update the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the TargetSite to update does not exist, a NOT_FOUND error is returned. This corresponds to the `target_site` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be TargetSite A target site for the SiteSearchEngine.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
