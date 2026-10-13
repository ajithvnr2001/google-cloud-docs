---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient
title: Class DlpServiceAsyncClient (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:26.544310+00:00
---

# Class DlpServiceAsyncClient (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DlpServiceAsyncClient (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    DlpServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dlp_v2.services.dlp_service.transports.base.DlpServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.dlp_v2.services.dlp_service.transports.base.DlpServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Sensitive Data Protection provides access to a powerful sensitive data inspection, classification, and de-identification platform that works on text, images, and Google Cloud storage repositories. To learn more about concepts and find how-to guides see <https://docs.cloud.google.com/sensitive-data-protection/docs/>.

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
`DlpServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DlpServiceAsyncClient
    
    
    DlpServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.dlp_v2.services.dlp_service.transports.base.DlpServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.dlp_v2.services.dlp_service.transports.base.DlpServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the dlp service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DlpServiceTransport,Callable[..., DlpServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DlpServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### activate_job_trigger
    
    
    activate_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ActivateJobTriggerRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.DlpJob

Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_activate_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ActivateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ActivateJobTriggerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[activate_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_activate_job_trigger)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ActivateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ActivateJobTriggerRequest), dict]]`   
The request object. Request message for ActivateJobTrigger.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob)` | Combines all of the information about a DLP job.  
  
### cancel_dlp_job
    
    
    cancel_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CancelDlpJobRequest, dict]
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

Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_cancel_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CancelDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CancelDlpJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[cancel_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_cancel_dlp_job)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CancelDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CancelDlpJobRequest), dict]]`   
The request object. The request message for canceling a DLP job.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### column_data_profile_path
    
    
    column_data_profile_path(
        organization: str, location: str, column_data_profile: str
    ) -> str

Returns a fully-qualified column_data_profile string.

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

### connection_path
    
    
    connection_path(project: str, location: str, connection: str) -> str

Returns a fully-qualified connection string.

### content_policy_path
    
    
    content_policy_path(project: str, location: str, content_policy: str) -> str

Returns a fully-qualified content_policy string.

### create_connection
    
    
    create_connection(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateConnectionRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        connection: typing.Optional[google.cloud.dlp_v2.types.dlp.Connection] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.Connection

Create a Connection to an external data source.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_connection():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        connection = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection.html)()
        connection.cloud_sql.username_password.username = "username_value"
        connection.cloud_sql.username_password.password_secret_version_name = "password_secret_version_name_value"
        connection.cloud_sql.max_connections = 1608
        connection.cloud_sql.database_engine = "DATABASE_ENGINE_POSTGRES"
        connection.state = "ERROR"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateConnectionRequest.html)(
            parent="parent_value",
            connection=connection,
        )
    
        # Make the request
        response = await client.[create_connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateConnectionRequest), dict]]`   
The request object. Request message for CreateConnection.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization): - Projects scope: `projects/{project_id}/locations/{location_id}` \- Organizations scope: `organizations/{org_id}/locations/{location_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`connection` |  `[Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection)`   
Required. The connection resource. This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection)` | A data connection to allow the DLP API to profile data in locations that require additional configuration.  
  
### create_content_policy
    
    
    create_content_policy(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateContentPolicyRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        content_policy: typing.Optional[google.cloud.dlp_v2.types.dlp.ContentPolicy] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.ContentPolicy

Create a ContentPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_content_policy():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        content_policy = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy.html)()
        content_policy.rules.action.return_verdict = "BLOCK"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateContentPolicyRequest.html)(
            parent="parent_value",
            content_policy=content_policy,
        )
    
        # Make the request
        response = await client.[create_content_policy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_content_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateContentPolicyRequest), dict]]`   
The request object. Request message for CreateContentPolicy.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project): - Projects scope: `projects/{project_id}/locations/{location_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`content_policy` |  `[ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy)`   
Required. The content_policy resource. This corresponds to the `content_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy)` | A policy to apply to content based on its inspection findings.  
  
### create_deidentify_template
    
    
    create_deidentify_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.dlp_v2.types.dlp.CreateDeidentifyTemplateRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deidentify_template: typing.Optional[
            google.cloud.dlp_v2.types.dlp.DeidentifyTemplate
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.DeidentifyTemplate

Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_deidentify_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDeidentifyTemplateRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_deidentify_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_deidentify_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDeidentifyTemplateRequest), dict]]`   
The request object. Request message for CreateDeidentifyTemplate.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` \- Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}` \- Organizations scope, no location specified (defaults to global): `organizations/{org_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyTemplate)`   
Required. The DeidentifyTemplate to create. This corresponds to the `deidentify_template` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DeidentifyTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyTemplate)` | DeidentifyTemplates contains instructions on how to de-identify content. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### create_discovery_config
    
    
    create_discovery_config(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateDiscoveryConfigRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        discovery_config: typing.Optional[
            google.cloud.dlp_v2.types.dlp.DiscoveryConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.DiscoveryConfig

Creates a config for discovery to scan and profile storage.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_discovery_config():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        discovery_config = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig.html)()
        discovery_config.status = "PAUSED"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDiscoveryConfigRequest.html)(
            parent="parent_value",
            discovery_config=discovery_config,
        )
    
        # Make the request
        response = await client.[create_discovery_config](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_discovery_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDiscoveryConfigRequest), dict]]`   
