---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference/
title: Microservices observability reference information \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:45.540336+00:00
---

# Microservices observability reference information  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Microservices observability reference information Stay organized with collections  Save and categorize content based on your preferences. 

## Configuration data

The configuration data found in the environment variables is defined in the following table.

**Fields** |  **Spec**  
---|---  
`project_id` | String  
  
The identifier of the project to which observability data is sent. If empty, the gRPC observability plugin attempt to fetch the project ID from the environment variables, or from the default credentials.  
  
If not found, the observability init functions return an error.  
`cloud_logging` | Object  
  
The logging options are categorized in this table.   
When absent, logging is disabled.  
`cloud_logging.client_rpc_events[]` | List  
  
A list of `client_rpc_events` configurations, representing the configuration for outgoing RPCs from the binary.  
  
The `client_rpc_events` configurations are evaluated in text order, the first one matched is used. If an RPC doesn't match an entry, it continues to the next entry in the list.  
`cloud_logging.client_rpc_events[].methods[]` | List [String]  
  
A list of method identifiers.   
  
By default, the list is empty, matching no methods.  
  
The value of the method is in the form of `[service]/[method]`.  
  
`*` is accepted as a wildcard for:  


  * The method name. If the value is `[service]/*`, it matches all methods in the specified service.
  * The whole value of the field which matches any `[service]/[method]`. It's not supported when client_rpc_events[].exclude is true.
  * The * wildcard cannot be used on the service name independently, `*/[method]` is not supported.

  
The service name, when specified, must be the fully qualified service name, including the package name.  
  
Examples:  


  * `goo.Foo/Bar` selects only the method `Bar` from service `goo.Foo`, here `goo` is the package name.
  * `goo.Foo/*` selects all methods from service `goo.Foo`
  * `*` selects all methods from all services.

  
`cloud_logging.client_rpc_events[].exclude` |  Bool  
  
Whether the methods denoted by the `client_rpc_events[].methods[]` should be excluded from logging.  
  
The default value is false, meaning the methods denoted by the `client_rpc_events[].methods[]` are included in the log record.  
  
If the value is true, the wildcard (*) cannot be used as the whole value in the `client_rpc_events[].methods[].`  
`cloud_logging.client_rpc_events[].max_metadata_bytes` | Int  
  
Maximum number of bytes of metadata to log. If the size of the metadata is greater than the defined limit, key-value pairs that exceed the limit are not logged.   
  
The default value is 0, meaning no metadata are logged.  
`cloud_logging.client_rpc_events[].max_message_bytes` | Int  
  
Maximum number of bytes of each message to log. If the size of the message is greater than the defined limit, content that exceeds the limit is truncated.   
  
The default value is 0, meaning no message payload is logged.  
`cloud_logging.server_rpc_events[]` | List  
  
A list of `server_rpc_events` configurations, represents the configuration for incoming RPCs to the binary.  
  
The `server_rpc_events` configurations are evaluated in text order, the first one matched is used. If an RPC doesn't match an entry, it continues to the next   
  
entry in the list.  
`cloud_logging.server_rpc_events[].methods[]` | List [String]  
  
A list of strings which can select a group of methods.   
  
By default, the list is empty, matching no methods.  
  
The value of the method is in the form of `[service]/[method]`.  
  
`*` is accepted as a wildcard for:  


  * The method name. If the value is `[service]/*`, it matches all methods in the specified service.
  * The whole value of the method which matches any `[service]/[method]`. It's not supported when `server_rpc_events[].exclude` is true.
  * The * wildcard cannot be used on the service name independently, `*/[method]` is not supported.

  
The service name, when specified, must be the fully qualified service name, including the package name.  
  
Examples:  


  * `goo.Foo/Bar` selects only the method `Bar` from service `goo.Foo`, here `goo` is the package name.
  * `goo.Foo/*` selects all methods from service `goo.Foo`
  * `*` selects all methods from all services.

  
`cloud_logging.server_rpc_events[].exclude` | Bool  
  
Whether the methods denoted by the `server_rpc_events[].methods[]` should be excluded from logging.  
  
The default value is false, meaning that the methods denoted by the `server_rpc_events[].methods[]` are logged.  
  
If the value is true, the wildcard (*) cannot be used as the whole value in any entry of `server_rpc_events[].methods[]`.  
`cloud_logging.server_rpc_events[].max_metadata_bytes` |  Int  
  
