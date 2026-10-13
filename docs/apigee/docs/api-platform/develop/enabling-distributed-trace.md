---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace/
title: Enabling distributed tracing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:43.155125+00:00
---

# Enabling distributed tracing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling distributed tracing Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page demonstrates the steps required to configure distributed tracing for your Apigee runtime. If you are new to using distributed tracing systems and would like more information, see [Understanding Distributed Tracing](https://opentelemetry.io/docs/concepts/observability-primer/#understanding-distributed-tracing).

For more information on the terms used in this page, see the [Cloud Trace overview](https://docs.cloud.google.com/trace/docs/overview).

## Introduction

Distributed tracing systems let you track a request in a software system distributed across multiple applications, services, and databases, as well as intermediaries like proxies. These tracing systems generate reports showing the time taken by a request at each step. Tracing reports can also provide a granular view of the various services called during a request, enabling a deeper understanding of what happens at each step in your software system.

The _trace tool_ in Apigee Edge and the _debug tool_ in Apigee are useful for troubleshooting and monitoring your API proxies. However, these tools do not send any data to distributed tracing servers like [Cloud Trace](https://docs.cloud.google.com/trace), [Jaeger](https://www.jaegertracing.io/docs/), or an [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/).

To view Apigee runtime data in a distributed tracing report, you must explicitly enable distributed tracing in your Apigee runtime. Once tracing is enabled, the runtime can send trace data to distributed tracing servers and participate in an existing trace. As a result, you can view data from inside and outside of your Apigee ecosystem from a single location.

You can view the following information in distributed tracing reports:

  * Execution time of an entire flow.
  * Time at which the request is received.
  * Time at which the request is sent to the target.
  * Time at which the response is received from the target.
  * Execution time of each policy in a flow.
  * Execution time of service callouts and target flows.
  * Time at which the response is sent to the client.



In the distributed tracing report, you can view the execution details of the flows as _spans_. A span refers to the time taken by a flow in a trace. The time taken to execute a flow is displayed as an aggregate of the time required to execute each policy in the flow. You can view each of the following flows as individual spans: 

Phase | Endpoint | Flow  
---|---|---  
Request | Proxy | Preflow  
PostFlow  
Target | Preflow  
PostFlow  
Response | Proxy | Preflow  
PostFlow  
Target | Preflow  
PostFlow  
  
Once you enable distributed tracing, the Apigee runtime will trace a set of predefined variables by default. For more information, see Default trace variables in tracing report. You can use the TraceCapture policy to extend the default runtime behavior and trace additional flow, policy, or custom variables. For more information, see the [TraceCapture](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy) policy. 

## Default trace variables in tracing report

**Applies to:** both the OpenTelemetry and OpenCensus configurations.

Once distributed tracing is enabled, you can view the following set of predefined variables in the tracing report. The variables are visible in the following spans:

  * `RESP_SENT`: This span is added after a response is received from the target server. It carries the target-side attributes listed under Variables in the `RESP_SENT` span.
  * `PROXY_POST_RESP_SENT`: This span is added after the proxy response is sent to the client. It carries the proxy-side attributes listed under Variables in the `PROXY_POST_RESP_SENT` span.
  * `EVENT_FLOW_RESP` and `EVENT_FLOW_END`: These spans are added for API proxies that handle [streaming Server-Sent Events (SSE)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events) responses. `EVENT_FLOW_RESP` marks the SSE response flow (executed once per response message). `EVENT_FLOW_END` marks the end of the SSE stream. These spans currently do not carry default attributes; they appear in the trace as named spans to make the SSE phases of the proxy visible in the tracing report.



### Default resource attributes

**Applies to:** OpenTelemetry only. This section does not apply to the OpenCensus configuration.

When you use OpenTelemetry with the OTLP trace protocol, the Apigee runtime attaches the following OpenTelemetry semantic convention resource attributes to every emitted span:

**Note:** The OpenTelemetry-based approach (the `OTLP` trace protocol) is supported only in Apigee (ApigeeX). It is not supported in Apigee hybrid.Attribute | Description  
---|---  
`service.name` | Fixed value `apigee.googleapis.com`.  
`service.instance.id` | Identifier of the message processor instance that emitted the span. Omitted when the runtime pod identity is not available.  
`cloud.provider` | Always `gcp`.  
`cloud.platform` | Always `gcp_apigee`.  
`cloud.region` | The region hosting the Apigee runtime, falling back to `global` when no region is configured.  
`cloud.resource_id` | Fully qualified Apigee resource path in the form `/apigee.googleapis.com/organizations/ORG/environments/ENV`.  
`gcp.apigee.organization` | The Apigee organization name.  
`gcp.apigee.environment` | The Apigee environment name.  
`gcp.project_id` | The Google Cloud project ID. Emitted only when the exporter is `OPEN_TELEMETRY_CLOUD_TRACE`.  
  
### Span kinds

**Applies to:** both the OpenTelemetry and OpenCensus configurations.

Apigee emits spans with the following [`SpanKind`](https://opentelemetry.io/docs/specs/otel/trace/api/#spankind) values:

`SpanKind` | Spans emitted with this kind  
---|---  
`SERVER` | The root proxy span (one per proxy invocation), representing the incoming request received by the Apigee runtime.  
`INTERNAL` | All other spans, including flow spans (for example, `RESP_SENT` and `PROXY_POST_RESP_SENT`) and every policy step span (for example, AssignMessage, VerifyAPIKey, ServiceCallout, JavaScript, KeyValueMapOperations).  
  
Apigee does not emit `CLIENT`, `PRODUCER`, or `CONSUMER` spans. In particular, outbound calls from Apigee to the target backend are not emitted as separate `CLIENT` spans; the outbound call is represented within the existing `INTERNAL` flow spans and the `traceparent` header is propagated to the target so that the target service can emit its own `SERVER` span and join the same trace.

### Variables in the `RESP_SENT` span

The following variables are visible in the `RESP_SENT` span. The **OTEL semantic variable** column shows the OpenTelemetry semantic convention name used when `spanSemantics` is set to `OTEL`; the **Attribute** column shows the legacy attribute name.

Legacy Variable | OTEL semantic variable | Attribute | Description  
---|---|---|---  
`REQUEST_URL` | `url.full` | `request.url` | Full URL of the incoming client request received by the proxy.  
`REQUEST_VERB` | `http.request.method` | `request.verb` | HTTP verb of the incoming client request (for example, `GET` or `POST`).  
`RESPONSE_STATUS_CODE` | `http.response.status_code` | `response.status.code` | Response status code returned by the target server.  
`ROUTE_NAME` | `gcp.apigee.route.name` | `route.name` | Name of the route rule that selected the target for this request.  
`ROUTE_TARGET` | `gcp.apigee.route.target` | `route.target` | Name of the target endpoint selected by the route rule.  
`TARGET_BASE_PATH` | `gcp.apigee.target.basepath` | `target.basepath` | Base path portion of the target URL.  
`TARGET_HOST` | `server.address` | `target.host` | Hostname of the target server contacted by the proxy.  
`TARGET_IP` | `server.address` | `target.ip` | Resolved IP address of the target server.  
`TARGET_NAME` | `gcp.apigee.target.name` | `target.name` | Name of the target endpoint defined in the API proxy.  
`TARGET_PORT` | `server.port` | `target.port` | TCP port used to connect to the target server.  
`TARGET_RECEIVED_END_TIMESTAMP` | `gcp.apigee.target.received_end_timestamp` | `target.received.end.timestamp` | Timestamp (epoch milliseconds) at which the proxy finished receiving the response from the target server.  
`TARGET_RECEIVED_START_TIMESTAMP` | `gcp.apigee.target.received_start_timestamp` | `target.received.start.timestamp` | Timestamp (epoch milliseconds) at which the proxy began receiving the response from the target server.  
`TARGET_SENT_END_TIMESTAMP` | `gcp.apigee.target.sent_end_timestamp` | `target.sent.end.timestamp` | Timestamp (epoch milliseconds) at which the proxy finished sending the request to the target server.  
`TARGET_SENT_START_TIMESTAMP` | `gcp.apigee.target.sent_start_timestamp` | `target.sent.start.timestamp` | Timestamp (epoch milliseconds) at which the proxy began sending the request to the target server.  
`TARGET_SSL_ENABLED` | `gcp.apigee.target.ssl_enabled` | `target.ssl.enabled` | Boolean indicating whether the connection to the target server used TLS.  
`TARGET_URL` | `url.full` | `target.url` | Full URL of the target server contacted by the proxy.  
  
### Variables in the `PROXY_POST_RESP_SENT` span

The following variables are visible in the `PROXY_POST_RESP_SENT` span. The **OTEL semantic variable** column shows the OpenTelemetry semantic convention name used when `spanSemantics` is set to `OTEL`; the **Attribute** column shows the legacy attribute name.

Legacy Variable | OTEL semantic variable | Attribute | Description  
---|---|---|---  
`API_PROXY_REVISION` | `gcp.apigee.proxy.revision` | `apiproxy.revision` | Revision number of the API proxy that handled the request.  
`APIPROXY_NAME` | `gcp.apigee.proxy.name` | `apiproxy.name` | Name of the API proxy that handled the request.  
`CLIENT_RECEIVED_END_TIMESTAMP` | `gcp.apigee.client.received_end_timestamp` | `client.received.end.timestamp` | Timestamp (epoch milliseconds) at which the proxy finished receiving the request from the client.  
`CLIENT_RECEIVED_START_TIMESTAMP` | `gcp.apigee.client.received_start_timestamp` | `client.received.start.timestamp` | Timestamp (epoch milliseconds) at which the proxy began receiving the request from the client.  
`CLIENT_SENT_END_TIMESTAMP` | `gcp.apigee.client.sent_end_timestamp` | `client.sent.end.timestamp` | Timestamp (epoch milliseconds) at which the proxy finished sending the response to the client.  
`CLIENT_SENT_START_TIMESTAMP` | `gcp.apigee.client.sent_start_timestamp` | `client.sent.start.timestamp` | Timestamp (epoch milliseconds) at which the proxy began sending the response to the client.  
`ENVIRONMENT_NAME` | `gcp.apigee.environment` | `environment.name` | Name of the Apigee environment in which the proxy executed.  
`FAULT_SOURCE` | `gcp.apigee.fault_source` | `message.header.X-Apigee-fault-source` | Source of the fault when an error occurs during proxy execution. Populated only on error flows.  
`IS_ERROR` | `gcp.apigee.is_error` | `is.error` | Boolean indicating whether the proxy execution ended in an error flow.  
`MESSAGE_ID` | `gcp.apigee.message.id` | `message.id` | Unique identifier assigned by Apigee to the request, useful for correlating logs and trace spans.  
`MESSAGE_STATUS_CODE` | `http.response.status_code` | `message.status.code` | Final response status code, including for calls without targets and for error flows.  
`PROXY_BASE_PATH` | `http.route` | `proxy.basepath` | Base path of the API proxy that matched the incoming request.  
`PROXY_CLIENT_IP` | `client.address` | `proxy.client.ip` | IP address of the client that sent the request to the proxy.  
`PROXY_NAME` | `gcp.apigee.proxy.name` | `proxy.name` | Name of the proxy endpoint within the API proxy that handled the request.  
`PROXY_PATH_SUFFIX` | `url.path` | `proxy.pathsuffix` | Portion of the request URL path that follows the proxy base path.  
`PROXY_URL` | `url.full` | `proxy.url` | Full URL of the proxy endpoint as received from the client.  
  
## Supported distributed tracing systems

**Recommendation:** For new deployments, choose one of the OpenTelemetry options (Cloud Trace with OpenTelemetry, or OpenTelemetry Collector). OpenCensus support is retained for compatibility with existing setups; OpenTelemetry supports higher sampling rates (up to 100%, vs 50% on OpenCensus), the W3C trace context standard, and a broader collector ecosystem.

You can configure your Apigee runtime to send trace data to the following distributed tracing systems:

Distributed tracing systems | Description  
---|---  
Cloud Trace with OpenTelemetry | Ideal for users who want a simple setup with OpenTelemetry and whose primary or only tracing backend is Cloud Trace. To send trace data to Cloud Trace with OpenTelemetry, do the following:

  1. Configure the Apigee runtime for Cloud Trace.
  2. Enable distributed tracing for Cloud Trace with OpenTelemetry.

**Note:** You are responsible for all costs associated with sending trace data to Cloud Trace. See the [pricing](https://docs.cloud.google.com/trace/pricing) and [quotas](https://docs.cloud.google.com/trace/limits) pages for details.  
OpenTelemetry Collector | Manage your own OpenTelemetry Collector to control trace data collection and processing. This is ideal if you need to send data to multiple systems (including non-Google ones) or customize how data is processed, grouped, or enhanced.  To send trace data to an OpenTelemetry Collector, do the following:

  1. Deploy and manage an OpenTelemetry Collector, as described in [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/).
  2. Enable distributed tracing for an OpenTelemetry Collector.

See Considerations when using an OpenTelemetry Collector for network reachability, TLS, and transport requirements that you must meet before enabling this option.  
Cloud Trace with OpenCensus | To send trace data to Cloud Trace with OpenCensus, do the following:

  1. Configure Apigee runtime for Cloud Trace (OpenCensus).
  2. Enable distributed tracing for Cloud Trace with OpenCensus.

**Note:** You are responsible for all costs associated with sending trace data to Cloud Trace. See the [pricing](https://docs.cloud.google.com/trace/pricing) and [quotas](https://docs.cloud.google.com/trace/limits) pages for details.  
Jaeger with OpenCensus | To send trace data to Jaeger with OpenCensus, enable distributed tracing for Jaeger.  
  
## Environment variables

The procedures on this page use the following environment variables. We recommend that you set them in your environment before you begin.
    
    
    **TOKEN** ="Authorization: Bearer $(gcloud auth application-default print-access-token)"
    **ENV_NAME** =YOUR_ENVIRONMENT_NAME
    **PROJECT_ID** =YOUR_GOOGLE_CLOUD_PROJECT_ID

Where: 

  * `**TOKEN**` defines the Authentication header with a bearer token. You use this header when calling Apigee APIs. For more information, see the reference page for the [print-access-token](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command.
  * **`ENV_NAME`** is the name of an environment in your organization.
  * **`PROJECT_ID`** is the ID of your Google Cloud project.



## Configure the Apigee runtime for OpenTelemetry or OpenCensus

The Apigee runtime supports two tracing standards: OpenTelemetry (recommended for new deployments) and OpenCensus. Choose the tracing standard that is appropriate for your environment, then follow the corresponding setup steps in the section below.

For OpenTelemetry, the Apigee runtime recognizes the `W3C` trace context header format, including the `traceparent`, `tracestate`, and `baggage` headers.

**Note: B3 headers are not supported for OpenTelemetry.** When you configure the Apigee runtime for OpenTelemetry, `B3` propagation headers (for example, `x-b3-traceid`, `x-b3-spanid`, `x-b3-sampled`, `x-b3-parentspanid`, `x-b3-flags`, and the single-header form `b3`) are **ignored** , even if present on the incoming request. Only the W3C trace context headers (`traceparent`, `tracestate`, and `baggage`) are honored for context propagation. Under OpenTelemetry, `B3` headers are ignored whether they are passed by the client or self-generated by a service mesh such as Istio; because the W3C trace context takes precedence over `B3`, the `B3` headers that Istio injects are also ignored. If your upstream callers currently emit only B3 headers, either configure them to also emit W3C `traceparent`, or use the OpenCensus configuration instead.**Note: Trace context propagation on outbound calls.** When distributed tracing is enabled, the Apigee runtime propagates the active trace context to the outbound requests made by the following policies and flows, so that the downstream service can continue the same trace: 

  * Target endpoint (backend target) requests, including route-rule targets
  * ServiceCallout
  * IntegrationCallout
  * VerifyIAM
  * Gen-AI Protection (`SanitizeUserPrompt` and `SanitizeModelResponse`)
  * SemanticCache (`SemanticCacheLookup` and `SemanticCachePopulate`)
  * JavaScript (`httpClient.send`)
  * ModelRouter (through the target that it selects)
  * Streaming Server-Sent Events (SSE) responses

For these policies and flows, Apigee propagates the W3C trace context headers (`traceparent`, `tracestate`, and `baggage`) when you use OpenTelemetry and the `B3` headers when you use OpenCensus.

## Configure pre-requisites for Cloud Trace (OpenTelemetry)

The Apigee (ApigeeX) runtime supports distributed tracing using Cloud Trace with OpenTelemetry. If you are using a customer-managed OpenTelemetry Collector, you can skip this section and proceed to Enabling distributed tracing for an OpenTelemetry Collector.

**Note:** These prerequisites apply only to the Cloud Trace route. They do not apply to a customer-managed OpenTelemetry Collector; if you use a collector, skip this section and see Enable distributed tracing for an OpenTelemetry Collector.

### Configure ApigeeX runtime for Cloud Trace

To configure your Apigee runtime for Cloud Trace, your Google Cloud project must have the following APIs enabled:

  * [Cloud Trace API](https://docs.cloud.google.com/trace/docs/reference) (trace.googleapis.com)
  * [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) (telemetry.googleapis.com)
  * [Service Usage API](https://docs.cloud.google.com/service-usage/docs/reference/rest) (serviceusage.googleapis.com)



Enabling these APIs allows your Google Cloud project to receive trace data over OpenTelemetry from authenticated sources.

To enable the APIs, do the following: 

  1. From the Google Cloud console, go to **APIs and Services** : 

[Go to APIs and Services](https://console.cloud.google.com/apis)

  2. Click **Enable APIs and Services** to open the **API Library**.
  3. From the **API Library** , enable the **Cloud Trace API** , the **Telemetry API** , and the **Service Usage API**. You can find each API by searching for it by name (for example, `Telemetry API`) from the API Library search bar.

**Note:** The **Telemetry API** is enabled from the **API Library** page (reached by clicking **Enable APIs and Services**), not from the **Enabled APIs & services** list. Use the API Library search bar to locate it.

In addition to enabling the APIs, you must grant the following roles to the service agent account:

  * `roles/telemetry.tracesWriter`
  * `roles/serviceusage.serviceUsageConsumer`



The specific service account depends on your Apigee environment:

  * **ApigeeX (non-hybrid):** Grant the roles to the **Apigee service agent** , a Google-managed P4SA (per-product per-project service account) that Apigee provisions automatically for the project. The service agent account has the format `service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com`.



See [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).

**Caution:** Granting these roles to the Apigee service agent (P4SA) is required. If the roles are missing, the Apigee runtime cannot export spans and no trace data reaches Cloud Trace.

## Enable distributed tracing (OpenTelemetry)

Before enabling distributed tracing, create the required environment variables.

### Enable distributed tracing for Cloud Trace

The following example shows you how to enable distributed tracing for Cloud Trace with OpenTelemetry:

  1. Execute this Apigee API call: 
         
         curl -H "**$TOKEN** " \
             -H "Content-Type: application/json" \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
             -X PATCH \
             -d '{
                   "exporter":"OPEN_TELEMETRY_CLOUD_TRACE",
                   "endpoint": "'"**$PROJECT_ID** "'",
                   "samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.05},
                   "traceProtocol": "OTLP",
                   "spanSemantics": "OTEL"
                 }'

The example request body consists of the following elements:

     * To support Cloud Trace with OpenTelemetry, the `exporter` parameter is set to `OPEN_TELEMETRY_CLOUD_TRACE` and the `traceProtocol` parameter is set to `OTLP`.
     * The `samplingRate` is set to 0.05. This means approximately 5% of the API calls are sent to distributed tracing. For OpenTelemetry, you can specify a sampling rate up to `1.0` (100%). For more information, see Performance considerations. **Note:** The `samplingRate` applies only to requests that do not carry a W3C `traceparent` header. When a request arrives with a `traceparent` header, Apigee uses the sampled flag in that header instead of the local `samplingConfig`. For details, see Header precedence over local configuration.
     * The `endpoint` parameter is set to the Google Cloud project ID that should receive the trace data (a bare project ID string, not a URL). **Note:** The `endpoint` parameter must be set to the project associated with the service account that was configured in the configuration step.**Alert:** The cloud trace project endpoint once set is immutable.
     * The `spanSemantics` parameter is optional and controls the attribute and span naming used on emitted spans. Supported values: 
       * `LEGACY` (default): use the historical Apigee attribute and span names shown in the **Attribute** column of the variable tables.
       * `OTEL`: use the OpenTelemetry semantic convention names shown in the **OTEL semantic variable** column. Requires `traceProtocol` to be `OTLP`.

A successful response looks similar to the following:
    
    {
      "exporter": "OPEN_TELEMETRY_CLOUD_TRACE",
      "endpoint": "my-gcp-project-id",
      "samplingConfig": {
        "sampler": "PROBABILITY",
        "samplingRate": 0.05
      },
      "traceProtocol": "OTLP",
      "spanSemantics": "OTEL"
    }




## Enable distributed tracing for an OpenTelemetry Collector

To enable distributed tracing for a customer-managed OpenTelemetry Collector, execute this Apigee API call:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
        -X PATCH \
        -d '{
              "exporter":"OPEN_TELEMETRY_COLLECTOR",
              "endpoint": "http://my-otel-collector.example.com:4318/v1/traces",
              "samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.05},
              "traceProtocol": "OTLP",
              "spanSemantics": "OTEL"
            }'

The example request body consists of the following elements:

  * To support a customer-managed OpenTelemetry Collector, the `exporter` parameter is set to `OPEN_TELEMETRY_COLLECTOR` and the `traceProtocol` parameter is set to `OTLP`.
  * The `endpoint` parameter is set to the full HTTP/HTTPS URL of your OpenTelemetry Collector's OTLP ingest endpoint (for example, `http://my-otel-collector.example.com:4318/v1/traces`). Unlike the Cloud Trace exporter, which takes a bare Google Cloud project ID, the `OPEN_TELEMETRY_COLLECTOR` exporter requires a complete URL that includes scheme, host, port, and path. Unlike the Cloud Trace endpoint, the OpenTelemetry Collector `endpoint` is mutable: you can reconfigure it later with another `PATCH` to `traceConfig`.
  * The `samplingRate` is set to 0.05. This means approximately 5% of the API calls are sent to distributed tracing. For more information, see Performance considerations. **Note:** The `samplingRate` applies only to requests that do not carry a W3C `traceparent` header. When a request arrives with a `traceparent` header, Apigee uses the sampled flag in that header instead of the local `samplingConfig`. For details, see Header precedence over local configuration.
  * The `otelCollectorSecurityScheme` parameter is optional and defaults to `NONE`. Set it to `MTLS` to enable mutual TLS between Apigee and the collector; see Configure mTLS for an OpenTelemetry Collector for the required `mtlsConfig` fields and the full API request body.



A successful response looks similar to the following:
    
    
    {
      "exporter": "OPEN_TELEMETRY_COLLECTOR",
      "endpoint": "http://my-otel-collector.example.com:4318/v1/traces",
      "samplingConfig": {
        "sampler": "PROBABILITY",
        "samplingRate": 0.05
      },
      "traceProtocol": "OTLP",
      "spanSemantics": "OTEL"
    }

### Considerations when using an OpenTelemetry Collector

Before you enable distributed tracing to a customer-managed OpenTelemetry Collector, review the following requirements.

#### Network reachability

  * Ensure that Apigee can reach the OpenTelemetry Collector.
  * To reach a collector that is not exposed on the public internet, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC).
  * If a forward proxy is present in your setup, configure it on the OpenTelemetry Collector. Connections from the message processor to the OpenTelemetry Collector are always direct.



#### Transport protocol

Only the OTLP/HTTP transport is supported for OpenTelemetry Collectors (port `4318` and path `/v1/traces` by OTLP convention). OTLP/gRPC (port `4317`) is not supported.

#### TLS and mTLS

Apigee supports two security schemes for the connection to an OpenTelemetry Collector, set through `otelCollectorSecurityScheme` on `traceConfig`:

  * **No security (HTTP)** (`NONE`, the default): Apigee connects to the collector over HTTP without mutual TLS.
  * **mTLS** (`MTLS`): mutual TLS, so the collector can also authenticate Apigee as the client. To enable mTLS, set `otelCollectorSecurityScheme` to `MTLS` on `traceConfig` and supply an `mtlsConfig` that references Apigee-managed keystores and truststores. See Configure mTLS for an OpenTelemetry Collector for the end-to-end setup.



### Configure mTLS for an OpenTelemetry Collector

Mutual TLS (mTLS) lets your OpenTelemetry Collector authenticate the Apigee runtime as the client, in addition to Apigee validating the collector's server certificate.

**Note:** The keystore, truststore, and alias names used in the following examples (for example, `otel-mtls`, `mp-client`, and `otel-mtls-truststore`) are examples only. You can use names of your choice.

Before you configure mTLS, verify the following prerequisites:

  * Your collector is configured to require client certificate authentication (for example, the OpenTelemetry Collector's `tls.client_ca_file` setting) and is deployed with a certificate authority (CA) file that contains the certificate chain you upload in step 1 of the setup.
  * The `endpoint` uses the `https://` scheme.
  * The `exporter` is `OPEN_TELEMETRY_COLLECTOR` and the `traceProtocol` is `OTLP`. mTLS is not applied to the `OPEN_TELEMETRY_CLOUD_TRACE` exporter, which authenticates by using Google Cloud OAuth instead.



#### Step 1: Upload the client key and certificate

Create a keystore for the Apigee client certificate that the collector authenticates, then upload the key and certificate as an alias:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /keystores \
        -X POST \
        -d '{ "name": "otel-mtls" }'
    
    curl -H "**$TOKEN** " \
        "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /keystores/otel-mtls/aliases?alias=mp-client&format=keycertfile" \
        -X POST \
        -F "keyFile=@client.key" \
        -F "certFile=@client.crt"

The `client.crt` file must be signed by a certificate authority that the collector's `tls.client_ca_file` trusts. For a self-signed setup, `client.crt` can be the same file that the collector uses as its `client_ca_file`.

#### Step 2: Upload the collector's server certificate

Create a truststore that the Apigee runtime uses to validate the collector's server certificate, then upload the collector's CA certificate as a CERT alias:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /keystores \
        -X POST \
        -d '{ "name": "otel-mtls-truststore" }'
    
    curl -H "**$TOKEN** " \
        "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /keystores/otel-mtls-truststore/aliases?alias=server-ca&format=keycertfile" \
        -X POST \
        -F "certFile=@server-ca.pem"

#### Step 3: Enable mTLS on `traceConfig`

PATCH the `traceConfig` to set the security scheme to `MTLS` and reference the keystore and truststore you just created:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
        -X PATCH \
        -d '{
              "exporter": "OPEN_TELEMETRY_COLLECTOR",
              "endpoint": "https://my-otel-collector.example.com:4318/v1/traces",
              "traceProtocol": "OTLP",
              "spanSemantics": "OTEL",
              "otelCollectorSecurityScheme": "MTLS",
              "mtlsConfig": {
                "keyStore":   "otel-mtls",
                "keyAlias":   "mp-client",
                "trustStore": "otel-mtls-truststore"
              }
            }'

The `mtlsConfig` object has three required fields:

  * `keyStore`: the name of the keystore that holds the Apigee client key and certificate from step 1 (for example, `otel-mtls`). To use an Apigee Reference instead, specify `ref://REFERENCE_NAME`.
  * `keyAlias`: the name of the KEY_CERT alias inside `keyStore` (for example, `mp-client`).
  * `trustStore`: the name of the keystore that holds the collector's server CA certificate from step 2 (for example, `otel-mtls-truststore`). To use an Apigee Reference instead, specify `ref://REFERENCE_NAME`.



Apigee enforces the following validation on `traceConfig` when `otelCollectorSecurityScheme` is `MTLS`:

  * `exporter` must be `OPEN_TELEMETRY_COLLECTOR`.
  * `traceProtocol` must be `OTLP`.
  * `endpoint` must use the `https://` scheme.
  * All three `mtlsConfig` fields must be populated. Missing any field returns HTTP 400.
  * The referenced keystores, aliases, and any references must already exist. Missing resources return HTTP 400.



#### Rotate the client key or certificate

To rotate the client key or certificate without a `traceConfig` change, upload new key material to the existing `mp-client` alias with a PUT:
    
    
    curl -H "**$TOKEN** " \
        "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /keystores/otel-mtls/aliases/mp-client" \
        -X PUT \
        -F "keyFile=@client-v2.key" \
        -F "certFile=@client-v2.crt"

The Apigee runtime detects the alias-revision change on its next configuration sync and rebuilds the mTLS OTLP exporter with the new credentials. No pod restart is required and no in-flight requests are dropped.

## Sampling criteria

The Apigee runtime decides whether to record a trace for each request by combining the incoming request headers with the environment trace configuration.

### W3C trace context header

Under the OpenTelemetry configuration, the runtime honors the [W3C trace context](https://www.w3.org/TR/trace-context/) `traceparent` header. The last byte of `traceparent` (the _trace-flags_ byte) carries the _sampled_ flag: a value of `01` indicates that the caller has already decided to record the trace, and `00` indicates that it has not.

The W3C trace context specification's [recommendations for the sampled flag](https://www.w3.org/TR/trace-context/#sampled-flag) advise that a component respect the incoming sampled flag when it makes a recording decision, and reflect a definitive recording decision in the flag. Apigee follows these recommendations: it respects the incoming sampled flag when deciding whether to record a trace (see Header precedence over local configuration) and sets the sampled flag on the `traceparent` header it propagates to downstream services to reflect whether the request is being recorded. As a security control against unwanted tracing driven by the incoming flag, set `sampler` to `OFF` (see Disable the distributed tracing configuration), which disables tracing even for requests whose `traceparent` has the sampled flag set.

### Header precedence over local configuration

When an incoming request carries a `traceparent` header, the Apigee runtime uses the sampled flag from that header instead of its local `samplingConfig`. A request with the sampled flag set to `01` is always traced; a request with the flag set to `00` is not traced. The environment-level `samplingConfig` applies only to requests that arrive without a `traceparent` header.

### Disabling trace

To disable tracing for every proxy in an environment (excludes proxy overrides), set `sampler` to `OFF` in the environment `traceConfig`. See Disable the distributed tracing configuration.

### Per-proxy overrides

To enable tracing for only a subset of proxies in an environment, leave the environment `samplingConfig` with `sampler` set to `OFF` and create a per-proxy override (with `sampler` set to `PROBABILITY` and a non-zero `samplingRate`) for each proxy you want to trace. See Override trace settings for API proxies.

### Performance impact of the sampling rate

The `samplingRate` you configure directly affects runtime performance. Every sampled request incurs additional CPU work on the message processor (span generation and export) and adds latency to the request path. As the sampling rate increases, so does the volume of traced traffic per MP, which can reduce throughput and increase tail latency (p95, p99). The impact grows with traffic volume: at low request rates the overhead is usually negligible, while at high request rates a high sampling rate can meaningfully reduce sustainable throughput and require additional MP capacity. In internal benchmarks, running at `samplingRate=1.0` (100% sampling) under sustained heavy traffic reduced throughput by up to approximately 15% compared to running with tracing disabled.

As a general guideline, keep `samplingRate` low (for example, `0.1` or lower) in production, and raise it only for specific proxies via per-proxy overrides when you need deeper visibility. For a detailed breakdown of the expected impact and capacity guidance, see Performance considerations.

## Performance considerations

A performance impact is expected when you enable distributed tracing for an Apigee runtime environment. The impact can result in increased memory usage, increased CPU requirements, and increased latency. The magnitude of the impact depends on the complexity of the API proxy (for example, the number of policies), the probabilistic sampling rate (set as the `samplingRate`), and most importantly on the traced traffic volume relative to the per-message-processor (MP) span export capacity.

The Apigee MP has a finite span export rate. With the default configuration, a single MP can sustainably export approximately **820 spans per second**. A typical API proxy execution emits approximately 10 spans (proxy preflow, target flow, postflows, attached policies), so a single MP can sustainably trace approximately **82 requests per second at 100% sampling**. Scaling MP replica count increases the aggregate ceiling linearly.

The following table summarizes the expected impact at `samplingRate=1.0` (100% probability) across two traffic regimes:

**Note:** The figures in the following table assume that incoming requests do not carry a W3C `traceparent` header. Requests that arrive with a `traceparent` header whose sampling byte is enabled (`1`) are always traced and take precedence over the configured `samplingRate`, which can change the effective trace volume and the resulting performance impact.Traffic regime (per MP) | Expected impact at `samplingRate=1.0` | Recommended action  
---|---|---  
Light traffic (less than approximately 82 traced requests per second per MP) | Throughput drops by approximately 1-2%; mean latency increases by approximately 1%; p99 latency increases by approximately 15-20%. Negligible in practice. | Safe to enable at 100%.  
Heavy traffic (significantly above approximately 82 traced requests per second per MP) | Throughput drops by approximately 14%; mean latency increases by approximately 24%; p75 latency increases by approximately 52%; error rate increases by approximately 1 percentage point. | Either lower `samplingRate` (for example, to `0.1` or `0.05`), or scale up your MP replica count so each MP serves fewer traced requests per second.  
  
For environments with high traffic and low latency requirements, the recommended probabilistic sampling rate is less than or equal to 10%. If you want to use distributed tracing to troubleshoot, consider increasing the probabilistic sampling (`samplingRate`) only for specific API proxies via per-proxy overrides.

## Configure Apigee runtimes for Cloud Trace (OpenCensus)

Both the Apigee runtime and the Apigee hybrid runtime support distributed tracing using Cloud Trace with OpenCensus. If you are using Jaeger, you can skip this section and proceed to Enabling distributed tracing for Jaeger with OpenCensus.

### Configure the Apigee runtime for Cloud Trace

To configure your Apigee runtime for Cloud Trace, your Google Cloud project must have the **Cloud Trace API** enabled.

To enable the API, do the following: 

  1. From the Google Cloud console, go to **APIs and Services** : 

[Go to APIs and Services](https://console.cloud.google.com/apis)

  2. Click **Enable APIs and Services**.
  3. Enable the **Cloud Trace API**.



### Configure Apigee hybrid runtime for Cloud Trace

To configure the Apigee hybrid runtime for Cloud Trace, enable the **Cloud Trace API**.

In addition to enabling the API, you must add the `iam.gserviceaccount.com` service account to use Cloud Trace with the hybrid runtime. To add the service account, along with the required `roles/cloudtrace.agent` role and keys, perform the following steps: 

  1. Create a new service account: 
         
         gcloud iam service-accounts create \
             apigee-runtime --display-name "Service Account Apigee hybrid runtime" \
             --project PROJECT_ID

  2. Add an IAM policy binding to the service account: 
         
         gcloud projects add-iam-policy-binding \
             PROJECT_ID --member "serviceAccount:apigee-runtime@PROJECT_ID.iam.gserviceaccount.com" \
             --role=roles/cloudtrace.agent --project PROJECT_ID

  3. Create a service account key and update your `overrides.yaml` as described in the following steps.
  4. Create a service account key: 
         
         gcloud iam service-accounts keys \
             create ~/apigee-runtime.json --iam-account apigee-runtime@PROJECT_ID.iam.gserviceaccount.com

Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  5. Add the service account to the `overrides.yaml` file. 
         
         envs:
          - name: ENV_NAME
            serviceAccountPaths:
              runtime: apigee-runtime.json
              synchronizer: apigee-sync.json
              udca: apigee-udca.json

  6. Apply the changes to the runtime using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm upgrade ENV_NAME apigee-env/ \
             --namespace APIGEE_NAMESPACE \
             --set env=ENV_NAME \
             --atomic \
             -f overrides.yaml




## Enable distributed tracing (OpenCensus)

Before enabling distributed tracing, create the required environment variables.

### Enable distributed tracing for Cloud Trace with OpenCensus

The following example shows you how to enable distributed tracing for Cloud Trace with OpenCensus:

  1. Execute this Apigee API call: 
         
         curl -H "**$TOKEN** " \
             -H "Content-Type: application/json" \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
             -X PATCH \
             -d '{
                   "exporter":"CLOUD_TRACE",
                   "endpoint": "'"**$PROJECT_ID** "'",
                   "samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.1}
                 }'

The example request body consists of the following elements:

     * To support Cloud Trace, the `exporter` parameter is set to `CLOUD_TRACE`. The `traceProtocol` parameter, which isn't specified, defaults to `OpenCensus`.
     * The `endpoint` parameter is set to the Google Cloud project where you want the trace to be sent.
     * The `samplingRate` is set to 0.1. This means approximately 10% of the API calls are sent to distributed tracing. For OpenCensus, the maximum configurable sampling rate is `0.5`. **Alert:** The `endpoint` parameter, once set, cannot be updated.

A successful response looks similar to the following:
    
    {
      "exporter": "CLOUD_TRACE",
      "endpoint": "staging",
      "samplingConfig": {
        "sampler": "PROBABILITY",
        "samplingRate": 0.1
      }
    }




### Enable distributed tracing for Jaeger with OpenCensus

The following example shows you how to enable distributed tracing for Jaeger:
    
    
    curl -s -H "**$TOKEN** " \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
        -X PATCH \
        -H "content-type:application/json" -d '{
        "samplingConfig": {
        "samplingRate": 0.4,
        "sampler": "PROBABILITY"},
        "endpoint": "http://DOMAIN:9411/api/v2/spans",
        "exporter": "JAEGER"
        }'

In this example:

  * To support Jaeger, the `exporter` parameter is set to `JAEGER`. The `traceProtocol` parameter, which isn't specified, defaults to `OpenCensus`.
  * The `endpoint` parameter is set to where Jaeger is installed and configured. **Alert:** The `endpoint` parameter, once set, cannot be updated.
  * The `samplingRate` is set to 0.4. This means approximately 40% of the API calls are sent to distributed tracing.



A performance impact is expected when you enable distributed tracing for an Apigee runtime environment. The impact can result in increased memory usage, increased CPU requirements, and increased latency. The magnitude of the impact will depend in part upon the complexity of the API proxy (for example, the number of policies) and the probabilistic sampling rate (set as the `samplingRate`). The higher the sampling rate, the higher the impact on performance.

For more information, see Performance considerations.

**Note: Configuration propagation delay.** A successful API response to `PATCH .../traceConfig` confirms that the configuration was accepted by the control plane. The Apigee runtime polls for configuration updates, so a change typically takes effect on the runtime within **approximately one to two minutes** after the API response. When verifying a configuration change, allow this propagation window before investigating further. Use the `revisionId` and `updateTime` fields returned by the API (see View the distributed tracing configuration) to confirm the control-plane state.

## View the distributed tracing configuration

To view the existing distributed tracing configuration in your runtime, log in to your runtime and then run the following command: 
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig

When you run the command, you can see a response similar to the following:
    
    
    {
      "exporter": "CLOUD_TRACE",
      "endpoint": "my-gcp-project-id",
      "samplingConfig": {
        "sampler": "PROBABILITY",
        "samplingRate": 0.1
      },
      "revisionId": "7",
      "updateTime": "2026-06-08T14:25:13.512000Z"
    }

The `revisionId` increments with each successful update and the `updateTime` reflects the server timestamp of the most recent change. Use these two fields to confirm that the control plane has accepted a configuration update; both are also returned by the `PATCH .../traceConfig` response.

## Update the distributed tracing configuration

The following command shows you how to update the existing distributed tracing configuration for Cloud Trace:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
        -X PATCH \
        -d '{
              "samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.6}
            }'

When you run the command, you can see a response similar to the following:
    
    
    {
      "samplingConfig": {
        "sampler": "PROBABILITY",
        "samplingRate": 0.6
      },
      "traceProtocol": "OTLP"
    }

In this example, the sampling rate is updated to `0.6`. To update the configuration for Jaeger, set the `exporter` field in the request to `JAEGER`.

## Disable the distributed tracing configuration

The following example shows how to disable distributed tracing configured for Cloud Trace:
    
    
    curl -H "**$TOKEN** " \
        -H "Content-Type: application/json" \
        https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig \
        -X PATCH \
        -d '{
              "samplingConfig": {"sampler": "OFF"}
            }'

**Note:** Setting `sampler` to `OFF` disables tracing for every request in the environment, including requests that arrive with a W3C `traceparent` header whose sampled flag is set. The runtime only consults `samplingRate` when `sampler` is `PROBABILITY`. See Sampling criteria for details.

When you run the command, you can see a response similar to the following:
    
    
    {
      "samplingConfig": {
        "sampler": "OFF"
      },
      "traceProtocol": "OTLP"
    }

## Override trace settings for API proxies

When you enable distributed tracing in your Apigee runtime, all the API proxies in the runtime use the same configuration for tracing. However, you can override the distributed tracing configuration for an API proxy or a group of API proxies. This provides you more granular control over the tracing configuration.

The following example overrides the distributed tracing configuration for the `hello-world` API proxy:
    
    
    curl -s -H "**$TOKEN** " \
         https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig/overrides \
         -X POST \
         -H "content-type:application/json" \
         -d '{"apiProxy": "hello-world","samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.1}}'

You can override the configuration to troubleshoot problems specific to an API proxy without having to change the configuration of all the API proxies.

### Update trace settings overrides

To update an override of the tracing configuration for an API proxy or group of API proxies, use the following steps: 

  1. Use the following command to retrieve any existing overrides of the tracing configuration: 
         
         curl -s -H "**$TOKEN** " \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig/overrides \
             -X GET 

This command should return a response similar to the following, which contains a "name" field that identifies the proxy or proxies governed by the override: 
         
         {
           "traceConfigOverrides": [
             {
               **"name": "dc8437ea-4faa-4b57-a14f-4b8d3a15fec1",**
               "apiProxy": "proxy1",
               "samplingConfig": {
                 "sampler": "PROBABILITY",
                 "samplingRate": 0.25
               }
             }
           ]
         }

  2. To update the proxy, use the value of the "name" field to send a POST request to the override configuration for that proxy,along with the updated field values. For example: 
         
         curl -s -H "**$TOKEN** " \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig/overrides/**dc8437ea-4faa-4b57-a14f-4b8d3a15fec1** \
             -X POST \
             -H "content-type:application/json" \
             -d '{"apiProxy": "proxy1","samplingConfig": {"sampler": "PROBABILITY","samplingRate": 0.05}}'




### Delete trace setting overrides

To delete an override of the tracing configuration for an API proxy or group of API proxies, use the following steps: 

  1. Use the following command to retrieve any existing overrides of the tracing configuration: 
         
         curl -s -H "**$TOKEN** " \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig/overrides \
             -X GET 

This command should return a response similar to the following, which contains a "name" field that identifies the proxy or proxies governed by the override: 
         
         {
           "traceConfigOverrides": [
             {
               **"name": "dc8437ea-4faa-4b57-a14f-4b8d3a15fec1",**
               "apiProxy": "proxy1",
               "samplingConfig": {
                 "sampler": "PROBABILITY",
                 "samplingRate": 0.25
               }
             }
           ]
         }

  2. To delete the proxy, use the value of the "name" field to send a DELETE request to the override configuration for that proxy,along with the updated field values. For example: 
         
         curl -s -H "**$TOKEN** " \
             https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENV_NAME** /traceConfig/overrides/**dc8437ea-4faa-4b57-a14f-4b8d3a15fec1** \
             -X DELETE \




## Troubleshoot distributed tracing

To troubleshoot distributed tracing, do the following:

  * Verify the distributed tracing configuration using the `traceConfig` API to ensure it matches your needs.
  * Confirm the service account has the correct IAM permissions (roles) in the destination project.
  * If using Cloud Trace with OpenTelemetry, check for incoming spans and any API enablement or quota errors.
  * If using a customer-managed OpenTelemetry Collector, do the following: 
    * Confirm Apigee can reach the Collector endpoint. Check your Private Service Connect (PSC) setup if used.
    * Check OpenTelemetry Collector logs for data or connection issues.
    * Ensure the collector's TLS certificate is valid.
  * Examine Apigee runtime logs for trace export errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
