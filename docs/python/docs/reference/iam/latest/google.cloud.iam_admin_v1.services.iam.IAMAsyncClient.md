---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient
title: Class IAMAsyncClient (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:30.738382+00:00
---

# Class IAMAsyncClient (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IAMAsyncClient (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    IAMAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Creates and manages Identity and Access Management (IAM) resources.

You can use this service to work with all of the following resources:

  * **Service accounts** , which identify an application or a virtual machine (VM) instance rather than a person
  * **Service account keys** , which service accounts use to authenticate with Google APIs
  * **IAM policies for service accounts** , which specify the roles that a principal has for the service account
  * **IAM custom roles** , which help you limit the number of permissions that you grant to principals



In addition, you can use this service to complete the following tasks, among others:

  * Test whether a service account can use specific permissions
  * Check which roles you can grant for a specific resource
  * Lint, or validate, condition expressions in an IAM policy



When you read data from the IAM API, each read is eventually consistent. In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. To deal with this behavior, your application can retry the request with truncated exponential backoff.

In contrast, writing data to the IAM API is sequentially consistent. In other words, write operations are always processed in the order in which they were received.

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
`IAMTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### IAMAsyncClient
    
    
    IAMAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,IAMTransport,Callable[..., IAMTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the IAMTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_role
    
    
    create_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.CreateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Creates a new custom `Role][google.iam.admin.v1.Role]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_create_role():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[CreateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateRoleRequest.html)(
        )
    
        # Make the request
        response = await client.[create_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_role)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.CreateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateRoleRequest), dict]]`   
The request object. The request to create a new role.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)` | A role in the Identity and Access Management API.  
  
### create_service_account
    
    
    create_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        service_account: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccount
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Creates a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_create_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[CreateServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountRequest.html)(
            name="name_value",
            account_id="account_id_value",
        )
    
        # Make the request
        response = await client.[create_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.CreateServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountRequest), dict]]`   
The request object. The service account create request.  
`name` |  ``str``   
Required. The resource name of the project associated with the service accounts, such as `projects/my-project-123`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`account_id` |  ``str``   
Required. The account id that is used to generate the service account email address and a stable unique id. It is unique within a project, must be 6-30 characters long, and match the regular expression `[a-z](https://docs.cloud.google.com/python/docs/reference/iam/latest/\[-a-z0-9\]*\[a-z0-9\])` to comply with RFC1035. This corresponds to the `account_id` field on the `request` instance; if `request` is provided, this should not be set.  
`service_account` |  `[ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)`   
The `ServiceAccount][google.iam.admin.v1.ServiceAccount]` resource to create. Currently, only the following values are user assignable: `display_name` and `description`. This corresponds to the `service_account` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)` | An IAM service account. A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the [overview of service accounts](https://cloud.google.com/iam/help/service-accounts/overview). When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.  
  
### create_service_account_key
    
    
    create_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        private_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPrivateKeyType
        ] = None,
        key_algorithm: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountKeyAlgorithm
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Creates a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_create_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[CreateServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[create_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_service_account_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.CreateServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountKeyRequest), dict]]`   
The request object. The service account key create request.  
`name` |  ``str``   
Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`private_key_type` |  `[ServiceAccountPrivateKeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountPrivateKeyType)`   
The output format of the private key. The default value is `TYPE_GOOGLE_CREDENTIALS_FILE`, which is the Google Credentials File format. This corresponds to the `private_key_type` field on the `request` instance; if `request` is provided, this should not be set.  
`key_algorithm` |  `[ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKeyAlgorithm)`   
Which type of key and algorithm to use for the key. The default is currently a 2K RSA key. However this may change in the future. This corresponds to the `key_algorithm` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccountKey](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKey)` | Represents a service account key. A service account has two sets of key-pairs: user-managed, and system-managed. User-managed key-pairs can be created and deleted by users. Users are responsible for rotating these keys periodically to ensure security of their service accounts. Users retain the private key of these key-pairs, and Google retains ONLY the public key. System-managed keys are automatically rotated by Google, and are used for signing for a maximum of two weeks. The rotation process is probabilistic, and usage of the new key will gradually ramp up and down over the key's lifetime. If you cache the public key set for a service account, we recommend that you update the cache every 15 minutes. User-managed keys can be added and removed at any time, so it is important to update the cache frequently. For Google-managed keys, Google will publish a key at least 6 hours before it is first used for signing and will keep publishing it for at least 6 hours after it was last used for signing. Public keys for all service accounts are also published at the OAuth2 Service Account API.  
  
### delete_role
    
    
    delete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.DeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Deletes a custom `Role][google.iam.admin.v1.Role]`.

When you delete a custom role, the following changes occur immediately:

  * You cannot bind a principal to the custom role in an IAM `Policy][google.iam.v1.Policy]`.
  * Existing bindings to the custom role are not changed, but they have no effect.
  * By default, the response from `ListRoles][google.iam.admin.v1.IAM.ListRoles]` does not include the custom role.



You have 7 days to undelete the custom role. After 7 days, the following changes occur:

  * The custom role is permanently deleted and cannot be recovered.
  * If an IAM policy contains a binding to the custom role, the binding is permanently removed.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_delete_role():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[DeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest.html)(
        )
    
        # Make the request
        response = await client.[delete_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_role)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.DeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest), dict]]`   
