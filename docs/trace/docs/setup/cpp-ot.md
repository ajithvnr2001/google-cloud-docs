---
url: https://docs.cloud.google.com/trace/docs/setup/cpp-ot/
title: C++ and OpenTelemetry \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:10.741122+00:00
---

# C++ and OpenTelemetry  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/setup/cpp-ot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  C++ and OpenTelemetry Stay organized with collections  Save and categorize content based on your preferences. 

You can instrument a C++ application with [OpenTelemetry](https://opentelemetry.io) and configure the Google Cloud C++ OpenTelemetry exporter to send trace spans to Cloud Trace in your Google Cloud project. You can use a basic tracing configuration, configure the trace sampling rate, or use a custom `TracerProvider` object. For general information about application instrumentation, see [Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview).

## Before you begin

Enable the Cloud Trace API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudtrace.googleapis.com)

## Install the OpenTelemetry packages

  * [Set up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).
  * Install the Google Cloud C++ OpenTelemetry exporter library. For installation information, see the [OpenTelemetry quickstart](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/opentelemetry/quickstart).



## Configure the export of spans to Cloud Trace

To configure the export of trace data, call the `google::cloud::otel::ConfigureBasicTracing(...)` function in your `main()` function:
    
    
    namespace gc = ::google::cloud;
    [](std::string project_id) {
      auto project = gc::Project(std::move(project_id));
      auto configuration = gc::otel::ConfigureBasicTracing(project);
    
      MyApplicationCode();
    }

The field `project_id` is the Google Cloud project where you want to store the traces.

