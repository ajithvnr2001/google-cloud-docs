---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient
title: Class IAMCredentialsClient (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:37.990029+00:00
---

# Class IAMCredentialsClient (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IAMCredentialsClient (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    IAMCredentialsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

A service account is a special type of Google account that belongs to your application or a virtual machine (VM), instead of to an individual end user. Your application assumes the identity of the service account to call Google APIs, so that the users aren't directly involved.

Service account credentials are used to temporarily assume the identity of the service account. Supported credential types include OAuth 2.0 access tokens, OpenID Connect ID tokens, self-signed JSON Web Tokens (JWTs), and more.

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
`IAMCredentialsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### IAMCredentialsClient
    
    
    IAMCredentialsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam credentials client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,IAMCredentialsTransport,Callable[..., IAMCredentialsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the IAMCredentialsTransport constructor. If set to None, a transport is chosen automatically.  
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
`IAMCredentialsClient` | The constructed client.  
  
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
`IAMCredentialsClient` | The constructed client.  
  
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
`IAMCredentialsClient` | The constructed client.  
  
### generate_access_token
    
    
    generate_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        scope: typing.Optional[typing.MutableSequence[str]] = None,
        lifetime: typing.Optional[google.protobuf.duration_pb2.Duration] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenResponse

Generates an OAuth 2.0 access token for a service account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    
    def sample_generate_access_token():
        # Create a client
        client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)()
    
        # Initialize request argument(s)
        request = iam_credentials_v1.[GenerateAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateAccessTokenRequest.html)(
            name="name_value",
            scope=['scope_value1', 'scope_value2'],
        )
    
        # Make the request
        response = client.[generate_access_token](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_generate_access_token)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.iam_credentials_v1.types.GenerateAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateAccessTokenRequest), dict]`   
The request object.  
`name` |  `str`   
Required. The resource name of the service account for which the credentials are requested, in the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`delegates` |  `MutableSequence[str]`   
The sequence of service accounts in a delegation chain. Each service account must be granted the `roles/iam.serviceAccountTokenCreator` role on its next service account in the chain. The last service account in the chain must be granted the `roles/iam.serviceAccountTokenCreator` role on the service account that is specified in the `name` field of the request. The delegates must have the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `delegates` field on the `request` instance; if `request` is provided, this should not be set.  
`scope` |  `MutableSequence[str]`   
Required. Code to identify the scopes to be included in the OAuth 2.0 access token. See <https://developers.google.com/identity/protocols/googlescopes> for more information. At least one value required. This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`lifetime` |  `google.protobuf.duration_pb2.Duration`   
The desired lifetime duration of the access token in seconds. Must be set to a value less than or equal to 3600 (1 hour). If a value is not specified, the token's lifetime will be set to a default value of one hour. This corresponds to the `lifetime` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### generate_id_token
    
    
    generate_id_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateIdTokenRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        audience: typing.Optional[str] = None,
        include_email: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateIdTokenResponse

Generates an OpenID Connect ID token for a service account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    
    def sample_generate_id_token():
        # Create a client
        client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)()
    
        # Initialize request argument(s)
        request = iam_credentials_v1.[GenerateIdTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateIdTokenRequest.html)(
            name="name_value",
            audience="audience_value",
        )
    
        # Make the request
        response = client.[generate_id_token](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_generate_id_token)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.iam_credentials_v1.types.GenerateIdTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateIdTokenRequest), dict]`   
The request object.  
`name` |  `str`   
Required. The resource name of the service account for which the credentials are requested, in the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`delegates` |  `MutableSequence[str]`   
The sequence of service accounts in a delegation chain. Each service account must be granted the `roles/iam.serviceAccountTokenCreator` role on its next service account in the chain. The last service account in the chain must be granted the `roles/iam.serviceAccountTokenCreator` role on the service account that is specified in the `name` field of the request. The delegates must have the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `delegates` field on the `request` instance; if `request` is provided, this should not be set.  
`audience` |  `str`   
Required. The audience for the token, such as the API or account that this token grants access to. This corresponds to the `audience` field on the `request` instance; if `request` is provided, this should not be set.  
`include_email` |  `bool`   
Include the service account email in the token. If set to `true`, the token will contain `email` and `email_verified` claims. This corresponds to the `include_email` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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

### parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

### service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

### sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignBlobResponse

Signs a blob using a service account's system-managed private key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    
    def sample_sign_blob():
        # Create a client
        client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)()
    
        # Initialize request argument(s)
        request = iam_credentials_v1.[SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignBlobRequest.html)(
            name="name_value",
            payload=b'payload_blob',
        )
    
        # Make the request
        response = client.[sign_blob](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_sign_blob)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.iam_credentials_v1.types.SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignBlobRequest), dict]`   
The request object.  
`name` |  `str`   
Required. The resource name of the service account for which the credentials are requested, in the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`delegates` |  `MutableSequence[str]`   
The sequence of service accounts in a delegation chain. Each service account must be granted the `roles/iam.serviceAccountTokenCreator` role on its next service account in the chain. The last service account in the chain must be granted the `roles/iam.serviceAccountTokenCreator` role on the service account that is specified in the `name` field of the request. The delegates must have the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `delegates` field on the `request` instance; if `request` is provided, this should not be set.  
`payload` |  `bytes`   
Required. The bytes to sign. This corresponds to the `payload` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignJwtResponse

Signs a JWT using a service account's system-managed private key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    
    def sample_sign_jwt():
        # Create a client
        client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)()
    
        # Initialize request argument(s)
        request = iam_credentials_v1.[SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignJwtRequest.html)(
            name="name_value",
            payload="payload_value",
        )
    
        # Make the request
        response = client.[sign_jwt](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_sign_jwt)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.iam_credentials_v1.types.SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignJwtRequest), dict]`   
The request object.  
`name` |  `str`   
Required. The resource name of the service account for which the credentials are requested, in the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`delegates` |  `MutableSequence[str]`   
The sequence of service accounts in a delegation chain. Each service account must be granted the `roles/iam.serviceAccountTokenCreator` role on its next service account in the chain. The last service account in the chain must be granted the `roles/iam.serviceAccountTokenCreator` role on the service account that is specified in the `name` field of the request. The delegates must have the following format: `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-` wildcard character is required; replacing it with a project ID is invalid. This corresponds to the `delegates` field on the `request` instance; if `request` is provided, this should not be set.  
`payload` |  `str`   
Required. The JWT payload to sign: a JSON object that contains a JWT Claims Set. This corresponds to the `payload` field on the `request` instance; if `request` is provided, this should not be set.  
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