The request object. The request to delete an existing role.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)` | A role in the Identity and Access Management API.  
  
### delete_service_account
    
    
    delete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountRequest, dict
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

Deletes a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

**Warning:** After you delete a service account, you might not be able to undelete it. If you know that you need to re-enable the service account in the future, use `DisableServiceAccount][google.iam.admin.v1.IAM.DisableServiceAccount]` instead.

If you delete a service account, IAM permanently removes the service account 30 days later. Google Cloud cannot recover the service account after it is permanently removed, even if you file a support request.

To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use `DisableServiceAccount][google.iam.admin.v1.IAM.DisableServiceAccount]` to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_delete_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[DeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_service_account)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.DeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountRequest), dict]]`   
The request object. The service account delete request.  
`name` |  ``str``   
Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_service_account_key
    
    
    delete_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountKeyRequest, dict
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

Deletes a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_delete_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_service_account_key)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountKeyRequest), dict]]`   
The request object. The service account key delete request.  
`name` |  ``str``   
Required. The resource name of the service account key in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### disable_service_account
    
    
    disable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountRequest, dict
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
    ) -> None

Disables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` immediately.

If an application uses the service account to authenticate, that application can no longer call Google APIs or access Google Cloud resources. Existing access tokens for the service account are rejected, and requests for new access tokens will fail.

To re-enable the service account, use `EnableServiceAccount][google.iam.admin.v1.IAM.EnableServiceAccount]`. After you re-enable the service account, its existing access tokens will be accepted, and you can request new access tokens.

To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use this method to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account with `DeleteServiceAccount][google.iam.admin.v1.IAM.DeleteServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_disable_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[DisableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountRequest.html)(
        )
    
        # Make the request
        await client.[disable_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_disable_service_account)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.DisableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountRequest), dict]]`   
The request object. The service account disable request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### disable_service_account_key
    
    
    disable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountKeyRequest, dict
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

Disable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`. A disabled service account key can be re-enabled with `EnableServiceAccountKey][google.iam.admin.v1.IAM.EnableServiceAccountKey]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_disable_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[DisableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[disable_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_disable_service_account_key)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.DisableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountKeyRequest), dict]]`   
The request object. The service account key disable request.  
`name` |  ``str``   
Required. The resource name of the service account key in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### enable_service_account
    
    
    enable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountRequest, dict
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
    ) -> None

Enables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that was disabled by `DisableServiceAccount][google.iam.admin.v1.IAM.DisableServiceAccount]`.

If the service account is already enabled, then this method has no effect.

If the service account was disabled by other means—for example, if Google disabled the service account because it was compromised—you cannot use this method to enable the service account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_enable_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[EnableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountRequest.html)(
        )
    
        # Make the request
        await client.[enable_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_enable_service_account)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.EnableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountRequest), dict]]`   
The request object. The service account enable request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### enable_service_account_key
    
    
    enable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountKeyRequest, dict
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

Enable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_enable_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[EnableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[enable_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_enable_service_account_key)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.EnableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountKeyRequest), dict]]`   
The request object. The service account key enable request.  
`name` |  ``str``   
Required. The resource name of the service account key in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`IAMAsyncClient` | The constructed client.  
  
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
`IAMAsyncClient` | The constructed client.  
  
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
`IAMAsyncClient` | The constructed client.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`. This IAM policy specifies which principals have access to the service account.

This method does not tell you whether the service account has been granted any roles on other resources. To check whether a service account has role grants on a resource, use the `getIamPolicy` method for that resource. For example, to view the role grants for a project, call the Resource Manager API's ``projects.getIamPolicy` <https://cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy>`__ method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_get_iam_policy():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = await client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
  
