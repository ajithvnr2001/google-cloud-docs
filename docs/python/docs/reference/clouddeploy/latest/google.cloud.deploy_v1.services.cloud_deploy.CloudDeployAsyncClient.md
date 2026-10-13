---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient
title: Class CloudDeployAsyncClient (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:39.984903+00:00
---

# Class CloudDeployAsyncClient (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudDeployAsyncClient (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    CloudDeployAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                typing.Callable[
                    [...],
                    google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

CloudDeploy service creates and manages Continuous Delivery operations on Google Cloud Platform via Skaffold (<https://skaffold.dev>).

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
`CloudDeployTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudDeployAsyncClient
    
    
    CloudDeployAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                typing.Callable[
                    [...],
                    google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud deploy async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudDeployTransport,Callable[..., CloudDeployTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudDeployTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### abandon_release
    
    
    abandon_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseResponse

Abandons a Release in the Delivery Pipeline.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_abandon_release():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[AbandonReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AbandonReleaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[abandon_release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_abandon_release)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.AbandonReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AbandonReleaseRequest), dict]]`   
The request object. The request object used by `AbandonRelease`.  
`name` |  ``str``   
Required. Name of the Release. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.AbandonReleaseResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AbandonReleaseResponse)` | The response object for AbandonRelease.  
  
### advance_rollout
    
    
    advance_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutResponse

Advances a Rollout in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_advance_rollout():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[AdvanceRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutRequest.html)(
            name="name_value",
            phase_id="phase_id_value",
        )
    
        # Make the request
        response = await client.[advance_rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_advance_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.AdvanceRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutRequest), dict]]`   
The request object. The request object used by `AdvanceRollout`.  
`name` |  ``str``   
Required. Name of the Rollout. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`phase_id` |  ``str``   
Required. The phase ID to advance the `Rollout` to. This corresponds to the `phase_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.AdvanceRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutResponse)` | The response object from AdvanceRollout.  
  
### approve_rollout
    
    
    approve_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutResponse

Approves a Rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_approve_rollout():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ApproveRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ApproveRolloutRequest.html)(
            name="name_value",
            approved=True,
        )
    
        # Make the request
        response = await client.[approve_rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_approve_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ApproveRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ApproveRolloutRequest), dict]]`   
The request object. The request object used by `ApproveRollout`.  
`name` |  ``str``   
Required. Name of the Rollout. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.ApproveRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ApproveRolloutResponse)` | The response object from ApproveRollout.  
  
### automation_path
    
    
    automation_path(
        project: str, location: str, delivery_pipeline: str, automation: str
    ) -> str

Returns a fully-qualified automation string.

### automation_run_path
    
    
    automation_run_path(
        project: str, location: str, delivery_pipeline: str, automation_run: str
    ) -> str

Returns a fully-qualified automation_run string.

### build_path
    
    
    build_path(project: str, location: str, build: str) -> str

Returns a fully-qualified build string.

### cancel_automation_run
    
    
    cancel_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunResponse

Cancels an AutomationRun. The `state` of the `AutomationRun` after cancelling is `CANCELLED`. `CancelAutomationRun` can be called on AutomationRun in the state `IN_PROGRESS` and `PENDING`; AutomationRun in a different state returns an `FAILED_PRECONDITION` error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_cancel_automation_run():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CancelAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelAutomationRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[cancel_automation_run](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cancel_automation_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CancelAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelAutomationRunRequest), dict]]`   
The request object. The request object used by `CancelAutomationRun`.  
`name` |  ``str``   
Required. Name of the `AutomationRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.CancelAutomationRunResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelAutomationRunResponse)` | The response object from CancelAutomationRun.  
  
### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
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

Starts asynchronous cancellation on a long-running operation.

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### cancel_rollout
    
    
    cancel_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutResponse

Cancels a Rollout in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_cancel_rollout():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CancelRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelRolloutRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[cancel_rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cancel_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CancelRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelRolloutRequest), dict]]`   
The request object. The request object used by `CancelRollout`.  
`name` |  ``str``   
Required. Name of the Rollout. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.CancelRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelRolloutResponse)` | The response object from CancelRollout.  
  
### cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

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

### config_path
    
    
    config_path(project: str, location: str) -> str

Returns a fully-qualified config string.

### create_automation
    
    
    create_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateAutomationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
        ] = None,
        automation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Automation in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_automation():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        automation = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation.html)()
        automation.service_account = "service_account_value"
        automation.rules.promote_release_rule.id = "id_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateAutomationRequest.html)(
            parent="parent_value",
            automation_id="automation_id_value",
            automation=automation,
        )
    
        # Make the request
        operation = await client.[create_automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_automation)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateAutomationRequest), dict]]`   
