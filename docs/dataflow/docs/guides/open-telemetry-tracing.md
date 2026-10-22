---
url: https://docs.cloud.google.com/dataflow/docs/guides/open-telemetry-tracing/
title: Use OpenTelemetry distributed tracing in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:15.035248+00:00
---

# Use OpenTelemetry distributed tracing in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/open-telemetry-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use OpenTelemetry distributed tracing in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

In distributed streaming pipelines, it can be difficult for you to identify which specific stage, external service call, or worker shuffle causes latency spikes using aggregated metrics alone. By using OpenTelemetry distributed tracing in Dataflow, you can track individual elements end-to-end across pipeline transforms, network boundaries, and integrated services under a single Trace ID. This visibility helps you pinpoint performance bottlenecks, optimize pipeline execution costs, and troubleshoot complex streaming workloads.

Use the following information to enable, configure, and use OpenTelemetry distributed tracing in your Apache Beam pipelines.

## Use cases

Distributed tracing in Dataflow is particularly useful in the following scenarios:

  * **Streaming workloads:** Track per-element processing time and identify stages that introduce lag or latency spikes.
  * **External service call tracing in user code:** Measure execution durations when your pipeline calls external databases, microservices, or generative AI APIs inside user code (such as in a `DoFn`). For example, you can measure the time for calls to external databases (such as Spanner or Bigtable), microservices (using HTTP or gRPC), or generative AI APIs (such as Gemini). For more information, see Write custom traces in DoFns and Integrate with client libraries.
  * **Cost and performance optimization:** Expose durations of specific operations in `PTransform` instances under real-world load to identify inefficient serialization, slow queries, or worker thread contention.
  * **Complex agentic and workflow pipelines:** Gain visibility into pipelines with multiple branches, iterative agent loops, and joins to determine which transform or branch takes the longest.



## Limitations

Distributed tracing in Dataflow has the following limitations:

  * This feature is designed and verified for streaming pipelines only.
  * To use this feature, you must use the Beam SDK for Java (version 2.76.0 or greater).
  * Cross-stage context propagation requires the Streaming Java Runner (previously called _Runner v1_). The Portable Runner (previously called _Runner v2_) resets trace context at shuffle boundaries.
  * Built-in OpenTelemetry tracing in Beam I/O connectors is supported for the following connectors only: Pub/Sub, Apache Kafka, and Spanner change streams. For Apache Kafka, tracing is supported only when you use the `KafkaIO` connector directly. It isn't supported when you use [Managed I/O for Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka). Other I/O connectors (such as `BigtableIO`) don't have built-in connector tracing; to trace operations with these services, instrument your calls inside user code (such as in a `DoFn`).
  * Operations that combine multiple elements into one don't propagate a single trace context. This includes operations like `GroupByKey`, `CoGroupByKey`, and `Combine`.
  * Context isn't propagated between setting a timer (`Timer.set()`) and the execution of the `@OnTimer` callback method.



## Prerequisites

To use distributed tracing in Dataflow, ensure that your environment meets the following requirements:

  1. Your job must meet the following requirements: 
     * Is a streaming pipeline
     * Uses the [Streaming Java Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner) (previously called _Runner v1_)
     * Uses the [Apache Beam Java SDK](https://beam.apache.org/documentation/sdks/java/) version 2.76.0 or greater
  2. If you export traces to Cloud Trace, enable the Telemetry API ( `telemetry.googleapis.com`) in your Google Cloud project.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com)

  3. The [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) must have the Cloud Trace Agent (`roles/cloudtrace.agent`) role, which includes the `cloudtrace.traces.patch` permission.




## Core concepts

Distributed tracing relies on the following [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/):

Trace
    A representation of a complete transaction or workflow as it flows through a distributed system. A _trace_ consists of one or more _spans_.
Span
    The basic building block of a _trace_ , representing a single unit of work. For example, a transform execution, method call, or RPC request.
Context
    The state that is propagated across threads and API boundaries. This includes the Trace ID and Span ID.
Propagator
    The mechanism used to inject and extract context representation across network boundaries. For example, W3C Trace Context.