### get_role
    
    
    get_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Gets the definition of a `Role][google.iam.admin.v1.Role]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_get_role():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[GetRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest.html)(
        )
    
        # Make the request
        response = await client.[get_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_role)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.GetRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest), dict]]`   
The request object. The request to get the definition of an existing role.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)` | A role in the Identity and Access Management API.  
  
### get_service_account
    
    
    get_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetServiceAccountRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Gets a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_get_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[GetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.GetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountRequest), dict]]`   
The request object. The service account get request.  
`name` |  ``str``   
Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)` | An IAM service account. A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the [overview of service accounts](https://cloud.google.com/iam/help/service-accounts/overview). When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.  
  
### get_service_account_key
    
    
    get_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.GetServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        public_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPublicKeyType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Gets a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_get_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[GetServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_service_account_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.GetServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountKeyRequest), dict]]`   
The request object. The service account key get by id request.  
`name` |  ``str``   
Required. The resource name of the service account key in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`public_key_type` |  `[ServiceAccountPublicKeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountPublicKeyType)`   
Optional. The output format of the public key. The default is `TYPE_NONE`, which means that the public key is not returned. This corresponds to the `public_key_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccountKey](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKey)` | Represents a service account key. A service account has two sets of key-pairs: user-managed, and system-managed. User-managed key-pairs can be created and deleted by users. Users are responsible for rotating these keys periodically to ensure security of their service accounts. Users retain the private key of these key-pairs, and Google retains ONLY the public key. System-managed keys are automatically rotated by Google, and are used for signing for a maximum of two weeks. The rotation process is probabilistic, and usage of the new key will gradually ramp up and down over the key's lifetime. If you cache the public key set for a service account, we recommend that you update the cache every 15 minutes. User-managed keys can be added and removed at any time, so it is important to update the cache frequently. For Google-managed keys, Google will publish a key at least 6 hours before it is first used for signing and will keep publishing it for at least 6 hours after it was last used for signing. Public keys for all service accounts are also published at the OAuth2 Service Account API.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### key_path
    
    
    key_path(project: str, service_account: str, key: str) -> str

Returns a fully-qualified key string.

### lint_policy
    
    
    lint_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.LintPolicyRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.LintPolicyResponse

Lints, or validates, an IAM policy. Currently checks the `google.iam.v1.Binding.condition][google.iam.v1.Binding.condition]` field, which contains a condition expression for a role binding.

Successful calls to this method always return an HTTP `200 OK` status code, even if the linter detects an issue in the IAM policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_lint_policy():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[LintPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintPolicyRequest.html)(
        )
    
        # Make the request
        response = await client.[lint_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_lint_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.LintPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintPolicyRequest), dict]]`   
The request object. The request to lint a Cloud IAM policy object.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.LintPolicyResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintPolicyResponse)` | The response of a lint operation. An empty response indicates the operation was able to fully execute and no lint issue was found.  
  
### list_roles
    
    
    list_roles(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ListRolesRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager

Lists every predefined `Role][google.iam.admin.v1.Role]` that IAM supports, or every custom role that is defined for an organization or project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_list_roles():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[ListRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest.html)(
        )
    
        # Make the request
        page_result = client.[list_roles](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_roles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.ListRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest), dict]]`   
The request object. The request to get all roles defined under a resource.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager)` | The response containing the roles defined under a resource. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_service_account_keys
    
    
    list_service_account_keys(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        key_types: typing.Optional[
            typing.MutableSequence[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest.KeyType
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysResponse

Lists every `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]` for a service account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_list_service_account_keys():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[ListServiceAccountKeysRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[list_service_account_keys](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_service_account_keys)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest), dict]]`   
The request object. The service account keys list request.  
`name` |  ``str``   
Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID`, will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`key_types` |  `:class:`MutableSequence[[google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest.KeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest.KeyType)]``   
Filters the types of keys the user wants to include in the list response. Duplicate key types are not allowed. If no key type is provided, all keys are returned. This corresponds to the `key_types` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ListServiceAccountKeysResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysResponse)` | The service account keys list response.  
  
### list_service_accounts
    
    
    list_service_accounts(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager

Lists every `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that belongs to a specific project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_list_service_accounts():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[ListServiceAccountsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_service_accounts](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_service_accounts)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.ListServiceAccountsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsRequest), dict]]`   
The request object. The service account list request.  
`name` |  ``str``   
Required. The resource name of the project associated with the service accounts, such as `projects/my-project-123`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager)` | The service account list response. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

### parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