The request object. The request object for `CreateAutomation`.  
`parent` |  ``str``   
Required. The parent collection in which the `Automation` must be created. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`automation` |  `[Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation)`   
Required. The `Automation` to create. This corresponds to the `automation` field on the `request` instance; if `request` is provided, this should not be set.  
`automation_id` |  ``str``   
Required. ID of the `Automation`. This corresponds to the `automation_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation) An Automation resource in the Cloud Deploy API. An Automation enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.  
  
### create_custom_target_type
    
    
    create_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
        ] = None,
        custom_target_type_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new CustomTargetType in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_custom_target_type():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        custom_target_type = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType.html)()
        custom_target_type.custom_actions.deploy_action = "deploy_action_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateCustomTargetTypeRequest.html)(
            parent="parent_value",
            custom_target_type_id="custom_target_type_id_value",
            custom_target_type=custom_target_type,
        )
    
        # Make the request
        operation = await client.[create_custom_target_type](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_custom_target_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateCustomTargetTypeRequest), dict]]`   
The request object. The request object for `CreateCustomTargetType`.  
`parent` |  ``str``   
Required. The parent collection in which the `CustomTargetType` must be created. The format is `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`custom_target_type` |  `[CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType)`   
Required. The `CustomTargetType` to create. This corresponds to the `custom_target_type` field on the `request` instance; if `request` is provided, this should not be set.  
`custom_target_type_id` |  ``str``   
Required. ID of the `CustomTargetType`. This corresponds to the `custom_target_type_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType) A CustomTargetType resource in the Cloud Deploy API. A CustomTargetType defines a type of custom target that can be referenced in a Target in order to facilitate deploying to other systems besides the supported runtimes.  
  
### create_delivery_pipeline
    
    
    create_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
        ] = None,
        delivery_pipeline_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DeliveryPipeline in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_delivery_pipeline():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeliveryPipelineRequest.html)(
            parent="parent_value",
            delivery_pipeline_id="delivery_pipeline_id_value",
        )
    
        # Make the request
        operation = await client.[create_delivery_pipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_delivery_pipeline)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeliveryPipelineRequest), dict]]`   
The request object. The request object for `CreateDeliveryPipeline`.  
`parent` |  ``str``   
Required. The parent collection in which the `DeliveryPipeline` must be created. The format is `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`delivery_pipeline` |  `[DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline)`   
Required. The `DeliveryPipeline` to create. This corresponds to the `delivery_pipeline` field on the `request` instance; if `request` is provided, this should not be set.  
`delivery_pipeline_id` |  ``str``   
Required. ID of the `DeliveryPipeline`. This corresponds to the `delivery_pipeline_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline) A DeliveryPipeline resource in the Cloud Deploy API. A DeliveryPipeline defines a pipeline through which a Skaffold configuration can progress.  
  
### create_deploy_policy
    
    
    create_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
        ] = None,
        deploy_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DeployPolicy in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_deploy_policy():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        deploy_policy = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy.html)()
        deploy_policy.rules.rollout_restriction.id = "id_value"
        deploy_policy.rules.rollout_restriction.time_windows.time_zone = "time_zone_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeployPolicyRequest.html)(
            parent="parent_value",
            deploy_policy_id="deploy_policy_id_value",
            deploy_policy=deploy_policy,
        )
    
        # Make the request
        operation = await client.[create_deploy_policy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_deploy_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeployPolicyRequest), dict]]`   
