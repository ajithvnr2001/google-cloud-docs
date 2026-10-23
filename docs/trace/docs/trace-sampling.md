---
url: https://docs.cloud.google.com/trace/docs/trace-sampling/
title: Trace sampling \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:41.453779+00:00
---

# Trace sampling  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-sampling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Trace sampling Stay organized with collections  Save and categorize content based on your preferences. 

_Trace sampling_ determines which requests and spans Cloud Trace ingests, helping you control storage costs and stay within quotas while capturing sufficient data to troubleshoot performance. To manage high request volumes, components in a distributed tracing system typically sample only a subset of traces or follow the sampling decisions of parent spans.

Sampling is distinct from [context propagation](https://docs.cloud.google.com/trace/docs/trace-context): sampling controls whether a component records span data, whereas context propagation passes trace identifiers between components so sampled spans can be linked.

## Sampling strategies

Sampling decisions can be either head-based or tail-based. In _head-based sampling_ , the sampling decision is made when the request is received by the component processing the span. In _tail-based sampling_ , the sampling decision is delayed until after the entire trace is available.

You might encounter the phrase "100% sampling" in documentation for distributed tracing systems. This phrase might apply to a trace or to a component. When applied to a trace, it means that all spans have been sampled, or equivalently, that the trace is complete. When applied to a component, it means that the component samples every span it processes.

### Head-based sampling

Head-based samplers are typically configured to always sample spans or to use a probabilistic sampling strategy:

  * With _always sample_ configurations, components that process and write trace data sample every span. Ideally, all traces are complete, and therefore you have the information necessary to troubleshoot failures. However, an always-sample configuration might cause you to exceed [quotas](https://docs.cloud.google.com/trace/docs/quotas) or your storage cost limits.

  * With _probabilistic_ sampling, not all spans are sampled. The actual behavior for this approach depends on the component's implementation. In some implementations, all spans have the same probability of being sampled. In others, the sampling decision of the parent influences whether a span is sampled.




A trace might not contain every span. If you use _probabilistic_ sampling, exceed quota, or use components that process but don't sample spans, then incomplete traces are expected.

### Tail-based sampling

Cloud Trace doesn't support tail-based sampling; sampling decisions must be made in the components that send data to Cloud Trace.

If you use tail-based sampling, then you can also use an intermediary server to receive trace data, evaluate sampling decisions, and relay sampled spans to Trace. For example, you can use an [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) with the [Tail Sampling Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor) to make a delayed sampling decision.

If you plan to use tail sampling, consider the following:

  * You must store all spans in a trace before you make a sampling decision. Therefore, you might require a large amount of temporary storage or incur other overhead.
  * In general, all components that can generate spans for a trace need to coordinate. Typically, developers that use OpenTelemetry route all spans for the same trace ID to the same collector.



## Components make sampling decisions

Each component makes its own decision about whether to sample the span it is processing. However, the parent's sampling decision, which might be available to the component through the trace context, can influence the component's decision. Applications that use the [`traceparent` header](https://www.w3.org/TR/trace-context/) can pass the parent's sampling decision by using the [`sampled` flag](https://www.w3.org/TR/trace-context/#sampled-flag).

For example, assume every component has a rule that says "if the parent span is sampled, then sample the current span; otherwise, sample 50% of the spans". In this scenario, the following is true:

  * The root span determines whether all spans in the trace are sampled.
  * When the root span is sampled, all spans in the trace are sampled. Therefore, the trace is complete.



## Sampling and Google Cloud services

**Note:** Cloud Trace has no role in a component's sampling decision.

Each Google Cloud service makes its own sampling decisions, and not all Google Cloud services sample. That is, a service might never send data to Cloud Trace.

When sampling is supported by a Google Cloud service, that service typically implements the following:

  * A default sample rate.
  * A mechanism to use the parent's sampling decision as a hint about whether to sample the span.
  * Maximum sampling rate.



To request that a Google Cloud service add support for sampling, use the [Google Issue Tracker](https://developers.google.com/issue-tracker/guides/access-ui).

## What's next

  * For a discussion about how you can pick a sampling strategy by span name, see [Jaeger remote sampling](https://www.youtube.com/live/Q2K1rJn67X8?si=q6idOBJkaifykl9g&t=2574).

  * We recommend that you review the following open-source documentation to help you determine which sampling approach is best for your in-development and deployed applications:

    * [OpenTelemetry Sampling](https://opentelemetry.io/docs/concepts/sampling/)
    * [OpenTelemetry probability sampling](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling/)
    * [OpenTelemetry tail sampling processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor)
    * [`sampled` flag](https://www.w3.org/TR/trace-context/#sampled-flag)
  * Google Cloud service documentation:

    * [Enabling distributed tracing in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace)
    * [Using distributed tracing with Cloud Run](https://docs.cloud.google.com/run/docs/trace)
    * [Cloud Endpoints: Trace sampling rate](https://docs.cloud.google.com/endpoints/docs/openapi/tracing#trace_sampling_rate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
