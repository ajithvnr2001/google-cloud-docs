---
url: https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing/
title: Pub/Sub OpenTelemetry tracing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:31.480829+00:00
---

# Pub/Sub OpenTelemetry tracing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Pub/Sub OpenTelemetry tracing Stay organized with collections  Save and categorize content based on your preferences. 

OpenTelemetry tracing lets you identify and trace the latency of various Pub/Sub client library operations, such as batching, lease management, and flow control. Collecting this information can help you debug client library issues.

Some potential use cases for OpenTelemetry tracing include the following:

  * Your service is experiencing a higher publishing latency than normal.
  * You are experiencing a high number of message redeliveries.
  * A change to your subscriber client's callback function causes processing to take longer than usual.



## Before you begin

Before configuring OpenTelemetry, complete the following tasks:

  * Set up Pub/Sub using one of the [client libraries](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-client-library).
  * Install the [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/) and set up a trace exporter and a tracer provider.
  * Enable the [Cloud Trace API](https://console.cloud.google.com/apis/enableflow?apiid=cloudtrace.googleapis.com).
  * Understand how to [read Cloud Observability traces](https://docs.cloud.google.com/trace/docs/finding-traces).



### Required roles

To ensure that the service account has the necessary permissions to export traces to Cloud Trace, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * All: [Cloud Trace Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export traces to Cloud Trace. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export traces to Cloud Trace:

  * All: `cloudtrace.traces.patch`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## OpenTelemetry tracing workflow

To set up OpenTelemetry tracing, you use the Pub/Sub client libraries and the OpenTelemetry SDK. With the SDK, you must set up a trace exporter and a tracer provider, before connecting to the Pub/Sub libraries. In some libraries, setting up a tracer provider is optional.

  * **Trace exporter.** The OpenTelemetry SDK uses the trace exporter to determine where to send traces.

  * **Tracer provider.** The Pub/Sub client libraries use the tracer provider to create traces.




The following steps outline how to set up tracing:

  1. Instantiate a Cloud Trace OpenTelemetry exporter.
  2. If required, instantiate and register a Tracer Provider using the OpenTelemetry SDK.
  3. Configure your client with the enable OpenTelemetry tracing option.
  4. Use the Pub/Sub client libraries to publish a message.



## How tracing works

For every message published, the client library creates a new trace. This trace represents the entire lifecycle of the message, from the moment you publish a message to when the message is acknowledged. A trace encapsulates information such as the duration of operations, parent spans and children spans, and linked spans.

A trace is made up of a _root span_ and its corresponding _child spans_. These spans represent the work the client library does when processing a message. Each message trace contains the following:

  * **For publishing**. Flow control, ordering key scheduling, batching, and the length of the publish RPC.
  * **For subscriptions**. Concurrency control, ordering key scheduling, and lease management.



In order to propagate information from the publish to subscribe side, the client libraries inject a tracing specific attribute on the publish side. The context propagation mechanism is only enabled when tracing is turned on and is prepended with the `googclient_` prefix.

### Publish Messages with tracing

The following code sample shows you how to enable tracing by using the Pub/Sub client library and the OpenTelemetry SDK. In this sample, the tracing results are exported to Cloud Trace.

**Note:** Cloud Trace only provides exporters for Java, Go, Node, and Python. To export with any other languages, use the [OpenTelemetry Collector with Google Cloud Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlecloudexporter/README.md). Setting up these processes requires additional setup steps not documented on this page.

### Considerations

When instantiating the tracer provider, you configure a sampling ratio with the OpenTelemetry SDK. This ratio determines how many traces the SDK should sample. A lower sampling rate can help reduce billing costs and prevent your service from exceeding the [Cloud Trace span quota](https://docs.cloud.google.com/trace/docs/quotas#daily-ingestion).

**Warning:** traces are subject to change. The name and attributes of a span might change without notice. Only use traces interactively. Don't use in automation. Running non-interactive traces can cause problems if the underlying trace architecture changes without notice.

### Go
    
    
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
    

### C++
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import (
        BatchSpanProcessor,
    )
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    from opentelemetry.sdk.trace.sampling import TraceIdRatioBased, ParentBased
    
    from google.cloud.pubsub_v1 import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)
    from google.cloud.pubsub_v1.types import [PublisherOptions](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PublisherOptions.html)
    
    # TODO(developer)
    # topic_project_id = "your-topic-project-id"
    # trace_project_id = "your-trace-project-id"
    # topic_id = "your-topic-id"
    
    # In this sample, we use a Google Cloud Trace to export the OpenTelemetry
    # traces: https://cloud.google.com/trace/docs/setup/python-ot
    # Choose and configure the exporter for your set up accordingly.
    
    sampler = ParentBased(root=TraceIdRatioBased(1))
    trace.set_tracer_provider(TracerProvider(sampler=sampler))
    
    # Export to Google Trace.
    cloud_trace_exporter = CloudTraceSpanExporter(
        project_id=trace_project_id,
    )
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(cloud_trace_exporter)
    )
    
    # Set the `enable_open_telemetry_tracing` option to True when creating
    # the publisher client. This in itself is necessary and sufficient for
    # the library to export OpenTelemetry traces. However, where the traces
    # must be exported to needs to be configured based on your OpenTelemetry
    # set up. Refer: https://opentelemetry.io/docs/languages/python/exporters/
    publisher = PublisherClient(
        publisher_options=PublisherOptions(
            enable_open_telemetry_tracing=True,
        ),
    )
    
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(topic_project_id, topic_id)
    # Publish messages.
    for n in range(1, 10):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data)
        print(future.result())
    
    print(f"Published messages to {topic_path}.")
    

### TypeScript
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_OR_ID';
    // const data = 'Hello, world!";
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Imports the OpenTelemetry API
    import {NodeTracerProvider} from '@opentelemetry/sdk-trace-node';
    import {diag, DiagConsoleLogger, DiagLogLevel} from '@opentelemetry/api';
    import {SimpleSpanProcessor} from '@opentelemetry/sdk-trace-base';
    
    // To output to the console for testing, use the ConsoleSpanExporter.
    // import {ConsoleSpanExporter} from '@opentelemetry/sdk-trace-base';
    
    // To output to Cloud Trace, import the OpenTelemetry bridge library.
    import {TraceExporter} from '@google-cloud/opentelemetry-cloud-trace-exporter';
    
    import {Resource} from '@opentelemetry/resources';
    import {SEMRESATTRS_SERVICE_NAME} from '@opentelemetry/semantic-conventions';
    
    // Enable the diagnostic logger for OpenTelemetry
    diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
    
    // Log spans out to the console, for testing.
    // const exporter = new ConsoleSpanExporter();
    
    // Log spans out to Cloud Trace, for production.
    const exporter = new TraceExporter();
    
    // Build a tracer provider and a span processor to do
    // something with the spans we're generating.
    const provider = new NodeTracerProvider({
      resource: new Resource({
        [SEMRESATTRS_SERVICE_NAME]: 'otel publisher example',
      }),
    });
    const processor = new SimpleSpanProcessor(exporter);
    provider.addSpanProcessor(processor);
    provider.register();
    
    // Creates a client; cache this for further use.
    const pubSubClient = new PubSub({enableOpenTelemetryTracing: true});
    
    async function publishMessage(topicNameOrId: string, data: string) {
      // Publishes the message as a string, e.g. "Hello, world!"
      // or JSON.stringify(someObject)
      const dataBuffer = Buffer.from(data);
    
      // Cache topic objects (publishers) and reuse them.
      const publisher = pubSubClient.topic(topicNameOrId);
    
      const messageId = await publisher.publishMessage({data: dataBuffer});
      console.log(`Message ${messageId} published.`);
    
      // The rest of the sample is in service to making sure that any
      // buffered Pub/Sub messages and/or OpenTelemetry spans are properly
      // flushed to the server side. In normal usage, you'd only need to do
      // something like this on process shutdown.
      await publisher.flush();
      await processor.forceFlush();
      await new Promise(r => setTimeout(r, OTEL_TIMEOUT * 1000));
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_OR_ID';
    // const data = 'Hello, world!";
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Imports the OpenTelemetry API
    const {NodeTracerProvider} = require('@opentelemetry/sdk-trace-node');
    const {diag, DiagConsoleLogger, DiagLogLevel} = require('@opentelemetry/api');
    const {SimpleSpanProcessor} = require('@opentelemetry/sdk-trace-base');
    
    // To output to the console for testing, use the ConsoleSpanExporter.
    // import {ConsoleSpanExporter} from '@opentelemetry/sdk-trace-base';
    
    // To output to Cloud Trace, import the OpenTelemetry bridge library.
    const {
      TraceExporter,
    } = require('@google-cloud/opentelemetry-cloud-trace-exporter');
    
    const {Resource} = require('@opentelemetry/resources');
    const {
      SEMRESATTRS_SERVICE_NAME,
    } = require('@opentelemetry/semantic-conventions');
    
    // Enable the diagnostic logger for OpenTelemetry
    diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
    
    // Log spans out to the console, for testing.
    // const exporter = new ConsoleSpanExporter();
    
    // Log spans out to Cloud Trace, for production.
    const exporter = new TraceExporter();
    
    // Build a tracer provider and a span processor to do
    // something with the spans we're generating.
    const provider = new NodeTracerProvider({
      resource: new Resource({
        [SEMRESATTRS_SERVICE_NAME]: 'otel publisher example',
      }),
    });
    const processor = new SimpleSpanProcessor(exporter);
    provider.addSpanProcessor(processor);
    provider.register();
    
    // Creates a client; cache this for further use.
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)({enableOpenTelemetryTracing: true});
    
    async function publishMessage(topicNameOrId, data) {
      // Publishes the message as a string, e.g. "Hello, world!"
      // or JSON.stringify(someObject)
      const dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(data);
    
      // Cache topic objects (publishers) and reuse them.
      const publisher = pubSubClient.topic(topicNameOrId);
    
      const messageId = await [publisher](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html).[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)({data: dataBuffer});
      console.log(`Message ${messageId} published.`);
    
      // The rest of the sample is in service to making sure that any
      // buffered Pub/Sub messages and/or OpenTelemetry spans are properly
      // flushed to the server side. In normal usage, you'd only need to do
      // something like this on process shutdown.
      await [publisher](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html).[flush](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)();
      await processor.forceFlush();
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)(r => setTimeout(r, OTEL_TIMEOUT * 1000));
    }

