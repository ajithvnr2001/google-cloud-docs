---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-otel-tracing/
title: Create a subscriber application with OpenTelemetry enabled \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:26.030899+00:00
---

# Create a subscriber application with OpenTelemetry enabled  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-otel-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create a subscriber application with OpenTelemetry enabled Stay organized with collections  Save and categorize content based on your preferences. 

Create a subscriber application with OpenTelemetry enabled, 100% tracing

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Pub/Sub OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/opentelemetry/configure_basic_tracing.h"
    #include "google/cloud/opentelemetry_options.h"
    #include "google/cloud/pubsub/message.h"
    #include "google/cloud/pubsub/publisher.h"
    #include "google/cloud/pubsub/subscriber.h"
    #include "google/cloud/pubsub/subscription.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 4) {
        std::cerr << "Usage: " << argv[0]
                  << " <project-id> <topic-id> <subscription-id>\n";
        return 1;
      }
    
      std::string const project_id = argv[1];
      std::string const topic_id = argv[2];
      std::string const subscription_id = argv[3];
    
      // Create a few namespace aliases to make the code easier to read.
      namespace gc = ::google::cloud;
      namespace otel = gc::otel;
      namespace pubsub = gc::pubsub;
    
      auto constexpr kWaitTimeout = std::chrono::seconds(30);
    
      auto project = gc::Project(project_id);
      auto configuration = otel::ConfigureBasicTracing(project);
    
      // Publish a message with tracing enabled.
      auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
          pubsub::Topic(project_id, topic_id),
          gc::Options{}.set<gc::OpenTelemetryTracingOption>(true)));
      // Block until the message is actually sent and throw on error.
      auto id = publisher.Publish(pubsub::MessageBuilder().SetData("Hi!").Build())
                    .get()
                    .value();
      std::cout << "Sent message with id: (" << id << ")\n";
    
      // Receive a message using streaming pull with tracing enabled.
      auto subscriber = pubsub::Subscriber(pubsub::MakeSubscriberConnection(
          pubsub::Subscription(project_id, subscription_id),
          gc::Options{}.set<gc::OpenTelemetryTracingOption>(true)));
    
      auto session =
          subscriber.Subscribe([&](pubsub::Message const& m, pubsub::AckHandler h) {
            std::cout << "Received message " << m << "\n";
            std::move(h).ack();
          });
    
      std::cout << "Waiting for messages on " + subscription_id + "...\n";
    
      // Blocks until the timeout is reached.
      auto result = session.wait_for(kWaitTimeout);
      if (result == std::future_status::timeout) {
        std::cout << "timeout reached, ending session\n";
        session.cancel();
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	texporter "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace"
    	"go.opentelemetry.io/otel"
    	"go.opentelemetry.io/otel/sdk/resource"
    	sdktrace "go.opentelemetry.io/otel/sdk/trace"
    	semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
    	"google.golang.org/api/option"
    )
    
    func subscribeOpenTelemetryTracing(w io.Writer, projectID, subID string, sampleRate float64) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	// sampleRate := "1.0"
    	ctx := context.Background()
    
    	exporter, err := texporter.New(texporter.WithProjectID(projectID),
    		// Disable spans created by the exporter.
    		texporter.WithTraceClientOptions(
    			[]option.ClientOption{option.WithTelemetryDisabled()},
    		),
    	)
    	if err != nil {
    		return fmt.Errorf("error instantiating exporter: %w", err)
    	}
    
    	resources := resource.NewWithAttributes(
    		semconv.SchemaURL,
    		semconv.ServiceNameKey.String("subscriber"),
    	)
    
    	// Instantiate a tracer provider with the following settings
    	tp := sdktrace.NewTracerProvider(
    		sdktrace.WithBatcher(exporter),
    		sdktrace.WithResource(resources),
    		sdktrace.WithSampler(
    			sdktrace.ParentBased(sdktrace.TraceIDRatioBased(sampleRate)),
    		),
    	)
    
    	defer tp.ForceFlush(ctx) // flushes any pending spans
    	otel.SetTracerProvider(tp)
    
    	// Create a new client with tracing enabled.
    	client, err := pubsub.NewClientWithConfig(ctx, projectID, &pubsub.ClientConfig{
    		EnableOpenTelemetryTracing: true,
    	})
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// client.Subscriber can be passed a subscription ID (e.g. "my-sub") or
    	// a fully qualified name (e.g. "projects/my-project/subscriptions/my-sub").
    	// If a subscription ID is provided, the project ID from the client is used.
    	sub := client.Subscriber(subID)
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var received int32
    	err = sub.Receive(ctx, func(_ context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		atomic.AddInt32(&received, 1)
    		msg.Ack()
    	})
    	if err != nil {
    		return fmt.Errorf("sub.Receive: %w", err)
    	}
    	fmt.Fprintf(w, "Received %d messages\n", received)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.opentelemetry.trace.TraceConfiguration;
    import com.google.cloud.opentelemetry.trace.TraceExporter;
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import io.opentelemetry.api.OpenTelemetry;
    import io.opentelemetry.sdk.OpenTelemetrySdk;
    import io.opentelemetry.sdk.resources.Resource;
    import io.opentelemetry.sdk.trace.SdkTracerProvider;
    import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;
    import io.opentelemetry.sdk.trace.export.SpanExporter;
    import io.opentelemetry.sdk.trace.samplers.Sampler;
    import io.opentelemetry.semconv.ResourceAttributes;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class OpenTelemetrySubscriberExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        openTelemetrySubscriberExample(projectId, subscriptionId);
      }
    
      public static void openTelemetrySubscriberExample(String projectId, String subscriptionId) {
        Resource resource =
            Resource.getDefault().toBuilder()
                .put(ResourceAttributes.SERVICE_NAME, "subscriber-example")
                .build();
    
        // Creates a Cloud Trace exporter.
        SpanExporter traceExporter =
            TraceExporter.createWithConfiguration(
                TraceConfiguration.builder().setProjectId(projectId).build());
    
        SdkTracerProvider sdkTracerProvider =
            SdkTracerProvider.builder()
                .setResource(resource)
                .addSpanProcessor(SimpleSpanProcessor.create(traceExporter))
                .setSampler(Sampler.alwaysOn())
                .build();
    
        OpenTelemetry openTelemetry =
            OpenTelemetrySdk.builder().setTracerProvider(sdkTracerProvider).buildAndRegisterGlobal();
    
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        // Instantiate an asynchronous message receiver.
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              // Handle incoming message, then ack the received message.
              System.out.println("Id: " + message.getMessageId());
              System.out.println("Data: " + message.getData().toStringUtf8());
              consumer.ack();
            };
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = null;
        try {
          subscriber =
              [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver)
                  .setOpenTelemetry(openTelemetry)
                  .setEnableOpenTelemetryTracing(true)
                  .build();
    
          // Start the subscriber.
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          System.out.printf("Listening for messages on %s:\n", subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)());
          // Allow the subscriber to run for 30s unless an unrecoverable error occurs.
          subscriber.awaitTerminated(30, TimeUnit.SECONDS);
        } catch (TimeoutException timeoutException) {
          // Shut down the subscriber after 30s. Stop receiving messages.
          subscriber.stopAsync();
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
