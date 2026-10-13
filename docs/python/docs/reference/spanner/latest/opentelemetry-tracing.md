---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/opentelemetry-tracing/
title: Tracing with OpenTelemetry \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:49.245284+00:00
---

# Tracing with OpenTelemetry  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/opentelemetry-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Tracing with OpenTelemetry Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

This library uses [OpenTelemetry](https://opentelemetry.io/) to automatically generate traces providing insight on calls to Cloud Spanner. For information on the benefits and utility of tracing, see the [Cloud Trace docs](https://cloud.google.com/trace/docs/overview).

To take advantage of these traces, we first need to install OpenTelemetry:
    
    
    pip install opentelemetry-api opentelemetry-sdk
    pip install opentelemetry-exporter-gcp-trace
    

We also need to tell OpenTelemetry which exporter to use. To export Spanner traces to [Cloud Tracing](https://cloud.google.com/trace), add the following lines to your application:
    
    
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    # BatchSpanProcessor exports spans to Cloud Trace
    # in a seperate thread to not block on the main thread
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    
    # Create and export one trace every 1000 requests
    sampler = TraceIdRatioBased(1/1000)
    tracer_provider = TracerProvider(sampler=sampler)
    tracer_provider.add_span_processor(
        # Initialize the cloud tracing exporter
        BatchSpanProcessor(CloudTraceSpanExporter())
    )
    observability_options = dict(
        tracer_provider=tracer_provider,
    
        # By default extended_tracing is set to True due
        # to legacy reasons to avoid breaking changes, you
        # can modify it though using the environment variable
        # SPANNER_ENABLE_EXTENDED_TRACING=false.
        enable_extended_tracing=False,
    
        # By default end to end tracing is set to False. Set to True
        # for getting spans for Spanner server.
        enable_end_to_end_tracing=True,
    )
    spanner = spanner.NewClient(project_id, observability_options=observability_options)
    

To get more fine-grained traces from gRPC, you can enable the gRPC instrumentation by the following
    
    
    pip install opentelemetry-instrumentation opentelemetry-instrumentation-grpc
    

and then in your Python code, please add the following lines:
    
    
    from opentelemetry.instrumentation.grpc import GrpcInstrumentorClient
    grpc_client_instrumentor = GrpcInstrumentorClient()
    grpc_client_instrumentor.instrument()
    

Generated spanner traces should now be available on [Cloud Trace](https://console.cloud.google.com/traces).

Tracing is most effective when many libraries are instrumented to provide insight over the entire lifespan of a request. For a list of libraries that can be instrumented, see the OpenTelemetry Integrations section of the [OpenTelemetry Python docs](https://opentelemetry-python.readthedocs.io/en/stable/)

## Annotating spans with SQL

By default your spans will be annotated with SQL statements where appropriate, but that can be a PII (Personally Identifiable Information) leak. Sadly due to legacy behavior, we cannot simply turn off this behavior by default. However you can control this behavior by setting

> SPANNER_ENABLE_EXTENDED_TRACING=false

to turn it off globally or when creating each SpannerClient, please set observability_options.enable_extended_tracing=false

## End to end tracing

In addition to client-side tracing, you can opt in for end-to-end tracing. End-to-end tracing helps you understand and debug latency issues that are specific to Spanner. Refer [here](about:invalid#zCSafez) for more information.

To configure end-to-end tracing.

  1. Opt in for end-to-end tracing. You can opt-in by either: * Setting the environment variable SPANNER_ENABLE_END_TO_END_TRACING=true before your application is started * In code, by setting observability_options.enable_end_to_end_tracing=true when creating each SpannerClient.

  2. Set the trace context propagation in OpenTelemetry.



    
    
    from opentelemetry.propagate import set_global_textmap
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
    set_global_textmap(TraceContextTextMapPropagator())
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