### patch_service_account
    
    
    patch_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.PatchServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Patches a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_patch_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[PatchServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.PatchServiceAccountRequest.html)(
        )
    
        # Make the request
        response = await client.[patch_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_patch_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.PatchServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.PatchServiceAccountRequest), dict]]`   
The request object. The service account patch request. You can patch only the `display_name` and `description` fields. You must use the `update_mask` field to specify which of these fields you want to patch. Only the fields specified in the request are guaranteed to be returned in the response. Other fields may be empty in the response.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)` | An IAM service account. A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the [overview of service accounts](https://cloud.google.com/iam/help/service-accounts/overview). When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.  
  
### query_auditable_services
    
    
    query_auditable_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesResponse

Returns a list of services that allow you to opt into audit logs that are not generated by default.

To learn more about audit logs, see the `Logging documentation <https://cloud.google.com/logging/docs/audit>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_query_auditable_services():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[QueryAuditableServicesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesRequest.html)(
        )
    
        # Make the request
        response = await client.[query_auditable_services](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_auditable_services)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.QueryAuditableServicesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesRequest), dict]]`   
The request object. A request to get the list of auditable services for a resource.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.QueryAuditableServicesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesResponse)` | A response containing a list of auditable services for a resource.  
  
### query_grantable_roles
    
    
    query_grantable_roles(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest, dict
            ]
        ] = None,
        *,
        full_resource_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager

Lists roles that can be granted on a Google Cloud resource. A role is grantable if the IAM policy for the resource can contain bindings to the role.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_query_grantable_roles():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[QueryGrantableRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesRequest.html)(
            full_resource_name="full_resource_name_value",
        )
    
        # Make the request
        page_result = client.[query_grantable_roles](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_grantable_roles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.QueryGrantableRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesRequest), dict]]`   
The request object. The grantable role query request.  
`full_resource_name` |  ``str``   
Required. The full resource name to query from the list of grantable roles. The name follows the Google Cloud Platform resource format. For example, a Cloud Platform project with id `my-project` will be named `//cloudresourcemanager.googleapis.com/projects/my-project`. This corresponds to the `full_resource_name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager)` | The grantable role query response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### query_testable_permissions
    
    
    query_testable_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager

Lists every permission that you can test on a resource. A permission is testable if you can check whether a principal has that permission on the resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_query_testable_permissions():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[QueryTestablePermissionsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsRequest.html)(
        )
    
        # Make the request
        page_result = client.[query_testable_permissions](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_testable_permissions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.QueryTestablePermissionsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsRequest), dict]]`   
The request object. A request to get permissions which can be tested on a resource.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager)` | The response containing permissions which can be tested on a resource. Iterating over this object will yield results and resolve additional pages automatically.  
  
### service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

Use this method to grant or revoke access to the service account. For example, you could grant a principal the ability to impersonate the service account.

This method does not enable the service account to access other resources. To grant roles to a service account on a resource, follow these steps:

  1. Call the resource's `getIamPolicy` method to get its current IAM policy.
  2. Edit the policy so that it binds the service account to an IAM role for the resource.
  3. Call the resource's `setIamPolicy` method to update its IAM policy.



For detailed instructions, see `Manage access to project, folders, and organizations <https://cloud.google.com/iam/help/service-accounts/granting-access-to-service-accounts>`**or`Manage access to other resources <https://cloud.google.com/iam/help/access/manage-other-resources>`**.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_set_iam_policy():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = await client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        bytes_to_sign: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignBlobResponse

**Note:** This method is deprecated. Use the ``signBlob` <https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signBlob>`__ method in the IAM Service Account Credentials API instead. If you currently use this method, see the`migration guide <https://cloud.google.com/iam/help/credentials/migrate-api>`__ for instructions.

Signs a blob using the system-managed private key for a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_sign_blob():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignBlobRequest.html)(
            name="name_value",
            bytes_to_sign=b'bytes_to_sign_blob',
        )
    
        # Make the request
        response = await client.[sign_blob](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_sign_blob)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignBlobRequest), dict]]`   
The request object. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The service account sign blob request.  
`name` |  ``str``   
Required. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`bytes_to_sign` |  ``bytes``   
Required. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The bytes to sign. This corresponds to the `bytes_to_sign` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.SignBlobResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignBlobResponse)` | Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api). The service account sign blob response.  
  
### sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignJwtResponse

**Note:** This method is deprecated. Use the ``signJwt` <https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signJwt>`__ method in the IAM Service Account Credentials API instead. If you currently use this method, see the`migration guide <https://cloud.google.com/iam/help/credentials/migrate-api>`__ for instructions.

