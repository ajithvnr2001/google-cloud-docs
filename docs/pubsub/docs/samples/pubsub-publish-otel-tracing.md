---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-otel-tracing/
title: Publish a message with OpenTelemetry tracing enabled \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:43.080735+00:00
---

# Publish a message with OpenTelemetry tracing enabled  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-otel-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Publish a message with OpenTelemetry tracing enabled Stay organized with collections  Save and categorize content based on your preferences. 

Publish a message with OpenTelemetry Tracing enabled while using a Cloud Trace exporter and sample rate of 100%.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Pub/Sub OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing)
  * [Quickstart: Trace a C++ Application](https://docs.cloud.google.com/cpp/docs/quickstart-open-telemetry)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a few namespace aliases to make the code easier to read.
    namespace gc = ::google::cloud;
    namespace otel = gc::otel;
    namespace pubsub = gc::pubsub;
    
    // This example uses a simple wrapper to export (upload) OTel tracing data
    // to Google Cloud Trace. More complex applications may use different
    // authentication, or configure their own OTel exporter.
    auto project = gc::Project(project_id);
    auto configuration = otel::ConfigureBasicTracing(project);
    
    auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
        pubsub::Topic(project_id, topic_id),
        // Configure this publisher to enable OTel tracing. Some applications may
        // chose to disable tracing in some publishers or to dynamically enable
        // this option based on their own configuration.
        gc::Options{}.set<gc::OpenTelemetryTracingOption>(true)));
    
    // After this point, use the Cloud Pub/Sub C++ client library as usual.
    // In this example, we will send a few messages and configure a callback
    // action for each one.
    std::vector<gc::future<void>> ids;
    for (int i = 0; i < 5; i++) {
      auto id = publisher.Publish(pubsub::MessageBuilder().SetData("Hi!").Build())
                    .then([](gc::future<gc::StatusOr<std::string>> f) {
                      auto id = f.get();
                      if (!id) {
                        std::cout << "Error in publish: " << id.status() << "\n";
                        return;
                      }
                      std::cout << "Sent message with id: (" << *id << ")\n";
                    });
      ids.push_back(std::move(id));
    }
    // Block until the messages are actually sent.
    for (auto& id : ids) id.get();

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"go.opentelemetry.io/otel"
    	"google.golang.org/api/option"
    
    	texporter "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace"
    	"go.opentelemetry.io/otel/sdk/resource"
    	sdktrace "go.opentelemetry.io/otel/sdk/trace"
    	semconv "go.opentelemetry.io/otel/semconv/v1.26.0"
    )
    
    // publishOpenTelemetryTracing publishes a single message with OpenTelemetry tracing
    // enabled, exporting to Cloud Trace.
    func publishOpenTelemetryTracing(w io.Writer, projectID, topicID string, sampling float64) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
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
    		semconv.ServiceNameKey.String("publisher"),
    	)
    
    	// Instantiate a tracer provider with the following settings
    	tp := sdktrace.NewTracerProvider(
    		sdktrace.WithBatcher(exporter),
    		sdktrace.WithResource(resources),
    		sdktrace.WithSampler(
    			sdktrace.ParentBased(sdktrace.TraceIDRatioBased(sampling)),
    		),
    	)
    
    	defer tp.ForceFlush(ctx) // flushes any pending spans
    	otel.SetTracerProvider(tp)
    
    	// Create a new client with tracing enabled.
    	client, err := pubsub.NewClientWithConfig(ctx, projectID, &pubsub.ClientConfig{
    		EnableOpenTelemetryTracing: true,
    	})
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
    		Data: []byte("Publishing message with tracing"),
    	})
    	if _, err := result.Get(ctx); err != nil {
    		return fmt.Errorf("pubsub: result.Get: %w", err)
    	}
    	fmt.Fprintln(w, "Published a traced message")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.opentelemetry.trace.TraceConfiguration;
    import com.google.cloud.opentelemetry.trace.TraceExporter;
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import io.opentelemetry.api.OpenTelemetry;
    import io.opentelemetry.sdk.OpenTelemetrySdk;
    import io.opentelemetry.sdk.resources.Resource;
    import io.opentelemetry.sdk.trace.SdkTracerProvider;
    import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;
    import io.opentelemetry.sdk.trace.export.SpanExporter;
    import io.opentelemetry.sdk.trace.samplers.Sampler;
    import io.opentelemetry.semconv.ResourceAttributes;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    
    public class OpenTelemetryPublisherExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        openTelemetryPublisherExample(projectId, topicId);
      }
    
      public static void openTelemetryPublisherExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
        Resource resource =
            Resource.getDefault().toBuilder()
                .put(ResourceAttributes.SERVICE_NAME, "publisher-example")
                .build();
    
        // Creates a Cloud Trace exporter.
        SpanExporter traceExporter =
            TraceExporter.createWithConfiguration(
                TraceConfiguration.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__)().setProjectId(projectId).build());
    
        SdkTracerProvider sdkTracerProvider =
            SdkTracerProvider.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__)()
                .setResource(resource)
                .addSpanProcessor(SimpleSpanProcessor.create(traceExporter))
                .setSampler(Sampler.alwaysOn())
                .build();
    
        OpenTelemetry openTelemetry =
            OpenTelemetrySdk.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__)().setTracerProvider(sdkTracerProvider).buildAndRegisterGlobal();
    
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
        try {
          // Create a publisher instance with the created OpenTelemetry object and enabling tracing.
          publisher =
              [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName)
                  .setOpenTelemetry(openTelemetry)
                  .setEnableOpenTelemetryTracing(true)
                  .build();
    
          String message = "Hello World!";
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
    
          // Once published, returns a server-assigned message id (unique within the topic)
          ApiFuture<String> messageIdFuture = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubMessage);
          String messageId = messageIdFuture.get();
          System.out.println("Published message ID: " + messageId);
        } finally {
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
