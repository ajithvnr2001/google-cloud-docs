---
url: https://docs.cloud.google.com/pubsub/docs/retry-requests/
title: Retry requests \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:13.586362+00:00
---

# Retry requests  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/retry-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Retry requests Stay organized with collections  Save and categorize content based on your preferences. 

Publishing failures are typically caused by client-side bottlenecks, such as insufficient service CPUs, bad thread health, or network congestion. The publisher retry policy defines the number of times Pub/Sub tries to deliver a message and the length of time between each attempt.

This document provides information about using retry requests with messages published to a topic.

## Before you begin

Before configuring the publish workflow, ensure you have completed the following tasks:

  * Learn about [topics and the publishing workflow](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles

To get the permissions that you need to retry message requests to a topic, ask your administrator to grant you the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role on the topic. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You need [additional permissions](https://docs.cloud.google.com/pubsub/docs/access-control) to create or update topics and subscriptions.

## About retry requests

Retry settings control how the Pub/Sub client libraries retry publish requests. The client libraries have the following retry settings:

  * **Initial request timeout** : the amount of time before a client library stops waiting for the initial publish request to complete.
  * **Retry delay** : the amount of time after a request times out that a client library waits to retry the request.
  * **Total timeout** : the amount of time after a client library stops retrying publish requests.



To retry publish requests, the initial request timeout must be shorter than the total timeout. For example, if you're using exponential backoff, the client libraries compute the request timeout and retry delay as follows:

  * After each publish request, the request timeout increases by the request timeout multiplier, up to the maximum request timeout.
  * After each retry, the retry delay increases by the retry delay multiplier, up to the maximum retry delay.



## Retry a message request

During the publishing process, you might see transient or permanent publishing failures. For transient errors, you typically don't need to take any special action as Pub/Sub automatically retries the messages.

An error can also occur when a publish operation succeeds but the publish response is not received in time by the publisher client. In this case too, the publish operation is retried. As a result, you can have two identical messages with different message IDs.

In case of persistent errors, consider implementing appropriate actions outside of the publishing process to avoid overwhelming Pub/Sub.

Publishing failures are automatically retried, except for errors that don't warrant retries. This sample code demonstrates creating a publisher with custom retry settings (note that not all client libraries support custom retry settings; see the [API Reference documentation](https://docs.cloud.google.com/pubsub/docs/reference/libraries#additional_resources) for your chosen language):

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    [](std::string project_id, std::string topic_id) {
      auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
      // By default a publisher will retry for 60 seconds, with an initial backoff
      // of 100ms, a maximum backoff of 60 seconds, and the backoff will grow by
      // 30% after each attempt. This changes those defaults.
      auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
          std::move(topic),
          Options{}
              .set<pubsub::RetryPolicyOption>(
                  pubsub::LimitedTimeRetryPolicy(
                      /*maximum_duration=*/std::chrono::minutes(10))
                      .clone())
              .set<pubsub::BackoffPolicyOption>(
                  pubsub::ExponentialBackoffPolicy(
                      /*initial_delay=*/std::chrono::milliseconds(200),
                      /*maximum_delay=*/std::chrono::seconds(45),
                      /*scaling=*/2.0)
                      .clone())));
    
      std::vector<future<bool>> done;
      for (char const* data : {"1", "2", "3", "go!"}) {
        done.push_back(
            publisher.Publish(pubsub::MessageBuilder().SetData(data).Build())
                .then([](future<StatusOr<std::string>> f) {
                  return f.get().ok();
                }));
      }
      publisher.Flush();
      int count = 0;
      for (auto& f : done) {
        if (f.get()) ++count;
      }
      std::cout << count << " messages sent successfully\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Api.Gax.Grpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.Threading.Tasks;
    
    public class PublishMessageWithRetrySettingsAsyncSample
    {
        public async Task PublishMessageWithRetrySettingsAsync(string projectId, string topicId, string messageText)
        {
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            // Retry settings control how the publisher handles retry-able failures
            var maxAttempts = 3;
            var initialBackoff = TimeSpan.FromMilliseconds(110); // default: 100 ms
            var maxBackoff = TimeSpan.FromSeconds(70); // default : 60 seconds
            var backoffMultiplier = 1.3; // default: 1.0
            var totalTimeout = TimeSpan.FromSeconds(100); // default: 600 seconds
    
            var publisher = await new [PublisherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClientBuilder.html)
            {
                TopicName = topicName,
                ApiSettings = new [PublisherServiceApiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiSettings.html)
                {
                    PublishSettings = [CallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html).[FromRetry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html#Google_Api_Gax_Grpc_CallSettings_FromRetry_Google_Api_Gax_Grpc_RetrySettings_)([RetrySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html).[FromExponentialBackoff](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_FromExponentialBackoff_System_Int32_System_TimeSpan_System_TimeSpan_System_Double_System_Predicate_System_Exception__Google_Api_Gax_Grpc_RetrySettings_IJitter_)(
                                   maxAttempts: maxAttempts,
                                   initialBackoff: initialBackoff,
                                   maxBackoff: maxBackoff,
                                   backoffMultiplier: backoffMultiplier,
                                   retryFilter: [RetrySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html).[FilterForStatusCodes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_FilterForStatusCodes_Grpc_Core_StatusCode___)([StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[Unavailable](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable))))
                           .[WithTimeout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettingsExtensions.html#Google_Api_Gax_Grpc_CallSettingsExtensions_WithTimeout_Google_Api_Gax_Grpc_CallSettings_System_TimeSpan_)(totalTimeout)
                }
            }.BuildAsync();
            string message = await publisher.PublishAsync(messageText);
            Console.WriteLine($"Published message {message}");
            // PublisherClient instance should be shutdown after use.
            // The TimeSpan specifies for how long to attempt to publish locally queued messages.
            await publisher.ShutdownAsync(TimeSpan.FromSeconds(15));
        }
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	vkit "cloud.google.com/go/pubsub/v2/apiv1"
    	gax "github.com/googleapis/gax-go/v2"
    	"google.golang.org/grpc/codes"
    )
    
    func publishWithRetrySettings(w io.Writer, projectID, topicID, msg string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// msg := "Hello World"
    	ctx := context.Background()
    
    	config := &pubsub.ClientConfig{
    		TopicAdminCallOptions: &vkit.TopicAdminCallOptions{
    			Publish: []gax.CallOption{
    				gax.WithRetry(func() gax.Retryer {
    					return gax.OnCodes([]codes.Code{
    						codes.Aborted,
    						codes.Canceled,
    						codes.Internal,
    						codes.ResourceExhausted,
    						codes.Unknown,
    						codes.Unavailable,
    						codes.DeadlineExceeded,
    					}, gax.Backoff{
    						Initial:    250 * time.Millisecond, // default 100 milliseconds
    						Max:        60 * time.Second,       // default 60 seconds
    						Multiplier: 1.45,                   // default 1.3
    					})
    				}),
    			},
    		},
    	}
    
    	client, err := pubsub.NewClientWithConfig(ctx, projectID, config)
    	if err != nil {
    		return fmt.Errorf("pubsub: NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	// Reuse this publisher for all publish calls to send messages in batches.
    	publisher := client.Publisher(topicID)
    	result := publisher.Publish(ctx, &pubsub.Message{
    		Data: []byte(msg),
    	})
    	// Block until the result is returned and a server-generated
    	// ID is returned for the published message.
    	id, err := result.Get(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub: result.Get: %w", err)
    	}
    	fmt.Fprintf(w, "Published a message; msg ID: %v\n", id)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import org.threeten.bp.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class PublishWithRetrySettingsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        publishWithRetrySettingsExample(projectId, topicId);
      }
    
      public static void publishWithRetrySettingsExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
    
        try {
          // Retry settings control how the publisher handles retry-able failures
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) initialRetryDelay = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMillis(100); // default: 100 ms
          double retryDelayMultiplier = 2.0; // back off for repeated failures, default: 1.3
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxRetryDelay = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofSeconds(60); // default : 60 seconds
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) initialRpcTimeout = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofSeconds(1); // default: 5 seconds
          double rpcTimeoutMultiplier = 1.0; // default: 1.0
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxRpcTimeout = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofSeconds(600); // default: 600 seconds
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) totalTimeout = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofSeconds(600); // default: 600 seconds
    
          [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html) retrySettings =
              [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                  .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(initialRetryDelay)
                  .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(retryDelayMultiplier)
                  .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(maxRetryDelay)
                  .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(initialRpcTimeout)
                  .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(rpcTimeoutMultiplier)
                  .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(maxRpcTimeout)
                  .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(totalTimeout)
                  .build();
    
          // Create a publisher instance with default settings bound to the topic
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName).[setRetrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.Builder.html#com_google_cloud_pubsub_v1_Publisher_Builder_setRetrySettings_com_google_api_gax_retrying_RetrySettings_)(retrySettings).build();
    
          String message = "first message";
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
    
          // Once published, returns a server-assigned message id (unique within the topic)
          ApiFuture<String> messageIdFuture = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubMessage);
          String messageId = messageIdFuture.get();
          System.out.println("Published a message with retry settings: " + messageId);
    
        } finally {
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID'
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const data = JSON.stringify({foo: 'bar'});
    
    // Imports the Google Cloud client library. v1 is for the lower level
    // proto access.
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    async function publishWithRetrySettings(topicNameOrId, data) {
      const pubsubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
      // Retry settings control how the publisher handles retryable failures. Default values are shown.
      // The `retryCodes` array determines which grpc errors will trigger an automatic retry.
      // The `backoffSettings` object lets you specify the behaviour of retries over time.
      //
      // Reference this document to see the current defaults for publishing:
      // https://github.com/googleapis/nodejs-pubsub/blob/6e2c28a9298a49dc1b194ce747ff5258c8df6deb/src/v1/publisher_client_config.json#L59
      //
      // Please note that _all_ items must be included when passing these settings to topic().
      // Otherwise, unpredictable (incorrect) defaults may be assumed.
      const retrySettings = {
        retryCodes: [
          10, // 'ABORTED'
          1, // 'CANCELLED',
          4, // 'DEADLINE_EXCEEDED'
          13, // 'INTERNAL'
          8, // 'RESOURCE_EXHAUSTED'
          14, // 'UNAVAILABLE'
          2, // 'UNKNOWN'
        ],
        backoffSettings: {
          // The initial delay time, in milliseconds, between the completion
          // of the first failed request and the initiation of the first retrying request.
          initialRetryDelayMillis: 100,
          // The multiplier by which to increase the delay time between the completion
          // of failed requests, and the initiation of the subsequent retrying request.
          retryDelayMultiplier: 4,
          // The maximum delay time, in milliseconds, between requests.
          // When this value is reached, retryDelayMultiplier will no longer be used to increase delay time.
          maxRetryDelayMillis: 60000,
          // The initial timeout parameter to the request.
          initialRpcTimeoutMillis: 60000,
          // The multiplier by which to increase the timeout parameter between failed requests.
          rpcTimeoutMultiplier: 1.0,
          // The maximum timeout parameter, in milliseconds, for a request. When this value is reached,
          // rpcTimeoutMultiplier will no longer be used to increase the timeout.
          maxRpcTimeoutMillis: 60000,
          // The total time, in milliseconds, starting from when the initial request is sent,
          // after which an error will be returned, regardless of the retrying attempts made meanwhile.
          totalTimeoutMillis: 600000,
        },
      };
    
      // Cache topic objects (publishers) and reuse them.
      const topic = pubsubClient.topic(topicNameOrId, {
        gaxOpts: {
          retry: retrySettings,
        },
      });
    
      // Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject)
      const dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(data);
      const messageId = await topic.[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)({data: dataBuffer});
      console.log(`Message ${messageId} published.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID'
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const data = JSON.stringify({foo: 'bar'});
    
    // Imports the Google Cloud client library. v1 is for the lower level
    // proto access.
    import {PubSub} from '@google-cloud/pubsub';
    
    async function publishWithRetrySettings(topicNameOrId: string, data: string) {
      const pubsubClient = new PubSub();
    
      // Retry settings control how the publisher handles retryable failures. Default values are shown.
      // The `retryCodes` array determines which grpc errors will trigger an automatic retry.
      // The `backoffSettings` object lets you specify the behaviour of retries over time.
      //
      // Reference this document to see the current defaults for publishing:
      // https://github.com/googleapis/nodejs-pubsub/blob/6e2c28a9298a49dc1b194ce747ff5258c8df6deb/src/v1/publisher_client_config.json#L59
      //
      // Please note that _all_ items must be included when passing these settings to topic().
      // Otherwise, unpredictable (incorrect) defaults may be assumed.
      const retrySettings = {
        retryCodes: [
          10, // 'ABORTED'
          1, // 'CANCELLED',
          4, // 'DEADLINE_EXCEEDED'
          13, // 'INTERNAL'
          8, // 'RESOURCE_EXHAUSTED'
          14, // 'UNAVAILABLE'
          2, // 'UNKNOWN'
        ],
        backoffSettings: {
          // The initial delay time, in milliseconds, between the completion
          // of the first failed request and the initiation of the first retrying request.
          initialRetryDelayMillis: 100,
          // The multiplier by which to increase the delay time between the completion
          // of failed requests, and the initiation of the subsequent retrying request.
          retryDelayMultiplier: 4,
          // The maximum delay time, in milliseconds, between requests.
          // When this value is reached, retryDelayMultiplier will no longer be used to increase delay time.
          maxRetryDelayMillis: 60000,
          // The initial timeout parameter to the request.
          initialRpcTimeoutMillis: 60000,
          // The multiplier by which to increase the timeout parameter between failed requests.
          rpcTimeoutMultiplier: 1.0,
          // The maximum timeout parameter, in milliseconds, for a request. When this value is reached,
          // rpcTimeoutMultiplier will no longer be used to increase the timeout.
          maxRpcTimeoutMillis: 60000,
          // The total time, in milliseconds, starting from when the initial request is sent,
          // after which an error will be returned, regardless of the retrying attempts made meanwhile.
          totalTimeoutMillis: 600000,
        },
      };
    
      // Cache topic objects (publishers) and reuse them.
      const topic = pubsubClient.topic(topicNameOrId, {
        gaxOpts: {
          retry: retrySettings,
        },
      });
    
      // Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject)
      const dataBuffer = Buffer.from(data);
      const messageId = await topic.publishMessage({data: dataBuffer});
      console.log(`Message ${messageId} published.`);
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google import api_core
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    # Configure the retry settings. Defaults shown in comments are values applied
    # by the library by default, instead of default values in the Retry object.
    custom_retry = api_core.[retry](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html#google_cloud_pubsub_v1_types_PublisherOptions_retry).Retry(
        initial=0.250,  # seconds (default: 0.1)
        maximum=90.0,  # seconds (default: 60.0)
        multiplier=1.45,  # default: 1.3
        deadline=300.0,  # seconds (default: 60.0)
        predicate=api_core.[retry](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html#google_cloud_pubsub_v1_types_PublisherOptions_retry).if_exception_type(
            api_core.exceptions.Aborted,
            api_core.exceptions.DeadlineExceeded,
            api_core.exceptions.InternalServerError,
            api_core.exceptions.ResourceExhausted,
            api_core.exceptions.ServiceUnavailable,
            api_core.exceptions.Unknown,
            api_core.exceptions.Cancelled,
        ),
    )
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    for n in range(1, 10):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic=topic_path, data=data, retry=custom_retry)
        print(future.result())
    
    print(f"Published messages with retry settings to {topic_path}.")

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_gax::exponential_backoff::ExponentialBackoffBuilder;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_pubsub::client::Publisher;
    use google_cloud_pubsub::model::Message;
    use google_cloud_pubsub::retry_policy::RetryableErrors;
    use std::time::Duration;
    
    pub async fn sample(project_id: &str, topic_id: &str) -> anyhow::Result<()> {
        let topic_name = format!("projects/{project_id}/topics/{topic_id}");
    
        // Configure custom retry settings.
        // In this example, we retry with a time limit of 5 minutes.
        let retry_policy = RetryableErrors.with_time_limit(Duration::from_secs(300));
    
        // Configure custom backoff settings.
        let backoff_policy = ExponentialBackoffBuilder::new()
            .with_initial_delay(Duration::from_millis(200))
            .with_maximum_delay(Duration::from_secs(45))
            .with_scaling(2.0)
            .clamp();
    
        let publisher = Publisher::builder(topic_name)
            .with_retry_policy(retry_policy)
            .with_backoff_policy(backoff_policy)
            .build()
            .await?;
    
        let message = Message::new().set_data("Hello, World!");
        let message_id = publisher.publish(message).await?;
    
        println!("published message with ID: {message_id}");
        Ok(())
    }

## Retry requests with ordering keys

Assume you have a single publisher client. You are using the Pub/Sub client libraries to publish messages 1, 2, and 3 for the same ordering key A. Now, assume that the published response for message 1 is not received by the publisher client before the RPC deadline expires. Message 1 must be republished. The sequence of messages received by the subscriber client then becomes 1, 1, 2, and 3, if you assume message 2 is published only after message 1 gets completed successfully. Each published message has its own message ID. From the subscriber client's perspective, four messages were published, with the first two having identical content.

Retrying publish requests with ordering keys can also be complicated by batch settings. The client library batches messages together for more efficient publishing. Continue with the previous example and assume that messages 1 and 2 are batched together. This batch is sent to the server as a single request. If the server fails to return a response in time, the publisher client retries this batch of two messages. Therefore, it is possible that the subscriber client receives messages 1, 2, 1, 2, and 3. If you use a Pub/Sub client library for publishing messages in order and a publish operation fails, the service fails the publish operations for all remaining messages on the same ordering key. A publisher client can then decide to follow any one of the following operations:

  * Republish all the failed messages in order

  * Republish a subset of the failed messages in order

  * Publish a new set of messages




If a non-retryable error occurs, the client library doesn't publish the message and stops publishing other messages with the same ordering key. For example, when a publisher sends a message to a topic that doesn't exist, a non-retryable error occurs. To continue publishing messages with the same ordering key, call a method to resume publishing and then start publishing again.

The following sample shows you how to resume publishing messages with the same ordering key.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    [](pubsub::Publisher publisher) {
      struct SampleData {
        std::string ordering_key;
        std::string data;
      } data[] = {
          {"key1", "message1"}, {"key2", "message2"}, {"key1", "message3"},
          {"key1", "message4"}, {"key1", "message5"},
      };
      std::vector<future<void>> done;
      for (auto& datum : data) {
        auto const& da = datum;  // workaround MSVC lambda capture confusion
        auto handler = [da, publisher](future<StatusOr<std::string>> f) mutable {
          auto const msg = da.ordering_key + "#" + da.data;
          auto id = f.get();
          if (!id) {
            std::cout << "An error has occurred publishing " << msg << "\n";
            publisher.ResumePublish(da.ordering_key);
            return;
          }
          std::cout << "Message " << msg << " published as id=" << *id << "\n";
        };
        done.push_back(
            publisher
                .Publish(pubsub::MessageBuilder{}
                             .SetData("Hello World! [" + datum.data + "]")
                             .SetOrderingKey(datum.ordering_key)
                             .Build())
                .then(handler));
      }
      publisher.Flush();
      // Block until all the messages are published (optional)
      for (auto& f : done) f.get();
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class ResumePublishSample
    {
        public async Task<int> PublishOrderedMessagesAsync(string projectId, string topicId, IEnumerable<(string, string)> keysAndMessages)
        {
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
    
            var customSettings = new PublisherClient.Settings
            {
                EnableMessageOrdering = true
            };
    
            [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher = await new [PublisherClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClientBuilder.html)
            {
                TopicName = topicName,
                Settings = customSettings
            }.BuildAsync();
    
            int publishedMessageCount = 0;
            var publishTasks = keysAndMessages.Select(async keyAndMessage =>
            {
                try
                {
                    string message = await publisher.PublishAsync(keyAndMessage.Item1, keyAndMessage.Item2);
                    Console.WriteLine($"Published message {message}");
                    Interlocked.Increment(ref publishedMessageCount);
                }
                catch (Exception exception)
                {
                    Console.WriteLine($"An error occurred when publishing message {keyAndMessage.Item2}: {exception.Message}");
                    publisher.ResumePublish(keyAndMessage.Item1);
                }
            });
            await Task.WhenAll(publishTasks);
            // PublisherClient instance should be shutdown after use.
            // The TimeSpan specifies for how long to attempt to publish locally queued messages.
            await publisher.[ShutdownAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_ShutdownAsync_System_Threading_CancellationToken_)(TimeSpan.FromSeconds(15));
            return publishedMessageCount;
        }
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"google.golang.org/api/option"
    )
    
    func resumePublishWithOrderingKey(w io.Writer, projectID, topicID string) {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    
    	// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.NewClient(ctx, projectID,
    		option.WithEndpoint("us-east1-pubsub.googleapis.com:443"))
    	if err != nil {
    		fmt.Fprintf(w, "pubsub.NewClient: %v", err)
    		return
    	}
    	defer client.Close()
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	// Reuse this publisher for all publish calls to send messages in batches.
    	publisher := client.Publisher(topicID)
    	publisher.EnableMessageOrdering = true
    	key := "some-ordering-key"
    
    	result := publisher.Publish(ctx, &pubsub.Message{
    		Data:        []byte("some-message"),
    		OrderingKey: key,
    	})
    	_, err = result.Get(ctx)
    	if err != nil {
    		// Fix internal state to make sure publishes with errors are not
    		// published out of order. This might mean moving messages to a queue
    		// and retrying those messages before publishing subsquent messages.
    		fmt.Printf("Failed to publish: %s\n", err)
    
    		// Resume publish on an ordering key that has had unrecoverable errors.
    		// After such an error publishes with this ordering key will fail
    		// until this method is called.
    		publisher.ResumePublish(key)
    	}
    
    	fmt.Fprint(w, "Published a message with ordering key successfully\n")
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutureCallback](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutureCallback.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.concurrent.TimeUnit;
    
    public class ResumePublishWithOrderingKeys {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Choose an existing topic.
        String topicId = "your-topic-id";
    
        resumePublishWithOrderingKeysExample(projectId, topicId);
      }
    
      public static void resumePublishWithOrderingKeysExample(String projectId, String topicId)
          throws IOException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        // Create a publisher and set message ordering to true.
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher =
            [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName)
                .setEnableMessageOrdering(true)
                .setEndpoint("us-east1-pubsub.googleapis.com:443")
                .build();
    
        try {
          Map<String, String> messages = new LinkedHashMap<String, String>();
          messages.put("message1", "key1");
          messages.put("message2", "key2");
          messages.put("message3", "key1");
          messages.put("message4", "key2");
    
          for (Map.Entry<String, String> entry : messages.entrySet()) {
            ByteString data = ByteString.copyFromUtf8(entry.getKey());
            PubsubMessage pubsubMessage =
                PubsubMessage.newBuilder().setData(data).setOrderingKey(entry.getValue()).build();
            ApiFuture<String> future = publisher.publish(pubsubMessage);
    
            // Add an asynchronous callback to handle publish success / failure.
            ApiFutures.addCallback(
                future,
                new ApiFutureCallback<String>() {
    
                  @Override
                  public void onFailure(Throwable throwable) {
                    if (throwable instanceof ApiException) {
                      ApiException apiException = ((ApiException) throwable);
                      // Details on the API exception.
                      System.out.println(apiException.getStatusCode().getCode());
                      System.out.println(apiException.isRetryable());
                    }
                    System.out.println("Error publishing message : " + pubsubMessage.getData());
                    // (Beta) Must call resumePublish to reset key and continue publishing with order.
                    publisher.resumePublish(pubsubMessage.getOrderingKey());
                  }
    
                  @Override
                  public void onSuccess(String messageId) {
                    // Once published, returns server-assigned message ids (unique within the topic).
                    System.out.println(pubsubMessage.getData() + " : " + messageId);
                  }
                },
                MoreExecutors.directExecutor());
          }
        } finally {
          publisher.shutdown();
          publisher.awaitTermination(1, TimeUnit.MINUTES);
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const data = JSON.stringify({foo: 'bar'});
    // const orderingKey = 'key1';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function resumePublish(topicNameOrId, data, orderingKey) {
      // Publishes the message as a string, e.g. "Hello, world!" or JSON.stringify(someObject)
      const dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(data);
    
      const publishOptions = {
        messageOrdering: true,
      };
    
      // Cache topic objects (publishers) and reuse them.
      //
      // Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering
      // key are in the same region. For list of locational endpoints for Pub/Sub, see:
      // https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
      const publisher = pubSubClient.topic(topicNameOrId, publishOptions);
    
      // Publishes the message
      try {
        const message = {
          data: dataBuffer,
          orderingKey: orderingKey,
        };
        const messageId = await [publisher](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html).[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)(message);
        console.log(`Message ${messageId} published.`);
    
        return messageId;
      } catch (e) {
        console.log(`Could not publish: ${e}`);
        [publisher](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html).[resumePublishing](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)(orderingKey);
        return null;
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer): Choose an existing topic.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    publisher_options = pubsub_v1.types.[PublisherOptions](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html)(enable_message_ordering=True)
    # Sending messages to the same region ensures they are received in order
    # even when multiple publishers are used.
    client_options = {"api_endpoint": "us-east1-pubsub.googleapis.com:443"}
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(
        publisher_options=publisher_options, client_options=client_options
    )
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    
    for message in [
        ("message1", "key1"),
        ("message2", "key2"),
        ("message3", "key1"),
        ("message4", "key2"),
    ]:
        # Data must be a bytestring
        data = message[0].encode("utf-8")
        ordering_key = message[1]
        # When you publish a message, the client returns a future.
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data=data, ordering_key=ordering_key)
        try:
            print(future.result())
        except RuntimeError:
            # Resume publish on an ordering key that has had unrecoverable errors.
            publisher.[resume_publish](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_resume_publish)(topic_path, ordering_key)
    
    print(f"Resumed publishing messages with ordering keys to {topic_path}.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    # Start sending messages in one request once the size of all queued messages
    # reaches 1 MB or the number of queued messages reaches 20
    publisher = pubsub.[publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id, async: {
      max_bytes:    1_000_000,
      max_messages: 20
    }
    
    publisher.enable_message_ordering!
    10.times do |i|
      publisher.[publish_async](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html) "This is message ##{i}.",
                              ordering_key: "ordering-key" do |result|
        if result.succeeded?
          puts "Message ##{i} successfully published."
        else
          puts "Message ##{i} failed to publish"
          # Allow publishing to continue on "ordering-key" after processing the
          # failure.
          publisher.resume_publish "ordering-key"
        end
      end
    end
    
    # Stop the async_publisher to send all queued messages immediately.
    publisher.[async_publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Publisher.html).stop!

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_pubsub::client::Publisher;
    use google_cloud_pubsub::model::Message;
    
    pub async fn sample(project: &str, topic_id: &str) -> anyhow::Result<()> {
        let publisher = Publisher::builder(format!("projects/{project}/topics/{topic_id}"))
            // Pub/Sub's ordered delivery guarantee only applies when publishes for
            // an ordering key are in the same region.
            .with_endpoint("https://us-east1-pubsub.googleapis.com")
            .build()
            .await?;
    
        let ordering_key = "ordering-key";
        let result = publisher.publish(
            Message::new()
                .set_data("message")
                .set_ordering_key(ordering_key),
        );
    
        match result.await {
            Ok(message_id) => println!("published message with ID: {message_id}"),
            Err(e) => {
                // Fix internal state to make sure publishes with errors are not
                // published out of order. This might mean moving messages to a queue
                // and retrying those messages before publishing subsequent messages.
                println!("error publishing message: {e}");
    
                // Resume publish on an ordering key that has had unrecoverable errors.
                // After an error, publishes with this ordering key will fail
                // until this method is called.
                publisher.resume_publish(ordering_key);
            }
        }
    
        Ok(())
    }

## What's next

To learn how to configure advanced publishing options, see the following:

  * [Compress messages](https://docs.cloud.google.com/pubsub/docs/compress-messages)

  * [Flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages)

  * [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages)

  * [Batch messaging](https://docs.cloud.google.com/pubsub/docs/batch-messaging)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