Exporter
    A component that sends collected _span_ data to a tracing backend, such as [Cloud Trace](https://docs.cloud.google.com/trace/docs) or a self-hosted [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/).
Sampler
    A mechanism that controls _trace_ volume by determining which traces are recorded and exported. For example, a 1% sampling rate.

## Enable OpenTelemetry tracing

To enable OpenTelemetry tracing with default settings, configure the required pipeline options and experiments when you submit your job. The default setting exports to Cloud Trace with 1% sampling.

To modify default values, see Set and modify tracing properties.

  1. Configure pipeline options and experiments when you run your job.

### Non-flex template job

Pass the following experiment flags when you submit a job:
         
         --experiments=enable_otel_defaults,element_metadata_supported,disable_portable_worker
         

### Flex template job

Pass the experiments by using the `--additional-experiments` flag in the `gcloud` command:
         
         gcloud dataflow flex-template run JOB_NAME \
             --template-file-gcs-location=gs://BUCKET_NAME/templates/TEMPLATE_NAME.json \**--additional-experiments="enable_otel_defaults,element_metadata_supported,disable_portable_worker" \**
             --region=REGION
         

Replace the following:

     * JOB_NAME: The name of your Dataflow job.
     * BUCKET_NAME: The Cloud Storage bucket containing your template.
     * TEMPLATE_NAME: The name of your Flex Template file.
     * REGION: The Google Cloud region where you want to run the job.

These experiments configure the following behaviors:

     * `enable_otel_defaults`: Configures standard OpenTelemetry defaults, including the Cloud Trace exporter and 1% sampling.
     * `element_metadata_supported`: Enables serialization and propagation of metadata (such as trace context) across pipeline stages.
     * `disable_portable_worker`: Forces the use of the Dataflow Streaming Java Runner (previously called Runner v1).
  2. If you use Beam SDK for Java versions 2.76.0 or 2.77.0, add required OpenTelemetry dependencies to your build configuration.

Due to an issue in versions 2.76.0 and 2.77.0, you must add the following dependencies to your `pom.xml` file for traces to be exported. For more information, see [Manage pipeline dependencies](https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies#java-management).
         
         <dependency>
             <groupId>io.opentelemetry</groupId>
             <artifactId>opentelemetry-sdk-extension-autoconfigure</artifactId>
             <scope>compile</scope>
         </dependency>
         
         <dependency>
             <groupId>io.opentelemetry</groupId>
             <artifactId>opentelemetry-exporter-otlp</artifactId>
             <version>1.62.0</version>
             <scope>compile</scope>
         </dependency>
         
         <dependency>
             <groupId>org.apache.beam</groupId>
             <artifactId>beam-sdks-java-extensions-opentelemetry-gcp-auth-extension</artifactId>
             <scope>compile</scope>
         </dependency>
         

  3. Explicitly enable OpenTelemetry tracing on supported I/O connectors in your pipeline code:

### Pub/Sub

To enable tracing when reading from or writing to Pub/Sub:
         
         // Reading from Pub/Sub
         pipeline.apply("ReadFromPubSub",
             PubsubIO.readMessages()
                 .withEnableOpenTelemetryTracing()
                 .fromSubscription("projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID"));
         
         // Writing to Pub/Sub
         pipeline.apply("WriteToPubSub",
             PubsubIO.writeStrings()
                 .withEnableOpenTelemetryTracing()
                 .to("projects/PROJECT_ID/topics/TOPIC_ID"));

Replace the following:

     * PROJECT_ID: The ID of your Google Cloud project.
     * SUBSCRIPTION_ID: The name of your Pub/Sub subscription.
     * TOPIC_ID: The name of your Pub/Sub topic.

Context propagation details:

     * **Upstream publisher:** When publishing messages from an external application, inject the W3C Trace Context into the Pub/Sub message attributes. For more information, see [Pub/Sub OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing).
     * **Attributes:** Beam expects and populates the following attributes: 
       * `googclient_traceparent`: Carries the W3C `traceparent` header.
       * `googclient_tracestate`: Carries the W3C `tracestate` header.
     * For header formatting, see the [W3C Trace Context specification](https://www.w3.org/TR/trace-context/). 

### Apache Kafka

**Note:** Tracing for Kafka is supported only when you use the `KafkaIO` connector directly. It isn't supported when you use [Managed I/O for Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka). 

To enable tracing when reading from or writing to Apache Kafka:
    
    // Reading from Kafka
    pipeline.apply("ReadFromKafka",
        KafkaIO.<String, String>read()
            .withEnableOpenTelemetryTracing()
            // ... additional configuration
            );
    
    // Writing to Kafka
    pipeline.apply("WriteToKafka",
        KafkaIO.<String, String>write()
            .withEnableOpenTelemetryTracing()
            // ... additional configuration
            );

Context propagation details:

     * `KafkaIO` uses standard Kafka record headers to propagate context.
     * It expects and injects headers complying with the [W3C Trace Context specification](https://www.w3.org/TR/trace-context/): 
       * `traceparent`: Identifies the incoming trace context.
       * `tracestate`: Provides additional vendor-specific routing and filtering metadata.

### Spanner

To enable tracing when reading from Spanner change streams:
    
    pipeline.apply("ReadChangeStream",
        SpannerIO.readChangeStream()
            .withSpannerConfig(spannerConfig)
            .withEnableOpenTelemetryTracing(true)
            .withChangeStreamName("CHANGE_STREAM_NAME"));

Replace the following:

     * CHANGE_STREAM_NAME: The name of the Spanner change stream.

Span creation details:

     * Enabling tracing starts a new trace and span for every database mutation record read by the Change Data Capture (CDC) reader.
     * Spanner reader poll cycles that return no new records might also produce trace spans that can be filtered out in the Cloud Trace UI.




## Set and modify tracing properties

When you specify `enable_otel_defaults`, Dataflow applies the following default properties:

Property | Default value | Description  
---|---|---  
`otel.traces.exporter` | `otlp` | Exports traces using the OpenTelemetry Protocol (OTLP).  
`otel.exporter.otlp.endpoint` | `https://telemetry.googleapis.com` | Targets the Cloud Trace OTLP receiver.  
`google.cloud.project` | _Your project ID_ | The Google Cloud project where traces are stored.  
`otel.traces.sampler.arg` | `0.01` (1%) | Records 1 out of every 100 traces.  
`otel.service.name` | `options.getAppName()` | The service name associated with the spans, derived from the pipeline `appName` option.  
  
To customize OpenTelemetry configuration, pass a semicolon-separated list of properties to the `--openTelemetryProperties` pipeline option.

The following example configures all default properties explicitly:
    
    
    --openTelemetryProperties="otel.traces.exporter=otlp;otel.exporter.otlp.endpoint=https://telemetry.googleapis.com;google.cloud.project=PROJECT_ID;otel.traces.sampler.arg=0.01;otel.service.name=CUSTOM_SERVICE_NAME;otel.java.global-autoconfigure.enabled=true"
    

### Set a custom service name

By default, the trace service name is derived from the pipeline `appName` option (`--appName=YourPipelineName`). You can override this value by setting the `otel.service.name` property:
    
    
    --openTelemetryProperties="otel.service.name=CUSTOM_SERVICE_NAME"
    

### Change sampling rate and properties

Setting a higher sampling rate gives you more robust tracing information. However, high sample rates (such as `1.0` or `always_on`) significantly increase the volume of trace data sent to Cloud Trace, which can increase your Google Cloud costs. Use high sample rates only for short-term debugging and reduce them for production workloads.

The following example configures the sampling rate explicitly. In this case you must provide a complete list of arguments:
    
    
    --openTelemetryProperties="otel.traces.exporter=otlp;otel.exporter.otlp.endpoint=https://telemetry.googleapis.com;google.cloud.project=PROJECT_ID;**otel.traces.sampler.arg= 0.02;**otel.service.name=CUSTOM_SERVICE_NAME;otel.java.global-autoconfigure.enabled=true"
    

### Export to third-party backends

To send traces to an external managed tracing backend or a self-hosted OpenTelemetry Collector instead of Cloud Trace:

  1. Omit the following experiment: `--experiments=**enable_otel_defaults**`.
  2. Configure exporter properties manually using `--openTelemetryProperties`:
         
         --openTelemetryProperties="otel.traces.exporter=otlp;otel.exporter.otlp.endpoint=http://COLLECTOR_HOST:4317;otel.traces.sampler=parentbased_always_on"
         




### Google Cloud authentication extension

The Beam runtime includes a Google Cloud authentication extension that automatically authenticates OpenTelemetry Protocol (OTLP) requests sent to Google APIs such as `telemetry.googleapis.com`.

  * **When using defaults:** Google Cloud authentication is enabled automatically.
  * **When exporting to non-Google endpoints:** If `enable_otel_defaults` is omitted, Beam disables the Google Cloud authentication extension by setting the system property `google.otel.auth.target.signals=none`.
  * **Manual configuration:** You can set the `google.otel.auth.target.signals` system property to `none` (disabled) or `trace` (enabled for traces only).



## Write custom traces in DoFns

You can create custom spans inside user code, such as inside a `DoFn`, to measure specific operations. This includes calls to external APIs or compute-intensive logic.

### Example DoFn implementation
    
    
    import io.opentelemetry.api.trace.Span;
    import io.opentelemetry.api.trace.StatusCode;
    import io.opentelemetry.api.trace.Tracer;
    import io.opentelemetry.context.Scope;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.SdkHarnessOptions;
    import org.apache.beam.sdk.transforms.DoFn;
    
    public class InvestigateTransactionDoFn extends DoFn<Transaction, RiskAssessment> {
      private transient Tracer tracer;
    
      @Setup
      public void setup(PipelineOptions options) {
        // Obtain the Tracer instance from SdkHarnessOptions
        this.tracer = options
            .as(SdkHarnessOptions.class)
            .getOpenTelemetry()
            .getTracer("org.apache.beam.examples.adk.aml");
      }
    
      @ProcessElement
      public void processElement(@Element Transaction tx, OutputReceiver<RiskAssessment> out) {
        // Create and start a custom span as a child of the active context
        Span span = tracer.spanBuilder("InvestigateTransactionDoFn:Analyze")
            .setAttribute("transaction.id", tx.getId())
            .setAttribute("transaction.amount", tx.getAmount())
            .startSpan();
    
        // Make the span current in the execution thread
        try (Scope scope = span.makeCurrent()) {
          // Perform your logic (such as calling an external service)
          RiskAssessment assessment = analyzeTransactionWithLLM(tx);
          out.output(assessment);
        } catch (Exception e) {
          // Record exception details and set error status on the span
          span.recordException(e);
          span.setStatus(StatusCode.ERROR, e.getMessage());
          throw e;
        } finally {
          // Always end the span
          span.end();
        }
      }
    
      private RiskAssessment analyzeTransactionWithLLM(Transaction tx) {
        // Application analysis logic
        return new RiskAssessment();
      }
    }
    

## Integrate with client libraries

When a `DoFn` invokes external libraries that also support OpenTelemetry, such as Google Cloud client libraries, configure the client to use the pipeline's OpenTelemetry instance so that child spans link directly to the pipeline trace.

### Example Spanner Java client

To execute manual Spanner queries inside a `DoFn` and link those spans to the active pipeline trace, initialize `SpannerOptions` with the pipeline's OpenTelemetry instance:
    
    
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html);
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).PipelineOptions;
    import org.apache.beam.sdk.[options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).SdkHarnessOptions;
    import org.apache.beam.sdk.transforms.DoFn;
    
    public class SpannerEnrichmentDoFn extends DoFn<String, String> {
      private transient [Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner;
      private transient [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) dbClient;
      private final String instanceId;
      private final String databaseId;
    
      public SpannerEnrichmentDoFn(String instanceId, String databaseId) {
        this.instanceId = instanceId;
        this.databaseId = databaseId;
      }
    
      @Setup
      public void setup(PipelineOptions pipelineOptions) {
        // Build SpannerOptions leveraging the pipeline's active OpenTelemetry instance
        [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html) options =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder()
                .setOpenTelemetry(pipelineOptions
                    .as(SdkHarnessOptions.class)
                    .getOpenTelemetry())
                .[setEnableEndToEndTracing](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.Builder.html#com_google_cloud_spanner_SpannerOptions_Builder_setEnableEndToEndTracing_boolean_)(true)
                .[setEnableExtendedTracing](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.Builder.html#com_google_cloud_spanner_SpannerOptions_Builder_setEnableExtendedTracing_boolean_)(true)
                .build();
    
        this.spanner = [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getService();
        [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html) db = [DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of([options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).[getProjectId](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.connection.ConnectionOptions.html#com_google_cloud_spanner_connection_ConnectionOptions_getProjectId__)(), instanceId, databaseId);
        this.dbClient = spanner.[getDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_getDatabaseClient_com_google_cloud_spanner_DatabaseId_)(db);
      }
    
      @ProcessElement
      public void processElement(@Element String inputId, OutputReceiver<String> out) {
        [Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html) statement = [Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html).newBuilder(
            "SELECT Details FROM AccountTable WHERE AccountId = @id")
            .bind("id").[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)(inputId)
            .build();
    
        // Spanner queries automatically generate child spans linked to the active trace
        try ([ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html) rs = dbClient.[singleUse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_singleUse__)().executeQuery(statement)) {
          while (rs.next()) {
            out.output(rs.getString("Details"));
          }
        }
      }
    
      @Teardown
      public void tearDown() {
        if (spanner != null) {
          spanner.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_close__)();
        }
      }
    }
    

## Context propagation across stages

In distributed data pipelines, carrying trace context across worker boundaries and shuffle operations is essential for end-to-end visibility.

When you insert `Redistribute.arbitrarily()` into your pipeline, active trace context is serialized into element metadata, transmitted across the network, and deserialized on the receiving worker VM. This ensures unbroken trace continuation across stages.

The following example illustrates how trace context propagates across pipeline stages:

  1. **Extract context:** `KafkaIO.read()` reads an incoming record and extracts the trace context from the message headers.
  2. **Process and create spans:** `DoFn A` processes the element within an active trace span.
  3. **Propagate across workers:** `Redistribute.arbitrarily()` serializes the active trace context into the element metadata and shuffles the element across the network.
  4. **Continue the trace:** `DoFn B` receives the element on a worker VM, deserializes the trace context, and continues processing under the same Trace ID.



## View traces in Cloud Trace

After you enable tracing, view pipeline traces in the Google Cloud console:

  1. In the Google Cloud console, go to the **Trace explorer** page.

[Go to Trace explorer](https://console.cloud.google.com/traces/explorer)

  2. In the filter box, filter by `Service: SERVICE_NAME`. This SERVICE_NAME matches your pipeline `appName` or configured `otel.service.name`.

Alternatively, search for a specific **Trace ID**.

  3. Select a trace from the results list to view its detailed timeline.

The timeline graph displays:

     * **Runner spans:** Spans generated by the Beam runtime. For example, `PubSubIO.Read` and `ProcessElement`.
     * **Custom spans:** Spans created inside your `DoFn` implementations. For example, `InvestigateTransactionDoFn:Analyze`.
     * **Client library spans:** Child spans generated by integrated client libraries. For example, Spanner RPC queries.

![View of traces in the console.](https://docs.cloud.google.com/static/dataflow/images/view-opentelemetry-traces_console.png)




## What's next

  * Learn more about exploring and analyzing distributed traces in the [Cloud Trace documentation](https://docs.cloud.google.com/trace/docs).
  * Trace messages from ingestion to processing by using [Pub/Sub OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing).
  * Monitor your pipeline throughput, CPU utilization, and execution details with the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).
  * View operational logs and diagnose errors by using [Dataflow pipeline logs](https://docs.cloud.google.com/dataflow/docs/guides/logging).
  * Investigate and resolve performance issues with [Troubleshoot slow or stuck jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-jobs) and [Detect and resolve pipeline bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