Maximum number of bytes of metadata to log. If the size of the metadata is greater than the defined limit, key-value pairs that exceed the limit are not logged.  
  
The default value is 0, meaning no metadata are logged.  
`cloud_logging.server_rpc_events[].max_message_bytes` |  Int  
  
Maximum number of bytes of each message to log. If the size of the message is greater than the defined limit, content that passes the limit is truncated.   
  
The default value is 0, meaning no message payload is logged.  
`cloud_monitoring` | Object  
  
Enables Cloud Monitoring. There are no configuration options. If you provide an empty configuration objection, monitoring is enabled. If you do not provide a configuration object, monitoring is disabled.  
  
For example, when no other options are specified, an empty configuration section enables monitoring.  

    
    
    export GRPC_GCP_OBSERVABILITY_CONFIG='{
        "project_id": "your-project-here",
        "cloud_monitoring": {
        }
    }'
      
  
`cloud_trace` | Object  
  
An empty configuration section enables tracing with the default configuration options. If you do not provide a configuration object, tracing is disabled.   
  
For example, an empty configuration section enables tracing with default configuration options.  

    
    
    export GRPC_GCP_OBSERVABILITY_CONFIG='{
        "project_id": "your-project-here",
        "cloud_trace": {
        }
    }'
    

  
  
When tracing is enabled, even with a `0` sampling rate, the decision to sample a particular trace is propagated.  
  
`cloud_trace.sampling_rate` | Number  
  
The global setting that controls the probability of an RPC being traced. For example:  


  * The value `0.05` means that there's a 5% chance for an RPC to be traced.
  * The value `1.0` means that every call is traced. 
  * The value `0` means don't start new traces.

  
By default, the sampling_rate is `0`.  
  
The plugin respects the sampling decision upstream. If an RPC is chosen for sampling upstream, the plugin collects spans and uploads the data to the backend, regardless of the sampling rate setting for the plugin.  
`labels` | Object  
  
A JSON object containing a set of key-value pairs. Both key and value are strings.  
  
Labels are applied on Cloud Logging, Cloud Monitoring, and Cloud Trace together.  
  
## Trace definitions

This section provides information on tracing.

### Trace context propagation

For cross-service tracing to work, the service owner must support the propagation of trace context received from upstream (or started by itself) to downstream. Trace context is propagated among services through gRPC metadata. Make sure that you enable the Cloud Monitoring, Cloud Logging, Cloud Trace APIs, and Microservices APIs, which let services in this configuration to report their telemetry data to the appropriate service.

Without propagation support, downstream services can't generate spans for a trace. Existing spans are not affected. The Microservices observability plugins support the [**OpenCensus Binary Format**](https://github.com/census-instrumentation/opencensus-specs/blob/master/encodings/BinaryEncoding.md) for encoding and encoding trace context.

### Spans

The name of a span is formatted as follows:

Type | Example value | Usage  
---|---|---  
RPC span | ` [Sent|Recv].helloworld.Greeter.SayHello ` | The span name is the full method name, connected by dots, with no prefix slash.  
Span names are prefixed with `Sent.` for CLIENT RPC span and `Recv.` for SERVER RPC span in front of the full method name.  
Attempt span | ` Attempt.helloworld.Greeter.SayHello ` | Attaching a prefix `Attempt.` in front of the full method name.  
  
### Span labels

The integrations provide different span labels.

For attempt spans, two additional retry-related attributes (span labels) are attached:

**Label** | **Example value** | **Usage**  
---|---|---  
previous-rpc-attempts | `0` | The retry attempts count before this RPC.  
transparent-retry | `True/False ` | Whether this RPC is initiated by a transparent retry.  
  
## Metrics definitions

The following metrics are available and are displayed in a dashboard named **Microservices (gRPC) Monitoring** for common user journeys.

The following are metrics from the gRPC client-side metrics:

