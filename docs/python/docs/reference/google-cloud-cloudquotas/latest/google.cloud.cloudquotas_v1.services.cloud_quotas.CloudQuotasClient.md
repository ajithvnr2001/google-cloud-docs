---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient
title: Class CloudQuotasClient (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:59.201777+00:00
---

# Class CloudQuotasClient (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudQuotasClient (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.18 
    
    
    CloudQuotasClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.cloudquotas_v1.services.cloud_quotas.transports.base.CloudQuotasTransport,
                typing.Callable[
                    [...],
                    google.cloud.cloudquotas_v1.services.cloud_quotas.transports.base.CloudQuotasTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

  * List/Get the metadata and current status of the quotas for a service.
  * Create/Update quota preferencess that declare the preferred quota values.
  * Check the status of a quota preference request.
  * List/Get pending and historical quota preference.



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
`CloudQuotasTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudQuotasClient
    
    
    CloudQuotasClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.cloudquotas_v1.services.cloud_quotas.transports.base.CloudQuotasTransport,
                typing.Callable[
                    [...],
                    google.cloud.cloudquotas_v1.services.cloud_quotas.transports.base.CloudQuotasTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud quotas client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudQuotasTransport,Callable[..., CloudQuotasTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudQuotasTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_quota_preference
    
    
    create_quota_preference(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.CreateQuotaPreferenceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        quota_preference: typing.Optional[
            google.cloud.cloudquotas_v1.types.resources.QuotaPreference
        ] = None,
        quota_preference_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.cloudquotas_v1.types.resources.QuotaPreference

Creates a new QuotaPreference that declares the desired value for a quota.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_create_quota_preference():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        quota_preference = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference.html)()
        quota_preference.quota_config.preferred_value = 1595
        quota_preference.service = "service_value"
        quota_preference.quota_id = "quota_id_value"
    
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.CreateQuotaPreferenceRequest.html)(
            parent="parent_value",
            quota_preference=quota_preference,
        )
    
        # Make the request
        response = client.[create_quota_preference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_create_quota_preference)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.CreateQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.CreateQuotaPreferenceRequest), dict]`   
The request object. Message for creating a QuotaPreference  
`parent` |  `str`   
Required. Identifier. Value for parent. Example: `projects/123/locations/global` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`quota_preference` |  `[google.cloud.cloudquotas_v1.types.QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference)`   
Required. The resource being created This corresponds to the `quota_preference` field on the `request` instance; if `request` is provided, this should not be set.  
`quota_preference_id` |  `str`   
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one. This corresponds to the `quota_preference_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.types.QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference)` | QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.  
  
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
`CloudQuotasClient` | The constructed client.  
  
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
`CloudQuotasClient` | The constructed client.  
  
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
`CloudQuotasClient` | The constructed client.  
  
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
  
### get_quota_info
    
    
    get_quota_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.GetQuotaInfoRequest, dict
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
    ) -> google.cloud.cloudquotas_v1.types.resources.QuotaInfo

Retrieve the QuotaInfo of a quota for a project, folder or organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_get_quota_info():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[GetQuotaInfoRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaInfoRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_quota_info](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_get_quota_info)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.GetQuotaInfoRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaInfoRequest), dict]`   
The request object. Message for getting a QuotaInfo  
`name` |  `str`   
Required. Identifier. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.types.QuotaInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaInfo)` | QuotaInfo represents information about a particular quota for a given project, folder or organization.  
  
### get_quota_preference
    
    
    get_quota_preference(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.GetQuotaPreferenceRequest,
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
    ) -> google.cloud.cloudquotas_v1.types.resources.QuotaPreference

Gets details of a single QuotaPreference.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_get_quota_preference():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[GetQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaPreferenceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_quota_preference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_get_quota_preference)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.GetQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaPreferenceRequest), dict]`   
The request object. Message for getting a QuotaPreference  
`name` |  `str`   
Required. Identifier. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.types.QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference)` | QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.  
  
### list_quota_infos
    
    
    list_quota_infos(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.ListQuotaInfosRequest, dict
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
    ) -> google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaInfosPager

Lists QuotaInfos of all quotas for a given project, folder or organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_list_quota_infos():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[ListQuotaInfosRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.ListQuotaInfosRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_quota_infos](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_list_quota_infos)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.ListQuotaInfosRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.ListQuotaInfosRequest), dict]`   
The request object. Message for requesting list of QuotaInfos  
`parent` |  `str`   
Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaInfosPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaInfosPager)` | Message for response to listing QuotaInfos Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_quota_preferences
    
    
    list_quota_preferences(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.ListQuotaPreferencesRequest,
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
    ) -> google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaPreferencesPager

Lists QuotaPreferences in a given project, folder or organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_list_quota_preferences():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[ListQuotaPreferencesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.ListQuotaPreferencesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_quota_preferences](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_list_quota_preferences)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.ListQuotaPreferencesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.ListQuotaPreferencesRequest), dict]`   
The request object. Message for requesting list of QuotaPreferences  
`parent` |  `str`   
Required. Identifier. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaPreferencesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.pagers.ListQuotaPreferencesPager)` | Message for response to listing QuotaPreferences Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_quota_info_path
    
    
    parse_quota_info_path(path: str) -> typing.Dict[str, str]

Parses a quota_info path into its component segments.

### parse_quota_preference_path
    
    
    parse_quota_preference_path(path: str) -> typing.Dict[str, str]

Parses a quota_preference path into its component segments.

### quota_info_path
    
    
    quota_info_path(project: str, location: str, service: str, quota_info: str) -> str

Returns a fully-qualified quota_info string.

### quota_preference_path
    
    
    quota_preference_path(project: str, location: str, quota_preference: str) -> str

Returns a fully-qualified quota_preference string.

### update_quota_preference
    
    
    update_quota_preference(
        request: typing.Optional[
            typing.Union[
                google.cloud.cloudquotas_v1.types.cloudquotas.UpdateQuotaPreferenceRequest,
                dict,
            ]
        ] = None,
        *,
        quota_preference: typing.Optional[
            google.cloud.cloudquotas_v1.types.resources.QuotaPreference
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
    ) -> google.cloud.cloudquotas_v1.types.resources.QuotaPreference

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    def sample_update_quota_preference():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        quota_preference = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference.html)()
        quota_preference.quota_config.preferred_value = 1595
        quota_preference.service = "service_value"
        quota_preference.quota_id = "quota_id_value"
    
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.UpdateQuotaPreferenceRequest.html)(
            quota_preference=quota_preference,
        )
    
        # Make the request
        response = client.[update_quota_preference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_update_quota_preference)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.cloudquotas_v1.types.UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.UpdateQuotaPreferenceRequest), dict]`   
The request object. Message for updating a QuotaPreference  
`quota_preference` |  `[google.cloud.cloudquotas_v1.types.QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference)`   
Required. The resource being updated This corresponds to the `quota_preference` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.cloudquotas_v1.types.QuotaPreference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.QuotaPreference)` | QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
