---
url: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient
title: Class LivestreamServiceAsyncClient (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:58.940867+00:00
---

# Class LivestreamServiceAsyncClient (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LivestreamServiceAsyncClient (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.1  1.7.4  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.4  0.2.0  0.1.5 
    
    
    LivestreamServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.video.live_stream_v1.services.livestream_service.transports.base.LivestreamServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.video.live_stream_v1.services.livestream_service.transports.base.LivestreamServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Using Live Stream API, you can generate live streams in the various renditions and streaming formats. The streaming format include HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send a source stream in the various ways, including Real-Time Messaging Protocol (RTMP) and Secure Reliable Transport (SRT).

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
`LivestreamServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### LivestreamServiceAsyncClient
    
    
    LivestreamServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.video.live_stream_v1.services.livestream_service.transports.base.LivestreamServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.video.live_stream_v1.services.livestream_service.transports.base.LivestreamServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the livestream service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,LivestreamServiceTransport,Callable[..., LivestreamServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the LivestreamServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### asset_path
    
    
    asset_path(project: str, location: str, asset: str) -> str

Returns a fully-qualified asset string.

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
  
### channel_path
    
    
    channel_path(project: str, location: str, channel: str) -> str

Returns a fully-qualified channel string.

### clip_path
    
    
    clip_path(project: str, location: str, channel: str, clip: str) -> str

Returns a fully-qualified clip string.

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

### create_asset
    
    
    create_asset(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateAssetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        asset: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Asset
        ] = None,
        asset_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a Asset with the provided unique ID in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_asset():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateAssetRequest.html)(
            parent="parent_value",
            asset_id="asset_id_value",
        )
    
        # Make the request
        operation = await client.[create_asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_asset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateAssetRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateAsset".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`asset` |  `[Asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Asset)`   
Required. The asset resource to be created. This corresponds to the `asset` field on the `request` instance; if `request` is provided, this should not be set.  
`asset_id` |  ``str``   
Required. The ID of the asset resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `asset_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Asset) An asset represents a video or an image.  
  
### create_channel
    
    
    create_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateChannelRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        channel: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Channel
        ] = None,
        channel_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a channel with the provided unique ID in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateChannelRequest.html)(
            parent="parent_value",
            channel_id="channel_id_value",
        )
    
        # Make the request
        operation = await client.[create_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_channel)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateChannel".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`channel` |  `[Channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel)`   
Required. The channel resource to be created. This corresponds to the `channel` field on the `request` instance; if `request` is provided, this should not be set.  
`channel_id` |  ``str``   
Required. The ID of the channel resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `channel_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel) Channel resource represents the processor that does a user-defined "streaming" operation, which includes getting an input stream through an input, transcoding it to multiple renditions, and publishing output live streams in certain formats (for example, HLS or DASH) to the specified location.  
  
### create_clip
    
    
    create_clip(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateClipRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        clip: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Clip
        ] = None,
        clip_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a clip with the provided clip ID in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_clip():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        clip = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[Clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Clip.html)()
        clip.clip_manifests.manifest_key = "manifest_key_value"
    
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateClipRequest.html)(
            parent="parent_value",
            clip_id="clip_id_value",
            clip=clip,
        )
    
        # Make the request
        operation = await client.[create_clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_clip)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateClipRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateClip".  
`parent` |  ``str``   
Required. The parent resource name, in the following form: `projects/{project}/locations/{location}/channels/{channel}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`clip` |  `[Clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Clip)`   
Required. The resource being created This corresponds to the `clip` field on the `request` instance; if `request` is provided, this should not be set.  
`clip_id` |  ``str``   
Required. The ID of the clip resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `clip_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Clip) Clip is a sub-resource under channel. Each clip represents a clipping operation that generates a VOD playlist from its channel given a set of timestamp ranges.  
  
### create_dvr_session
    
    
    create_dvr_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateDvrSessionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dvr_session: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.DvrSession
        ] = None,
        dvr_session_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a DVR session with the provided unique ID in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_dvr_session():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        dvr_session = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession.html)()
        dvr_session.dvr_manifests.manifest_key = "manifest_key_value"
    
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateDvrSessionRequest.html)(
            parent="parent_value",
            dvr_session_id="dvr_session_id_value",
            dvr_session=dvr_session,
        )
    
        # Make the request
        operation = await client.[create_dvr_session](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_dvr_session)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateDvrSessionRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateDvrSession".  
`parent` |  ``str``   
Required. The parent resource name, in the following form: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`dvr_session` |  `[DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession)`   
Required. The resource being created This corresponds to the `dvr_session` field on the `request` instance; if `request` is provided, this should not be set.  
`dvr_session_id` |  ``str``   
Required. The ID of the DVR session resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `dvr_session_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession) DvrSession is a sub-resource under channel. Each DvrSession represents a DVR recording of the live stream for a specific time range.  
  