**Metric Name** | **Description** | **Kind, type, unit** | **Labels**  
---|---|---|---  
`custom.googleapis.com/opencensus/grpc.io/client/started_rpcs` | The count of client RPCs attempts started, including those that have not completed. | Cumulative, Int64, 1 | `grpc_client_method`  
`custom.googleapis.com/opencensus/grpc.io/client/completed_rpcs` | The count of client RPCs completed, for example, when a response is received or sent by the server. | Cumulative, Int64, 1 | `grpc_client_method`, `grpc_client_status`  
`custom.googleapis.com/opencensus/grpc.io/client/roundtrip_latency` | End-to-end time taken to complete an RPC attempt including the time it takes to pick a subchannel. | Cumulative, Distribution, ms | `grpc_client_method`  
`custom.googleapis.com/opencensus/grpc.io/client/api_latency` | The total time taken by the gRPC library to complete an RPC from the application's perspective. | Cumulative, Distribution, ms | `grpc_client_method`, `grpc_client_status`  
`custom.googleapis.com/opencensus/grpc.io/client/sent_compressed_message_bytes_per_rpc` | The total bytes (compressed, not encrypted) sent across all request messages per RPC attempt. | Cumulative, Distribution, By | `grpc_client_method`, `grpc_client_status`  
`custom.googleapis.com/opencensus/grpc.io/client/received_compressed_message_bytes_per_rpc` | The total bytes (compressed, not encrypted) received across all response messages per RPC attempt. | Cumulative, Distribution, By | `grpc_client_method`, `grpc_client_status`  
  
The following gRPC server side metrics are available:

**Metric Name** | **Description** | **Kind, type, unit** | **Labels**  
---|---|---|---  
`custom.googleapis.com/opencensus/grpc.io/server/started_rpcs` |   
The count of RPCs ever received at the server, including RPCs that have not completed. | Cumulative, Int64, 1 | `grpc_server_method`  
`custom.googleapis.com/opencensus/grpc.io/server/completed_rpcs` |   
The total count of RPCs completed, for example, when a response is sent by the server. | Cumulative, Int64, 1 | `grpc_server_method`, `grpc_server_status`  
`custom.googleapis.com/opencensus/grpc.io/server/sent_compressed_message_bytes_per_rpc` |   
The total bytes (compressed not encrypted) sent across all response messages per RPC. | Cumulative, Distribution, By | `grpc_server_method`, `grpc_server_status`  
`custom.googleapis.com/opencensus/grpc.io/server/received_compressed_message_bytes_per_rpc` |   
The total bytes (compressed not encrypted) received across all request messages per RPC. | Cumulative, Distribution, By | `grpc_server_method`, `grpc_server_status`  
`custom.googleapis.com/opencensus/grpc.io/server/server_latency ` |   
The total time taken by an RPC from server transport's (HTTP2 / inproc / cronet) perspective. | Cumulative, Distribution, ms | `grpc_server_method`  
  
Each distribution in the table above contains a histogram with buckets as follows:

  * Size in bytes: 0, 1024, 2048, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824, 4294967296

  * Latency in ms: 0, 0.01, 0.05, 0.1, 0.3, 0.6, 0.8, 1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 40, 50, 65, 80, 100, 130, 160, 200, 250, 300, 400, 500, 650, 800, 1000, 2000, 5000, 10000, 20000, 50000, 100000




Tag description:

  * `grpc_client_method`: Full gRPC method name, including package, service and method, for example, `google.bigtable.v2.Bigtable/CheckAndMutateRow`
  * `grpc_client_status`: gRPC server status code received, for example, `OK`, `CANCELLED`, `DEADLINE_EXCEEDED`
  * `grpc_server_method`: Full gRPC method name, including package, service and method, for example, `com.exampleapi.v4.BookshelfService/Checkout`
  * `grpc_server_status`: gRPC server status code returned, for example, `OK`, `CANCELLED`, `DEADLINE_EXCEEDED`



## Log record definitions

The Microservices observability logs are uploaded to Cloud Logging using the log name (`PROJECT_ID` is the placeholder for the string representing your project):
    
    
    logName=projects/[PROJECT_ID]/logs/microservices.googleapis.com%2Fobservability%2Fgrpc
    

The following is the JSON representation of the generated log record:
    
    
    {
        "authority": string,
        "callId": string,
        "type": string,
        "logger": string,
        "serviceName": string,
        "methodName": string,
        "peer": {
            "type": string,
            "address": string,
            "ipPort": int
        },
        "payload": {
            "timeout": string,
            "metadata":
                {
                    string: string,
                    string: string
                },
            "statusCode": string,
            "statusMessage": string,
            "statusDetails": string,
            "message": string,
            "messageLength": int,
        },
        "sequenceId": int
    }
    
    

The following table describes the fields in the log entry:

**Fields** | **Spec**  
---|---  
authority | String  
  
A single process can be used to run multiple virtual servers with different identities.  
  