### Java
    
    
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

### Receive messages with tracing

### Go
    
    
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
    

### C++
    
    
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

### Python
    
    
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import (
        BatchSpanProcessor,
    )
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    from opentelemetry.sdk.trace.sampling import TraceIdRatioBased, ParentBased
    
    from google.cloud import pubsub_v1
    from google.cloud.pubsub_v1 import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    from google.cloud.pubsub_v1.types import SubscriberOptions
    
    # TODO(developer)
    # subscription_project_id = "your-subscription-project-id"
    # subscription_id = "your-subscription-id"
    # cloud_trace_project_id = "your-cloud-trace-project-id"
    # timeout = 300.0
    
    # In this sample, we use a Google Cloud Trace to export the OpenTelemetry
    # traces: https://cloud.google.com/trace/docs/setup/python-ot
    # Choose and configure the exporter for your set up accordingly.
    
    sampler = ParentBased(root=TraceIdRatioBased(1))
    trace.set_tracer_provider(TracerProvider(sampler=sampler))
    
    # Export to Google Trace
    cloud_trace_exporter = CloudTraceSpanExporter(
        project_id=cloud_trace_project_id,
    )
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(cloud_trace_exporter)
    )
    # Set the `enable_open_telemetry_tracing` option to True when creating
    # the subscriber client. This in itself is necessary and sufficient for
    # the library to export OpenTelemetry traces. However, where the traces
    # must be exported to needs to be configured based on your OpenTelemetry
    # set up. Refer: https://opentelemetry.io/docs/languages/python/exporters/
    subscriber = SubscriberClient(
        subscriber_options=SubscriberOptions(enable_open_telemetry_tracing=True)
    )
    
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_id}`
    subscription_path = subscriber.subscription_path(
        subscription_project_id, subscription_id
    )
    
    # Define callback to be called when a message is received.
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        # Ack message after processing it.
        print(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # Optimistically subscribe to messages on the subscription.
            streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(
                subscription_path, callback=callback
            )
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            print("Successfully subscribed until the timeout passed.")
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.
    

### TypeScript
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_OR_ID';
    
    // Imports the Google Cloud client library
    import {Message, PubSub} from '@google-cloud/pubsub';
    
    // Imports the OpenTelemetry API
    import {NodeTracerProvider} from '@opentelemetry/sdk-trace-node';
    import {diag, DiagConsoleLogger, DiagLogLevel} from '@opentelemetry/api';
    import {SimpleSpanProcessor} from '@opentelemetry/sdk-trace-base';
    
    // To output to the console for testing, use the ConsoleSpanExporter.
    // import {ConsoleSpanExporter} from '@opentelemetry/sdk-trace-base';
    
    // To output to Cloud Trace, import the OpenTelemetry bridge library.
    import {TraceExporter} from '@google-cloud/opentelemetry-cloud-trace-exporter';
    
    import {Resource} from '@opentelemetry/resources';
    import {SEMRESATTRS_SERVICE_NAME} from '@opentelemetry/semantic-conventions';
    
    // Enable the diagnostic logger for OpenTelemetry
    diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
    
    // Log spans out to the console, for testing.
    // const exporter = new ConsoleSpanExporter();
    
    // Log spans out to Cloud Trace, for production.
    const exporter = new TraceExporter();
    
    // Build a tracer provider and a span processor to do
    // something with the spans we're generating.
    const provider = new NodeTracerProvider({
      resource: new Resource({
        [SEMRESATTRS_SERVICE_NAME]: 'otel subscriber example',
      }),
    });
    const processor = new SimpleSpanProcessor(exporter);
    provider.addSpanProcessor(processor);
    provider.register();
    
    // Creates a client; cache this for further use.
    const pubSubClient = new PubSub({enableOpenTelemetryTracing: true});
    
    async function subscriptionListen(subscriptionNameOrId: string) {
      const subscriber = pubSubClient.subscription(subscriptionNameOrId);
    
      // Message handler for subscriber
      const messageHandler = async (message: Message) => {
        console.log(`Message ${message.id} received.`);
        message.ack();
      };
    
      // Error handler for subscriber
      const errorHandler = async (error: Error) => {
        console.log('Received error:', error);
      };
    
      // Listens for new messages from the topic
      subscriber.on('message', messageHandler);
      subscriber.on('error', errorHandler);
    
      // Ensures that all spans got flushed by the exporter. This function
      // is in service to making sure that any buffered Pub/Sub messages
      // and/or OpenTelemetry spans are properly flushed to the server
      // side. In normal usage, you'd only need to do something like this
      // on process shutdown.
      async function shutdown() {
        await subscriber.close();
        await processor.forceFlush();
        await new Promise(r => setTimeout(r, OTEL_TIMEOUT * 1000));
      }
    
      // Wait a bit for the subscription to receive messages, then shut down
      // gracefully. This is for the sample only; normally you would not need
      // this delay.
      await new Promise<void>(r =>
        setTimeout(async () => {
          subscriber.removeAllListeners();
          await shutdown();
          r();
        }, SUBSCRIBER_TIMEOUT * 1000),
      );
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Imports the OpenTelemetry API
    const {NodeTracerProvider} = require('@opentelemetry/sdk-trace-node');
    const {diag, DiagConsoleLogger, DiagLogLevel} = require('@opentelemetry/api');
    const {SimpleSpanProcessor} = require('@opentelemetry/sdk-trace-base');
    
    // To output to the console for testing, use the ConsoleSpanExporter.
    // import {ConsoleSpanExporter} from '@opentelemetry/sdk-trace-base';
    
    // To output to Cloud Trace, import the OpenTelemetry bridge library.
    const {
      TraceExporter,
    } = require('@google-cloud/opentelemetry-cloud-trace-exporter');
    
    const {Resource} = require('@opentelemetry/resources');
    const {
      SEMRESATTRS_SERVICE_NAME,
    } = require('@opentelemetry/semantic-conventions');
    
    // Enable the diagnostic logger for OpenTelemetry
    diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
    
    // Log spans out to the console, for testing.
    // const exporter = new ConsoleSpanExporter();
    
    // Log spans out to Cloud Trace, for production.
    const exporter = new TraceExporter();
    
    // Build a tracer provider and a span processor to do
    // something with the spans we're generating.
    const provider = new NodeTracerProvider({
      resource: new Resource({
        [SEMRESATTRS_SERVICE_NAME]: 'otel subscriber example',
      }),
    });
    const processor = new SimpleSpanProcessor(exporter);
    provider.addSpanProcessor(processor);
    provider.register();
    
    // Creates a client; cache this for further use.
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)({enableOpenTelemetryTracing: true});
    
    async function subscriptionListen(subscriptionNameOrId) {
      const subscriber = pubSubClient.subscription(subscriptionNameOrId);
    
      // Message handler for subscriber
      const messageHandler = async message => {
        console.log(`Message ${message.id} received.`);
        message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
      };
    
      // Error handler for subscriber
      const errorHandler = async error => {
        console.log('Received error:', error);
      };
    
      // Listens for new messages from the topic
      subscriber.[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
      subscriber.[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', errorHandler);
    
      // Ensures that all spans got flushed by the exporter. This function
      // is in service to making sure that any buffered Pub/Sub messages
      // and/or OpenTelemetry spans are properly flushed to the server
      // side. In normal usage, you'd only need to do something like this
      // on process shutdown.
      async function shutdown() {
        await subscriber.close();
        await processor.forceFlush();
        await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)(r => setTimeout(r, OTEL_TIMEOUT * 1000));
      }
    
      // Wait a bit for the subscription to receive messages, then shut down
      // gracefully. This is for the sample only; normally you would not need
      // this delay.
      await new [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)(r =>
        setTimeout(async () => {
          subscriber.removeAllListeners();
          await shutdown();
          r();
        }, SUBSCRIBER_TIMEOUT * 1000),
      );
    }

### Java
    
    
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

## Analyze a trace

The following sections contain detailed information about how to track and analyze a trace in the Google Cloud console.

### Considerations

  * When publishing a batch of messages, the publish RPC span is captured in a separate trace.
  * A publish RPC has multiple origin spans, since multiple create calls can result in a publish RPC when they are batched together.
  * Spans in OpenTelemetry can have zero or one parent spans.

Spans representing batched operations, such a _publish batch_ , (which logically should have multiple _parents_) can't be represented using zero or one parent spans.




### Track spans created during the message lifecycle

The following image shows an example of spans that are created in a single trace for a single message.

![View spans in tracing](https://docs.cloud.google.com/static/pubsub/images/pubsub-open-telemetry-tracing-overview.png)

Each span can have additional attributes. Span attributes convey additional metadata such as the message's ordering key, the message ID, and the size of the message.

![View spans in tracing](https://docs.cloud.google.com/static/pubsub/images/pubsub-open-telemetry-spans.png)

The main publish and subscribe spans are augmented with span events which correspond to when a network call is issued and when it is completed.

![View spans in tracing](https://docs.cloud.google.com/static/pubsub/images/pubsub-open-telemetry-span-events.png)

## Troubleshoot common issues

The following issues can cause problems with tracing:

  * The service account that you use for exporting traces doesn't have the required `roles/cloudtrace.agent` role.
  * The quota of the maximum number of ingested spans in Cloud Trace has been reached.
  * Your application is terminated without calling the appropriate flush function.



## What's next

  * [Best practices for subscriptions](https://docs.cloud.google.com/pubsub/docs/subscribe-best-practices)
  * [Best practices for publishing](https://docs.cloud.google.com/pubsub/docs/publish-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