### create_event
    
    
    create_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateEventRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        event: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Event
        ] = None,
        event_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.video.live_stream_v1.types.resources.Event

Creates an event with the provided unique ID in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_event():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateEventRequest.html)(
            parent="parent_value",
            event_id="event_id_value",
        )
    
        # Make the request
        response = await client.[create_event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateEventRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateEvent".  
`parent` |  ``str``   
Required. The parent channel for the resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`event` |  `[Event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Event)`   
Required. The event resource to be created. This corresponds to the `event` field on the `request` instance; if `request` is provided, this should not be set.  
`event_id` |  ``str``   
Required. The ID of the event resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `event_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Event)` | Event is a sub-resource of a channel, which can be scheduled by the user to execute operations on a channel resource without having to stop the channel.  
  
### create_input
    
    
    create_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.CreateInputRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        input: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Input
        ] = None,
        input_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates an input with the provided unique ID in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_create_input():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[CreateInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateInputRequest.html)(
            parent="parent_value",
            input_id="input_id_value",
        )
    
        # Make the request
        operation = await client.[create_input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_create_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.CreateInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.CreateInputRequest), dict]]`   
The request object. Request message for "LivestreamService.CreateInput".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`input` |  `[Input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Input)`   
Required. The input resource to be created. This corresponds to the `input` field on the `request` instance; if `request` is provided, this should not be set.  
`input_id` |  ``str``   
Required. The ID of the input resource to be created. This value must be 1-63 characters, begin and end with a lower-case letter or a number, and consist of only lower-case letters, numbers, and hyphens. In other words, it must match the following regex: `^[a-z0-9](https://docs.cloud.google.com/python/docs/reference/livestream/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. This corresponds to the `input_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Input) Input resource represents the endpoint from which the channel ingests the input stream.  
  
### delete_asset
    
    
    delete_asset(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteAssetRequest, dict
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

Deletes the specified asset if it is not used.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_asset():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteAssetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_asset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteAssetRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteAsset".  
`name` |  ``str``   
Required. The name of the asset resource, in the form of: `projects/{project}/locations/{location}/assets/{assetId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_channel
    
    
    delete_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteChannelRequest, dict
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

Deletes the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteChannelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_channel)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteChannel".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_clip
    
    
    delete_clip(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteClipRequest, dict
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

Deletes the specified clip job resource. This method only deletes the clip job and does not delete the VOD clip stored in Cloud Storage.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_clip():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteClipRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_clip)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteClipRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteClip".  
`name` |  ``str``   
Required. The name of the clip resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}/clips/{clipId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_dvr_session
    
    
    delete_dvr_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteDvrSessionRequest,
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

Deletes the specified DVR session.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_dvr_session():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteDvrSessionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_dvr_session](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_dvr_session)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteDvrSessionRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteDvrSession".  
`name` |  ``str``   
Required. The name of the event resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_event
    
    
    delete_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteEventRequest, dict
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

Deletes the specified event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_event():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_event)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteEventRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteEvent".  
`name` |  ``str``   
Required. The name of the event resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_input
    
    
    delete_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.DeleteInputRequest, dict
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

Deletes the specified input.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_delete_input():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DeleteInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_delete_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.DeleteInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DeleteInputRequest), dict]]`   
The request object. Request message for "LivestreamService.DeleteInput".  
`name` |  ``str``   
Required. The name of the input resource, in the form of: `projects/{project}/locations/{location}/inputs/{inputId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### dvr_session_path
    
    
    dvr_session_path(
        project: str, location: str, channel: str, dvr_session: str
    ) -> str

Returns a fully-qualified dvr_session string.

### event_path
    
    
    event_path(project: str, location: str, channel: str, event: str) -> str

Returns a fully-qualified event string.

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
`LivestreamServiceAsyncClient` | The constructed client.  
  
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
`LivestreamServiceAsyncClient` | The constructed client.  
  
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
`LivestreamServiceAsyncClient` | The constructed client.  
  
### get_asset
    
    
    get_asset(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetAssetRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Asset

Returns the specified asset.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_asset():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetAssetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_asset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetAssetRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetAssetRequest), dict]]`   
The request object. Request message for "LivestreamService.GetAsset".  
`name` |  ``str``   
Required. Name of the resource, in the following form: `projects/{project}/locations/{location}/assets/{asset}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Asset](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Asset)` | An asset represents a video or an image.  
  
### get_channel
    
    
    get_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetChannelRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Channel

Returns the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetChannelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_channel)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.GetChannel".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel)` | Channel resource represents the processor that does a user-defined "streaming" operation, which includes getting an input stream through an input, transcoding it to multiple renditions, and publishing output live streams in certain formats (for example, HLS or DASH) to the specified location.  
  
### get_clip
    
    
    get_clip(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetClipRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Clip

Returns the specified clip.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_clip():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetClipRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_clip)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetClipRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetClipRequest), dict]]`   
The request object. Request message for "LivestreamService.GetClip".  
`name` |  ``str``   
Required. Name of the resource, in the following form: `projects/{project}/locations/{location}/channels/{channel}/clips/{clip}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Clip](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Clip)` | Clip is a sub-resource under channel. Each clip represents a clipping operation that generates a VOD playlist from its channel given a set of timestamp ranges.  
  
### get_dvr_session
    
    
    get_dvr_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetDvrSessionRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.DvrSession

Returns the specified DVR session.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_dvr_session():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetDvrSessionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_dvr_session](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_dvr_session)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetDvrSessionRequest), dict]]`   
The request object. Request message for "LivestreamService.GetDvrSession".  
`name` |  ``str``   
Required. Name of the resource, in the following form: `projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession)` | DvrSession is a sub-resource under channel. Each DvrSession represents a DVR recording of the live stream for a specific time range.  
  