The request object. The request object for `CreateDeployPolicy`.  
`parent` |  ``str``   
Required. The parent collection in which the `DeployPolicy` must be created. The format is `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`deploy_policy` |  `[DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy)`   
Required. The `DeployPolicy` to create. This corresponds to the `deploy_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`deploy_policy_id` |  ``str``   
Required. ID of the `DeployPolicy`. This corresponds to the `deploy_policy_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy) A DeployPolicy resource in the Cloud Deploy API. A DeployPolicy inhibits manual or automation-driven actions within a Delivery Pipeline or Target.  
  
### create_release
    
    
    create_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateReleaseRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        release: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Release] = None,
        release_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Release in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_release():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateReleaseRequest.html)(
            parent="parent_value",
            release_id="release_id_value",
        )
    
        # Make the request
        operation = await client.[create_release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_release)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateReleaseRequest), dict]]`   
The request object. The request object for `CreateRelease`,  
`parent` |  ``str``   
Required. The parent collection in which the `Release` is created. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`release` |  `[Release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release)`   
Required. The `Release` to create. This corresponds to the `release` field on the `request` instance; if `request` is provided, this should not be set.  
`release_id` |  ``str``   
Required. ID of the `Release`. This corresponds to the `release_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release) A Release resource in the Cloud Deploy API. A Release defines a specific Skaffold configuration instance that can be deployed.  
  
### create_rollout
    
    
    create_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateRolloutRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        rollout: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Rollout] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Rollout in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_rollout():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        rollout = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[Rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.html)()
        rollout.target_id = "target_id_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateRolloutRequest.html)(
            parent="parent_value",
            rollout_id="rollout_id_value",
            rollout=rollout,
        )
    
        # Make the request
        operation = await client.[create_rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_rollout)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateRolloutRequest), dict]]`   
The request object. CreateRolloutRequest is the request object used by `CreateRollout`.  
`parent` |  ``str``   
Required. The parent collection in which the `Rollout` must be created. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout` |  `[Rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout)`   
Required. The `Rollout` to create. This corresponds to the `rollout` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout_id` |  ``str``   
Required. ID of the `Rollout`. This corresponds to the `rollout_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout) A Rollout resource in the Cloud Deploy API. A Rollout contains information around a specific deployment to a Target.  
  
### create_target
    
    
    create_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateTargetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
        target_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Target in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_create_target():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CreateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateTargetRequest.html)(
            parent="parent_value",
            target_id="target_id_value",
        )
    
        # Make the request
        operation = await client.[create_target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_target)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.CreateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateTargetRequest), dict]]`   
The request object. The request object for `CreateTarget`.  
`parent` |  ``str``   
Required. The parent collection in which the `Target` must be created. The format is `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`target` |  `[Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target)`   
Required. The `Target` to create. This corresponds to the `target` field on the `request` instance; if `request` is provided, this should not be set.  
`target_id` |  ``str``   
Required. ID of the `Target`. This corresponds to the `target_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target) A Target resource in the Cloud Deploy API. A Target defines a location to which a Skaffold configuration can be deployed.  
  
### custom_target_type_path
    
    
    custom_target_type_path(
        project: str, location: str, custom_target_type: str
    ) -> str

Returns a fully-qualified custom_target_type string.

### delete_automation
    
    
    delete_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteAutomationRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single Automation resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_delete_automation():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeleteAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteAutomationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_automation)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.DeleteAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteAutomationRequest), dict]]`   
The request object. The request object for `DeleteAutomation`.  
`name` |  ``str``   
Required. The name of the `Automation` to delete. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/automations/{automation_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_custom_target_type
    
    
    delete_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteCustomTargetTypeRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single CustomTargetType.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_delete_custom_target_type():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeleteCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteCustomTargetTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_custom_target_type](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_custom_target_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.DeleteCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteCustomTargetTypeRequest), dict]]`   
The request object. The request object for `DeleteCustomTargetType`.  
`name` |  ``str``   
Required. The name of the `CustomTargetType` to delete. Format must be `projects/{project_id}/locations/{location_name}/customTargetTypes/{custom_target_type}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_delivery_pipeline
    
    
    delete_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeliveryPipelineRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single DeliveryPipeline.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_delete_delivery_pipeline():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeleteDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeliveryPipelineRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_delivery_pipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_delivery_pipeline)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.DeleteDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeliveryPipelineRequest), dict]]`   
