---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient
title: Class TopicAdminClient (1.157.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:25.541548+00:00
---

# Class TopicAdminClient (1.157.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TopicAdminClient (1.157.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.157.0 (latest)  1.153.0  1.152.0  1.151.0  1.150.1  1.149.0  1.148.0  1.147.0  1.145.0  1.143.1  1.142.0  1.141.5  1.140.2  1.139.4  1.138.0  1.137.1  1.136.1  1.135.0  1.134.2  1.133.1  1.132.2  1.131.0  1.130.0  1.129.6  1.127.3  1.126.6  1.125.13  1.123.18  1.122.2  1.121.1  1.120.24  1.119.1  1.118.0  1.117.0  1.116.4  1.115.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-pubsub/google-cloud-pubsub/src/main/java/com/google/cloud/pubsub/v1/TopicAdminClient.java)| [Product Reference](https://cloud.google.com/pubsub/docs/)  
---|---  
  
Service Description: The service that an application uses to manipulate topics, and to send messages to a topic.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName name = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       Topic response = topicAdminClient.createTopic(name);
     }
     

Note: close() needs to be called on the TopicAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateTopic |  Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTopic(Topic request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTopic(TopicName name) 
  * createTopic(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTopicCallable() 

  
UpdateTopic |  Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTopic(UpdateTopicRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTopic(Topic topic, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTopicCallable() 

  
Publish |  Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * publish(PublishRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * publish(TopicName topic, List<PubsubMessage> messages) 
  * publish(String topic, List<PubsubMessage> messages) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * publishCallable() 

  
GetTopic |  Gets the configuration of a topic. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTopic(GetTopicRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTopic(TopicName topic) 
  * getTopic(String topic) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTopicCallable() 

  
ListTopics |  Lists matching topics. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTopics(ListTopicsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTopics(ProjectName project) 
  * listTopics(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTopicsPagedCallable() 
  * listTopicsCallable() 

  
ListTopicSubscriptions |  Lists the names of the attached subscriptions on this topic. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTopicSubscriptions(ListTopicSubscriptionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTopicSubscriptions(TopicName topic) 
  * listTopicSubscriptions(String topic) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTopicSubscriptionsPagedCallable() 
  * listTopicSubscriptionsCallable() 

  
ListTopicSnapshots |  Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTopicSnapshots(ListTopicSnapshotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTopicSnapshots(TopicName topic) 
  * listTopicSnapshots(String topic) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTopicSnapshotsPagedCallable() 
  * listTopicSnapshotsCallable() 

  
DeleteTopic |  Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTopic(DeleteTopicRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTopic(TopicName topic) 
  * deleteTopic(String topic) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTopicCallable() 

  
DetachSubscription |  Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detachSubscription(DetachSubscriptionRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detachSubscriptionCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TopicAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TopicAdminSettings topicAdminSettings =
         TopicAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TopicAdminClient topicAdminClient = TopicAdminClient.create(topicAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TopicAdminSettings topicAdminSettings =
         TopicAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     TopicAdminClient topicAdminClient = TopicAdminClient.create(topicAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TopicAdminSettings topicAdminSettings = TopicAdminSettings.newHttpJsonBuilder().build();
     TopicAdminClient topicAdminClient = TopicAdminClient.create(topicAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TopicAdminClient

## Static Methods 

### create()
    
    
    public static final TopicAdminClient create()

Constructs an instance of TopicAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TopicAdminSettings settings)
    
    
    public static final TopicAdminClient create(TopicAdminSettings settings)

Constructs an instance of TopicAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TopicAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PublisherStub stub)
    
    
    public static final TopicAdminClient create(PublisherStub stub)

Constructs an instance of TopicAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(TopicAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublisherStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.stub.PublisherStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient)` |   
  
## Constructors 

### TopicAdminClient(TopicAdminSettings settings)
    
    
    protected TopicAdminClient(TopicAdminSettings settings)

Constructs an instance of TopicAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TopicAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminSettings)`  
  
  
### TopicAdminClient(PublisherStub stub)
    
    
    protected TopicAdminClient(PublisherStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublisherStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.stub.PublisherStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createTopic(@Nullable TopicName name)
    
    
    public final Topic createTopic(@Nullable TopicName name)

Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName name = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       Topic response = topicAdminClient.createTopic(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. Identifier. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### createTopic(ProjectTopicName name) (deprecated)
    
    
    public final Topic createTopic(ProjectTopicName name)

**Deprecated.** _Use[#createTopic(TopicName)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_createTopic_) instead._

Creates the given topic with the given name. See the <a href="[https://cloud.google.com/pubsub/docs/admin#resource_names">](https://cloud.google.com/pubsub/docs/admin#resource_names"&gt); resource name rules</a>.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ProjectTopicName name = ProjectTopicName.of("[PROJECT]", "[TOPIC]");
       Topic response = topicAdminClient.createTopic(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName)`  
Required. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### createTopic(Topic request)
    
    
    public final Topic createTopic(Topic request)

Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       Topic request =
           Topic.newBuilder()
               .setName(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .putAllLabels(new HashMap<String, String>())
               .setMessageStoragePolicy(MessageStoragePolicy.newBuilder().build())
               .setKmsKeyName(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setSchemaSettings(SchemaSettings.newBuilder().build())
               .setSatisfiesPzs(true)
               .setMessageRetentionDuration(Duration.newBuilder().build())
               .setIngestionDataSourceSettings(IngestionDataSourceSettings.newBuilder().build())
               .addAllMessageTransforms(new ArrayList<MessageTransform>())
               .putAllTags(new HashMap<String, String>())
               .build();
       Topic response = topicAdminClient.createTopic(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### createTopic(String name)
    
    
    public final Topic createTopic(String name)

Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String name = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       Topic response = topicAdminClient.createTopic(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Identifier. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### createTopicCallable()
    
    
    public final UnaryCallable<Topic,Topic> createTopicCallable()

Creates the given topic with the given name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       Topic request =
           Topic.newBuilder()
               .setName(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .putAllLabels(new HashMap<String, String>())
               .setMessageStoragePolicy(MessageStoragePolicy.newBuilder().build())
               .setKmsKeyName(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setSchemaSettings(SchemaSettings.newBuilder().build())
               .setSatisfiesPzs(true)
               .setMessageRetentionDuration(Duration.newBuilder().build())
               .setIngestionDataSourceSettings(IngestionDataSourceSettings.newBuilder().build())
               .addAllMessageTransforms(new ArrayList<MessageTransform>())
               .putAllTags(new HashMap<String, String>())
               .build();
       ApiFuture<Topic> future = topicAdminClient.createTopicCallable().futureCall(request);
       // Do something.
       Topic response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)>` |   
  
### deleteTopic(@Nullable TopicName topic)
    
    
    public final void deleteTopic(@Nullable TopicName topic)

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       topicAdminClient.deleteTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. Name of the topic to delete. Format is `projects/{project}/topics/{topic}`.  
  
### deleteTopic(DeleteTopicRequest request)
    
    
    public final void deleteTopic(DeleteTopicRequest request)

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       DeleteTopicRequest request =
           DeleteTopicRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .build();
       topicAdminClient.deleteTopic(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeleteTopicRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTopic(ProjectTopicName topic) (deprecated)
    
    
    public final void deleteTopic(ProjectTopicName topic)

**Deprecated.** _Use[#deleteTopic(TopicName)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_deleteTopic_) instead._

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ProjectTopicName topic = ProjectTopicName.of("[PROJECT]", "[TOPIC]");
       topicAdminClient.deleteTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName)`  
Required. Name of the topic to delete. Format is `projects/{project}/topics/{topic}`.  
  
### deleteTopic(String topic)
    
    
    public final void deleteTopic(String topic)

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       topicAdminClient.deleteTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the topic to delete. Format is `projects/{project}/topics/{topic}`.  
  
### deleteTopicCallable()
    
    
    public final UnaryCallable<DeleteTopicRequest,Empty> deleteTopicCallable()

Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       DeleteTopicRequest request =
           DeleteTopicRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .build();
       ApiFuture<Empty> future = topicAdminClient.deleteTopicCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeleteTopicRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### detachSubscription(DetachSubscriptionRequest request)
    
    
    public final DetachSubscriptionResponse detachSubscription(DetachSubscriptionRequest request)

Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       DetachSubscriptionRequest request =
           DetachSubscriptionRequest.newBuilder()
               .setSubscription(SubscriptionName.of("[PROJECT]", "[SUBSCRIPTION]").toString())
               .build();
       DetachSubscriptionResponse response = topicAdminClient.detachSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetachSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DetachSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionResponse)` |   
  
### detachSubscriptionCallable()
    
    
    public final UnaryCallable<DetachSubscriptionRequest,DetachSubscriptionResponse> detachSubscriptionCallable()

Detaches a subscription from this topic. All messages retained in the subscription are dropped. Subsequent `Pull` and `StreamingPull` requests will return FAILED_PRECONDITION. If the subscription is a push subscription, pushes to the endpoint will stop.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       DetachSubscriptionRequest request =
           DetachSubscriptionRequest.newBuilder()
               .setSubscription(SubscriptionName.of("[PROJECT]", "[SUBSCRIPTION]").toString())
               .build();
       ApiFuture<DetachSubscriptionResponse> future =
           topicAdminClient.detachSubscriptionCallable().futureCall(request);
       // Do something.
       DetachSubscriptionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetachSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionRequest),[DetachSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionResponse)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = topicAdminClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(String resource) (deprecated)
    
    
    public final Policy getIamPolicy(String resource)

**Deprecated.** _Use[#getIamPolicy(GetIamPolicyRequest)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_getIamPolicy_com_google_iam_v1_GetIamPolicyRequest_) instead._

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String formattedResource = ProjectTopicName.format("[PROJECT]", "[TOPIC]");
       Policy response = topicAdminClient.getIamPolicy(formattedResource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = topicAdminClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getSettings()
    
    
    public final @Nullable TopicAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.pubsub.v1.TopicAdminSettings` |   
  
### getStub()
    
    
    public PublisherStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PublisherStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.stub.PublisherStub)` |   
  
### getTopic(@Nullable TopicName topic)
    
    
    public final Topic getTopic(@Nullable TopicName topic)

Gets the configuration of a topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       Topic response = topicAdminClient.getTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. The name of the topic to get. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### getTopic(GetTopicRequest request)
    
    
    public final Topic getTopic(GetTopicRequest request)

Gets the configuration of a topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       GetTopicRequest request =
           GetTopicRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .build();
       Topic response = topicAdminClient.getTopic(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.GetTopicRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### getTopic(ProjectTopicName topic) (deprecated)
    
    
    public final Topic getTopic(ProjectTopicName topic)

**Deprecated.** _Use[#getTopic(TopicName)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_getTopic_) instead._

Gets the configuration of a topic.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ProjectTopicName topic = ProjectTopicName.of("[PROJECT]", "[TOPIC]");
       Topic response = topicAdminClient.getTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName)`  
Required. The name of the topic to get. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### getTopic(String topic)
    
    
    public final Topic getTopic(String topic)

Gets the configuration of a topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       Topic response = topicAdminClient.getTopic(topic);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the topic to get. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### getTopicCallable()
    
    
    public final UnaryCallable<GetTopicRequest,Topic> getTopicCallable()

Gets the configuration of a topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       GetTopicRequest request =
           GetTopicRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .build();
       ApiFuture<Topic> future = topicAdminClient.getTopicCallable().futureCall(request);
       // Do something.
       Topic response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.GetTopicRequest),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listTopicSnapshots(@Nullable TopicName topic)
    
    
    public final TopicAdminClient.ListTopicSnapshotsPagedResponse listTopicSnapshots(@Nullable TopicName topic)

Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       for (String element : topicAdminClient.listTopicSnapshots(topic).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. The name of the topic that snapshots are attached to. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSnapshotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSnapshotsPagedResponse)` |   
  
### listTopicSnapshots(ListTopicSnapshotsRequest request)
    
    
    public final TopicAdminClient.ListTopicSnapshotsPagedResponse listTopicSnapshots(ListTopicSnapshotsRequest request)

Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSnapshotsRequest request =
           ListTopicSnapshotsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : topicAdminClient.listTopicSnapshots(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTopicSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSnapshotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSnapshotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSnapshotsPagedResponse)` |   
  
### listTopicSnapshots(String topic)
    
    
    public final TopicAdminClient.ListTopicSnapshotsPagedResponse listTopicSnapshots(String topic)

Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       for (String element : topicAdminClient.listTopicSnapshots(topic).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the topic that snapshots are attached to. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSnapshotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSnapshotsPagedResponse)` |   
  
### listTopicSnapshotsCallable()
    
    
    public final UnaryCallable<ListTopicSnapshotsRequest,ListTopicSnapshotsResponse> listTopicSnapshotsCallable()

Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSnapshotsRequest request =
           ListTopicSnapshotsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTopicSnapshotsResponse response =
             topicAdminClient.listTopicSnapshotsCallable().call(request);
         for (String element : response.getSnapshotsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSnapshotsRequest),[ListTopicSnapshotsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSnapshotsResponse)>` |   
  
### listTopicSnapshotsPagedCallable()
    
    
    public final UnaryCallable<ListTopicSnapshotsRequest,TopicAdminClient.ListTopicSnapshotsPagedResponse> listTopicSnapshotsPagedCallable()

Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSnapshotsRequest request =
           ListTopicSnapshotsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future =
           topicAdminClient.listTopicSnapshotsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSnapshotsRequest),[ListTopicSnapshotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSnapshotsPagedResponse)>` |   
  
### listTopicSubscriptions(@Nullable TopicName topic)
    
    
    public final TopicAdminClient.ListTopicSubscriptionsPagedResponse listTopicSubscriptions(@Nullable TopicName topic)

Lists the names of the attached subscriptions on this topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       for (String element : topicAdminClient.listTopicSubscriptions(topic).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. The name of the topic that subscriptions are attached to. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSubscriptionsPagedResponse)` |   
  
### listTopicSubscriptions(ListTopicSubscriptionsRequest request)
    
    
    public final TopicAdminClient.ListTopicSubscriptionsPagedResponse listTopicSubscriptions(ListTopicSubscriptionsRequest request)

Lists the names of the attached subscriptions on this topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSubscriptionsRequest request =
           ListTopicSubscriptionsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : topicAdminClient.listTopicSubscriptions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSubscriptionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSubscriptionsPagedResponse)` |   
  
### listTopicSubscriptions(ProjectTopicName topic) (deprecated)
    
    
    public final TopicAdminClient.ListTopicSubscriptionsPagedResponse listTopicSubscriptions(ProjectTopicName topic)

**Deprecated.** _Use[#listTopicSubscriptions(TopicName)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_listTopicSubscriptions_) instead._

Lists the names of the subscriptions on this topic.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ProjectTopicName topic = ProjectTopicName.of("[PROJECT]", "[TOPIC]");
       for (ProjectSubscriptionName element : topicAdminClient.listTopicSubscriptions(topic).iterateAllAsProjectSubscriptionName()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName)`  
Required. The name of the topic that subscriptions are attached to. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSubscriptionsPagedResponse)` |   
  
### listTopicSubscriptions(String topic)
    
    
    public final TopicAdminClient.ListTopicSubscriptionsPagedResponse listTopicSubscriptions(String topic)

Lists the names of the attached subscriptions on this topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       for (String element : topicAdminClient.listTopicSubscriptions(topic).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the topic that subscriptions are attached to. Format is `projects/{project}/topics/{topic}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSubscriptionsPagedResponse)` |   
  
### listTopicSubscriptionsCallable()
    
    
    public final UnaryCallable<ListTopicSubscriptionsRequest,ListTopicSubscriptionsResponse> listTopicSubscriptionsCallable()

Lists the names of the attached subscriptions on this topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSubscriptionsRequest request =
           ListTopicSubscriptionsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTopicSubscriptionsResponse response =
             topicAdminClient.listTopicSubscriptionsCallable().call(request);
         for (String element : response.getSubscriptionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSubscriptionsRequest),[ListTopicSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSubscriptionsResponse)>` |   
  
### listTopicSubscriptionsPagedCallable()
    
    
    public final UnaryCallable<ListTopicSubscriptionsRequest,TopicAdminClient.ListTopicSubscriptionsPagedResponse> listTopicSubscriptionsPagedCallable()

Lists the names of the attached subscriptions on this topic.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicSubscriptionsRequest request =
           ListTopicSubscriptionsRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future =
           topicAdminClient.listTopicSubscriptionsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicSubscriptionsRequest),[ListTopicSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicSubscriptionsPagedResponse)>` |   
  
### listTopics(@Nullable ProjectName project)
    
    
    public final TopicAdminClient.ListTopicsPagedResponse listTopics(@Nullable ProjectName project)

Lists matching topics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ProjectName project = ProjectName.of("[PROJECT]");
       for (Topic element : topicAdminClient.listTopics(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.ProjectName`  
Required. The name of the project in which to list topics. Format is `projects/{project-id}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicsPagedResponse)` |   
  
### listTopics(ListTopicsRequest request)
    
    
    public final TopicAdminClient.ListTopicsPagedResponse listTopics(ListTopicsRequest request)

Lists matching topics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicsRequest request =
           ListTopicsRequest.newBuilder()
               .setProject(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Topic element : topicAdminClient.listTopics(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicsPagedResponse)` |   
  
### listTopics(String project)
    
    
    public final TopicAdminClient.ListTopicsPagedResponse listTopics(String project)

Lists matching topics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String project = ProjectName.of("[PROJECT]").toString();
       for (Topic element : topicAdminClient.listTopics(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the project in which to list topics. Format is `projects/{project-id}`.  
**Returns**  
---  
**Type** | **Description**  
`[TopicAdminClient.ListTopicsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicsPagedResponse)` |   
  
### listTopicsCallable()
    
    
    public final UnaryCallable<ListTopicsRequest,ListTopicsResponse> listTopicsCallable()

Lists matching topics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicsRequest request =
           ListTopicsRequest.newBuilder()
               .setProject(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTopicsResponse response = topicAdminClient.listTopicsCallable().call(request);
         for (Topic element : response.getTopicsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicsRequest),[ListTopicsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicsResponse)>` |   
  
### listTopicsPagedCallable()
    
    
    public final UnaryCallable<ListTopicsRequest,TopicAdminClient.ListTopicsPagedResponse> listTopicsPagedCallable()

Lists matching topics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       ListTopicsRequest request =
           ListTopicsRequest.newBuilder()
               .setProject(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Topic> future = topicAdminClient.listTopicsPagedCallable().futureCall(request);
       // Do something.
       for (Topic element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ListTopicsRequest),[ListTopicsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.ListTopicsPagedResponse)>` |   
  
### publish(@Nullable TopicName topic, List<PubsubMessage> messages)
    
    
    public final PublishResponse publish(@Nullable TopicName topic, List<PubsubMessage> messages)

Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TopicName topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]");
       List<PubsubMessage> messages = new ArrayList<>();
       PublishResponse response = topicAdminClient.publish(topic, messages);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`topic` | `@org.jspecify.annotations.Nullable com.google.pubsub.v1.TopicName`  
Required. The messages in the request will be published on this topic. Format is `projects/{project}/topics/{topic}`.  
`messages` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage)>`  
Required. The messages to publish.  
**Returns**  
---  
**Type** | **Description**  
`[PublishResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishResponse)` |   
  
### publish(PublishRequest request)
    
    
    public final PublishResponse publish(PublishRequest request)

Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       PublishRequest request =
           PublishRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .addAllMessages(new ArrayList<PubsubMessage>())
               .build();
       PublishResponse response = topicAdminClient.publish(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PublishRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublishResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishResponse)` |   
  
### publish(String topic, List<PubsubMessage> messages)
    
    
    public final PublishResponse publish(String topic, List<PubsubMessage> messages)

Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String topic = TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString();
       List<PubsubMessage> messages = new ArrayList<>();
       PublishResponse response = topicAdminClient.publish(topic, messages);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The messages in the request will be published on this topic. Format is `projects/{project}/topics/{topic}`.  
`messages` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage)>`  
Required. The messages to publish.  
**Returns**  
---  
**Type** | **Description**  
`[PublishResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishResponse)` |   
  
### publishCallable()
    
    
    public final UnaryCallable<PublishRequest,PublishResponse> publishCallable()

Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       PublishRequest request =
           PublishRequest.newBuilder()
               .setTopic(TopicName.ofProjectTopicName("[PROJECT]", "[TOPIC]").toString())
               .addAllMessages(new ArrayList<PubsubMessage>())
               .build();
       ApiFuture<PublishResponse> future = topicAdminClient.publishCallable().futureCall(request);
       // Do something.
       PublishResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PublishRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishRequest),[PublishResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PublishResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = topicAdminClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicy(String resource, Policy policy) (deprecated)
    
    
    public final Policy setIamPolicy(String resource, Policy policy)

**Deprecated.** _Use[#setIamPolicy(SetIamPolicyRequest)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_setIamPolicy_com_google_iam_v1_SetIamPolicyRequest_) instead._

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String formattedResource = ProjectTopicName.format("[PROJECT]", "[TOPIC]");
       Policy policy = Policy.newBuilder().build();
       Policy response = topicAdminClient.setIamPolicy(formattedResource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = topicAdminClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = topicAdminClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissions(String resource, List<String> permissions) (deprecated)
    
    
    public final TestIamPermissionsResponse testIamPermissions(String resource, List<String> permissions)

**Deprecated.** _Use[#testIamPermissions(TestIamPermissionsRequest)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient#com_google_cloud_pubsub_v1_TopicAdminClient_testIamPermissions_com_google_iam_v1_TestIamPermissionsRequest_) instead._

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

Sample code:
    
    
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       String formattedResource = ProjectTopicName.format("[PROJECT]", "[TOPIC]");
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response = topicAdminClient.testIamPermissions(formattedResource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(SchemaName.of("[PROJECT]", "[SCHEMA]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           topicAdminClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateTopic(Topic topic, FieldMask updateMask)
    
    
    public final Topic updateTopic(Topic topic, FieldMask updateMask)

Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       Topic topic = Topic.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Topic response = topicAdminClient.updateTopic(topic, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)`  
Required. The updated topic object.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Indicates which fields in the provided topic to update. Must be specified and non-empty. Note that if `update_mask` contains "message_storage_policy" but the `message_storage_policy` is not set in the `topic` provided above, then the updated value is determined by the policy configured at the project or organization level.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### updateTopic(UpdateTopicRequest request)
    
    
    public final Topic updateTopic(UpdateTopicRequest request)

Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       UpdateTopicRequest request =
           UpdateTopicRequest.newBuilder()
               .setTopic(Topic.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Topic response = topicAdminClient.updateTopic(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)` |   
  
### updateTopicCallable()
    
    
    public final UnaryCallable<UpdateTopicRequest,Topic> updateTopicCallable()

Updates an existing topic by updating the fields specified in the update mask. Note that certain properties of a topic are not modifiable.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TopicAdminClient topicAdminClient = TopicAdminClient.create()) {
       UpdateTopicRequest request =
           UpdateTopicRequest.newBuilder()
               .setTopic(Topic.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Topic> future = topicAdminClient.updateTopicCallable().futureCall(request);
       // Do something.
       Topic response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest),[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
