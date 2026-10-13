---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client
title: Class Client (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:48.847082+00:00
---

# Class Client (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client

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
        subscriber_options: typing.Union[
            google.cloud.pubsub_v1.types.SubscriberOptions, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    )

A subscriber client for Google Cloud Pub/Sub.

This creates an object that is capable of subscribing to messages. Generally, you can instantiate this client with no arguments, and you get sensible defaults.

## Properties 

### api

The underlying gapic API client.

.. versionchanged:: 2.10.0 Instead of a GAPIC `SubscriberClient` client instance, this property is a proxy object to it with the same interface.

**deprecated:** Use the GAPIC methods and properties on the client instance directly instead of through the `api` attribute. 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### closed

Return whether the client has been closed and cannot be used anymore.

.. versionadded:: 2.8.0

### open_telemetry_enabled

Returns True if Open Telemetry is enabled. False otherwise.

### target

Return the target (where the API is).

### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`SubscriberTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### Client
    
    
    Client(
        subscriber_options: typing.Union[
            google.cloud.pubsub_v1.types.SubscriberOptions, typing.Sequence
        ] = (),
        **kwargs: typing.Any
    )

Instantiates the subscriber client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SubscriberTransport,Callable[..., SubscriberTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the SubscriberTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### acknowledge
    
    
    acknowledge(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.AcknowledgeRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        ack_ids: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Acknowledges the messages associated with the `ack_ids` in the `AcknowledgeRequest`. The Pub/Sub system can remove the relevant messages from the subscription.

Acknowledging a message whose ack deadline has expired may succeed, but such a message may be redelivered later. Acknowledging a message more than once will not result in an error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_acknowledge():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.AcknowledgeRequest(
            subscription="subscription_value",
            ack_ids=['ack_ids_value1', 'ack_ids_value2'],
        )
    
        # Make the request
        client.acknowledge(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.AcknowledgeRequest, dict]`   
The request object. Request for the Acknowledge method.  
`subscription` |  `str`   
Required. The subscription whose message is being acknowledged. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`ack_ids` |  `MutableSequence[str]`   
Required. The acknowledgment ID for the messages being acknowledged that was returned by the Pub/Sub system in the `Pull` response. Must not be empty. This corresponds to the `ack_ids` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### close
    
    
    close() -> None

Close the underlying channel to release socket resources.

After a channel has been closed, the client instance cannot be used anymore.

This method is idempotent.

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

### create_snapshot
    
    
    create_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.CreateSnapshotRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        subscription: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Snapshot

Creates a snapshot from the requested subscription. Snapshots are used in `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__ operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. If the snapshot already exists, returns `ALREADY_EXISTS`. If the requested subscription doesn't exist, returns `NOT_FOUND`. If the backlog in the subscription is too old -- and the resulting snapshot would expire in less than 1 hour -- then `FAILED_PRECONDITION` is returned. See also the `Snapshot.expire_time` field. If the name is not provided in the request, the server will assign a random name for this snapshot on the same project as the subscription, conforming to the [resource name format](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). The generated name is populated in the returned Snapshot object. Note that for REST API requests, you must specify a name in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_create_snapshot():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.CreateSnapshotRequest(
            name="name_value",
            subscription="subscription_value",
        )
    
        # Make the request
        response = client.create_snapshot(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.CreateSnapshotRequest, dict]`   
The request object. Request for the `CreateSnapshot` method.  
`name` |  `str`   
Required. User-provided name for this snapshot. If the name is not provided in the request, the server will assign a random name for this snapshot on the same project as the subscription. Note that for REST API requests, you must specify a name. See the `resource name rules <https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names>`__. Format is `projects/{project}/snapshots/{snap}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`subscription` |  `str`   
Required. The subscription whose backlog the snapshot retains. Specifically, the created snapshot is guaranteed to retain: (a) The existing backlog on the subscription. More precisely, this is defined as the messages in the subscription's backlog that are unacknowledged upon the successful completion of the `CreateSnapshot` request; as well as: (b) Any messages published to the subscription's topic following the successful completion of the CreateSnapshot request. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Snapshot` | A snapshot resource. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.  
  
### create_subscription
    
    
    create_subscription(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.Subscription, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        push_config: typing.Optional[google.cloud.pubsub_v1.types.PushConfig] = None,
        ack_deadline_seconds: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Subscription

Creates a subscription to a given topic. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). If the subscription already exists, returns `ALREADY_EXISTS`. If the corresponding topic doesn't exist, returns `NOT_FOUND`.

If the name is not provided in the request, the server will assign a random name for this subscription on the same project as the topic, conforming to the [resource name format](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). The generated name is populated in the returned Subscription object. Note that for REST API requests, you must specify a name in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_create_subscription():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.Subscription(
            name="name_value",
            topic="topic_value",
        )
    
        # Make the request
        response = client.create_subscription(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.Subscription, dict]`   
The request object. A subscription resource. If none of `push_config`, `bigquery_config`, `cloud_storage_config`, or `bigtable_config` is set, then the subscriber will pull and ack messages using API methods. At most one of these fields may be set.  
`name` |  `str`   
Required. Identifier. The name of the subscription. It must have the format `"projects/{project}/subscriptions/{subscription}"`. `{subscription}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (


), plus (`<code>+</code><code>) or percent signs (</code><code>%</code><code>). It must be between 3 and 255 characters in length, and it must not start with </code>"goog"<code>. This corresponds to the </code>name<code> field on the </code>request<code> instance; if </code>request` is provided, this should not be set.  
`topic` |  `str`   
Required. The name of the topic from which this subscription is receiving messages. Format is `projects/{project}/topics/{topic}`. The value of this field will be `_deleted-topic_` if the topic has been deleted. This corresponds to the `topic` field on the `request` instance; if `request` is provided, this should not be set.  
`push_config` |  `google.pubsub_v1.types.PushConfig`   
Optional. If push delivery is used with this subscription, this field is used to configure it. This corresponds to the `push_config` field on the `request` instance; if `request` is provided, this should not be set.  
`ack_deadline_seconds` |  `int`   
Optional. The approximate amount of time (on a best-effort basis) Pub/Sub waits for the subscriber to acknowledge receipt before resending the message. In the interval after the message is delivered and before it is acknowledged, it is considered to be _outstanding_. During that time period, the message will not be redelivered (on a best-effort basis). For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call `ModifyAckDeadline` with the corresponding `ack_id` if using non-streaming pull or send the `ack_id` in a `StreamingModifyAckDeadlineRequest` if using streaming pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message. This corresponds to the `ack_deadline_seconds` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Subscription` | A subscription resource. If none of push_config, bigquery_config, cloud_storage_config, or bigtable_config is set, then the subscriber will pull and ack messages using API methods. At most one of these fields may be set.  
  
### delete_snapshot
    
    
    delete_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.DeleteSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Removes an existing snapshot. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. When the snapshot is deleted, all messages retained in the snapshot are immediately dropped. After a snapshot is deleted, a new one may be created with the same name, but the new one has no association with the old snapshot or its subscription, unless the same subscription is specified.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_delete_snapshot():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.DeleteSnapshotRequest(
            snapshot="snapshot_value",
        )
    
        # Make the request
        client.delete_snapshot(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.DeleteSnapshotRequest, dict]`   
The request object. Request for the `DeleteSnapshot` method.  
`snapshot` |  `str`   
Required. The name of the snapshot to delete. Format is `projects/{project}/snapshots/{snap}`. This corresponds to the `snapshot` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_subscription
    
    
    delete_subscription(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.DeleteSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes an existing subscription. All messages retained in the subscription are immediately dropped. Calls to `Pull` after deletion will return `NOT_FOUND`. After a subscription is deleted, a new one may be created with the same name, but the new one has no association with the old subscription or its topic unless the same topic is specified.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_delete_subscription():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.DeleteSubscriptionRequest(
            subscription="subscription_value",
        )
    
        # Make the request
        client.delete_subscription(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.DeleteSubscriptionRequest, dict]`   
The request object. Request for the DeleteSubscription method.  
`subscription` |  `str`   
Required. The subscription to delete. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### from_service_account_file
    
    
    from_service_account_file(
        filename: str, **kwargs: typing.Any
    ) -> google.cloud.pubsub_v1.subscriber.client.Client

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
`SubscriberClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(
        filename: str, **kwargs: typing.Any
    ) -> google.cloud.pubsub_v1.subscriber.client.Client

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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
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
  
### get_snapshot
    
    
    get_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.GetSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Snapshot

Gets the configuration details of a snapshot. Snapshots are used in `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__ operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_get_snapshot():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.GetSnapshotRequest(
            snapshot="snapshot_value",
        )
    
        # Make the request
        response = client.get_snapshot(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.GetSnapshotRequest, dict]`   
The request object. Request for the GetSnapshot method.  
`snapshot` |  `str`   
Required. The name of the snapshot to get. Format is `projects/{project}/snapshots/{snap}`. This corresponds to the `snapshot` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Snapshot` | A snapshot resource. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.  
  
### get_subscription
    
    
    get_subscription(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.GetSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Subscription

Gets the configuration details of a subscription.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_get_subscription():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.GetSubscriptionRequest(
            subscription="subscription_value",
        )
    
        # Make the request
        response = client.get_subscription(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.GetSubscriptionRequest, dict]`   
The request object. Request for the GetSubscription method.  
`subscription` |  `str`   
Required. The name of the subscription to get. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Subscription` | A subscription resource. If none of push_config, bigquery_config, cloud_storage_config, or bigtable_config is set, then the subscriber will pull and ack messages using API methods. At most one of these fields may be set.  
  
### list_snapshots
    
    
    list_snapshots(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ListSnapshotsRequest, dict]
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
    ) -> google.pubsub_v1.services.subscriber.pagers.ListSnapshotsPager

Lists the existing snapshots. Snapshots are used in `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__ operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_list_snapshots():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ListSnapshotsRequest(
            project="project_value",
        )
    
        # Make the request
        page_result = client.list_snapshots(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ListSnapshotsRequest, dict]`   
The request object. Request for the `ListSnapshots` method.  
`project` |  `str`   
Required. The name of the project in which to list snapshots. Format is `projects/{project-id}`. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.pubsub_v1.services.subscriber.pagers.ListSnapshotsPager](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.pubsub_v1.services.subscriber.pagers.ListSnapshotsPager)` | Response for the ListSnapshots method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_subscriptions
    
    
    list_subscriptions(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ListSubscriptionsRequest, dict]
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
    ) -> google.pubsub_v1.services.subscriber.pagers.ListSubscriptionsPager

Lists matching subscriptions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_list_subscriptions():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ListSubscriptionsRequest(
            project="project_value",
        )
    
        # Make the request
        page_result = client.list_subscriptions(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ListSubscriptionsRequest, dict]`   