The request object. The request object for `DeleteDeliveryPipeline`.  
`name` |  ``str``   
Required. The name of the `DeliveryPipeline` to delete. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_deploy_policy
    
    
    delete_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeployPolicyRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single DeployPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_delete_deploy_policy():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeleteDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeployPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_deploy_policy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_deploy_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.DeleteDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeployPolicyRequest), dict]]`   
The request object. The request object for `DeleteDeployPolicy`.  
`name` |  ``str``   
Required. The name of the `DeployPolicy` to delete. The format is `projects/{project_id}/locations/{location_name}/deployPolicies/{deploy_policy_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
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

Deletes a long-running operation.

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_target
    
    
    delete_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteTargetRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single Target.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_delete_target():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeleteTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteTargetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_target)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.DeleteTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteTargetRequest), dict]]`   
The request object. The request object for `DeleteTarget`.  
`name` |  ``str``   
Required. The name of the `Target` to delete. The format is `projects/{project_id}/locations/{location_name}/targets/{target_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delivery_pipeline_path
    
    
    delivery_pipeline_path(project: str, location: str, delivery_pipeline: str) -> str

Returns a fully-qualified delivery_pipeline string.

### deploy_policy_path
    
    
    deploy_policy_path(project: str, location: str, deploy_policy: str) -> str

Returns a fully-qualified deploy_policy string.

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
`CloudDeployAsyncClient` | The constructed client.  
  
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
`CloudDeployAsyncClient` | The constructed client.  
  
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
`CloudDeployAsyncClient` | The constructed client.  
  
### get_automation
    
    
    get_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Automation

Gets details of a single Automation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_automation():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_automation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRequest), dict]]`   
The request object. The request object for `GetAutomation`  
`name` |  ``str``   
Required. Name of the `Automation`. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/automations/{automation_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation)` | An Automation resource in the Cloud Deploy API. An Automation enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.  
  
### get_automation_run
    
    
    get_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AutomationRun

Gets details of a single AutomationRun.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_automation_run():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_automation_run](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_automation_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRunRequest), dict]]`   
The request object. The request object for `GetAutomationRun`  
`name` |  ``str``   
Required. Name of the `AutomationRun`. Format must be `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.AutomationRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun)` | An AutomationRun resource in the Cloud Deploy API. An AutomationRun represents an execution instance of an automation rule.  
  
### get_config
    
    
    get_config(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetConfigRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Config

Gets the configuration for a location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_config():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetConfigRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_config](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetConfigRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetConfigRequest), dict]]`   
The request object. Request to get a configuration.  
`name` |  ``str``   
Required. Name of requested configuration. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.Config](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Config)` | Service-wide configuration.  
  
### get_custom_target_type
    
    
    get_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetCustomTargetTypeRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType

Gets details of a single CustomTargetType.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_custom_target_type():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetCustomTargetTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_custom_target_type](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_custom_target_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetCustomTargetTypeRequest), dict]]`   
The request object. The request object for `GetCustomTargetType`.  
`name` |  ``str``   
Required. Name of the `CustomTargetType`. Format must be `projects/{project_id}/locations/{location_name}/customTargetTypes/{custom_target_type}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType)` | A CustomTargetType resource in the Cloud Deploy API. A CustomTargetType defines a type of custom target that can be referenced in a Target in order to facilitate deploying to other systems besides the supported runtimes.  
  
### get_delivery_pipeline
    
    
    get_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeliveryPipelineRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline

Gets details of a single DeliveryPipeline.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_delivery_pipeline():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeliveryPipelineRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_delivery_pipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_delivery_pipeline)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeliveryPipelineRequest), dict]]`   
The request object. The request object for `GetDeliveryPipeline`  
`name` |  ``str``   
Required. Name of the `DeliveryPipeline`. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline)` | A DeliveryPipeline resource in the Cloud Deploy API. A DeliveryPipeline defines a pipeline through which a Skaffold configuration can progress.  
  
### get_deploy_policy
    
    
    get_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeployPolicyRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy

Gets details of a single DeployPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_deploy_policy():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeployPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deploy_policy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_deploy_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeployPolicyRequest), dict]]`   
The request object. The request object for `GetDeployPolicy`  
`name` |  ``str``   
Required. Name of the `DeployPolicy`. Format must be `projects/{project_id}/locations/{location_name}/deployPolicies/{deploy_policy_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy)` | A DeployPolicy resource in the Cloud Deploy API. A DeployPolicy inhibits manual or automation-driven actions within a Delivery Pipeline or Target.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### get_job_run
    
    
    get_job_run(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetJobRunRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.JobRun

Gets details of a single JobRun.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_job_run():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetJobRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_job_run](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_job_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetJobRunRequest), dict]]`   
The request object. GetJobRunRequest is the request object used by `GetJobRun`.  
`name` |  ``str``   
Required. Name of the `JobRun`. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}/rollouts/{rollout_name}/jobRuns/{job_run_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.JobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun)` | A JobRun resource in the Cloud Deploy API. A JobRun contains information of a single Rollout job evaluation.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
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
  
### get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
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
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_release
    
    
    get_release(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetReleaseRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Release

Gets details of a single Release.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_release():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetReleaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_release)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetReleaseRequest), dict]]`   
The request object. The request object for `GetRelease`.  
`name` |  ``str``   
Required. Name of the `Release`. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.Release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release)` | A Release resource in the Cloud Deploy API. A Release defines a specific Skaffold configuration instance that can be deployed.  
  
### get_rollout
    
    
    get_rollout(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetRolloutRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Rollout

Gets details of a single Rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_rollout():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetRolloutRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetRolloutRequest), dict]]`   
The request object. GetRolloutRequest is the request object used by `GetRollout`.  
`name` |  ``str``   
Required. Name of the `Rollout`. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}/rollouts/{rollout_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout)` | A Rollout resource in the Cloud Deploy API. A Rollout contains information around a specific deployment to a Target.  
  
### get_target
    
    
    get_target(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetTargetRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Target

Gets details of a single Target.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_get_target():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[GetTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetTargetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_target)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.GetTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetTargetRequest), dict]]`   
The request object. The request object for `GetTarget`.  
`name` |  ``str``   
Required. Name of the `Target`. Format must be `projects/{project_id}/locations/{location_name}/targets/{target_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target)` | A Target resource in the Cloud Deploy API. A Target defines a location to which a Skaffold configuration can be deployed.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### ignore_job
    
    
    ignore_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobResponse

Ignores the specified Job in a Rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_ignore_job():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[IgnoreJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.IgnoreJobRequest.html)(
            rollout="rollout_value",
            phase_id="phase_id_value",
            job_id="job_id_value",
        )
    
        # Make the request
        response = await client.[ignore_job](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_ignore_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.IgnoreJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.IgnoreJobRequest), dict]]`   
The request object. The request object used by `IgnoreJob`.  
`rollout` |  ``str``   
Required. Name of the Rollout. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. This corresponds to the `rollout` field on the `request` instance; if `request` is provided, this should not be set.  
`phase_id` |  ``str``   
Required. The phase ID the Job to ignore belongs to. This corresponds to the `phase_id` field on the `request` instance; if `request` is provided, this should not be set.  
`job_id` |  ``str``   
Required. The job ID for the Job to ignore. This corresponds to the `job_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.IgnoreJobResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.IgnoreJobResponse)` | The response object from IgnoreJob.  
  
### job_path
    
    
    job_path(project: str, location: str, job: str) -> str

Returns a fully-qualified job string.

### job_run_path
    
    
    job_run_path(
        project: str,
        location: str,
        delivery_pipeline: str,
        release: str,
        rollout: str,
        job_run: str,
    ) -> str

Returns a fully-qualified job_run string.

### list_automation_runs
    
    
    list_automation_runs(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager

Lists AutomationRuns in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_automation_runs():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListAutomationRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_automation_runs](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_automation_runs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListAutomationRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsRequest), dict]]`   
The request object. The request object for `ListAutomationRuns`.  
`parent` |  ``str``   
Required. The parent `Delivery Pipeline`, which owns this collection of automationRuns. Format must be `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager)` | The response object from ListAutomationRuns. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_automations
    
    
    list_automations(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager

Lists Automations in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_automations():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListAutomationsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_automations](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_automations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListAutomationsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsRequest), dict]]`   
The request object. The request object for `ListAutomations`.  
`parent` |  ``str``   
Required. The parent `Delivery Pipeline`, which owns this collection of automations. Format must be `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager)` | The response object from ListAutomations. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_custom_target_types
    
    
    list_custom_target_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest, dict
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
        google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager
    )

Lists CustomTargetTypes in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_custom_target_types():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListCustomTargetTypesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_custom_target_types](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_custom_target_types)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListCustomTargetTypesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesRequest), dict]]`   
The request object. The request object for `ListCustomTargetTypes`.  
`parent` |  ``str``   
Required. The parent that owns this collection of custom target types. Format must be `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager)` | The response object from ListCustomTargetTypes. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_delivery_pipelines
    
    
    list_delivery_pipelines(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest, dict
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
        google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager
    )