The request object. Request message for CreateDiscoveryConfig.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization): - Projects scope: `projects/{project_id}/locations/{location_id}` \- Organizations scope: `organizations/{org_id}/locations/{location_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`discovery_config` |  `[DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig)`   
Required. The DiscoveryConfig to create. This corresponds to the `discovery_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig)` | Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project. The generated data profiles are retained according to the [data retention policy] (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).  
  
### create_dlp_job
    
    
    create_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateDlpJobRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        inspect_job: typing.Optional[google.cloud.dlp_v2.types.dlp.InspectJobConfig] = None,
        risk_job: typing.Optional[
            google.cloud.dlp_v2.types.dlp.RiskAnalysisJobConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.DlpJob

Creates a new job to inspect storage or calculate risk metrics. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.

When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDlpJobRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_dlp_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateDlpJobRequest), dict]]`   
The request object. Request message for CreateDlpJobRequest. Used to initiate long running jobs such as calculating risk metrics or inspecting Google Cloud Storage.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`inspect_job` |  `[InspectJobConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectJobConfig)`   
An inspection job scans a storage repository for InfoTypes. This corresponds to the `inspect_job` field on the `request` instance; if `request` is provided, this should not be set.  
`risk_job` |  `[RiskAnalysisJobConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.RiskAnalysisJobConfig)`   
A risk analysis job calculates re-identification risk metrics for a BigQuery table. This corresponds to the `risk_job` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob)` | Combines all of the information about a DLP job.  
  
### create_inspect_template
    
    
    create_inspect_template(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateInspectTemplateRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        inspect_template: typing.Optional[
            google.cloud.dlp_v2.types.dlp.InspectTemplate
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.InspectTemplate

Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_inspect_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateInspectTemplateRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_inspect_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateInspectTemplateRequest), dict]]`   
The request object. Request message for CreateInspectTemplate.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` \- Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}` \- Organizations scope, no location specified (defaults to global): `organizations/{org_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`inspect_template` |  `[InspectTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectTemplate)`   
Required. The InspectTemplate to create. This corresponds to the `inspect_template` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.InspectTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectTemplate)` | The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### create_job_trigger
    
    
    create_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateJobTriggerRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        job_trigger: typing.Optional[google.cloud.dlp_v2.types.dlp.JobTrigger] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.JobTrigger

Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        job_trigger = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger.html)()
        job_trigger.status = "CANCELLED"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateJobTriggerRequest.html)(
            parent="parent_value",
            job_trigger=job_trigger,
        )
    
        # Make the request
        response = await client.[create_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_job_trigger)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateJobTriggerRequest), dict]]`   
The request object. Request message for CreateJobTrigger.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`job_trigger` |  `[JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger)`   
Required. The JobTrigger to create. This corresponds to the `job_trigger` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger)` | Contains a configuration to make API calls on a repeating basis. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers to learn more.  
  
### create_stored_info_type
    
    
    create_stored_info_type(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.CreateStoredInfoTypeRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        config: typing.Optional[google.cloud.dlp_v2.types.dlp.StoredInfoTypeConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.StoredInfoType

Creates a pre-built stored infoType to be used for inspection. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_create_stored_info_type():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CreateStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateStoredInfoTypeRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_create_stored_info_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.CreateStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CreateStoredInfoTypeRequest), dict]]`   
The request object. Request message for CreateStoredInfoType.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` \- Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}` \- Organizations scope, no location specified (defaults to global): `organizations/{org_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`config` |  `[StoredInfoTypeConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StoredInfoTypeConfig)`   
Required. Configuration of the storedInfoType to create. This corresponds to the `config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.StoredInfoType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StoredInfoType)` | StoredInfoType resource message that contains information about the current version and any pending updates.  
  
### deidentify_content
    
    
    deidentify_content(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeidentifyContentRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.DeidentifyContentResponse

De-identifies potentially sensitive info from a ContentItem. This method has limits on input size and output size. See <https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data> to learn more.

When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_deidentify_content():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeidentifyContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyContentRequest.html)(
        )
    
        # Make the request
        response = await client.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_deidentify_content)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeidentifyContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyContentRequest), dict]]`   
The request object. Request to de-identify a ContentItem.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DeidentifyContentResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyContentResponse)` | Results of de-identifying a ContentItem.  
  
### deidentify_template_path
    
    
    deidentify_template_path(organization: str, deidentify_template: str) -> str

Returns a fully-qualified deidentify_template string.

### delete_connection
    
    
    delete_connection(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteConnectionRequest, dict]
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

Delete a Connection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_connection():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_connection)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteConnectionRequest), dict]]`   
The request object. Request message for DeleteConnection.  
`name` |  ``str``   
Required. Resource name of the Connection to be deleted, in the format: `projects/{project}/locations/{location}/connections/{connection}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_content_policy
    
    
    delete_content_policy(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteContentPolicyRequest, dict]
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