Signs a JSON Web Token (JWT) using the system-managed private key for a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_sign_jwt():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignJwtRequest.html)(
            name="name_value",
            payload="payload_value",
        )
    
        # Make the request
        response = await client.[sign_jwt](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_sign_jwt)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignJwtRequest), dict]]`   
The request object. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The service account sign JWT request.  
`name` |  ``str``   
Required. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. Using `-` as a wildcard for the `PROJECT_ID` will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`payload` |  ``str``   
Required. Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__. The JWT payload to sign. Must be a serialized JSON object that contains a JWT Claims Set. For example: `{"sub": "user@example.com", "iat": 313435}` If the JWT Claims Set contains an expiration time (`exp`) claim, it must be an integer timestamp that is not in the past and no more than 12 hours in the future. If the JWT Claims Set does not contain an expiration time (`exp`) claim, this claim is added automatically, with a timestamp that is 1 hour in the future. This corresponds to the `payload` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.SignJwtResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignJwtResponse)` | Deprecated. [Migrate to Service Account Credentials API](https://cloud.google.com/iam/help/credentials/migrate-api). The service account sign JWT response.  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests whether the caller has the specified permissions on a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_test_iam_permissions():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = await client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]]`   
The request object. Request message for `TestIamPermissions` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`permissions` |  `:class:`MutableSequence[str]``   
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__. This corresponds to the `permissions` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### undelete_role
    
    
    undelete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UndeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Undeletes a custom `Role][google.iam.admin.v1.Role]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_undelete_role():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[UndeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest.html)(
        )
    
        # Make the request
        response = await client.[undelete_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_undelete_role)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.UndeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest), dict]]`   
The request object. The request to undelete an existing role.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)` | A role in the Identity and Access Management API.  
  
### undelete_service_account
    
    
    undelete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountResponse

Restores a deleted `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

**Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort.

After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_undelete_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[UndeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteServiceAccountRequest.html)(
        )
    
        # Make the request
        response = await client.[undelete_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_undelete_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.UndeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteServiceAccountRequest), dict]]`   
The request object. The service account undelete request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### update_role
    
    
    update_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UpdateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Updates the definition of a custom `Role][google.iam.admin.v1.Role]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_update_role():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[UpdateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest.html)(
        )
    
        # Make the request
        response = await client.[update_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_update_role)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.UpdateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest), dict]]`   
The request object. The request to update a role.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)` | A role in the Identity and Access Management API.  
  
### update_service_account
    
    
    update_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ServiceAccount, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

**Note:** We are in the process of deprecating this method. Use `PatchServiceAccount][google.iam.admin.v1.IAM.PatchServiceAccount]` instead.

Updates a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

You can update only the `display_name` field.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_update_service_account():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount.html)(
        )
    
        # Make the request
        response = await client.[update_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_update_service_account)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount), dict]]`   
The request object. An IAM service account. A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the `overview of service accounts <https://cloud.google.com/iam/help/service-accounts/overview>`__. When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)` | An IAM service account. A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the [overview of service accounts](https://cloud.google.com/iam/help/service-accounts/overview). When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.  
  
### upload_service_account_key
    
    
    upload_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UploadServiceAccountKeyRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Uploads the public key portion of a key pair that you manage, and associates the public key with a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

After you upload the public key, you can use the private key from the key pair as a service account key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import iam_admin_v1
    
    async def sample_upload_service_account_key():
        # Create a client
        client = iam_admin_v1.[IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_admin_v1.[UploadServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UploadServiceAccountKeyRequest.html)(
        )
    
        # Make the request
        response = await client.[upload_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.html#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_upload_service_account_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.iam_admin_v1.types.UploadServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UploadServiceAccountKeyRequest), dict]]`   
The request object. The service account key upload request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.iam_admin_v1.types.ServiceAccountKey](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKey)` | Represents a service account key. A service account has two sets of key-pairs: user-managed, and system-managed. User-managed key-pairs can be created and deleted by users. Users are responsible for rotating these keys periodically to ensure security of their service accounts. Users retain the private key of these key-pairs, and Google retains ONLY the public key. System-managed keys are automatically rotated by Google, and are used for signing for a maximum of two weeks. The rotation process is probabilistic, and usage of the new key will gradually ramp up and down over the key's lifetime. If you cache the public key set for a service account, we recommend that you update the cache every 15 minutes. User-managed keys can be added and removed at any time, so it is important to update the cache frequently. For Google-managed keys, Google will publish a key at least 6 hours before it is first used for signing and will keep publishing it for at least 6 hours after it was last used for signing. Public keys for all service accounts are also published at the OAuth2 Service Account API.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
