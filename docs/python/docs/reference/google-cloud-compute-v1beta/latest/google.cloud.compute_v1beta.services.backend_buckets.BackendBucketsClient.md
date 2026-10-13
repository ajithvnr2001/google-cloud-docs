---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient
title: Class BackendBucketsClient (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:18:13.099763+00:00
---

# Class BackendBucketsClient (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackendBucketsClient (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    BackendBucketsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.backend_buckets.transports.base.BackendBucketsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.backend_buckets.transports.base.BackendBucketsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The BackendBuckets API.

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
`BackendBucketsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### BackendBucketsClient
    
    
    BackendBucketsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.compute_v1beta.services.backend_buckets.transports.base.BackendBucketsTransport,
                typing.Callable[
                    [...],
                    google.cloud.compute_v1beta.services.backend_buckets.transports.base.BackendBucketsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backend buckets client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,BackendBucketsTransport,Callable[..., BackendBucketsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the BackendBucketsTransport constructor. If set to None, a transport is chosen automatically. NOTE: "rest" transport functionality is currently in a beta state (preview). We welcome your feedback via an issue in this library's source repository.  
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

### add_signed_url_key
    
    
    add_signed_url_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddSignedUrlKeyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        signed_url_key_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.SignedUrlKey
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

Adds a key for validating requests with signed URLs for this backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_signed_url_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[add_signed_url_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_add_signed_url_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.AddSignedUrlKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`signed_url_key_resource` |  `[google.cloud.compute_v1beta.types.SignedUrlKey](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SignedUrlKey)`   
The body resource for this request This corresponds to the `signed_url_key_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### add_signed_url_key_unary
    
    
    add_signed_url_key_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AddSignedUrlKeyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        signed_url_key_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.SignedUrlKey
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

Adds a key for validating requests with signed URLs for this backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_add_signed_url_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[add_signed_url_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_add_signed_url_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AddSignedUrlKeyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.AddSignedUrlKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`signed_url_key_resource` |  `[google.cloud.compute_v1beta.types.SignedUrlKey](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SignedUrlKey)`   
The body resource for this request This corresponds to the `signed_url_key_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### aggregated_list
    
    
    aggregated_list(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.AggregatedListBackendBucketsRequest,
                dict,
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
    ) -> google.cloud.compute_v1beta.services.backend_buckets.pagers.AggregatedListPager

Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_aggregated_list():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[AggregatedListBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListBackendBucketsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[aggregated_list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_aggregated_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.AggregatedListBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.AggregatedListBackendBucketsRequest), dict]`   
The request object. A request message for BackendBuckets.AggregatedList. See the method description for details.  
`project` |  `str`   
Name of the project scoping this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.services.backend_buckets.pagers.AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.pagers.AggregatedListPager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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
                google.cloud.compute_v1beta.types.compute.DeleteBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes the specified BackendBucket resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to delete. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_signed_url_key
    
    
    delete_signed_url_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteSignedUrlKeyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        key_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.extended_operation.ExtendedOperation

Deletes a key for validating requests with signed URLs for this backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_signed_url_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            key_name="key_name_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete_signed_url_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_delete_signed_url_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.DeleteSignedUrlKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`key_name` |  `str`   
The name of the Signed URL Key to delete. This corresponds to the `key_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_signed_url_key_unary
    
    
    delete_signed_url_key_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.DeleteSignedUrlKeyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        key_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes a key for validating requests with signed URLs for this backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_delete_signed_url_key():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            key_name="key_name_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete_signed_url_key](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_delete_signed_url_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteSignedUrlKeyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.DeleteSignedUrlKey. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`key_name` |  `str`   
The name of the Signed URL Key to delete. This corresponds to the `key_name` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.DeleteBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Operation

Deletes the specified BackendBucket resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[DeleteBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[delete](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_delete)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.DeleteBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeleteBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Delete. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to delete. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
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
`BackendBucketsClient` | The constructed client.  
  
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
`BackendBucketsClient` | The constructed client.  
  
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
`BackendBucketsClient` | The constructed client.  
  
### get
    
    
    get(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.BackendBucket

Returns the specified BackendBucket resource.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[get](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_get)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Get. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to return. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)` | Represents a Cloud Storage Bucket resource. This Cloud Storage bucket resource is referenced by a URL map of a load balancer. For more information, readBackend Buckets.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.GetIamPolicyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Policy

Gets the access control policy for a resource. May be empty if no such policy or resource exists.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_get_iam_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[GetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetIamPolicyBackendBucketRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.GetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GetIamPolicyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.GetIamPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Policy)` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
                google.cloud.compute_v1beta.types.compute.InsertBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Creates a BackendBucket resource in the specified project using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertBackendBucketRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.InsertBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Creates a BackendBucket resource in the specified project using the data included in the request.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[InsertBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertBackendBucketRequest.html)(
            project="project_value",
        )
    
        # Make the request
        response = client.[insert](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_insert)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.InsertBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InsertBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Insert. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.compute_v1beta.types.compute.ListBackendBucketsRequest, dict
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
    ) -> google.cloud.compute_v1beta.services.backend_buckets.pagers.ListPager

Retrieves the list of BackendBucket resources available to the specified project.
    
    
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListBackendBucketsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[list](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_list)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListBackendBucketsRequest), dict]`   
The request object. A request message for BackendBuckets.List. See the method description for details.  
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
`[google.cloud.compute_v1beta.services.backend_buckets.pagers.ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.pagers.ListPager)` | Contains a list of BackendBucket resources. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_usable
    
    
    list_usable(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.ListUsableBackendBucketsRequest,
                dict,
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
    ) -> google.cloud.compute_v1beta.services.backend_buckets.pagers.ListUsablePager

Retrieves a list of all usable backend buckets in the specified project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_list_usable():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[ListUsableBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListUsableBackendBucketsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[list_usable](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_list_usable)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.ListUsableBackendBucketsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ListUsableBackendBucketsRequest), dict]`   
The request object. A request message for BackendBuckets.ListUsable. See the method description for details.  
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
`[google.cloud.compute_v1beta.services.backend_buckets.pagers.ListUsablePager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.pagers.ListUsablePager)` | Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### patch
    
    
    patch(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to patch. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### patch_unary
    
    
    patch_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.PatchBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_patch():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[PatchBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[patch](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_patch)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.PatchBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PatchBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Patch. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to patch. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_edge_security_policy
    
    
    set_edge_security_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetEdgeSecurityPolicyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        security_policy_reference_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.SecurityPolicyReference
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

Sets the edge security policy for the specified backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_edge_security_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[set_edge_security_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_set_edge_security_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.SetEdgeSecurityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the security policy should be set. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`security_policy_reference_resource` |  `[google.cloud.compute_v1beta.types.SecurityPolicyReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyReference)`   
The body resource for this request This corresponds to the `security_policy_reference_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_edge_security_policy_unary
    
    
    set_edge_security_policy_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetEdgeSecurityPolicyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        security_policy_reference_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.SecurityPolicyReference
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

Sets the edge security policy for the specified backend bucket.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_edge_security_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[set_edge_security_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_set_edge_security_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetEdgeSecurityPolicyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.SetEdgeSecurityPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to which the security policy should be set. The name should conform to RFC1035. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`security_policy_reference_resource` |  `[google.cloud.compute_v1beta.types.SecurityPolicyReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyReference)`   
The body resource for this request This corresponds to the `security_policy_reference_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.SetIamPolicyBackendBucketRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        global_set_policy_request_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.GlobalSetPolicyRequest
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.compute_v1beta.types.compute.Policy

Sets the access control policy on the specified resource. Replaces any existing policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_set_iam_policy():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[SetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetIamPolicyBackendBucketRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.SetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SetIamPolicyBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.SetIamPolicy. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`resource` |  `str`   
Name or id of the resource for this request. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`global_set_policy_request_resource` |  `[google.cloud.compute_v1beta.types.GlobalSetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.GlobalSetPolicyRequest)`   
The body resource for this request This corresponds to the `global_set_policy_request_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.compute_v1beta.types.Policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Policy)` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.TestIamPermissionsBackendBucketRequest,
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
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[TestIamPermissionsBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsBackendBucketRequest.html)(
            project="project_value",
            resource="resource_value",
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.TestIamPermissionsBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TestIamPermissionsBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.TestIamPermissions. See the method description for details.  
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
  
### update
    
    
    update(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Updates the specified BackendBucket resource with the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to update. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### update_unary
    
    
    update_unary(
        request: typing.Optional[
            typing.Union[
                google.cloud.compute_v1beta.types.compute.UpdateBackendBucketRequest, dict
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        backend_bucket: typing.Optional[str] = None,
        backend_bucket_resource: typing.Optional[
            google.cloud.compute_v1beta.types.compute.BackendBucket
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

Updates the specified BackendBucket resource with the data included in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest)
    
    def sample_update():
        # Create a client
        client = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[BackendBucketsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html)()
    
        # Initialize request argument(s)
        request = [compute_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest).[UpdateBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateBackendBucketRequest.html)(
            backend_bucket="backend_bucket_value",
            project="project_value",
        )
    
        # Make the request
        response = client.[update](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.backend_buckets.BackendBucketsClient.html#google_cloud_compute_v1beta_services_backend_buckets_BackendBucketsClient_update)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.compute_v1beta.types.UpdateBackendBucketRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.UpdateBackendBucketRequest), dict]`   
The request object. A request message for BackendBuckets.Update. See the method description for details.  
`project` |  `str`   
Project ID for this request. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket` |  `str`   
Name of the BackendBucket resource to update. This corresponds to the `backend_bucket` field on the `request` instance; if `request` is provided, this should not be set.  
`backend_bucket_resource` |  `[google.cloud.compute_v1beta.types.BackendBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BackendBucket)`   
The body resource for this request This corresponds to the `backend_bucket_resource` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