### get_event
    
    
    get_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetEventRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Event

Returns the specified event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_event():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetEventRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetEventRequest), dict]]`   
The request object. Request message for "LivestreamService.GetEvent".  
`name` |  ``str``   
Required. The name of the event resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Event](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Event)` | Event is a sub-resource of a channel, which can be scheduled by the user to execute operations on a channel resource without having to stop the channel.  
  
### get_input
    
    
    get_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetInputRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Input

Returns the specified input.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_input():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_input)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetInputRequest), dict]]`   
The request object. Request message for "LivestreamService.GetInput".  
`name` |  ``str``   
Required. The name of the input resource, in the form of: `projects/{project}/locations/{location}/inputs/{inputId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Input)` | Input resource represents the endpoint from which the channel ingests the input stream.  
  
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
  
### get_pool
    
    
    get_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.GetPoolRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.resources.Pool

Returns the specified pool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_get_pool():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[GetPoolRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetPoolRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_pool](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_get_pool)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.GetPoolRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.GetPoolRequest), dict]]`   
The request object. Request message for "LivestreamService.GetPool".  
`name` |  ``str``   
Required. The name of the pool resource, in the form of: `projects/{project}/locations/{location}/pools/{poolId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.Pool](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Pool)` | Pool resource defines the configuration of Live Stream pools for a specific location. Currently we support only one pool resource per project per location. After the creation of the first input, a default pool is created automatically at "projects/{project}/locations/{location}/pools/default".  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.video.live_stream_v1.services.livestream_service.transports.base.LivestreamServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### input_path
    
    
    input_path(project: str, location: str, input: str) -> str

