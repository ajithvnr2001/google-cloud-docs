---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client
title: Class Client (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:39.565128+00:00
---

# Class Client (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Client (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.2  2.38.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.3  2.26.1  2.25.2  2.23.1  2.22.0  2.21.5  2.20.3  2.19.8  2.18.4  2.17.1  2.16.1  2.15.2  2.14.1  2.13.12  2.12.1  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.1  2.5.0  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.7.2  1.6.1  1.5.0  1.4.3  1.3.1  1.2.0  1.1.0  1.0.2  0.45.0  0.44.0  0.43.0 
    
    
    Client(
        batch_settings: typing.Union[
            google.cloud.pubsub_v1.types.BatchSettings, typing.Sequence
        ] = (),
        publisher_options: typing.Union[
            google.cloud.pubsub_v1.types.PublisherOptions, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    )

A publisher client for Google Cloud Pub/Sub.

This creates an object that is capable of publishing messages. Generally, you can instantiate this client with no arguments, and you get sensible defaults.

## Parameters  
  
---  
**Name** | **Description**  
`batch_settings` |  `typing.Union[[google.cloud.pubsub_v1.types.BatchSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.BatchSettings), typing.Sequence]`   
The settings for batch publishing.  
`publisher_options` |  `typing.Union[[google.cloud.pubsub_v1.types.PublisherOptions](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions), typing.Sequence]`   
The options for the publisher client. Note that enabling message ordering will override the publish retry timeout to be infinite.  
  
## Properties 

### api

The underlying gapic API client.

.. versionchanged:: 2.10.0 Instead of a GAPIC `PublisherClient` client instance, this property is a proxy object to it with the same interface.

**deprecated:** Use the GAPIC methods and properties on the client instance directly instead of through the `api` attribute. 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### target

Return the target (where the API is).

### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`PublisherTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### Client
    
    
    Client(
        batch_settings: typing.Union[
            google.cloud.pubsub_v1.types.BatchSettings, typing.Sequence
        ] = (),
        publisher_options: typing.Union[
            google.cloud.pubsub_v1.types.PublisherOptions, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    )

Instantiates the publisher client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,PublisherTransport,Callable[..., PublisherTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the PublisherTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_topic
    
    
    create_topic(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.Topic, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Topic

Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names).
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_create_topic():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.Topic(
            name="name_value",
        )
    
        # Make the request
        response = client.create_topic(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.Topic, dict]`   
The request object. A topic resource.  
`name` |  `str`   
Required. Identifier. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (


), plus (`<code>+</code><code>) or percent signs (</code><code>%</code><code>). It must be between 3 and 255 characters in length, and it must not start with </code>"goog"<code>. This corresponds to the </code>name<code> field on the </code>request<code> instance; if </code>request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Topic` | A topic resource.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### delete_topic
    
    
    delete_topic(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.DeleteTopicRequest, dict]
        ] = None,
        *,
        topic: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_delete_topic():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.DeleteTopicRequest(
            topic="topic_value",
        )
    
        # Make the request
        client.delete_topic(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.DeleteTopicRequest, dict]`   
The request object. Request for the `DeleteTopic` method.  
`topic` |  `str`   
Required. Name of the topic to delete. Format is `projects/{project}/topics/{topic}`. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### detach_subscription
    
    
    detach_subscription(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.DetachSubscriptionRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.DetachSubscriptionResponse

Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_detach_subscription():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.DetachSubscriptionRequest(
            subscription="subscription_value",
        )
    
        # Make the request
        response = client.detach_subscription(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.DetachSubscriptionRequest, dict]`   
The request object. Request for the DetachSubscription method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.DetachSubscriptionResponse` | Response for the DetachSubscription method. Reserved for future use.  
  
### ensure_cleanup_and_commit_timer_runs
    
    
    ensure_cleanup_and_commit_timer_runs() -> None

Ensure a cleanup/commit timer thread is running.

If a cleanup/commit timer thread is already running, this does nothing.

### from_service_account_file
    
    
    from_service_account_file(
        filename: str,
        batch_settings: typing.Union[
            google.cloud.pubsub_v1.types.BatchSettings, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    ) -> google.cloud.pubsub_v1.publisher.client.Client

Creates an instance of this client using the provided credentials file.

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
`PublisherClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(
        filename: str,
        batch_settings: typing.Union[
            google.cloud.pubsub_v1.types.BatchSettings, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    ) -> google.cloud.pubsub_v1.publisher.client.Client

Creates an instance of this client using the provided credentials file.

### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
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
  
### get_topic
    
    
    get_topic(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.GetTopicRequest, dict]
        ] = None,
        *,
        topic: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Topic

Gets the configuration of a topic.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_get_topic():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.GetTopicRequest(
            topic="topic_value",
        )
    
        # Make the request
        response = client.get_topic(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.GetTopicRequest, dict]`   
The request object. Request for the GetTopic method.  
`topic` |  `str`   
Required. The name of the topic to get. Format is `projects/{project}/topics/{topic}`. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Topic` | A topic resource.  
  
### list_topic_snapshots
    
    
    list_topic_snapshots(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ListTopicSnapshotsRequest, dict]
        ] = None,
        *,
        topic: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.pubsub_v1.services.publisher.pagers.ListTopicSnapshotsPager

Lists the names of the snapshots on this topic. Snapshots are used in `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__ operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_list_topic_snapshots():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ListTopicSnapshotsRequest(
            topic="topic_value",
        )
    
        # Make the request
        page_result = client.list_topic_snapshots(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ListTopicSnapshotsRequest, dict]`   
The request object. Request for the `ListTopicSnapshots` method.  
`topic` |  `str`   
Required. The name of the topic that snapshots are attached to. Format is `projects/{project}/topics/{topic}`. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.pubsub_v1.services.publisher.pagers.ListTopicSnapshotsPager](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.pubsub_v1.services.publisher.pagers.ListTopicSnapshotsPager)` | Response for the ListTopicSnapshots method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_topic_subscriptions
    
    
    list_topic_subscriptions(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ListTopicSubscriptionsRequest, dict]
        ] = None,
        *,
        topic: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.pubsub_v1.services.publisher.pagers.ListTopicSubscriptionsPager

Lists the names of the attached subscriptions on this topic.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_list_topic_subscriptions():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ListTopicSubscriptionsRequest(
            topic="topic_value",
        )
    
        # Make the request
        page_result = client.list_topic_subscriptions(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ListTopicSubscriptionsRequest, dict]`   
The request object. Request for the `ListTopicSubscriptions` method.  
`topic` |  `str`   
Required. The name of the topic that subscriptions are attached to. Format is `projects/{project}/topics/{topic}`. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.pubsub_v1.services.publisher.pagers.ListTopicSubscriptionsPager](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.pubsub_v1.services.publisher.pagers.ListTopicSubscriptionsPager)` | Response for the ListTopicSubscriptions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_topics
    
    
    list_topics(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ListTopicsRequest, dict]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.pubsub_v1.services.publisher.pagers.ListTopicsPager

Lists matching topics.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_list_topics():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ListTopicsRequest(
            project="project_value",
        )
    
        # Make the request
        page_result = client.list_topics(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ListTopicsRequest, dict]`   
The request object. Request for the `ListTopics` method.  
`project` |  `str`   
Required. The name of the project in which to list topics. Format is `projects/{project-id}`. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.pubsub_v1.services.publisher.pagers.ListTopicsPager](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.pubsub_v1.services.publisher.pagers.ListTopicsPager)` | Response for the ListTopics method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_schema_path
    
    
    parse_schema_path(path: str) -> typing.Dict[str, str]

Parses a schema path into its component segments.

### parse_snapshot_path
    
    
    parse_snapshot_path(path: str) -> typing.Dict[str, str]

Parses a snapshot path into its component segments.

### parse_subscription_path
    
    
    parse_subscription_path(path: str) -> typing.Dict[str, str]

Parses a subscription path into its component segments.

### parse_topic_path
    
    
    parse_topic_path(path: str) -> typing.Dict[str, str]

Parses a topic path into its component segments.

### publish
    
    
    publish(
        topic: str,
        data: bytes,
        ordering_key: str = "",
        retry: OptionalRetry = _MethodDefault._DEFAULT_VALUE,
        timeout: types.OptionalTimeout = _MethodDefault._DEFAULT_VALUE,
        **attrs: typing.Union[bytes, str]
    ) -> pubsub_v1.publisher.futures.Future

Publish a single message.

**Note:** Messages in Pub/Sub are blobs of bytes. They are _binary_ data, not text. You must send data as a bytestring (`bytes` in Python 3; `str` in Python 2), and this library will raise an exception if you send a text string.  The reason that this is so important (and why we do not try to coerce for you) is because Pub/Sub is also platform independent and there is no way to know how to decode messages properly on the other side; therefore, encoding and decoding is a required exercise for the developer.

Add the given message to this object; this will cause it to be published once the batch either has enough messages or a sufficient period of time has elapsed. This method may block if LimitExceededBehavior.BLOCK is used in the flow control settings.

.. rubric:: Example

> > > from google.cloud import pubsub_v1 client = pubsub_v1.PublisherClient() topic = client.topic_path('[PROJECT]', '[TOPIC]') data = b'The rain in Wales falls mainly on the snails.' response = client.publish(topic, data, username='guido')

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If called after publisher has been stopped by a `stop()` method call.  
`pubsub_v1.publisher.exceptions.MessageTooLargeError` | If publishing the `message` would exceed the max size limit on the backend.  
  
### resume_publish
    
    
    resume_publish(topic: str, ordering_key: str) -> None

Resume publish on an ordering key that has had unrecoverable errors.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If called after publisher has been stopped by a `stop()` method call.  
`ValueError` | If the topic/ordering key combination has not been seen before by this client.  
  
### schema_path
    
    
    schema_path(project: str, schema: str) -> str

Returns a fully-qualified schema string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### snapshot_path
    
    
    snapshot_path(project: str, snapshot: str) -> str

Returns a fully-qualified snapshot string.

### stop
    
    
    stop() -> None

Immediately publish all outstanding messages.

Asynchronously sends all outstanding messages and prevents future calls to `publish()`. Method should be invoked prior to deleting this `Client()` object in order to ensure that no pending messages are lost.

**Note:** This method is non-blocking. Use `Future()` objects returned by `publish()` to make sure all publish requests completed, either in success or error. 

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If called after publisher has been stopped by a `stop()` method call.  
  
### subscription_path
    
    
    subscription_path(project: str, subscription: str) -> str

Returns a fully-qualified subscription string.

### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### topic_path
    
    
    topic_path(project: str, topic: str) -> str

Returns a fully-qualified topic string.

### update_topic
    
    
    update_topic(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.UpdateTopicRequest, dict]
        ] = None,
        *,
        topic: typing.Optional[google.cloud.pubsub_v1.types.Topic] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[
            int,
            float,
            google.api_core.timeout.ConstantTimeout,
            google.api_core.timeout.ExponentialTimeout,
        ] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Topic

Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_update_topic():
        # Create a client
        client = pubsub_v1.PublisherClient()
    
        # Initialize request argument(s)
        topic = pubsub_v1.Topic()
        topic.name = "name_value"
    
        request = pubsub_v1.UpdateTopicRequest(
            topic=topic,
        )
    
        # Make the request
        response = client.update_topic(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.UpdateTopicRequest, dict]`   
The request object. Request for the UpdateTopic method.  
`topic` |  `google.pubsub_v1.types.Topic`   
Required. The updated topic object. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Indicates which fields in the provided topic to update. Must be specified and non-empty. Note that if `update_mask` contains "message_storage_policy" but the `message_storage_policy` is not set in the `topic` provided above, then the updated value is determined by the policy configured at the project or organization level. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `TimeoutType`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Topic` | A topic resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