Delete a ContentPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_content_policy():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteContentPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_content_policy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_content_policy)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteContentPolicyRequest), dict]]`   
The request object. Request message for DeleteContentPolicy.  
`name` |  ``str``   
Required. Resource name of the ContentPolicy to be deleted, in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_deidentify_template
    
    
    delete_deidentify_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.dlp_v2.types.dlp.DeleteDeidentifyTemplateRequest, dict
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

Deletes a DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_deidentify_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDeidentifyTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_deidentify_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_deidentify_template)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDeidentifyTemplateRequest), dict]]`   
The request object. Request message for DeleteDeidentifyTemplate.  
`name` |  ``str``   
Required. Resource name of the organization and deidentify template to be deleted, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_discovery_config
    
    
    delete_discovery_config(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteDiscoveryConfigRequest, dict]
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

Deletes a discovery configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_discovery_config():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDiscoveryConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_discovery_config](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_discovery_config)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDiscoveryConfigRequest), dict]]`   
The request object. Request message for DeleteDiscoveryConfig.  
`name` |  ``str``   
Required. Resource name of the project and the config, for example `projects/dlp-test-project/discoveryConfigs/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_dlp_job
    
    
    delete_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteDlpJobRequest, dict]
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

Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDlpJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_dlp_job)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteDlpJobRequest), dict]]`   
The request object. The request message for deleting a DLP job.  
`name` |  ``str``   
Required. The name of the DlpJob resource to be deleted. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_file_store_data_profile
    
    
    delete_file_store_data_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.dlp_v2.types.dlp.DeleteFileStoreDataProfileRequest, dict
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

Delete a FileStoreDataProfile. Will not prevent the profile from being regenerated if the resource is still included in a discovery configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_file_store_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteFileStoreDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteFileStoreDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_file_store_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_file_store_data_profile)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteFileStoreDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteFileStoreDataProfileRequest), dict]]`   
The request object. Request message for DeleteFileStoreProfile.  
`name` |  ``str``   
Required. Resource name of the file store data profile. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_inspect_template
    
    
    delete_inspect_template(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteInspectTemplateRequest, dict]
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

Deletes an InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_inspect_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteInspectTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_inspect_template)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteInspectTemplateRequest), dict]]`   
The request object. Request message for DeleteInspectTemplate.  
`name` |  ``str``   
Required. Resource name of the organization and inspectTemplate to be deleted, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_job_trigger
    
    
    delete_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteJobTriggerRequest, dict]
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

Deletes a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteJobTriggerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_job_trigger)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteJobTriggerRequest), dict]]`   
The request object. Request message for DeleteJobTrigger.  
`name` |  ``str``   
Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_stored_info_type
    
    
    delete_stored_info_type(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteStoredInfoTypeRequest, dict]
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

Deletes a stored infoType. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_stored_info_type():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteStoredInfoTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_stored_info_type)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteStoredInfoTypeRequest), dict]]`   
The request object. Request message for DeleteStoredInfoType.  
`name` |  ``str``   
Required. Resource name of the organization and storedInfoType to be deleted, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_table_data_profile
    
    
    delete_table_data_profile(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.DeleteTableDataProfileRequest, dict]
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

Delete a TableDataProfile. Will not prevent the profile from being regenerated if the table is still included in a discovery configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_delete_table_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DeleteTableDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteTableDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_table_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_delete_table_data_profile)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.DeleteTableDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeleteTableDataProfileRequest), dict]]`   
The request object. Request message for DeleteTableProfile.  
`name` |  ``str``   
Required. Resource name of the table data profile. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### discovery_config_path
    
    
    discovery_config_path(project: str, location: str, discovery_config: str) -> str

Returns a fully-qualified discovery_config string.

### dlp_content_path
    
    
    dlp_content_path(project: str) -> str

Returns a fully-qualified dlp_content string.

### dlp_job_path
    
    
    dlp_job_path(project: str, dlp_job: str) -> str

Returns a fully-qualified dlp_job string.

### file_store_data_profile_path
    
    
    file_store_data_profile_path(
        organization: str, location: str, file_store_data_profile: str
    ) -> str

Returns a fully-qualified file_store_data_profile string.

### finding_path
    
    
    finding_path(project: str, location: str, finding: str) -> str

Returns a fully-qualified finding string.

### finish_dlp_job
    
    
    finish_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.FinishDlpJobRequest, dict]
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

Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_finish_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[FinishDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FinishDlpJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[finish_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_finish_dlp_job)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.FinishDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FinishDlpJobRequest), dict]]`   
The request object. The request message for finishing a DLP hybrid job.  
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
`DlpServiceAsyncClient` | The constructed client.  
  
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
`DlpServiceAsyncClient` | The constructed client.  
  
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
`DlpServiceAsyncClient` | The constructed client.  
  
### get_column_data_profile
    
    
    get_column_data_profile(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetColumnDataProfileRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.ColumnDataProfile

Gets a column data profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_column_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetColumnDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetColumnDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_column_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_column_data_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetColumnDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetColumnDataProfileRequest), dict]]`   
The request object. Request to get a column data profile.  
`name` |  ``str``   
Required. Resource name, for example `organizations/12345/locations/us/columnDataProfiles/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ColumnDataProfile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ColumnDataProfile)` | The profile for a scanned column within a table.  
  
