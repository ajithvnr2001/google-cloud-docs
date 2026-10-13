---
url: https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client
title: Class WebRiskServiceV1Beta1Client (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:48.810425+00:00
---

# Class WebRiskServiceV1Beta1Client (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class WebRiskServiceV1Beta1Client (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.1  1.11.1  1.10.1  1.9.0  1.8.4  1.7.2  1.6.1  1.5.0  1.4.3  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.0 
    
    
    WebRiskServiceV1Beta1Client(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.transports.base.WebRiskServiceV1Beta1Transport,
                typing.Callable[
                    [...],
                    google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.transports.base.WebRiskServiceV1Beta1Transport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Web Risk v1beta1 API defines an interface to detect malicious URLs on your website and in client applications.

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
`WebRiskServiceV1Beta1Transport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### WebRiskServiceV1Beta1Client
    
    
    WebRiskServiceV1Beta1Client(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.transports.base.WebRiskServiceV1Beta1Transport,
                typing.Callable[
                    [...],
                    google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.transports.base.WebRiskServiceV1Beta1Transport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the web risk service v1 beta1 client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,WebRiskServiceV1Beta1Transport,Callable[..., WebRiskServiceV1Beta1Transport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the WebRiskServiceV1Beta1Transport constructor. If set to None, a transport is chosen automatically.  
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

### compute_threat_list_diff
    
    
    compute_threat_list_diff(
        request: typing.Optional[
            typing.Union[
                google.cloud.webrisk_v1beta1.types.webrisk.ComputeThreatListDiffRequest,
                dict,
            ]
        ] = None,
        *,
        threat_type: typing.Optional[
            google.cloud.webrisk_v1beta1.types.webrisk.ThreatType
        ] = None,
        version_token: typing.Optional[bytes] = None,
        constraints: typing.Optional[
            google.cloud.webrisk_v1beta1.types.webrisk.ComputeThreatListDiffRequest.Constraints
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.webrisk_v1beta1.types.webrisk.ComputeThreatListDiffResponse

Gets the most recent threat list diffs.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import webrisk_v1beta1
    
    def sample_compute_threat_list_diff():
        # Create a client
        client = webrisk_v1beta1.[WebRiskServiceV1Beta1Client](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html)()
    
        # Initialize request argument(s)
        request = webrisk_v1beta1.[ComputeThreatListDiffRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest.html)(
            threat_type="UNWANTED_SOFTWARE",
        )
    
        # Make the request
        response = client.[compute_threat_list_diff](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html#google_cloud_webrisk_v1beta1_services_web_risk_service_v1_beta1_WebRiskServiceV1Beta1Client_compute_threat_list_diff)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest), dict]`   
The request object. Describes an API diff request.  
`threat_type` |  `[google.cloud.webrisk_v1beta1.types.ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ThreatType)`   
The ThreatList to update. This corresponds to the `threat_type` field on the `request` instance; if `request` is provided, this should not be set.  
`version_token` |  `bytes`   
The current version token of the client for the requested list (the client version that was received from the last successful diff). This corresponds to the `version_token` field on the `request` instance; if `request` is provided, this should not be set.  
`constraints` |  `[google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest.Constraints](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ComputeThreatListDiffRequest.Constraints)`   
Required. The constraints associated with this request. This corresponds to the `constraints` field on the `request` instance; if `request` is provided, this should not be set.  
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
`WebRiskServiceV1Beta1Client` | The constructed client.  
  
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
`WebRiskServiceV1Beta1Client` | The constructed client.  
  
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
`WebRiskServiceV1Beta1Client` | The constructed client.  
  
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

### search_hashes
    
    
    search_hashes(
        request: typing.Optional[
            typing.Union[
                google.cloud.webrisk_v1beta1.types.webrisk.SearchHashesRequest, dict
            ]
        ] = None,
        *,
        hash_prefix: typing.Optional[bytes] = None,
        threat_types: typing.Optional[
            typing.MutableSequence[google.cloud.webrisk_v1beta1.types.webrisk.ThreatType]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.webrisk_v1beta1.types.webrisk.SearchHashesResponse

Gets the full hashes that match the requested hash prefix. This is used after a hash prefix is looked up in a threatList and there is a match. The client side threatList only holds partial hashes so the client must query this method to determine if there is a full hash match of a threat.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import webrisk_v1beta1
    
    def sample_search_hashes():
        # Create a client
        client = webrisk_v1beta1.[WebRiskServiceV1Beta1Client](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html)()
    
        # Initialize request argument(s)
        request = webrisk_v1beta1.[SearchHashesRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.SearchHashesRequest.html)(
            threat_types=['UNWANTED_SOFTWARE'],
        )
    
        # Make the request
        response = client.[search_hashes](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html#google_cloud_webrisk_v1beta1_services_web_risk_service_v1_beta1_WebRiskServiceV1Beta1Client_search_hashes)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.webrisk_v1beta1.types.SearchHashesRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.SearchHashesRequest), dict]`   
The request object. Request to return full hashes matched by the provided hash prefixes.  
`hash_prefix` |  `bytes`   
A hash prefix, consisting of the most significant 4-32 bytes of a SHA256 hash. For JSON requests, this field is base64-encoded. This corresponds to the `hash_prefix` field on the `request` instance; if `request` is provided, this should not be set.  
`threat_types` |  `MutableSequence[[google.cloud.webrisk_v1beta1.types.ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ThreatType)]`   
Required. The ThreatLists to search in. This corresponds to the `threat_types` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### search_uris
    
    
    search_uris(
        request: typing.Optional[
            typing.Union[google.cloud.webrisk_v1beta1.types.webrisk.SearchUrisRequest, dict]
        ] = None,
        *,
        uri: typing.Optional[str] = None,
        threat_types: typing.Optional[
            typing.MutableSequence[google.cloud.webrisk_v1beta1.types.webrisk.ThreatType]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.webrisk_v1beta1.types.webrisk.SearchUrisResponse

This method is used to check whether a URI is on a given threatList.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import webrisk_v1beta1
    
    def sample_search_uris():
        # Create a client
        client = webrisk_v1beta1.[WebRiskServiceV1Beta1Client](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html)()
    
        # Initialize request argument(s)
        request = webrisk_v1beta1.[SearchUrisRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.SearchUrisRequest.html)(
            uri="uri_value",
            threat_types=['UNWANTED_SOFTWARE'],
        )
    
        # Make the request
        response = client.[search_uris](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.services.web_risk_service_v1_beta1.WebRiskServiceV1Beta1Client.html#google_cloud_webrisk_v1beta1_services_web_risk_service_v1_beta1_WebRiskServiceV1Beta1Client_search_uris)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.webrisk_v1beta1.types.SearchUrisRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.SearchUrisRequest), dict]`   
The request object. Request to check URI entries against threatLists.  
`uri` |  `str`   
Required. The URI to be checked for matches. This corresponds to the `uri` field on the `request` instance; if `request` is provided, this should not be set.  
`threat_types` |  `MutableSequence[[google.cloud.webrisk_v1beta1.types.ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1beta1.types.ThreatType)]`   
Required. The ThreatLists to search in. This corresponds to the `threat_types` field on the `request` instance; if `request` is provided, this should not be set.  
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
