---
url: https://docs.cloud.google.com/storage/docs/traces/
title: Use client-side traces \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:27.767455+00:00
---

# Use client-side traces  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/traces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use client-side traces Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable client-side traces with [OpenTelemetry](https://opentelemetry.io/) when you use the Cloud Storage client libraries to interact with Cloud Storage. You can collect and view trace data using the following supported Cloud Storage client libraries:

  * [The C++ client library](https://docs.cloud.google.com/storage/docs/reference/libraries#client-libraries-install-cpp)

  * [The Python client library](https://docs.cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python)

  * [The Java client library](https://docs.cloud.google.com/storage/docs/reference/libraries#client-libraries-install-java)




## Overview

Enabling traces in the Cloud Storage client libraries lets you monitor performance, pinpoint latency issues, and quickly perform debugging for Cloud Storage requests. Traces let you see the sequence of a completed request, providing a detailed view of how the request was received, managed, and responded to by Cloud Storage. A single trace is composed of multiple _spans_ , which are detailed, time-stamped records of each function or operation your application performed throughout the Cloud Storage request.

## Benefits

Collecting and propagating trace data provides the following benefits to your application:

  * **Enhanced performance visibility** : because trace data is generated in near real-time as Cloud Storage completes each request you make, you can quickly identify bottlenecks in performance and detect latency issues.

  * **Error handling** : you can pinpoint where issues arise, speeding up root cause analysis and reducing downtime using the information about each Cloud Storage request that's provided in a trace.




## How client-side traces work

The following sections provide a detailed look at how trace collection works.

### How trace collection works with OpenTelemetry

The Cloud Storage client libraries supports trace data collection using the [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/) to set up the following components required to collect and propagate trace data:

  * [**Trace provider**](https://opentelemetry.io/docs/concepts/signals/traces/#tracer-provider): used by the Cloud Storage client libraries, the trace provider is responsible for creating and managing the tracing system, including generating and managing traces and spans in your application.

  * [**Trace exporter**](https://opentelemetry.io/docs/concepts/signals/traces/#trace-exporters): used by the OpenTelemetry SDK, the trace exporter is responsible for sending trace data to a backend observability platform such as [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview), where you can analyze and visualize trace data. To learn more about the trace exporter, see How trace exporters work.




### How trace exporters work

Configuring traces using the OpenTelemetry SDK includes selecting an observability backend to export your data to where it is analyzed, stored, and visualized. While you can export your trace data to any observability backend of your choice, we recommend using [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview), which can be accessed using the Google Cloud console and provides integration with other Google Cloud services.

Once the trace provider and the trace exporter are configured and enabled, you can view trace data in near real-time as traces and spans are generated for each Cloud Storage request.

Using the Cloud Trace explorer in the Google Cloud console, you can view each trace which contains the following:

  * A high-level view of a Cloud Storage request from end to end.

  * Multiple spans, each span capturing a time-stamped single operation within the Cloud Storage request that was performed.




To read more about traces and spans, see the [OpenTelemetry documentation about traces and spans](https://opentelemetry.io/docs/concepts/signals/traces/).

## Pricing

Trace data is chargeable. Charges are based on the number of trace spans ingested and scanned by Cloud Trace. To learn more about chargeable trace spans and pricing examples, see [Cloud Trace costs](https://docs.cloud.google.com/trace/pricing#trace-costs).

## Before you begin

Before you can collect traces for your Cloud Storage API usage, you must complete the following steps:

  1. [Install the Cloud Storage client library](https://docs.cloud.google.com/storage/docs/reference/libraries#install).

  2. [Set up authentication](https://docs.cloud.google.com/storage/docs/reference/libraries#authentication).

  3. Enable the Cloud Trace API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudtrace.googleapis.com)

  4. Enable the Cloud Storage API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com&_ga=2.70110096.1642044780.1726157710-823539626.1726157710)




### Required roles

To get the permission that you need to write traces to Cloud Trace, ask your administrator to grant you the [Cloud Trace Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) IAM role on the project used by the client. 

This predefined role contains the `cloudtrace.traces.patch` permission, which is required to write traces to Cloud Trace. 

You might also be able to get these permissions with [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview), or you can create [custom roles](https://docs.cloud.google.com/trace/docs/iam#create_custom_roles) to grant specific permissions. For instructions on granting roles on projects, see [Grant or revoke a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role). For more information about the Cloud Trace Agent role, see [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent).

## Configure tracing for your application

Use the following instructions to configure tracing and begin collecting trace data using the Cloud Storage client library:

### C++

  1. Install the following versions:

     * C++ client library version v2.16.0 or later

     * C++ version 14 or later

  2. To enable OpenTelemetry tracing instrumentation in the C++ client library, update your [build system configuration](https://github.com/googleapis/google-cloud-cpp/blob/main/google/cloud/opentelemetry/quickstart/README.md) for CMake or Bazel.

  3. Create an instance of the Cloud Storage client with OpenTelemetry traces enabled. 
         
         #include "google/cloud/opentelemetry/configure_basic_tracing.h"
         #include "google/cloud/storage/client.h"
         #include "google/cloud/opentelemetry_options.h"
         #include <iostream>
         
         int main(int argc, char* argv[]) {
           if (argc != 3) {
             std::cerr << "Usage: " << argv[0] << " <bucket-name> <project-id>\n";
             return 1;
           }
           std::string const bucket_name = argv[1];
           std::string const project_id = argv[2];
         
           // Create aliases to make the code easier to read.
           namespace gc = ::google::cloud;
           namespace gcs = ::google::cloud::storage;
         
           // Instantiate a basic tracing configuration which exports traces to Cloud
           // Trace. By default, spans are sent in batches and always sampled.
           auto project = gc::Project(project_id);
           auto configuration = gc::otel::ConfigureBasicTracing(project);
         
           // Create a client with OpenTelemetry tracing enabled.
           auto options = gc::Options{}.set<gc::OpenTelemetryTracingOption>(true);
           auto client = gcs::Client(options);
         
           auto writer = client.WriteObject(bucket_name, "quickstart.txt");
           writer << "Hello World!";
           writer.Close();
           if (!writer.metadata()) {
             std::cerr << "Error creating object: " << writer.metadata().status()
                       << "\n";
             return 1;
           }
           std::cout << "Successfully created object: " << *writer.metadata() << "\n";
         
           auto reader = client.ReadObject(bucket_name, "quickstart.txt");
           if (!reader) {
             std::cerr << "Error reading object: " << reader.status() << "\n";
             return 1;
           }
         
           std::string contents{std::istreambuf_iterator<char>{reader}, {}};
           std::cout << contents << "\n";
         
           // The basic tracing configuration object goes out of scope. The collected
           // spans are flushed to Cloud Trace.
         
           return 0;
         }




### Java

  1. Install the following [Cloud Storage Java client library](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview#getting-started) versions:

     * `com.google.cloud:google-cloud-storage:2.47.0` or later

     * `com.google.cloud:libraries-bom:26.53.0` or later

  2. Install the [Cloud Trace exporter for OpenTelemetry](https://github.com/GoogleCloudPlatform/opentelemetry-operations-java/blob/main/exporters/trace/README.md). You can also use any exporter of your choice.

  3. Install the [Cloud Trace propagator](https://github.com/GoogleCloudPlatform/opentelemetry-operations-java/tree/main/propagators/gcp/README.md).

  4. Create an instance of the Cloud Storage client with OpenTelemetry traces enabled.
         
         public class QuickstartOpenTelemetrySample {
           public static void main(String... args) throws Exception {
             SpanExporter spanExporter = TraceExporter.createWithDefaultConfiguration();
             TextMapPropagator propagators =
                 TextMapPropagator.composite(
                     W3CTraceContextPropagator.getInstance(),
                     new XCloudTraceContextPropagator(/* oneway= */ true));
         
             OpenTelemetrySdk openTelemetry =
                 OpenTelemetrySdk.builder()
                     .setPropagators(ContextPropagators.create(propagators))
                     .setTracerProvider(
                         SdkTracerProvider.builder()
                             // Sample Rate is set to alwaysOn
                             // It is recommended to sample based on a ratio for standard use ie.
                             // .setSampler(Sampler.traceIdRatioBased(0.2)) // sample only 20% of trace ids
                             .setSampler(Sampler.alwaysOn())
                             .addSpanProcessor(BatchSpanProcessor.builder(spanExporter).build())
                             .build())
                     .build();
             StorageOptions options = StorageOptions.newBuilder().setOpenTelemetry(openTelemetry).build();
             Storage storage = options.getService();
             System.out.println("Created an instance of storage with OpenTelemetry configured");
           }
         }




### Python

  1. Install the Cloud Storage Python client library:
         
         pip install google-cloud-storage[tracing]>=2.18.0

  2. Install the Cloud Trace exporter and propagator. You can also use any exporter of your choice.
         
         pip install opentelemetry-exporter-gcp-trace opentelemetry-propagator-gcp

  3. Install the OpenTelemetry requests instrumentation to trace the underlying HTTP requests.
         
         pip install opentelemetry-instrumentation-requests

  4. Set the environment variable to selectively opt in to tracing for the Python storage client:
         
         export ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES=True

  5. Configure the trace exporter and trace provider. 
         
         from opentelemetry import trace
         from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
         from opentelemetry.resourcedetector.gcp_resource_detector import (
             GoogleCloudResourceDetector,
         )
         from opentelemetry.sdk.trace import TracerProvider
         from opentelemetry.sdk.trace.export import BatchSpanProcessor
         from opentelemetry.sdk.trace.sampling import ALWAYS_ON
         # Optional: Enable traces emitted from the requests HTTP library.
         from opentelemetry.instrumentation.requests import RequestsInstrumentor
         
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         # The ID of your GCS bucket
         # bucket_name = "your-bucket-name"
         # The ID of your GCS object
         # blob_name = "your-object-name"
         # The contents to upload to the file
         # data = "The quick brown fox jumps over the lazy dog."
         
         # In this sample, we use Google Cloud Trace to export the OpenTelemetry
         # traces: https://cloud.google.com/trace/docs/setup/python-ot
         # Choose and configure the exporter for your environment.
         
         tracer_provider = TracerProvider(
             # Sampling is set to ALWAYS_ON.
             # It is recommended to sample based on a ratio to control trace ingestion volume,
             # for instance, sampler=TraceIdRatioBased(0.2)
             sampler=ALWAYS_ON,
             resource=GoogleCloudResourceDetector().detect(),
         )
         
         # Export to Google Cloud Trace.
         tracer_provider.add_span_processor(BatchSpanProcessor(CloudTraceSpanExporter()))
         trace.set_tracer_provider(tracer_provider)
         
         # Optional: Enable traces emitted from the requests HTTP library.
         RequestsInstrumentor().instrument(tracer_provider=tracer_provider)
         
         # Get the tracer and create a new root span.
         tracer = tracer_provider.get_tracer("My App")
         with tracer.start_as_current_span("trace-quickstart"):
             # Instantiate a storage client and perform a write and read workload.
             storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
             blob = bucket.blob(blob_name)
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(data)
             print(f"{blob_name} uploaded to {bucket_name}.")
         
             blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
             print("Downloaded storage object {} from bucket {}.".format(blob_name, bucket_name))
         

**Note:** In the following sample, trace results are exported to Cloud Trace. For more options for exporting your traces, see [OpenTelemetry's list of available exporters](https://opentelemetry.io/docs/languages/js/exporters/).



## View your traces

Use the Cloud Trace explorer to view your trace data in the Google Cloud console:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. In the **Trace explorer** page, click a specific trace in the scatter plot to view the trace details.

The **Trace details** pane displays a table of trace spans.

  3. Optional: click a span row to view detailed information about a specific span such as the following information:

     * **Attributes** : key-value pairs that provide additional information about the span.

     * **Logs & events**: log entries that are associated with the span.

     * **Stack traces** : stack traces that are associated with the span.

     * **Metadata & Links**: links to other Google Cloud services that are associated with the span.




For more information about using the Cloud Trace explorer, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## What's next

  * [Find and explore traces.](https://docs.cloud.google.com/trace/docs/finding-traces)

  * [Display recent traces.](https://docs.cloud.google.com/trace/docs/finding-traces#view-recent)

  * [Find a trace by ID.](https://docs.cloud.google.com/trace/docs/finding-traces#find)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