### get_connection
    
    
    get_connection(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetConnectionRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.Connection

Get a Connection by name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_connection():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetConnectionRequest), dict]]`   
The request object. Request message for GetConnection.  
`name` |  ``str``   
Required. Resource name in the format: `projects/{project}/locations/{location}/connections/{connection}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection)` | A data connection to allow the DLP API to profile data in locations that require additional configuration.  
  
### get_content_policy
    
    
    get_content_policy(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetContentPolicyRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.ContentPolicy

Get a ContentPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_content_policy():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetContentPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_content_policy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_content_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetContentPolicyRequest), dict]]`   
The request object. Request message for GetContentPolicy.  
`name` |  ``str``   
Required. Resource name in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy)` | A policy to apply to content based on its inspection findings.  
  
### get_deidentify_template
    
    
    get_deidentify_template(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetDeidentifyTemplateRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.DeidentifyTemplate

Gets a DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_deidentify_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDeidentifyTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deidentify_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_deidentify_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDeidentifyTemplateRequest), dict]]`   
The request object. Request message for GetDeidentifyTemplate.  
`name` |  ``str``   
Required. Resource name of the organization and deidentify template to be read, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DeidentifyTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyTemplate)` | DeidentifyTemplates contains instructions on how to de-identify content. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### get_discovery_config
    
    
    get_discovery_config(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetDiscoveryConfigRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.DiscoveryConfig

Gets a discovery configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_discovery_config():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDiscoveryConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_discovery_config](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_discovery_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDiscoveryConfigRequest), dict]]`   
The request object. Request message for GetDiscoveryConfig.  
`name` |  ``str``   
Required. Resource name of the project and the configuration, for example `projects/dlp-test-project/discoveryConfigs/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig)` | Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project. The generated data profiles are retained according to the [data retention policy] (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).  
  
### get_dlp_job
    
    
    get_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetDlpJobRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.DlpJob

Gets the latest state of a long-running DlpJob. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDlpJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_dlp_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetDlpJobRequest), dict]]`   
The request object. The request message for `GetDlpJob][google.privacy.dlp.v2.DlpService.GetDlpJob]`.  
`name` |  ``str``   
Required. The name of the DlpJob resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob)` | Combines all of the information about a DLP job.  
  
### get_file_store_data_profile
    
    
    get_file_store_data_profile(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetFileStoreDataProfileRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.FileStoreDataProfile

Gets a file store data profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_file_store_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetFileStoreDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetFileStoreDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_file_store_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_file_store_data_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetFileStoreDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetFileStoreDataProfileRequest), dict]]`   
The request object. Request to get a file store data profile.  
`name` |  ``str``   
Required. Resource name, for example `organizations/12345/locations/us/fileStoreDataProfiles/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.FileStoreDataProfile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileStoreDataProfile)` | The profile for a file store. - Cloud Storage: maps 1:1 with a bucket. - Amazon S3: maps 1:1 with a bucket.  
  
### get_inspect_template
    
    
    get_inspect_template(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetInspectTemplateRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.InspectTemplate

Gets an InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_inspect_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetInspectTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_inspect_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetInspectTemplateRequest), dict]]`   
The request object. Request message for GetInspectTemplate.  
`name` |  ``str``   
Required. Resource name of the organization and inspectTemplate to be read, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.InspectTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectTemplate)` | The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### get_job_trigger
    
    
    get_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetJobTriggerRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.JobTrigger

Gets a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetJobTriggerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_job_trigger)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetJobTriggerRequest), dict]]`   
The request object. Request message for GetJobTrigger.  
`name` |  ``str``   
Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger)` | Contains a configuration to make API calls on a repeating basis. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers to learn more.  
  
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
  
### get_project_data_profile
    
    
    get_project_data_profile(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetProjectDataProfileRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.ProjectDataProfile

Gets a project data profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_project_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetProjectDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetProjectDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_project_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_project_data_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetProjectDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetProjectDataProfileRequest), dict]]`   
The request object. Request to get a project data profile.  
`name` |  ``str``   
Required. Resource name, for example `organizations/12345/locations/us/projectDataProfiles/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ProjectDataProfile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ProjectDataProfile)` | An aggregated profile for this project, based on the resources profiled within it.  
  
### get_stored_info_type
    
    
    get_stored_info_type(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetStoredInfoTypeRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.StoredInfoType

Gets a stored infoType. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_stored_info_type():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetStoredInfoTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_stored_info_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetStoredInfoTypeRequest), dict]]`   
The request object. Request message for GetStoredInfoType.  
`name` |  ``str``   
Required. Resource name of the organization and storedInfoType to be read, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.StoredInfoType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StoredInfoType)` | StoredInfoType resource message that contains information about the current version and any pending updates.  
  
