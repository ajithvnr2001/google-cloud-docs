---
url: https://docs.cloud.google.com/endpoints/docs/grpc/tracing/
title: Tracing your API \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:16.632301+00:00
---

# Tracing your API  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Tracing your API Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/tracing "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

After you deploy the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) or [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy_v2) and your API's backend code, the proxy intercepts all requests and performs any necessary checks before forwarding the request to the API backend. When the backend responds, the proxy gathers and reports telemetry. One piece of telemetry data that the proxy captures is tracing, by using [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview).

This page explains how to:

  * View traces in the Google Cloud console.
  * Estimate your cost for Trace.
  * Configure the proxy to disable trace sampling.



## Viewing traces

A trace tracks an incoming request to your API and the various events (such as RPC calls or instrumented sections of code), along with precise timings of each event. These events are represented as _spans_ in the trace.

To view traces for your project, go to the Cloud Trace page in Google Cloud console:

[Go to Trace](https://console.cloud.google.com/traces)

On the **Trace explorer** page, you can drill down to view an individual trace and see the spans that ESP creates in a trace. You can use the filter to view traces for a single API or operation.

The traces and spans created for your API will differ depending upon whether your API uses ESPv2 or ESP. A summary of the trace formats for each implementation follows below.

For more information on the **Trace explorer** page, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## Spans created by ESPv2

ESPv2 creates traces in the following format:

![Example trace with spans for ESPv2](https://docs.cloud.google.com/static/endpoints/docs/images/trace-example-espv2.png)

At a minimum, ESPv2 creates 2 spans per trace:

  * A `ingress OPERATION_NAME` span for the entire request and response.
  * A `router BACKEND egress` span for the time ESPv2 waits for the backend to process the request and respond back. This includes the network hop between ESPv2 and the backend.



Depending on the configuration of your API, ESPv2 may create additional spans:

  * If your API requires authentication, ESPv2 caches the public key it needs to authenticate for 5 minutes. If the public key isn't in the cache, ESPv2 retrieves and caches the public key and creates a `JWT Remote PubKey Fetch` span.
  * If your API requires an API key, ESPv2 caches the information that it needs to validate the API key. If the information isn't in the cache, ESPv2 calls Service Control and creates a `Service Control remote call: Check` span.



In general, ESPv2 only creates spans for network calls that block the incoming request. Non-blocking requests will not be traced. Any local processing will create [time events](https://docs.cloud.google.com/endpoints/docs/grpc/trace/docs/viewing-details#annotating_with_time_events) instead of spans. For example:

  * Quota enforcement requires remote calls, but the calls do not occur in the path of an API request and will not have spans associated with them in the trace.
  * API keys are cached by ESPv2 for a short period of time. Any requests that use the cache will have a time event associated in the trace.



## Spans created by ESP

**Warning:** ESP does not provided detailed information for spans. It also creates extra spans that are not meaningful. Please [migrate to ESPv2](https://docs.cloud.google.com/endpoints/docs/openapi/migrate-to-esp-v2) to view detailed traces that follow tracing best practices.

ESP creates traces in the following format:

![Example trace with spans for ESP](https://docs.cloud.google.com/static/endpoints/docs/images/trace-example.png)

At a minimum, ESP creates 4 spans per trace:

  * A span for the entire request and response.
  * A `CheckServiceControl` span for the call to the [Service Control's](https://docs.cloud.google.com/service-control/overview) `services.check` method to get the configuration for your API.
  * A `QuotaControl` span to check if there is a [quota](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-overview) configured on your API.
  * A `Backend` span that tracks the time spent in your API's backend code.



Depending on the configuration for your API, ESP creates additional spans:

  * If your API requires authentication, ESP creates a `CheckAuth` span in every trace. To authenticate a request, ESP caches the public key it needs to authenticate for 5 minutes. If the public key isn't in the cache, ESP retrieves and caches the public key and creates a `HttpFetch` span.
  * If your API requires an API key, ESP creates a `CheckServiceControlCache` span in every trace. ESP caches the information that it needs to validate the API key. If the information isn't in the cache, ESP calls Service Control and creates a `Call ServiceControl server` span.
  * If you have a quota set for your API, ESP creates a `QuotaServiceControlCache` span in every trace. ESP caches the information that it needs to check the quota. If the information isn't in the cache, ESP calls Service Control and creates a `Call ServiceControl server` span.



## Trace sampling rate

ESP samples a small number of requests to your API to get trace data. To control the sampling rate, ESP maintains a request counter and a timer. The number of requests per second to your API determines the sampling rate. If there are no requests within a second, ESP doesn't send a trace.

If the number of requests in a second is:

  * Less than or equal to 999, ESP sends 1 trace.
  * Between 1000 and 1999, ESP sends 2 traces.
  * Between 2000 and 2999, ESP sends 3 traces.
  * And so on.



In summary, you can estimate the sampling rate with the [`ceiling` function](https://wikipedia.org/wiki/Floor_and_ceiling_functions): `ceiling(requests per second/1000)`

## Estimating the cost of Trace

To estimate the cost of Trace, you need to estimate the number of spans that ESP sends to Trace in a month.

To estimate the number of spans per month:

  1. Estimate the number of requests per second to your API. To get this estimate, you can use the **Requests** graph on the **Endpoints** > **Services** page or Cloud Logging. See [Monitoring your API](https://docs.cloud.google.com/endpoints/docs/grpc/monitoring-your-api#logs) for more information.
  2. Calculate the number of traces that ESP sends to Trace per second: `ceiling(requests per second/1000)`
  3. Estimate the number of spans in a trace. To get this estimate, you can use the information in Spans created by ESP or view the **Trace List** page to see traces for your API.
  4. Estimate the number of seconds in a month that your API gets traffic. For example, some APIs get requests only during certain times of the day, and other APIs get requests sporadically.
  5. Multiply the number of seconds in the month by the number of spans.



For example:

  1. Assume that the maximum number of requests per second for an API is 5.
  2. The trace sampling rate is ceiling (5/1000) = 1
  3. The API doesn't have a quota configured, doesn't require an API key, and doesn't require authentication. Therefore, the number of spans that ESP creates per trace is 4.
  4. This API gets requests only during business hours, Monday through Friday. The number of seconds in a month that the API gets traffic is approximately: 3600 X 8 X 20 = 576,000
  5. The number of spans per month is approximately 576,000 x 4 = 2,304,000



After you know the approximate number of spans in a month, refer to the [Trace pricing](https://cloud.google.com/stackdriver/pricing#trace-costs) page for detailed pricing information.

## Disabling trace sampling

If you want to stop ESP from sampling requests and sending traces, you can set an ESP startup option and restart ESP. The traces ESP sends to Cloud Trace are independent of the graphs displayed on the **Endpoints** > **Services** page. The graphs continue to be available if you disable trace sampling.

The following section assumes you have already deployed your API and ESP, or you are familiar with the deployment process. For more information, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend).

### Compute Engine

To disable ESP trace sampling in Compute Engine with Docker:

  1. Connect to your VM instance: 
         
         gcloud compute ssh [INSTANCE_NAME]

  2. In the ESP flags for the `docker run` command, add the option `--disable_cloud_trace_auto_sampling`: 
         
         sudo docker run \
             --name=esp \
             --detach \
             --publish=80:8080 \
             --net=esp_net \
             gcr.io/endpoints-release/endpoints-runtime:1 \
             --service=[SERVICE_NAME] \
             --rollout_strategy=managed \
             --backend=[YOUR_API_CONTAINER_NAME]:8080 \
             --disable_cloud_trace_auto_sampling

  3. Issue the `docker run` command to restart ESP.



To re-enable trace sampling:

  1. Remove the `--disable_cloud_trace_auto_sampling`. 
  2. Issue the `docker run` command to restart ESP.



### GKE

To disable ESP trace sampling in GKE:

  1. Open your deployment manifest file, referred to as `deployment.yaml`, and add the following to the `containers` section: 
         
         containers:
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=[SERVICE_NAME]",
             "--rollout_strategy=managed",
             "--disable_cloud_trace_auto_sampling"
           ]

  2. Start the Kubernetes service by using the [`kubectl create`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) command: 
         
         kubectl create -f deployment.yaml




To re-enable trace sampling:

  1. Remove the `--disable_cloud_trace_auto_sampling` option. 
  2. Start the Kubernetes service: 
         
         kubectl create -f deployment.yaml




If you are running ESP on a Compute Engine VM instance without a Docker container, there is no equivalent VM instance metadata key-value pair for the `--disable_cloud_trace_auto_sampling` option. If you want to disable trace sampling, you must run ESP in a container.

A client can force a request to be traced by adding the `X-Cloud-Trace-Context` header to the request, as described in [Forcing a request to be traced](https://docs.cloud.google.com/trace/docs/setup#force-trace). If a request contains the `X-Cloud-Trace-Context` header, ESP sends the trace data to Trace even if you have disabled trace sampling.

## Trace Context Propagation

For distributed tracing, a request header can contain a trace context which specifies a trace ID. The trace ID is used when ESPv2 creates new trace spans and sends them to [Cloud Trace](https://docs.cloud.google.com/trace). The trace ID is used to search all traces and join spans for a single request. If no trace context is specified in the request, and trace is enabled, a random trace ID is generated for all trace spans.

In the following example, Cloud Trace correlates spans created by ESPv2 (1) with spans created by the backend (2) for a single request. This helps debug latency issues across the entire system:

![Example trace context propagation for ESPv2](https://docs.cloud.google.com/static/endpoints/docs/images/trace-context-propagation-espv2.png)

For more details, read [OpenTelemetry Core Concepts: Context Propagation](https://opentelemetry.lightstep.com/core-concepts/context-propagation/)

**Note:** Distributed tracing requires your clients and/or your backends to support tracing. This is out of scope of this documentation. We recommend using [OpenTelemetry](https://opentelemetry.lightstep.com/).

### Supported Headers

ESPv2 supports the following trace context propagation headers:

  * `traceparent`: The standard [W3C](https://www.w3.org/TR/trace-context/) trace context propagation header. Supported by most modern tracing frameworks.
  * `x-cloud-trace-context`: GCP's trace context propagation header. Supported by older tracing frameworks and Google's libraries, but vendor-specific.
  * `grpc-trace-bin`: Trace context propagation header used by gRPC backends with the [OpenCensus](https://opencensus.io/) tracing library.



If you are building a new application, we recommend using `traceparent` trace context propagation. ESPv2 will extract and propagate this header by default. See [ESPv2 tracing startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options#tracing) for details on changing the default behavior.

**Note:** Unlike ESPv2, trace context propagation in ESP needs to be manually enabled via the startup options. ESP does not support the `traceparent` header.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