Returns a fully-qualified input string.

### list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListAssetsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListAssetsAsyncPager
    )

Returns a list of all assets in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_assets():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListAssetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_assets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListAssetsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListAssets".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListAssetsAsyncPager)` | Response message for "LivestreamService.ListAssets". Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_channels
    
    
    list_channels(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListChannelsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListChannelsAsyncPager
    )

Returns a list of all channels in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_channels():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListChannelsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListChannelsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_channels](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_channels)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListChannelsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListChannelsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListChannels".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListChannelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListChannelsAsyncPager)` | Response message for "LivestreamService.ListChannels". Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_clips
    
    
    list_clips(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListClipsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListClipsAsyncPager
    )

Returns a list of all clips in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_clips():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListClipsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListClipsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_clips](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_clips)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListClipsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListClipsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListClips".  
`parent` |  ``str``   
Required. Parent value for ListClipsRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListClipsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListClipsAsyncPager)` | Response message for "LivestreamService.ListClips". Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_dvr_sessions
    
    
    list_dvr_sessions(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListDvrSessionsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListDvrSessionsAsyncPager
    )

Returns a list of all DVR sessions in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_dvr_sessions():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListDvrSessionsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListDvrSessionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_dvr_sessions](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_dvr_sessions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListDvrSessionsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListDvrSessionsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListDvrSessions".  
`parent` |  ``str``   
Required. Parent value for ListDvrSessionsRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListDvrSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListDvrSessionsAsyncPager)` | Response message for "LivestreamService.ListDvrSessions". Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_events
    
    
    list_events(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListEventsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListEventsAsyncPager
    )

Returns a list of all events in the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_events():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListEventsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListEventsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_events](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_events)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListEventsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListEventsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListEvents".  
`parent` |  ``str``   
Required. The parent channel for the resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListEventsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListEventsAsyncPager)` | Response message for "LivestreamService.ListEvents". Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_inputs
    
    
    list_inputs(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.ListInputsRequest, dict
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
        google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListInputsAsyncPager
    )

Returns a list of all inputs in the specified region.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_list_inputs():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[ListInputsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListInputsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_inputs](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_list_inputs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.ListInputsRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ListInputsRequest), dict]]`   
The request object. Request message for "LivestreamService.ListInputs".  
`parent` |  ``str``   
Required. The parent location for the resource, in the form of: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListInputsAsyncPager](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.pagers.ListInputsAsyncPager)` | Response message for "LivestreamService.ListInputs". Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

### parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

### parse_channel_path
    
    
    parse_channel_path(path: str) -> typing.Dict[str, str]

Parses a channel path into its component segments.

### parse_clip_path
    
    
    parse_clip_path(path: str) -> typing.Dict[str, str]

Parses a clip path into its component segments.

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

### parse_dvr_session_path
    
    
    parse_dvr_session_path(path: str) -> typing.Dict[str, str]

Parses a dvr_session path into its component segments.

### parse_event_path
    
    
    parse_event_path(path: str) -> typing.Dict[str, str]

Parses a event path into its component segments.

### parse_input_path
    
    
    parse_input_path(path: str) -> typing.Dict[str, str]

Parses a input path into its component segments.

### parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

### parse_pool_path
    
    
    parse_pool_path(path: str) -> typing.Dict[str, str]

Parses a pool path into its component segments.

### parse_secret_version_path
    
    
    parse_secret_version_path(path: str) -> typing.Dict[str, str]

Parses a secret_version path into its component segments.

### pool_path
    
    
    pool_path(project: str, location: str, pool: str) -> str

Returns a fully-qualified pool string.

### preview_input
    
    
    preview_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.PreviewInputRequest, dict
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
    ) -> google.cloud.video.live_stream_v1.types.service.PreviewInputResponse

Preview the streaming content of the specified input.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_preview_input():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[PreviewInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.PreviewInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[preview_input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_preview_input)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.PreviewInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.PreviewInputRequest), dict]]`   
The request object. Request message for "LivestreamService.PreviewInput".  
`name` |  ``str``   
Required. The name of the input resource, in the form of: `projects/{project}/locations/{location}/inputs/{inputId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.video.live_stream_v1.types.PreviewInputResponse](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.PreviewInputResponse)` | Response message for "LivestreamService.PreviewInput"  
  