### get_table_data_profile
    
    
    get_table_data_profile(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.GetTableDataProfileRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.TableDataProfile

Gets a table data profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_get_table_data_profile():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[GetTableDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetTableDataProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_table_data_profile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_get_table_data_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.GetTableDataProfileRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.GetTableDataProfileRequest), dict]]`   
The request object. Request to get a table data profile.  
`name` |  ``str``   
Required. Resource name, for example `organizations/12345/locations/us/tableDataProfiles/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.TableDataProfile](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.TableDataProfile)` | The profile for a scanned table.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.dlp_v2.services.dlp_service.transports.base.DlpServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### hybrid_inspect_dlp_job
    
    
    hybrid_inspect_dlp_job(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.HybridInspectDlpJobRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.HybridInspectResponse

Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_hybrid_inspect_dlp_job():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[HybridInspectDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectDlpJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[hybrid_inspect_dlp_job](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_hybrid_inspect_dlp_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.HybridInspectDlpJobRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectDlpJobRequest), dict]]`   
The request object. Request to search for potentially sensitive info in a custom location.  
`name` |  ``str``   
Required. Resource name of the job to execute a hybrid inspect on, for example `projects/dlp-test-project/dlpJob/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.HybridInspectResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectResponse)` | Quota exceeded errors will be thrown once quota has been met.  
  
### hybrid_inspect_job_trigger
    
    
    hybrid_inspect_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.HybridInspectJobTriggerRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.HybridInspectResponse

Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_hybrid_inspect_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[HybridInspectJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectJobTriggerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[hybrid_inspect_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_hybrid_inspect_job_trigger)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.HybridInspectJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectJobTriggerRequest), dict]]`   
The request object. Request to search for potentially sensitive info in a custom location.  
`name` |  ``str``   
Required. Resource name of the trigger to execute a hybrid inspect on, for example `projects/dlp-test-project/jobTriggers/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.HybridInspectResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.HybridInspectResponse)` | Quota exceeded errors will be thrown once quota has been met.  
  
### inspect_content
    
    
    inspect_content(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.InspectContentRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.InspectContentResponse

Finds potentially sensitive info in content. This method has limits on input size, processing time, and output size.

When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

For how to guides, see <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images> and <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text>,
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_inspect_content():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[InspectContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectContentRequest.html)(
        )
    
        # Make the request
        response = await client.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_inspect_content)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.InspectContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectContentRequest), dict]]`   
