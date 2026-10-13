---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1
title: Google Cloud Trace v1 API - Namespace Google.Cloud.Trace.V1 (3.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:45.670712+00:00
---

# Google Cloud Trace v1 API - Namespace Google.Cloud.Trace.V1 (3.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Trace v1 API - Namespace Google.Cloud.Trace.V1 (3.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/3.4.0/Google.Cloud.Trace.V1)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/3.3.0/Google.Cloud.Trace.V1)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/3.2.0/Google.Cloud.Trace.V1)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/3.1.0/Google.Cloud.Trace.V1)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/3.0.0/Google.Cloud.Trace.V1)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/2.3.0/Google.Cloud.Trace.V1)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/2.2.0/Google.Cloud.Trace.V1)



## Classes 

### [GetTraceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.GetTraceRequest)

The request message for the `GetTrace` method.

### [ListTracesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.ListTracesRequest)

The request message for the `ListTraces` method. All fields are required unless specified.

### [ListTracesRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.ListTracesRequest.Types)

Container for nested types declared in the ListTracesRequest message type.

### [ListTracesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.ListTracesResponse)

The response message for the `ListTraces` method.

### [PatchTracesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.PatchTracesRequest)

The request message for the `PatchTraces` method.

### [Trace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.Trace)

A trace describes how long it takes for an application to perform an operation. It consists of a set of spans, each of which represent a single timed event within the operation.

### [TraceService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceService)

This file describes an API for collecting and viewing traces and spans within a trace. A Trace is a collection of spans corresponding to a single operation or set of operations for an application. A span is an individual timed event which forms a node of the trace tree. Spans for a single trace may span multiple services.

### [TraceService.TraceServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceService.TraceServiceBase)

Base class for server-side implementations of TraceService

### [TraceService.TraceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceService.TraceServiceClient)

Client for TraceService

### [TraceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceClient)

TraceService client wrapper, for convenient use.

### [TraceServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceClientBuilder)

Builder class for [TraceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceClient) to provide simple configuration of credentials, endpoint etc.

### [TraceServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceClientImpl)

TraceService client wrapper implementation, for convenient use.

### [TraceServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceSettings)

Settings for [TraceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceServiceClient) instances.

### [TraceSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceSpan)

A span represents a single timed event within a trace. Spans can be nested and form a trace tree. Often, a trace contains a root span that describes the end-to-end latency of an operation and, optionally, one or more subspans for its suboperations. Spans do not need to be contiguous. There may be gaps between spans in a trace.

### [TraceSpan.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceSpan.Types)

Container for nested types declared in the TraceSpan message type.

### [Traces](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.Traces)

List of new or updated traces.

## Enums 

### [ListTracesRequest.Types.ViewType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.ListTracesRequest.Types.ViewType)

Type of data returned for traces in the list.

### [TraceSpan.Types.SpanKind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V1/latest/Google.Cloud.Trace.V1.TraceSpan.Types.SpanKind)

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