Lists DeliveryPipelines in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_delivery_pipelines():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListDeliveryPipelinesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_delivery_pipelines](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_delivery_pipelines)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest), dict]]`   
The request object. The request object for `ListDeliveryPipelines`.  
`parent` |  ``str``   
Required. The parent, which owns this collection of pipelines. Format must be `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager)` | The response object from ListDeliveryPipelines. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_deploy_policies
    
    
    list_deploy_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager

Lists DeployPolicies in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_deploy_policies():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListDeployPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deploy_policies](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_deploy_policies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListDeployPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesRequest), dict]]`   
The request object. The request object for `ListDeployPolicies`.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deploy policies. Format must be `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager)` | The response object from ListDeployPolicies. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_job_runs
    
    
    list_job_runs(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager

Lists JobRuns in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_job_runs():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListJobRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_job_runs](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_job_runs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListJobRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsRequest), dict]]`   
The request object. ListJobRunsRequest is the request object used by `ListJobRuns`.  
`parent` |  ``str``   
Required. The `Rollout` which owns this collection of `JobRun` objects. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager)` | ListJobRunsResponse is the response object returned by ListJobRuns. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
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
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_releases
    
    
    list_releases(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager

Lists Releases in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_releases():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListReleasesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_releases](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_releases)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListReleasesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesRequest), dict]]`   
The request object. The request object for `ListReleases`.  
`parent` |  ``str``   
Required. The `DeliveryPipeline` which owns this collection of `Release` objects. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager)` | The response object from ListReleases. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_rollouts
    
    
    list_rollouts(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager

Lists Rollouts in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_rollouts():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListRolloutsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_rollouts](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_rollouts)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListRolloutsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsRequest), dict]]`   
The request object. ListRolloutsRequest is the request object used by `ListRollouts`.  
`parent` |  ``str``   
Required. The `Release` which owns this collection of `Rollout` objects. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager)` | ListRolloutsResponse is the response object returned by ListRollouts. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_targets
    
    
    list_targets(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager

Lists Targets in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_list_targets():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[ListTargetsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_targets](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_targets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.ListTargetsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsRequest), dict]]`   
The request object. The request object for `ListTargets`.  
`parent` |  ``str``   
Required. The parent, which owns this collection of targets. Format must be `projects/{project_id}/locations/{location_name}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager)` | The response object from ListTargets. Iterating over this object will yield results and resolve additional pages automatically.  
  
### membership_path
    
    
    membership_path(project: str, location: str, membership: str) -> str

Returns a fully-qualified membership string.

### parse_automation_path
    
    
    parse_automation_path(path: str) -> typing.Dict[str, str]

Parses a automation path into its component segments.

### parse_automation_run_path
    
    
    parse_automation_run_path(path: str) -> typing.Dict[str, str]

Parses a automation_run path into its component segments.

### parse_build_path
    
    
    parse_build_path(path: str) -> typing.Dict[str, str]

Parses a build path into its component segments.

### parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

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

### parse_config_path
    
    
    parse_config_path(path: str) -> typing.Dict[str, str]

Parses a config path into its component segments.

### parse_custom_target_type_path
    
    
    parse_custom_target_type_path(path: str) -> typing.Dict[str, str]

Parses a custom_target_type path into its component segments.

### parse_delivery_pipeline_path
    
    
    parse_delivery_pipeline_path(path: str) -> typing.Dict[str, str]

Parses a delivery_pipeline path into its component segments.

### parse_deploy_policy_path
    
    
    parse_deploy_policy_path(path: str) -> typing.Dict[str, str]

Parses a deploy_policy path into its component segments.

### parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

### parse_job_run_path
    
    
    parse_job_run_path(path: str) -> typing.Dict[str, str]

Parses a job_run path into its component segments.

### parse_membership_path
    
    
    parse_membership_path(path: str) -> typing.Dict[str, str]

Parses a membership path into its component segments.

### parse_release_path
    
    
    parse_release_path(path: str) -> typing.Dict[str, str]

Parses a release path into its component segments.

### parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

### parse_rollout_path
    
    
    parse_rollout_path(path: str) -> typing.Dict[str, str]

Parses a rollout path into its component segments.

### parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

### parse_target_path
    
    
    parse_target_path(path: str) -> typing.Dict[str, str]

Parses a target path into its component segments.

### parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

### release_path
    
    
    release_path(
        project: str, location: str, delivery_pipeline: str, release: str
    ) -> str

Returns a fully-qualified release string.

### repository_path
    
    
    repository_path(
        project: str, location: str, connection: str, repository: str
    ) -> str

Returns a fully-qualified repository string.

### retry_job
    
    
    retry_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.RetryJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RetryJobResponse

Retries the specified Job in a Rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_retry_job():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[RetryJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryJobRequest.html)(
            rollout="rollout_value",
            phase_id="phase_id_value",
            job_id="job_id_value",
        )
    
        # Make the request
        response = await client.[retry_job](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_retry_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.RetryJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryJobRequest), dict]]`   