The request object. Request to search for potentially sensitive info in a ContentItem.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.InspectContentResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectContentResponse)` | Results of inspecting an item.  
  
### inspect_template_path
    
    
    inspect_template_path(organization: str, inspect_template: str) -> str

Returns a fully-qualified inspect_template string.

### job_trigger_path
    
    
    job_trigger_path(project: str, job_trigger: str) -> str

Returns a fully-qualified job_trigger string.

### list_column_data_profiles
    
    
    list_column_data_profiles(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListColumnDataProfilesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListColumnDataProfilesAsyncPager

Lists column data profiles for an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_column_data_profiles():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListColumnDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListColumnDataProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_column_data_profiles](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_column_data_profiles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListColumnDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListColumnDataProfilesRequest), dict]]`   
The request object. Request to list the profiles generated for a given organization or project.  
`parent` |  ``str``   
Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListColumnDataProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListColumnDataProfilesAsyncPager)` | List of profiles generated for a given organization or project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_connections
    
    
    list_connections(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListConnectionsRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListConnectionsAsyncPager

Lists Connections in a parent. Use SearchConnections to see all connections within an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_connections():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListConnectionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_connections](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_connections)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListConnectionsRequest), dict]]`   
The request object. Request message for ListConnections.  
`parent` |  ``str``   
Required. Resource name of the organization or project, for example, `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListConnectionsAsyncPager)` | Response message for ListConnections. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_content_policies
    
    
    list_content_policies(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListContentPoliciesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListContentPoliciesAsyncPager

Lists ContentPolicies in a parent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_content_policies():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListContentPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListContentPoliciesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_content_policies](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_content_policies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListContentPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListContentPoliciesRequest), dict]]`   
The request object. Request message for ListContentPolicies.  
`parent` |  ``str``   
Required. Resource name of the project, for example, `projects/project-id/locations/asia`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListContentPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListContentPoliciesAsyncPager)` | Response message for ListContentPolicies. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_deidentify_templates
    
    
    list_deidentify_templates(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListDeidentifyTemplatesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListDeidentifyTemplatesAsyncPager

Lists DeidentifyTemplates. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_deidentify_templates():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deidentify_templates](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_deidentify_templates)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest), dict]]`   
The request object. Request message for ListDeidentifyTemplates.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` \- Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}` \- Organizations scope, no location specified (defaults to global): `organizations/{org_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListDeidentifyTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListDeidentifyTemplatesAsyncPager)` | Response message for ListDeidentifyTemplates. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_discovery_configs
    
    
    list_discovery_configs(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListDiscoveryConfigsRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListDiscoveryConfigsAsyncPager

Lists discovery configurations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_discovery_configs():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListDiscoveryConfigsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDiscoveryConfigsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_discovery_configs](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_discovery_configs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListDiscoveryConfigsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDiscoveryConfigsRequest), dict]]`   
The request object. Request message for ListDiscoveryConfigs.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value is as follows: `projects/{project_id}/locations/{location_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListDiscoveryConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListDiscoveryConfigsAsyncPager)` | Response message for ListDiscoveryConfigs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_dlp_jobs
    
    
    list_dlp_jobs(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListDlpJobsRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListDlpJobsAsyncPager

Lists DlpJobs that match the specified filter in the request. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_dlp_jobs():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListDlpJobsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDlpJobsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_dlp_jobs](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_dlp_jobs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListDlpJobsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListDlpJobsRequest), dict]]`   
The request object. The request message for listing DLP jobs.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListDlpJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListDlpJobsAsyncPager)` | The response message for listing DLP jobs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_file_store_data_profiles
    
    
    list_file_store_data_profiles(
        request: typing.Optional[
            typing.Union[
                google.cloud.dlp_v2.types.dlp.ListFileStoreDataProfilesRequest, dict
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
        google.cloud.dlp_v2.services.dlp_service.pagers.ListFileStoreDataProfilesAsyncPager
    )

Lists file store data profiles for an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_file_store_data_profiles():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListFileStoreDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListFileStoreDataProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_file_store_data_profiles](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_file_store_data_profiles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListFileStoreDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListFileStoreDataProfilesRequest), dict]]`   
The request object. Request to list the file store profiles generated for a given organization or project.  
`parent` |  ``str``   
Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListFileStoreDataProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListFileStoreDataProfilesAsyncPager)` | List of file store data profiles generated for a given organization or project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_info_types
    
    
    list_info_types(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListInfoTypesRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.ListInfoTypesResponse

Returns a list of the sensitive information types that the DLP API supports. See <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_info_types():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListInfoTypesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListInfoTypesRequest.html)(
        )
    
        # Make the request
        response = await client.[list_info_types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_info_types)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListInfoTypesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListInfoTypesRequest), dict]]`   
The request object. Request for the list of infoTypes.  
`parent` |  ``str``   
The parent resource name. The format of this value is as follows: :: `locations/{location_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ListInfoTypesResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListInfoTypesResponse)` | Response to the ListInfoTypes request.  
  
### list_inspect_templates
    
    
    list_inspect_templates(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListInspectTemplatesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListInspectTemplatesAsyncPager

Lists InspectTemplates. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_inspect_templates():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListInspectTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListInspectTemplatesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_inspect_templates](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_inspect_templates)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListInspectTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListInspectTemplatesRequest), dict]]`   
The request object. Request message for ListInspectTemplates.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` \- Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}` \- Organizations scope, no location specified (defaults to global): `organizations/{org_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListInspectTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListInspectTemplatesAsyncPager)` | Response message for ListInspectTemplates. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_job_triggers
    
    
    list_job_triggers(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListJobTriggersRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListJobTriggersAsyncPager

Lists job triggers. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_job_triggers():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListJobTriggersRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListJobTriggersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_job_triggers](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_job_triggers)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListJobTriggersRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListJobTriggersRequest), dict]]`   
The request object. Request message for ListJobTriggers.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListJobTriggersAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListJobTriggersAsyncPager)` | Response message for ListJobTriggers. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_project_data_profiles
    
    
    list_project_data_profiles(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListProjectDataProfilesAsyncPager

Lists project data profiles for an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_project_data_profiles():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListProjectDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_project_data_profiles](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_project_data_profiles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListProjectDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesRequest), dict]]`   
The request object. Request to list the profiles generated for a given organization or project.  
`parent` |  ``str``   
Required. organizations/{org_id}/locations/{loc_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListProjectDataProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListProjectDataProfilesAsyncPager)` | List of profiles generated for a given organization or project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_stored_info_types
    
    
    list_stored_info_types(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListStoredInfoTypesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListStoredInfoTypesAsyncPager

Lists stored infoTypes. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_stored_info_types():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListStoredInfoTypesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListStoredInfoTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_stored_info_types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_stored_info_types)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListStoredInfoTypesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListStoredInfoTypesRequest), dict]]`   
The request object. Request message for ListStoredInfoTypes.  
`parent` |  ``str``   
Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have `specified a processing location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__: - Projects scope, location specified: `projects/{project_id}/locations/{location_id}` \- Projects scope, no location specified (defaults to global): `projects/{project_id}` The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: :: parent=projects/example-project/locations/europe-west3 This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListStoredInfoTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListStoredInfoTypesAsyncPager)` | Response message for ListStoredInfoTypes. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_table_data_profiles
    
    
    list_table_data_profiles(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ListTableDataProfilesRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.ListTableDataProfilesAsyncPager

Lists table data profiles for an organization.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_list_table_data_profiles():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ListTableDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListTableDataProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_table_data_profiles](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_list_table_data_profiles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ListTableDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListTableDataProfilesRequest), dict]]`   
The request object. Request to list the profiles generated for a given organization or project.  
`parent` |  ``str``   
Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.ListTableDataProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListTableDataProfilesAsyncPager)` | List of profiles generated for a given organization or project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_column_data_profile_path
    
    
    parse_column_data_profile_path(path: str) -> typing.Dict[str, str]

Parses a column_data_profile path into its component segments.

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

### parse_connection_path
    
    
    parse_connection_path(path: str) -> typing.Dict[str, str]

Parses a connection path into its component segments.

### parse_content_policy_path
    
    
    parse_content_policy_path(path: str) -> typing.Dict[str, str]

Parses a content_policy path into its component segments.

### parse_deidentify_template_path
    
    
    parse_deidentify_template_path(path: str) -> typing.Dict[str, str]

Parses a deidentify_template path into its component segments.

### parse_discovery_config_path
    
    
    parse_discovery_config_path(path: str) -> typing.Dict[str, str]

Parses a discovery_config path into its component segments.

### parse_dlp_content_path
    
    
    parse_dlp_content_path(path: str) -> typing.Dict[str, str]

Parses a dlp_content path into its component segments.

### parse_dlp_job_path
    
    
    parse_dlp_job_path(path: str) -> typing.Dict[str, str]

Parses a dlp_job path into its component segments.

### parse_file_store_data_profile_path
    
    
    parse_file_store_data_profile_path(path: str) -> typing.Dict[str, str]

Parses a file_store_data_profile path into its component segments.

### parse_finding_path
    
    
    parse_finding_path(path: str) -> typing.Dict[str, str]

Parses a finding path into its component segments.

### parse_inspect_template_path
    
    
    parse_inspect_template_path(path: str) -> typing.Dict[str, str]

Parses a inspect_template path into its component segments.

### parse_job_trigger_path
    
    
    parse_job_trigger_path(path: str) -> typing.Dict[str, str]

Parses a job_trigger path into its component segments.

### parse_project_data_profile_path
    
    
    parse_project_data_profile_path(path: str) -> typing.Dict[str, str]

Parses a project_data_profile path into its component segments.

### parse_stored_info_type_path
    
    
    parse_stored_info_type_path(path: str) -> typing.Dict[str, str]

Parses a stored_info_type path into its component segments.

### parse_table_data_profile_path
    
    
    parse_table_data_profile_path(path: str) -> typing.Dict[str, str]

Parses a table_data_profile path into its component segments.

### project_data_profile_path
    
    
    project_data_profile_path(
        organization: str, location: str, project_data_profile: str
    ) -> str

Returns a fully-qualified project_data_profile string.

### redact_image
    
    
    redact_image(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.RedactImageRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.RedactImageResponse

Redacts potentially sensitive info from an image. This method has limits on input size, processing time, and output size. See <https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images> to learn more.

When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_redact_image():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[RedactImageRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.RedactImageRequest.html)(
        )
    
        # Make the request
        response = await client.[redact_image](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_redact_image)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.RedactImageRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.RedactImageRequest), dict]]`   
