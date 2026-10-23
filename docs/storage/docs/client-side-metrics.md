---
url: https://docs.cloud.google.com/storage/docs/client-side-metrics/
title: Use gRPC client-side metrics \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:41.851604+00:00
---

# Use gRPC client-side metrics  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/client-side-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use gRPC client-side metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to emit [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api) client-side metrics to Cloud Monitoring when you use gRPC to interact with Cloud Storage using one of the following supported interfaces:

  * [Cloud Storage C++ client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-cpp)

  * [Cloud Storage Go client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-go)

  * [Cloud Storage Java client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-java), version 2.41.0 and later



  * [Apache Beam connector on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage#enable-connector-grpc), version 2.2.26 and later 


  * [Cloud Storage connector on Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage)



Client-side metrics can be used to monitor the performance of the client application that interacts with Cloud Storage using gRPC. The client-side metric differs from server-side metrics, which provide insight on Cloud Storage performance from the server-side perspective.

## How it works

You can opt in to emit client-side metrics to Cloud Monitoring when using gRPC to interact with Cloud Storage using one of the supported interfaces. You can view client-side metrics using the Metrics Explorer to help you monitor and optimize interactions between Cloud Storage and the gRPC client, manage usage, and troubleshoot performance bottlenecks and technical issues.

## Pricing

Cloud Storage client-side metrics are non-chargeable, meaning you can emit, store, and access Cloud Storage client-side metrics without incurring [Cloud Monitoring charges](https://docs.cloud.google.com/monitoring/pricing#monitoring-costs). For more information about pricing, refer to [Google Cloud Observability pricing](https://docs.cloud.google.com/monitoring/pricing).

## Before you begin

To use client-side metrics, you must first complete the following steps:

  1. Verify that the Cloud Storage client library or connector you want to use supports gRPC. The following Cloud Storage client libraries and connectors support gRPC:

     * [C++, Java, or Go client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-client-library)

     * [Apache Beam IO on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage#enable-connector-grpc)

     * [Cloud Storage connector on Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage)

  2. [Set up authentication](https://docs.cloud.google.com/storage/docs/reference/libraries#authentication).

  3. Enable the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api#enabling-api-v3).

  4. Enable the Cloud Storage API.

[Go to Cloud Storage API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com&_ga=2.70110096.1642044780.1726157710-823539626.1726157710)

  5. Set the required roles and permissions needed to emit client-side metrics.




### Required roles

To set the permissions that you need to emit gRPC client-side metrics to Cloud Monitoring, grant the [Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) IAM role on the service account used by the gRPC client.

This predefined role contains the permissions required to emit gRPC client-side metrics to Cloud Monitoring. To see the exact permissions that are required, refer to the Required permissions section:

#### Required permissions

  * `monitoring.timeSeries.create`



This IAM permission is included in the following Cloud Storage predefined roles:

  * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)
  * [Storage Object User](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)



You might also be able to get these permissions with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). For more information about the Monitoring Metric Writer role, see [IAM documentation about `roles/monitoring.metricWriter`](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter).

#### Considerations

  * If you're using [Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) on Managed Service for Apache Spark, you need to grant the Monitoring Metric Writer (`roles/monitoring.metricWriter`) IAM role to the [Managed Service for Apache Spark virtual machine (VM) service account](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage).

  * If you're using Apache Beam connector on Dataflow, you need to grant the Monitoring Metric Writer (`roles/monitoring.metricWriter`) IAM role to the [Dataflow worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account).


**Note:** By default, both Managed Service for Apache Spark VM service account and Dataflow worker service account use the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

## View metrics in Metrics Explorer

Use the following instructions to view Cloud Storage gRPC client-side metrics in the Metrics Explorer.

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/projectselector/monitoring/metrics-explorer?supportedpurview=project,folder,organizationId)

  2. Select the project you want to view metrics for.

  3. From the **Metric** drop-down menu, click **Select a metric**.

  4. In the **Filter by resource or metric name** search bar, enter **`storage.googleapis.com/Client`** or search for the metric you want to apply by metric name and click **Apply**. To add more than one metric, click **Add query**.

Cloud Storage applies the metrics to your project. You can filter or aggregate your metrics using the following drop-down menus:

     * To select and view a subset of your data based on specified criteria, use the **Filter** drop-down menu.

     * To combine multiple data points into a single value and see a summarized view of your metrics, use the **Aggregation** drop-down menu.

Let your application run for at least a minute before you check for any published metrics.




To view the metrics you've added to your project using a dashboard, see [Dashboards overview](https://docs.cloud.google.com/monitoring/dashboards).

## Metrics descriptions

The following sections outline Cloud Storage client-side metrics that can be used to monitor the performance of the gRPC client.

### Client per-attempt metrics

The following metrics gather performance data about individual attempts made by a client to communicate with a server. Client per-attempt metrics can help you measure retry behavior, bottlenecks, and optimize communication between a client and server.

**Note:** The `grpc.lb.locality` attribute is only present when requests use direct connectivity. If no value is present for `grpc.lb.locality`, it means that direct connectivity isn't enabled. For more information about direct connectivity, see VPC Service Controls documentation on [direct connectivity to APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#direct-connectivity).Full metric | Description | Instrument type | Unit | Attributes  
---|---|---|---|---  
`storage.googleapis.com/client/grpc/client/attempt/started` | `Preview`. The total number of RPC attempts started, including those that haven't completed. | Counter | `{attempt}` | 

  * `grpc.method`: the full gRPC method name, including package, service, and method.
  * `grpc.target`: canonicalized target URI used when created gRPC channel.

  
`storage.googleapis.com/client/grpc/client/attempt/duration` | `Preview`. The end-to-end time it takes to complete an RPC attempt, including the time it takes to pick a subchannel. | Histogram | `s` | 

  * `grpc.method`: full gRPC method name, including package, service, and method.
  * `grpc.target`: canonicalized target URI used when creating gRPC channel.
  * `grpc.status`: gRPC server status code received, such as `OK`, `CANCELLED`, or `DEADLINE_EXCEEDED`.
  * `grpc.lb.locality`: the locality the traffic is being sent to. This will be set to the resolver attribute passed down from the `weighted_target` policy, or the empty string if the resolver attribute is unset.

  
`storage.googleapis.com/client/grpc/client/attempt/sent_total_compressed_message_size` | `Preview`. The total bytes, compressed but not encrypted, that are sent across all request messages except metadata per RPC attempt. This doesn't include gRPC or transport framing bytes. | Histogram | `By` | 

  * `grpc.method`: full gRPC method name, including package, service, and method.
  * `grpc.target`: canonicalized target URI used when creating gRPC channel.
  * `grpc.status`: gRPC server status code received, such as `OK`, `CANCELLED`, or `DEADLINE_EXCEEDED`.
  * `grpc.lb.locality`: the locality the traffic is being sent to. This will be set to the resolver attribute passed down from the `weighted_target` policy, or the empty string if the resolver attribute is unset.

  
`storage.googleapis.com/client/grpc/client/attempt/rcvd_total_compressed_message_size` | `Preview`. The total bytes, compressed but not encrypted, that are received across all response messages except metadata per RPC attempt. This doesn't include gRPC or transport framing bytes. | Histogram | `By` | 

  * `grpc.method`: full gRPC method name, including package, service, and method.
  * `grpc.target`: canonicalized target URI used when creating gRPC channel.
  * `grpc.status`: gRPC server status code received, such as `OK`, `CANCELLED`, or `DEADLINE_EXCEEDED`.
  * `grpc.lb.locality`: the locality the traffic is being sent to. This will be set to the resolver attribute passed down from the `weighted_target` policy, or the empty string if the resolver attribute is unset.

  
  
For more information about client per-attempt instruments, see [OpenTelemetry metrics documentation in GitHub](https://github.com/grpc/proposal/blob/master/A66-otel-stats.md#opentelemetry-metrics).

### Client per-call metrics

The following metrics provide an aggregated view of the entire lifecycle of a client call to a server. Client per-call metrics provide high-level data about client calls, provide tracking metrics to understand call patterns, and help you identify frequencies in errors.

Full metric | Description | Instrument type | Unit | Attributes  
---|---|---|---|---  
`storage.googleapis.com/client/grpc/client/call/duration` | `Preview`. Measures the end-to-end time the gRPC library takes to complete an RPC from the application's perspective. | Histogram | `s` | 

  * `grpc.method`: full gRPC method name, including package, service, and method.
  * `grpc.target`: canonicalized target URI used when creating gRPC channel.
  * `grpc.status`: gRPC server status code received such as `OK`, `CANCELLED`, or `DEADLINE_EXCEEDED`.

  
  
For more information about client per-call instruments, see [OpenTelemetry metrics documentation in GitHub](https://github.com/grpc/proposal/blob/master/A66-otel-stats.md#opentelemetry-metrics).

### Request load sensing metrics

The following metrics provide insights on the effectiveness of your client application's use of request load sensing. Request load sensing metrics can help you balance server loads, optimize resource utilization, and improve client response times. The following metrics are only available with direct connectivity.

Full metric | Description | Instrument type | Unit | Attributes  
---|---|---|---|---  
`storage.googleapis.com/client/grpc/lb/rls/cache_entries` | `Preview`. The number of entries in the request load sensing cache. | Gauge | `{entry}` | 

  * `grpc.target`: indicates the target of the gRPC channel the WRR is used in.
  * `grpc.lb.rls.server_target`: the target URI of the request load sensing server talks to.
  * `grpc.lb.rls.instance_uuid`: a universally unique identifier (UUID) for an individual request load sensing client instance. The value isn't meaningful by itself, but it's useful for differentiating between request load sensing client instances in cases where there are either multiple instances in the same gRPC channel or where there are multiple channels to the same target.

  
`storage.googleapis.com/client/grpc/lb/rls/cache_size` | `Preview`. The current size of the request load sensing cache. | Gauge | `By` | 

  * `grpc.target`: the target of the gRPC channel the WRR is used in.
  * `grpc.lb.rls.server_target`: the target URI of the request load sensing server talks to.
  * `grpc.lb.rls.instance_uuid`: a UUID for an individual request load sensing client instance. The value isn't meaningful by itself, but it's useful for differentiating between request load sensing client instances in cases where there are either multiple instances in the same gRPC channel or where there are multiple channels to the same target.

  
`storage.googleapis.com/client/grpc/lb/rls/default_target_picks` | `Preview`. The number of load balancer (LB) picks sent to the default target. | Counter | `{pick}` | 

  * `grpc.target`: indicates the target of the gRPC channel in which request load sensing is used.
  * `grpc.lb.rls.server_target`: the target URI of the request load sensing server to talk to.
  * `grpc.lb.rls.data_plane_target`: a target string used by request load sensing for routing data plane traffic. The value is either returned by the request load sensing server for a particular key or configured as the default target in the request load sensing config.
  * `grpc.lb.pick_result`:the result of an LB pick, such as `"complete"`, `"fail"`, or `"drop"`.

  
`storage.googleapis.com/client/grpc/lb/rls/target_picks` | `Preview`. The number of LB picks sent to each request load sensing target. If the default target is also returned by the request load sensing server, RPCs sent to that target from the cache are counted in this metric, not in `grpc.rls.default_target_picks`. | Counter | `{pick}` | 

  * `grpc.target`: the target of the gRPC channel in which request load sensing is used.
  * `grpc.lb.rls.server_target`: the target URI of the request load sensing server to talk to.
  * `grpc.lb.rls.data_plane_target`: a target string used by request load sensing for routing data plane traffic. The value is either returned by the request load sensing server for a particular key or configured as the default target in the request load sensing config.
  * `grpc.lb.pick_result`: the result of an LB pick such as `"complete"`, `"fail"`, or `"drop"`.

  
`storage.googleapis.com/client/grpc/lb/rls/failed_picks` | `Preview`. The number of LB picks that failed due to either a failed request load sensing request or the request load sensing channel being throttled. | Counter | `{pick}` | 

  * `grpc.target`: the target of the gRPC channel in which request load sensing is used.
  * `grpc.lb.rls.server_target`: the target URI of the request load sensing server to talk to.

  
  
### xDiscovery Service client metrics

The following metrics provide insights on how your client application interacts with the [xDiscovery Service (xDS)](https://github.com/grpc/proposal/blob/master/A27-xds-global-load-balancing.md) control plane to discover and configure connections to backend services. xDS metrics can help you track service request latency, monitor configuration updates, and optimize overall xDS performance.

The following metrics are only available with direct connectivity.

Full metric | Description | Instrument type | Unit | Attributes  
---|---|---|---|---  
`storage.googleapis.com/client/grpc/xds_client/connected` | `Preview`. Measures whether or not the xDS client has a working ADS stream to the xDS server. For a given server, this metric is set to `1` when the stream is initially created. If there is a connectivity failure or when the ADS stream fails without seeing a response message as per `A57`, the metric is set to `0`. Once set to `0`, the metric will be reset to `1` when the first response is received on an ADS stream. This metric is only available for Cloud Client Libraries for C++. | Gauge | `{bool}` | 

  * `grpc.target`: for clients, indicates the target of the gRPC channel the `XdsClient` is used in. For servers, will be the string `"#server"`.
  * `grpc.xds.server`: the target URI of the xDS server the `XdsClient` is communicating with.

  
`storage.googleapis.com/client/grpc/xds_client/resource_updates_invalid` | `Preview`. The number of resources received that were considered invalid. This metric is only available for Cloud Client Libraries for C++. | Counter | `{resource}` | 

  * `grpc.target`: for clients, indicates the target of the gRPC channel in which the `XdsClient` is used. For servers, will be the string `"#server"`.
  * `grpc.xds.server`: the target URI of the xDS server the `XdsClient` is communicating with.
  * `grpc.xds.resource_type`: indicates an xDS resource type, such as `"envoy.config.listener.v3.Listener"`.

  
`storage.googleapis.com/client/grpc/xds_client/resource_updates_valid` | `Preview`. The number of resources received that were considered valid, even if unchanged. This metric is only available for Cloud Client Libraries for C++. | Counter | `{resource}` | 

  * `grpc.target`: for clients, indicates the target of the gRPC channel in which the `XdsClient` is used. For servers, will be the string `"#server"`.
  * `grpc.xds.server`: the target URI of the xDS server the `XdsClient` is communicating with.
  * `grpc.xds.resource_type`: indicates an xDS resource type, such as `"envoy.config.listener.v3.Listener"`.

  
`storage.googleapis.com/client/grpc/xds_client/resources` | `Preview`. The number of xDS resources. This metric is only available for Cloud Client Libraries for C++. | Gauge | `{resource}` | 

  * `grpc.target`: for clients, indicates the target of the gRPC channel in which the `XdsClient` is used. For servers, will be the string `"#server"`.
  * `grpc.xds.authority`: the xDS authority. The value will be `"#old"` for non-xdstp resource names which were identified in the xDS API, before the introduction of the `xdstp://` URI representation.
  * `grpc.xds.cache_state`: indicates the cache state of an xDS resource.
  * `grpc.xds.resource_type` indicates an xDS resource type, such as `"envoy.config.listener.v3.Listener"`.

  
`storage.googleapis.com/client/grpc/xds_client/server_failure` | `Preview`. The number of xDS servers that are no longer functioning correctly and have either become unavailable, overloaded, or are providing incorrect or invalid configuration data. This metric is only available for Cloud Client Libraries for C++. | Counter | `{failure}` | 

  * `grpc.target`: the target URI of the xDS server with the `XdsClient` is communicating with.
  * `grpc.xds.server`: for clients, this indicates the target of the gRPC channel in which the `XdsClient` is used. For servers, this is the string `"#server"`.

  
  
For more information about xDS client metrics, see the [xDS-Based global load balancing](https://github.com/grpc/proposal/blob/master/A27-xds-global-load-balancing.md) documentation in GitHub.

## Opt out of client-side metrics

You can opt out of client-side metrics if needed.

### Java
    
    
    public GrpcStorageOptions.Builder setEnableGrpcClientMetrics(false enableGrpcClientMetrics)
    

For more information, see [Cloud Client Libraries for Java class `GrpcStorageOptions.Builder` method for gRPC client metrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.GrpcStorageOptions.Builder#com_google_cloud_storage_GrpcStorageOptions_Builder_setEnableGrpcClientMetrics_boolean_).

### C++

To opt out of client-side metrics for the gRPC API using Cloud Client Libraries for C++, see [Struct `EnableGrpcMetricsOption`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage__experimental_1_1EnableGrpcMetricsOption#structgoogle_1_1cloud_1_1storage__experimental_1_1EnableGrpcMetricsOption_1a85dd23fc45887c08217b4198223f845c).

If you're using [Bazel](https://github.com/googleapis/google-cloud-cpp/blob/main/bazel/googleapis.BUILD) to build your application and want to disable client-side metrics, set the `enable_grpc_metrics` option to `false` in your application's build file.

## What's next

  * Learn more about [observability in Google Cloud](https://docs.cloud.google.com/monitoring/docs).

  * Learn how to [add custom traces and metrics to your application](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/custom-instrumentation).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