The request object. RetryJobRequest is the request object used by `RetryJob`.  
`rollout` |  ``str``   
Required. Name of the Rollout. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. This corresponds to the `rollout` field on the `request` instance; if `request` is provided, this should not be set.  
`phase_id` |  ``str``   
Required. The phase ID the Job to retry belongs to. This corresponds to the `phase_id` field on the `request` instance; if `request` is provided, this should not be set.  
`job_id` |  ``str``   
Required. The job ID for the Job to retry. This corresponds to the `job_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.RetryJobResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryJobResponse)` | The response object from 'RetryJob'.  
  
### rollback_target
    
    
    rollback_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        target_id: typing.Optional[str] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetResponse

Creates a `Rollout` to roll back the specified target.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_rollback_target():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[RollbackTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetRequest.html)(
            name="name_value",
            target_id="target_id_value",
            rollout_id="rollout_id_value",
        )
    
        # Make the request
        response = await client.[rollback_target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_rollback_target)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.RollbackTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetRequest), dict]]`   
The request object. The request object for `RollbackTarget`.  
`name` |  ``str``   
Required. The `DeliveryPipeline` for which the rollback `Rollout` must be created. The format is `projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`target_id` |  ``str``   
Required. ID of the `Target` that is being rolled back. This corresponds to the `target_id` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout_id` |  ``str``   
Required. ID of the rollback `Rollout` to create. This corresponds to the `rollout_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.RollbackTargetResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetResponse)` | The response object from RollbackTarget.  
  
### rollout_path
    
    
    rollout_path(
        project: str, location: str, delivery_pipeline: str, release: str, rollout: str
    ) -> str

Returns a fully-qualified rollout string.

### service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### target_path
    
    
    target_path(project: str, location: str, target: str) -> str

Returns a fully-qualified target string.

### terminate_job_run
    
    
    terminate_job_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunResponse

Terminates a Job Run in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_terminate_job_run():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[TerminateJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TerminateJobRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[terminate_job_run](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_terminate_job_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.TerminateJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TerminateJobRunRequest), dict]]`   
The request object. The request object used by `TerminateJobRun`.  
`name` |  ``str``   
Required. Name of the `JobRun`. Format must be `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}/jobRuns/{jobRun}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.deploy_v1.types.TerminateJobRunResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TerminateJobRunResponse)` | The response object from TerminateJobRun.  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### update_automation
    
    
    update_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateAutomationRequest, dict
            ]
        ] = None,
        *,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single Automation resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_update_automation():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        automation = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation.html)()
        automation.service_account = "service_account_value"
        automation.rules.promote_release_rule.id = "id_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[UpdateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateAutomationRequest.html)(
            automation=automation,
        )
    
        # Make the request
        operation = await client.[update_automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_automation)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.UpdateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateAutomationRequest), dict]]`   
The request object. The request object for `UpdateAutomation`.  
`automation` |  `[Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation)`   
Required. The `Automation` to update. This corresponds to the `automation` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten by the update in the `Automation` resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it's in the mask. If the user doesn't provide a mask then all fields are overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation) An Automation resource in the Cloud Deploy API. An Automation enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.  
  
### update_custom_target_type
    
    
    update_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates a single CustomTargetType.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_update_custom_target_type():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        custom_target_type = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType.html)()
        custom_target_type.custom_actions.deploy_action = "deploy_action_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[UpdateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateCustomTargetTypeRequest.html)(
            custom_target_type=custom_target_type,
        )
    
        # Make the request
        operation = await client.[update_custom_target_type](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_custom_target_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.UpdateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateCustomTargetTypeRequest), dict]]`   
The request object. The request object for `UpdateCustomTargetType`.  
`custom_target_type` |  `[CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType)`   
Required. The `CustomTargetType` to update. This corresponds to the `custom_target_type` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten by the update in the `CustomTargetType` resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it's in the mask. If the user doesn't provide a mask then all fields are overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType) A CustomTargetType resource in the Cloud Deploy API. A CustomTargetType defines a type of custom target that can be referenced in a Target in order to facilitate deploying to other systems besides the supported runtimes.  
  
### update_delivery_pipeline
    
    
    update_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single DeliveryPipeline.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_update_delivery_pipeline():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[UpdateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeliveryPipelineRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_delivery_pipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_delivery_pipeline)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.UpdateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeliveryPipelineRequest), dict]]`   
The request object. The request object for `UpdateDeliveryPipeline`.  
`delivery_pipeline` |  `[DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline)`   
Required. The `DeliveryPipeline` to update. This corresponds to the `delivery_pipeline` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten by the update in the `DeliveryPipeline` resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it's in the mask. If the user doesn't provide a mask then all fields are overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline) A DeliveryPipeline resource in the Cloud Deploy API. A DeliveryPipeline defines a pipeline through which a Skaffold configuration can progress.  
  
### update_deploy_policy
    
    
    update_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single DeployPolicy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_update_deploy_policy():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        deploy_policy = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy.html)()
        deploy_policy.rules.rollout_restriction.id = "id_value"
        deploy_policy.rules.rollout_restriction.time_windows.time_zone = "time_zone_value"
    
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[UpdateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeployPolicyRequest.html)(
            deploy_policy=deploy_policy,
        )
    
        # Make the request
        operation = await client.[update_deploy_policy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_deploy_policy)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.UpdateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeployPolicyRequest), dict]]`   
The request object. The request object for `UpdateDeployPolicy`.  
`deploy_policy` |  `[DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy)`   
Required. The `DeployPolicy` to update. This corresponds to the `deploy_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten by the update in the `DeployPolicy` resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it's in the mask. If the user doesn't provide a mask then all fields are overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy) A DeployPolicy resource in the Cloud Deploy API. A DeployPolicy inhibits manual or automation-driven actions within a Delivery Pipeline or Target.  
  
### update_target
    
    
    update_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateTargetRequest, dict
            ]
        ] = None,
        *,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single Target.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest)
    
    async def sample_update_target():
        # Create a client
        client = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [deploy_v1](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest).[UpdateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateTargetRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.html#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_target)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.deploy_v1.types.UpdateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateTargetRequest), dict]]`   
The request object. The request object for `UpdateTarget`.  
`target` |  `[Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target)`   
Required. The `Target` to update. This corresponds to the `target` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten by the update in the `Target` resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it's in the mask. If the user doesn't provide a mask then all fields are overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target) A Target resource in the Cloud Deploy API. A Target defines a location to which a Skaffold configuration can be deployed.  
  
### worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