The authority is the name of such a server identity. It's typically a portion of the URI in the form of host or host:port.  
callId | String  
  
Uniquely identifies a [client/server] call that is an UUID. Each call can have several log entries. They all have the same callId.  
type | String  
  
The type of the log event.  
  
Types of event are:   
`EVENT_TYPE_UNKNOWN`  
`CLIENT_HEADER`  
`SERVER_HEADER`  
`CLIENT_MESSAGE`  
`SERVER_MESSAGE`  
`CLIENT_HALF_CLOSE`  
`SERVER_TRAILER`  
`CANCEL`  
logger | String  
  
The type of the event logger.  
  
Types of event logger are:   
`LOGGER_UNKNOWN`, `CLIENT`, `SERVER`  
serviceName | String  
  
The name of the service.  
methodName | String  
  
The name of the RPC method.  
peer | Object  
  
Peer address information. On the client side, peer is logged on server header events and trailer events. On the server side, peer is always logged on the client header event.  
peer.type | String  
  
The type of the address, whether it's IPv4, IPv6, or UNIX.  
peer.address | String  
  
The content of the address.  
peer.ip_port | Int  
  
The port number for the address. Only available for IPv4 and IPv6 addresses.  
payload | Object  
  
Payload can include a combination of metadata, timeout, message, and status depending on the event.   
  


  * For message events, payload is actual data passed as client/server messages and length of message.
  * For header events, payload includes the header name and value.
  * For trailer events, payload includes status details along with trailer metadata (if present).
  * For client header events, if timeout is set, payload includes timeout as well.

  
payload.timeout | String  
  
A string representing `google.protobuf.Duration`, such as "1.2 s".  
  
The RPC timeout value.  
payload.metadata | Mapping[String, String]  
  
Used by header event or trailer event.  
payload.message | String (Bytes)  
  
The message payload.  
payload.messageLength | Int  
  
Size of the message, regardless of whether the full message is being logged (for example, they could be truncated or omitted).  
payload.statusCode | String  
  
The gRPC status code.  
payload.statusMessage | String  
  
The gRPC status message.  
payload.statusDetails | String  
  
The value of the `grpc-status-details-bin` metadata key, if any. This is always an encoded `google.rpc.Status` message.  
payloadTruncated | Bool  
  
True if the message or metadata field is either truncated or omitted because of configuration options.  
sequenceId | Int  
  
The message sequence ID for this call. The first message has a value of 1, to disambiguate from an unset value. The purpose of this field is to detect missing entries in environments where durability or ordering is not guaranteed.  
  
## Resource labels

Resource labels identify the source that generates observability data. Each resource label is a key-value pair, where keys are predefined values that are specific to the source environment (for example, GKE or Compute Engine).

For metrics and tracing on GKE deployments, resource labels are populated by default except for the container name and namespace name. The missing values can be populated using the [Downward API](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/#the-downward-api).

The following are the environment variable keys:

  * CONTAINER_NAME
  * NAMESPACE



For example, the `env` section in the following includes two resource labels:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: app1
      name: app1
    spec:
      replicas: 2
      selector:
        matchLabels:
          run: app1
      template:
        metadata:
          labels:
            run: app1
        spec:
          containers:
            - image: 'o11y-examples:1.00'
              name: container1
              ports:
                - protocol: TCP
                  containerPort: 50051
              env:
                - name: CONTAINER_NAME
                  value: container1
                - name: NAMESPACE
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.namespace
    
    

## Custom labels

Custom labels represent additional user-provided information in the observability data. Labels consist of a key and a value. The key-value pair is attached to tracing data as span labels, to metrics data as metrics labels, and to logging data as log entry labels. All custom labels are of the STRING type.

You can provide custom labels in the configuration by specifying a list of key- value pairs for `labels`. The implementation reads the configuration and creates a separate label for each key-value pair, then attaches the label to the observability data. For example:
    
    
    "labels": {
        "DATACENTER": "SAN_JOSE_DC",
        "APP_ID": "24512"
      }
    

Each log entry has the following additional labels in them:
    
    
    {
       "DATACENTER": "SAN_JOSE_DC"
       "APP_ID": "24512"
    }
    

## What's next

  * For information on metrics kinds and types, see [Value types and metric kinds](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).
  * For information on distributions, see the [Distribution reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution).
  * For information about charting Distribution metrics, see [Distribution metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics).
  * For information on units (such as `1`, `ms` and `By`), see the [unit field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