The request object. Request to search for potentially sensitive info in an image and redact it by covering it with a colored rectangle.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.RedactImageResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.RedactImageResponse)` | Results of redacting an image.  
  
### reidentify_content
    
    
    reidentify_content(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.ReidentifyContentRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.ReidentifyContentResponse

Re-identifies content that has been de-identified. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_reidentify_content():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ReidentifyContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ReidentifyContentRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_reidentify_content)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.ReidentifyContentRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ReidentifyContentRequest), dict]]`   
The request object. Request to re-identify an item.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ReidentifyContentResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ReidentifyContentResponse)` | Results of re-identifying an item.  
  
### search_connections
    
    
    search_connections(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.SearchConnectionsRequest, dict]
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
    ) -> google.cloud.dlp_v2.services.dlp_service.pagers.SearchConnectionsAsyncPager

Searches for Connections in a parent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_search_connections():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[SearchConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.SearchConnectionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[search_connections](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_search_connections)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.SearchConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.SearchConnectionsRequest), dict]]`   
The request object. Request message for SearchConnections.  
`parent` |  ``str``   
Required. Resource name of the organization or project with a wildcard location, for example, `organizations/433245324/locations/-` or `projects/project-id/locations/-`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.services.dlp_service.pagers.SearchConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.SearchConnectionsAsyncPager)` | Response message for SearchConnections. Iterating over this object will yield results and resolve additional pages automatically.  
  
### stored_info_type_path
    
    
    stored_info_type_path(organization: str, stored_info_type: str) -> str

Returns a fully-qualified stored_info_type string.

### table_data_profile_path
    
    
    table_data_profile_path(
        organization: str, location: str, table_data_profile: str
    ) -> str

Returns a fully-qualified table_data_profile string.

### update_connection
    
    
    update_connection(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateConnectionRequest, dict]
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
    ) -> google.cloud.dlp_v2.types.dlp.Connection

Update a Connection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_connection():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        connection = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection.html)()
        connection.cloud_sql.username_password.username = "username_value"
        connection.cloud_sql.username_password.password_secret_version_name = "password_secret_version_name_value"
        connection.cloud_sql.max_connections = 1608
        connection.cloud_sql.database_engine = "DATABASE_ENGINE_POSTGRES"
        connection.state = "ERROR"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateConnectionRequest.html)(
            name="name_value",
            connection=connection,
        )
    
        # Make the request
        response = await client.[update_connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateConnectionRequest), dict]]`   
The request object. Request message for UpdateConnection.  
`name` |  ``str``   
Required. Resource name in the format: `projects/{project}/locations/{location}/connections/{connection}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.Connection](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Connection)` | A data connection to allow the DLP API to profile data in locations that require additional configuration.  
  