### secret_version_path
    
    
    secret_version_path(project: str, secret: str, version: str) -> str

Returns a fully-qualified secret_version string.

### start_channel
    
    
    start_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.StartChannelRequest, dict
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

Starts the specified channel. Part of the video pipeline will be created only when the StartChannel request is received by the server.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_start_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[StartChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StartChannelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[start_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_start_channel)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.StartChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StartChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.StartChannel".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ChannelOperationResponse](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ChannelOperationResponse) Response message for Start/Stop Channel long-running operations.  
  
### start_distribution
    
    
    start_distribution(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.StartDistributionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        distribution_keys: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Starts distribution which delivers outputs to the destination indicated by the Distribution configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_start_distribution():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[StartDistributionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StartDistributionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[start_distribution](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_start_distribution)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.StartDistributionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StartDistributionRequest), dict]]`   
The request object. Request message for "LivestreamService.StartDistribution".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`distribution_keys` |  `:class:`MutableSequence[str]``   
Optional. A list of keys to identify the distribution configuration in the channel resource. If left empty, all the distributions in the channel specification will be started. This corresponds to the `distribution_keys` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ChannelOperationResponse](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ChannelOperationResponse) Response message for Start/Stop Channel long-running operations.  
  
### stop_channel
    
    
    stop_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.StopChannelRequest, dict
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

Stops the specified channel. Part of the video pipeline will be released when the StopChannel request is received by the server.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_stop_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[StopChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StopChannelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[stop_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_stop_channel)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.StopChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StopChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.StopChannel".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ChannelOperationResponse](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ChannelOperationResponse) Response message for Start/Stop Channel long-running operations.  
  
### stop_distribution
    
    
    stop_distribution(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.StopDistributionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        distribution_keys: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Stops the specified distribution.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_stop_distribution():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[StopDistributionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StopDistributionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[stop_distribution](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_stop_distribution)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.StopDistributionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.StopDistributionRequest), dict]]`   
The request object. Request message for "LivestreamService.StopDistribution".  
`name` |  ``str``   
Required. The name of the channel resource, in the form of: `projects/{project}/locations/{location}/channels/{channelId}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`distribution_keys` |  `:class:`MutableSequence[str]``   
Optional. A list of key to identify the distribution configuration in the channel resource. If left empty, all the distributions in the channel specification will be stopped. This corresponds to the `distribution_keys` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ChannelOperationResponse](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.ChannelOperationResponse) Response message for Start/Stop Channel long-running operations.  
  
### update_channel
    
    
    update_channel(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.UpdateChannelRequest, dict
            ]
        ] = None,
        *,
        channel: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Channel
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

Updates the specified channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_update_channel():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[UpdateChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateChannelRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_update_channel)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.UpdateChannelRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateChannelRequest), dict]]`   
The request object. Request message for "LivestreamService.UpdateChannel".  
`channel` |  `[Channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel)`   
Required. The channel resource to be updated. This corresponds to the `channel` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Field mask is used to specify the fields to be overwritten in the Channel resource by the update. You can only update the following fields: - 
    
    
    inputAttachments` __ - 

inputConfig`<code> <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig></code>__ - <pre>output`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output>`**\- elementaryStreams`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream>`** \- 
    
    
    muxStreams` __ - 

manifests`<code> <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest></code>__ - <pre>spriteSheets`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet>`**\- logConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig>`** \- 
    
    
    timecodeConfig` __ - 