The `ConfigureBasicTracing(...)` function instantiates a [`TracerProvider`](https://opentelemetry.io/docs/specs/otel/trace/api/#tracerprovider) object that implements a Cloud Trace exporter. If the object returned by the call to `ConfigureBasicTracing(...)` goes out of scope, then the previous `TracerProvider` object is reinstated, when one exists.

### Configure sample rate

Applications might generate a large volume of trace data. The following sample illustrates how to configure the sampling rate:
    
    
    namespace gc = ::google::cloud;
    [](std::string project_id) {
      auto project = gc::Project(std::move(project_id));
      auto options = gc::Options{}.set<gc::otel::BasicTracingRateOption>(.001);
      auto configuration = gc::otel::ConfigureBasicTracing(project, options);
    
      MyApplicationCode();
    }

**Note:** A sampling rate of 1.0 samples all traces. This setting might generate a large volume of trace data and might increase your usage bill.

### Export to Cloud Trace with a custom `TracerProvider`

You might have use cases that require a custom `TracerProvider` object. For example, if you want to use multiple exporters at the same time, you need to make a custom `TracerProvider` object. In these cases, you can use the Cloud Trace exporter directly:
    
    
    namespace gc = ::google::cloud;
    using ::opentelemetry::trace::Scope;
    [](std::string project_id) {
      // Use the Cloud Trace Exporter directly.
      auto project = gc::Project(std::move(project_id));
      auto exporter = gc::otel::MakeTraceExporter(project);
    
      // Advanced use cases may need to create their own tracer provider, e.g. to
      // export to Cloud Trace and another backend simultaneously. In this
      // example, we just tweak some OpenTelemetry settings that google-cloud-cpp
      // does not expose.
      opentelemetry::sdk::trace::BatchSpanProcessorOptions options;
      options.schedule_delay_millis = std::chrono::milliseconds(1000);
      auto processor =
          opentelemetry::sdk::trace::BatchSpanProcessorFactory::Create(
              std::move(exporter), options);
    
      // Create a tracer provider and set it as the global trace provider
      opentelemetry::trace::Provider::SetTracerProvider(
          std::shared_ptr<opentelemetry::trace::TracerProvider>(
              opentelemetry::sdk::trace::TracerProviderFactory::Create(
                  std::move(processor))));
    
      MyApplicationCode();
    
      // Clear the global trace provider
      opentelemetry::trace::Provider::SetTracerProvider(
          opentelemetry::nostd::shared_ptr<
              opentelemetry::trace::TracerProvider>());
    }

### Instrument your own application

For information about how to configure your application to capture trace spans, see [OpenTelemetry Tracing](https://opentelemetry.io/docs/instrumentation/cpp/manual/#tracing). This page describes how to do all of the following:

  * Create a span
  * Create nested spans
  * Set span attributes
  * Create spans with events
  * Create spans with links


    
    
    // For more details on the OpenTelemetry code in this sample, see:
    //     https://opentelemetry.io/docs/instrumentation/cpp/manual/
    namespace gc = ::google::cloud;
    using ::opentelemetry::trace::Scope;
    [](std::string project_id) {
      auto project = gc::Project(std::move(project_id));
      auto configuration = gc::otel::ConfigureBasicTracing(project);
    
      // Initialize the `Tracer`. This would typically be done once.
      auto provider = opentelemetry::trace::Provider::GetTracerProvider();
      auto tracer = provider->GetTracer("my-application");
    
      // If your application makes multiple client calls that are logically
      // connected, you may want to instrument your application.
      auto my_function = [tracer] {
        // Start an active span. The span is ended when the `Scope` object is
        // destroyed.
        auto scope = Scope(tracer->StartSpan("my-function-span"));
    
        // Any spans created by the client library will be children of
        // "my-function-span". i.e. In the distributed trace, the client calls are
        // sub-units of work of `my_function()`, and will be displayed as such in
        // Cloud Trace.
        Client client;
        client.CreateFoo();
        client.DeleteFoo();
      };
    
      // As an example, start a span to cover both calls to `my_function()`.
      auto scope = Scope(tracer->StartSpan("my-application-span"));
      my_function();
      my_function();
    }

## Sample application

For a sample application, see the [quickstart](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/opentelemetry/quickstart).

## Configure your platform

You can use Cloud Trace on Google Cloud and other platforms.

### Running on Google Cloud

When your application is running on Google Cloud, you don't need to provide authentication credentials in the form of a service account to the client library. However, you do need to ensure that your Google Cloud platform has the [Cloud Trace API access scope](https://developers.google.com/identity/protocols/googlescopes#cloudtrace) enabled.

For a list of supported Google Cloud environments, see [Environment support](https://docs.cloud.google.com/trace/docs/overview#environment_support).

For the following configurations, the default access-scope settings enable the Cloud Trace API:

  * App Engine flexible environment 
  * App Engine standard environment 

  * Google Kubernetes Engine (GKE)

**Note:** If you use Autopilot or if you enable Workload Identity Federation for GKE for your GKE cluster, then ensure that you [configure your application to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).
  * Compute Engine

  * Cloud Run




If you use custom access scopes, then you must ensure that [Cloud Trace API access scope](https://developers.google.com/identity/protocols/googlescopes#cloudtrace) is enabled:

  * For information about how to configure the access scopes for your environment by using the Google Cloud console, see [Configuring your Google Cloud project](https://docs.cloud.google.com/trace/docs/setup#gcp-config).

  * For `gcloud` users, specify access scopes using the `--scopes` flag and include the `trace.append` Cloud Trace API access scope. For example, to create a GKE cluster with only the Cloud Trace API enabled, do the following:
        
        gcloud container clusters create example-cluster-name --scopes=https://www.googleapis.com/auth/trace.append




### Running locally and elsewhere

If your application is running outside of Google Cloud, then you must provide authentication credentials in the form of a service account to the client library. The service account must contain the [Cloud Trace agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent). For instructions, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

Google Cloud client libraries use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/production) to find your application's credentials.

You can provide these credentials in one of three ways:

  * Run `gcloud auth application-default login`

  * Place the service account in a default path for your operating system. The following lists the default paths for Windows and Linux:

    * Windows: `%APPDATA%/gcloud/application_default_credentials.json`

    * Linux: `$HOME/.config/gcloud/application_default_credentials.json`

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path to your service account:




### Linux/macOS
    
    
        export GOOGLE_APPLICATION_CREDENTIALS=path-to-your-service-accounts-private-key

### Windows
    
    
        set GOOGLE_APPLICATION_CREDENTIALS=path-to-your-service-accounts-private-key

PowerShell:
    
    
        $env:GOOGLE_APPLICATION_CREDENTIALS="path-to-your-service-accounts-private-key"

## View traces

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

## Troubleshooting

For information on troubleshooting issues with Cloud Trace, go to the [Troubleshooting page](https://docs.cloud.google.com/trace/docs/troubleshooting).

To debug the C++ Cloud Trace exporter, see the [Troubleshooting](https://docs.cloud.google.com/cpp/docs/reference/opentelemetry/latest/namespacegoogle_1_1cloud_1_1otel#troubleshooting) section of the reference documentation.

## Resources

For the latest details about OpenTelemetry for C++, along with additional documentation and examples, see [OpenTelemetry](https://opentelemetry.io).

For release information, see the following:

  * [Latest library release for C++](https://github.com/open-telemetry/opentelemetry-cpp/releases)
  * [Latest Cloud Trace exporter release for C++](https://github.com/googleapis/google-cloud-cpp/releases)



For OpenTelemetry reference content, see the following:

  * [`Tracer`](https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/classopentelemetry_1_1trace_1_1Tracer.html)
  * [`Span`](https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/classopentelemetry_1_1trace_1_1Span.html)



For GitHub repositories, see the following:

  * [`open-telemetry/opentelemetry-cpp`](https://github.com/open-telemetry/opentelemetry-cpp/)
  * [`google-cloud-cpp` OpenTelemetry Exporters Library](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/opentelemetry)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