### update_content_policy
    
    
    update_content_policy(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateContentPolicyRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        content_policy: typing.Optional[google.cloud.dlp_v2.types.dlp.ContentPolicy] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.ContentPolicy

Update a ContentPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_content_policy():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        content_policy = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy.html)()
        content_policy.rules.action.return_verdict = "BLOCK"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateContentPolicyRequest.html)(
            name="name_value",
            content_policy=content_policy,
        )
    
        # Make the request
        response = await client.[update_content_policy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_content_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateContentPolicyRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateContentPolicyRequest), dict]]`   
The request object. Request message for UpdateContentPolicy.  
`name` |  ``str``   
Required. Resource name in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`content_policy` |  `[ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy)`   
Required. The content_policy with new values for the relevant fields. This corresponds to the `content_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.ContentPolicy](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ContentPolicy)` | A policy to apply to content based on its inspection findings.  
  
### update_deidentify_template
    
    
    update_deidentify_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.dlp_v2.types.dlp.UpdateDeidentifyTemplateRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        deidentify_template: typing.Optional[
            google.cloud.dlp_v2.types.dlp.DeidentifyTemplate
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
    ) -> google.cloud.dlp_v2.types.dlp.DeidentifyTemplate

Updates the DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_deidentify_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateDeidentifyTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[update_deidentify_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_deidentify_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateDeidentifyTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateDeidentifyTemplateRequest), dict]]`   
The request object. Request message for UpdateDeidentifyTemplate.  
`name` |  ``str``   
Required. Resource name of organization and deidentify template to be updated, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyTemplate)`   
New DeidentifyTemplate value. This corresponds to the `deidentify_template` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DeidentifyTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DeidentifyTemplate)` | DeidentifyTemplates contains instructions on how to de-identify content. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### update_discovery_config
    
    
    update_discovery_config(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateDiscoveryConfigRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        discovery_config: typing.Optional[
            google.cloud.dlp_v2.types.dlp.DiscoveryConfig
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
    ) -> google.cloud.dlp_v2.types.dlp.DiscoveryConfig

Updates a discovery configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_discovery_config():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        discovery_config = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig.html)()
        discovery_config.status = "PAUSED"
    
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateDiscoveryConfigRequest.html)(
            name="name_value",
            discovery_config=discovery_config,
        )
    
        # Make the request
        response = await client.[update_discovery_config](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_discovery_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateDiscoveryConfigRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateDiscoveryConfigRequest), dict]]`   
The request object. Request message for UpdateDiscoveryConfig.  
`name` |  ``str``   
Required. Resource name of the project and the configuration, for example `projects/dlp-test-project/discoveryConfigs/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`discovery_config` |  `[DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig)`   
Required. New DiscoveryConfig value. This corresponds to the `discovery_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.DiscoveryConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DiscoveryConfig)` | Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project. The generated data profiles are retained according to the [data retention policy] (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).  
  
### update_inspect_template
    
    
    update_inspect_template(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateInspectTemplateRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        inspect_template: typing.Optional[
            google.cloud.dlp_v2.types.dlp.InspectTemplate
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
    ) -> google.cloud.dlp_v2.types.dlp.InspectTemplate

Updates the InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_inspect_template():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateInspectTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[update_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_inspect_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateInspectTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateInspectTemplateRequest), dict]]`   
The request object. Request message for UpdateInspectTemplate.  
`name` |  ``str``   
Required. Resource name of organization and inspectTemplate to be updated, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`inspect_template` |  `[InspectTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectTemplate)`   
New InspectTemplate value. This corresponds to the `inspect_template` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.InspectTemplate](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.InspectTemplate)` | The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates to learn more.  
  
### update_job_trigger
    
    
    update_job_trigger(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateJobTriggerRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        job_trigger: typing.Optional[google.cloud.dlp_v2.types.dlp.JobTrigger] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.JobTrigger

Updates a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_job_trigger():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateJobTriggerRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[update_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_job_trigger)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateJobTriggerRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateJobTriggerRequest), dict]]`   
The request object. Request message for UpdateJobTrigger.  
`name` |  ``str``   
Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`job_trigger` |  `[JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger)`   
New JobTrigger value. This corresponds to the `job_trigger` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger)` | Contains a configuration to make API calls on a repeating basis. See https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers to learn more.  
  
### update_stored_info_type
    
    
    update_stored_info_type(
        request: typing.Optional[
            typing.Union[google.cloud.dlp_v2.types.dlp.UpdateStoredInfoTypeRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        config: typing.Optional[google.cloud.dlp_v2.types.dlp.StoredInfoTypeConfig] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.dlp_v2.types.dlp.StoredInfoType

Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    
    async def sample_update_stored_info_type():
        # Create a client
        client = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateStoredInfoTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[update_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceAsyncClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceAsyncClient_update_stored_info_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.dlp_v2.types.UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.UpdateStoredInfoTypeRequest), dict]]`   
The request object. Request message for UpdateStoredInfoType.  
`name` |  ``str``   
Required. Resource name of organization and storedInfoType to be updated, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`config` |  `[StoredInfoTypeConfig](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StoredInfoTypeConfig)`   
Updated configuration for the storedInfoType. If not provided, a new version of the storedInfoType will be created with the existing configuration. This corresponds to the `config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Mask to control which fields get updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.dlp_v2.types.StoredInfoType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StoredInfoType)` | StoredInfoType resource message that contains information about the current version and any pending updates.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