encryptions`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption>`__ The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the mask is not present, then each field from the list above is updated if the field appears in the request payload. To unset a field, add the field to the update mask and remove it from the request payload. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Channel](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Channel) Channel resource represents the processor that does a user-defined "streaming" operation, which includes getting an input stream through an input, transcoding it to multiple renditions, and publishing output live streams in certain formats (for example, HLS or DASH) to the specified location.  
  
### update_dvr_session
    
    
    update_dvr_session(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.UpdateDvrSessionRequest,
                dict,
            ]
        ] = None,
        *,
        dvr_session: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.DvrSession
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

Updates the specified DVR session.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_update_dvr_session():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        dvr_session = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession.html)()
        dvr_session.dvr_manifests.manifest_key = "manifest_key_value"
    
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[UpdateDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateDvrSessionRequest.html)(
            dvr_session=dvr_session,
        )
    
        # Make the request
        operation = await client.[update_dvr_session](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_update_dvr_session)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.UpdateDvrSessionRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateDvrSessionRequest), dict]]`   
The request object. Request message for "LivestreamService.UpdateDvrSession".  
`dvr_session` |  `[DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession)`   
Required. The DVR session resource to be updated. This corresponds to the `dvr_session` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Field mask is used to specify the fields to be overwritten in the DvrSession resource by the update. You can only update the following fields: - `dvrWindows` The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DvrSession](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.DvrSession) DvrSession is a sub-resource under channel. Each DvrSession represents a DVR recording of the live stream for a specific time range.  
  
### update_input
    
    
    update_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.UpdateInputRequest, dict
            ]
        ] = None,
        *,
        input: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Input
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

Updates the specified input.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_update_input():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[UpdateInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateInputRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_update_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.UpdateInputRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdateInputRequest), dict]]`   
The request object. Request message for "LivestreamService.UpdateInput".  
`input` |  `[Input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Input)`   
Required. The input resource to be updated. This corresponds to the `input` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Field mask is used to specify the fields to be overwritten in the Input resource by the update. You can only update the following fields: - `<code>tier</code><code> <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Tier></code>__ -``preprocessingConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#PreprocessingConfig>`**\- ```securityRules`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule>`** The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the mask is not present, then each field from the list above is updated if the field appears in the request payload. To unset a field, add the field to the update mask and remove it from the request payload. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Input](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Input) Input resource represents the endpoint from which the channel ingests the input stream.  
  
### update_pool
    
    
    update_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.video.live_stream_v1.types.service.UpdatePoolRequest, dict
            ]
        ] = None,
        *,
        pool: typing.Optional[
            google.cloud.video.live_stream_v1.types.resources.Pool
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

Updates the specified pool.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud.video import [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest)
    
    async def sample_update_pool():
        # Create a client
        client = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[LivestreamServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [live_stream_v1](https://docs.cloud.google.com/python/docs/reference/livestream/latest).[UpdatePoolRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdatePoolRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_pool](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.services.livestream_service.LivestreamServiceAsyncClient.html#google_cloud_video_live_stream_v1_services_livestream_service_LivestreamServiceAsyncClient_update_pool)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.video.live_stream_v1.types.UpdatePoolRequest](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.UpdatePoolRequest), dict]]`   
The request object. Request message for "LivestreamService.UpdatePool".  
`pool` |  `[Pool](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Pool)`   
Required. The pool resource to be updated. This corresponds to the `pool` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Field mask is used to specify the fields to be overwritten in the Pool resource by the update. You can only update the following fields: - `networkConfig` The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Pool](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.Pool) Pool resource defines the configuration of Live Stream pools for a specific location. Currently we support only one pool resource per project per location. After the creation of the first input, a default pool is created automatically at "projects/{project}/locations/{location}/pools/default".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