The request object. Request for the `ListSubscriptions` method.  
`project` |  `str`   
Required. The name of the project in which to list subscriptions. Format is `projects/{project-id}`. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.pubsub_v1.services.subscriber.pagers.ListSubscriptionsPager](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.pubsub_v1.services.subscriber.pagers.ListSubscriptionsPager)` | Response for the ListSubscriptions method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### listing_path
    
    
    listing_path(project: str, location: str, data_exchange: str, listing: str) -> str

Returns a fully-qualified listing string.

### modify_ack_deadline
    
    
    modify_ack_deadline(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ModifyAckDeadlineRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        ack_ids: typing.Optional[typing.MutableSequence[str]] = None,
        ack_deadline_seconds: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Modifies the ack deadline for a specific message. This method is useful to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. Note that this does not modify the subscription-level `ackDeadlineSeconds` used for subsequent messages.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_modify_ack_deadline():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ModifyAckDeadlineRequest(
            subscription="subscription_value",
            ack_ids=['ack_ids_value1', 'ack_ids_value2'],
            ack_deadline_seconds=2066,
        )
    
        # Make the request
        client.modify_ack_deadline(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ModifyAckDeadlineRequest, dict]`   
The request object. Request for the ModifyAckDeadline method.  
`subscription` |  `str`   
Required. The name of the subscription. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`ack_ids` |  `MutableSequence[str]`   
Required. List of acknowledgment IDs. This corresponds to the `ack_ids` field on the `request` instance; if `request` is provided, this should not be set.  
`ack_deadline_seconds` |  `int`   
Required. The new ack deadline with respect to the time this request was sent to the Pub/Sub system. For example, if the value is 10, the new ack deadline will expire 10 seconds after the `ModifyAckDeadline` call was made. Specifying zero might immediately make the message available for delivery to another subscriber client. This typically results in an increase in the rate of message redeliveries (that is, duplicates). The minimum deadline you can specify is 0 seconds. The maximum deadline you can specify in a single request is 600 seconds (10 minutes). This corresponds to the `ack_deadline_seconds` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### modify_push_config
    
    
    modify_push_config(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.ModifyPushConfigRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        push_config: typing.Optional[google.cloud.pubsub_v1.types.PushConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Modifies the `PushConfig` for a specified subscription.

This may be used to change a push subscription to a pull one (signified by an empty `PushConfig`) or vice versa, or change the endpoint URL and other attributes of a push subscription. Messages will accumulate for delivery continuously through the call regardless of changes to the `PushConfig`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_modify_push_config():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.ModifyPushConfigRequest(
            subscription="subscription_value",
        )
    
        # Make the request
        client.modify_push_config(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.ModifyPushConfigRequest, dict]`   
The request object. Request for the ModifyPushConfig method.  
`subscription` |  `str`   
Required. The name of the subscription. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`push_config` |  `google.pubsub_v1.types.PushConfig`   
Required. The push configuration for future deliveries. An empty `pushConfig` indicates that the Pub/Sub system should stop pushing messages from the given subscription and allow messages to be pulled and acknowledged - effectively pausing the subscription if `Pull` or `StreamingPull` is not called. This corresponds to the `push_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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

### parse_listing_path
    
    
    parse_listing_path(path: str) -> typing.Dict[str, str]

Parses a listing path into its component segments.

### parse_snapshot_path
    
    
    parse_snapshot_path(path: str) -> typing.Dict[str, str]

Parses a snapshot path into its component segments.

### parse_subscription_path
    
    
    parse_subscription_path(path: str) -> typing.Dict[str, str]

Parses a subscription path into its component segments.

### parse_topic_path
    
    
    parse_topic_path(path: str) -> typing.Dict[str, str]

Parses a topic path into its component segments.

### pull
    
    
    pull(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.PullRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[str] = None,
        return_immediately: typing.Optional[bool] = None,
        max_messages: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.PullResponse

Pulls messages from the server.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_pull():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.PullRequest(
            subscription="subscription_value",
            max_messages=1277,
        )
    
        # Make the request
        response = client.pull(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.PullRequest, dict]`   
The request object. Request for the `Pull` method.  
`subscription` |  `str`   
Required. The subscription from which messages should be pulled. Format is `projects/{project}/subscriptions/{sub}`. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`return_immediately` |  `bool`   
Optional. If this field set to true, the system will respond immediately even if it there are no messages available to return in the `Pull` response. Otherwise, the system may wait (for a bounded amount of time) until at least one message is available, rather than returning no messages. Warning: setting this field to `true` is discouraged because it adversely impacts the performance of `Pull` operations. We recommend that users do not set this field. This corresponds to the `return_immediately` field on the `request` instance; if `request` is provided, this should not be set.  
`max_messages` |  `int`   
Required. The maximum number of messages to return for this request. Must be a positive integer. The Pub/Sub system may return fewer than the number specified. This corresponds to the `max_messages` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.PullResponse` | Response for the Pull method.  
  
### seek
    
    
    seek(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.SeekRequest, dict]
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
    ) -> google.cloud.pubsub_v1.types.SeekResponse

Seeks an existing subscription to a point in time or to a given snapshot, whichever is provided in the request. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. Note that both the subscription and the snapshot must be on the same topic.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_seek():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.SeekRequest(
            subscription="subscription_value",
        )
    
        # Make the request
        response = client.seek(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.SeekRequest, dict]`   
The request object. Request for the `Seek` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.SeekResponse` | Response for the Seek method (this response is empty).  
  
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
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

### streaming_pull
    
    
    streaming_pull(
        requests: typing.Optional[
            typing.Iterator[google.cloud.pubsub_v1.types.StreamingPullRequest]
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
    ) -> typing.Iterable[google.cloud.pubsub_v1.types.StreamingPullResponse]

Establishes a stream with the server, which sends messages down to the client. The client streams acknowledgments and ack deadline modifications back to the server. The server will close the stream and return the status on any error. The server may close the stream with status `UNAVAILABLE` to reassign server-side resources, in which case, the client should re-establish the stream. Flow control can be achieved by configuring the underlying RPC channel.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_streaming_pull():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.StreamingPullRequest(
            subscription="subscription_value",
            stream_ack_deadline_seconds=2813,
        )
    
        # This method expects an iterator which contains
        # 'pubsub_v1.StreamingPullRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = client.streaming_pull(requests=request_generator())
    
        # Handle the response
        for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`requests` |  `Iterator[google.pubsub_v1.types.StreamingPullRequest]`   
The request object iterator. Request for the `StreamingPull` streaming RPC method. This request is used to establish the initial stream as well as to stream acknowledgments and ack deadline modifications from the client to the server.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[google.pubsub_v1.types.StreamingPullResponse]` | Response for the StreamingPull method. This response is used to stream messages from the server to the client.  
  
### subscribe
    
    
    subscribe(
        subscription: str,
        callback: typing.Callable[[subscriber.message.Message], typing.Any],
        flow_control: typing.Union[
            google.cloud.pubsub_v1.types.FlowControl, typing.Sequence
        ] = (),
        scheduler: typing.Optional[subscriber.scheduler.ThreadScheduler] = None,
        use_legacy_flow_control: bool = False,
        await_callbacks_on_shutdown: bool = False,
    ) -> google.cloud.pubsub_v1.subscriber.futures.StreamingPullFuture

Asynchronously start receiving messages on a given subscription.

This method starts a background thread to begin pulling messages from a Pub/Sub subscription and scheduling them to be processed using the provided `callback`.

The `callback` will be called with an individual xref_Message. It is the responsibility of the callback to either call `ack()` or `nack()` on the message when it finished processing. If an exception occurs in the callback during processing, the exception is logged and the message is `nack()` ed.

The `flow_control` argument can be used to control the rate of at which messages are pulled. The settings are relatively conservative by default to prevent "message hoarding" - a situation where the client pulls a large number of messages but can not process them fast enough leading it to "starve" other clients of messages. Increasing these settings may lead to faster throughput for messages that do not take a long time to process.

The `use_legacy_flow_control` argument disables enforcing flow control settings at the Cloud Pub/Sub server, and only the client side flow control will be enforced.

This method starts the receiver in the background and returns a _Future_ representing its execution. Waiting on the future (calling `result()`) will block forever or until a non-recoverable error is encountered (such as loss of network connectivity). Cancelling the future will signal the process to shutdown gracefully and exit.

**Note:** properties that may be surprising. Please take a look at <https://cloud.google.com/pubsub/docs/pull#streamingpull> for more details on how streaming pull behaves compared to the synchronous pull method.  Example:
    
    
    from google.cloud import pubsub_v1
    
    subscriber_client = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    
    # existing subscription
    subscription = [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.html).subscription_path(
        'my-project-id', 'my-subscription')
    
    def callback(message):
        print(message)
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r_client.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(
        subscription, callback)
    
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()  # Trigger the shutdown.
        future.result()  # Block until the shutdown is complete.
    

**Parameter**  
---  
**Name** | **Description**  
`use_legacy_flow_control` |  `bool`   
If set to `True`, flow control at the Cloud Pub/Sub server is disabled, though client-side flow control is still enabled. If set to `False` (default), both server-side and client-side flow control are enabled.  
  
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
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

### update_snapshot
    
    
    update_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.UpdateSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[google.cloud.pubsub_v1.types.Snapshot] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Snapshot

Updates an existing snapshot by updating the fields specified in the update mask. Snapshots are used in `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__ operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_update_snapshot():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        request = pubsub_v1.UpdateSnapshotRequest(
        )
    
        # Make the request
        response = client.update_snapshot(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.UpdateSnapshotRequest, dict]`   
The request object. Request for the UpdateSnapshot method.  
`snapshot` |  `google.pubsub_v1.types.Snapshot`   
Required. The updated snapshot object. This corresponds to the `snapshot` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Indicates which fields in the provided snapshot to update. Must be specified and non-empty. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Snapshot` | A snapshot resource. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.  
  
### update_subscription
    
    
    update_subscription(
        request: typing.Optional[
            typing.Union[google.cloud.pubsub_v1.types.UpdateSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: typing.Optional[google.cloud.pubsub_v1.types.Subscription] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.pubsub_v1.types.Subscription

Updates an existing subscription by updating the fields specified in the update mask. Note that certain properties of a subscription, such as its topic, are not modifiable.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google import pubsub_v1
    
    def sample_update_subscription():
        # Create a client
        client = pubsub_v1.SubscriberClient()
    
        # Initialize request argument(s)
        subscription = pubsub_v1.Subscription()
        subscription.name = "name_value"
        subscription.topic = "topic_value"
    
        request = pubsub_v1.UpdateSubscriptionRequest(
            subscription=subscription,
        )
    
        # Make the request
        response = client.update_subscription(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.pubsub_v1.types.UpdateSubscriptionRequest, dict]`   
The request object. Request for the UpdateSubscription method.  
`subscription` |  `google.pubsub_v1.types.Subscription`   
Required. The updated subscription object. This corresponds to the `subscription` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Indicates which fields in the provided subscription to update. Must be specified and non-empty. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.pubsub_v1.types.Subscription` | A subscription resource. If none of push_config, bigquery_config, cloud_storage_config, or bigtable_config is set, then the subscriber will pull and ack messages using API methods. At most one of these fields may be set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
