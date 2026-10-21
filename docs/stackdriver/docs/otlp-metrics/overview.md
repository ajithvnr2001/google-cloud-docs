---
url: https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview/
title: OTLP support in Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:19:07.886320+00:00
---

# OTLP support in Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  OTLP support in Google Cloud Observability Stay organized with collections  Save and categorize content based on your preferences. 

You can ingest OTLP-formatted log, metric, and trace data into Google Cloud Observability by using the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), which implements the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). This API lets you collect vendor-neutral telemetry from OpenTelemetry SDKs and collectors without using custom Google Cloud exporters.

When you send telemetry to your project by using the Telemetry API, Google Cloud Observability processes each signal as follows:

  * **Log data:** Converts OTLP log records into [log entries](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and routes them for storage.
  * **Metric data:** Maps metric data to Prometheus time series in Cloud Monitoring.
  * **Trace data:** Stores distributed traces in a format that is generally consistent with OTLP.



If you run workloads on Google Kubernetes Engine, then you can use [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke) instead of manually deploying and managing an OpenTelemetry Collector.

## Protocol support

The OTLP endpoint supports all of the OTLP transport and serialization protocols, including `http/protobuf`, `http/json`, and `grpc`. When exporting directly from applications using SDKs, we recommend using the gRPC OTLP exporter rather than HTTP exporters because most SDK exporters lack support for dynamic token refreshing.

## Authentication

You must configure your exporters with the credentials necessary to send data to your Google Cloud project. For example, when you use collectors, typically you use the `googleclientauth` extension to authenticate with Google credentials.

For an example of authentication when using direct export of trace data, see [Configure authentication](https://docs.cloud.google.com/stackdriver/docs/instrumentation/migrate-to-otlp-endpoints#auth). This example illustrates how to configure the exporter with your Google Cloud [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) and add a language-specific Google Auth Library to your application.

To send telemetry data to your Google Cloud project by using the Telemetry API, you must also do the following:

  * Configure a quota project. To learn more, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

  * Grant the following Identity and Access Management (IAM) roles to the user or to the service account that the application uses:

    * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) role (`roles/serviceusage.serviceUsageConsumer`) on the quota project.
    * [Cloud Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.writer) role (`roles/telemetry.writer`) on the project. This role lets your application write log, metric, and trace data.



## OTLP ingestion

This section describes how your log, metric, and trace data is converted from OTLP into Google Cloud Observability data structures.

### Log data ingestion

When you use the Telemetry API to ingest OTLP-formatted logs, your log data is converted into Cloud Logging [log entries](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). An incoming OTLP-formatted log request in JSON has the following general structure:
    
    
    "resourceLogs": [
        {
          "resource": {
            "attributes": [...]
          },
          "scopeLogs": [
            {
              "scope": { ...}
              "logRecords": [...]
            }
          ]
        }
    ]
    

Each item in each `logRecords` array becomes a single Cloud Logging log entry. The `resource` attributes determine the [monitored resource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.resource) in the resulting [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). For more information about which attributes are required for ingestion of OTLP-formatted logs, see [OTLP attributes to resource-type mapping](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/otlp-attribute-to-logging-resource).

To support ingestion of OTLP-formatted logs, the Cloud Logging [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) structure contains an additional field, [`otel`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.otel). Because the OTLP and Cloud Logging data models differ in structure, the `otel` field preserves a copy of the resource, scope, and entity metadata from the incoming OTLP request.

For example, if you send an OTLP `resourceLogs` payload like the following to the Telemetry API, then each resulting log entry contains a `resource` field (for the monitored resource) and an `otel` field, as shown on the other tabs:

###  `resourceLogs`
    
    
    {
      "resourceLogs": [
        {
          "resource": {
            "attributes": [
              {
                "key": "gcp.project_id",
                "value": { "stringValue": "PROJECT_ID" }
              },
              {
                "key": "gcp.resource_type",
                "value": { "stringValue": "global" }
              }
            ]
          },
          "scopeLogs": [
            {
              "scope": {
                "name": "my.library",
                "version": "1.0.0",
                "attributes": [
                  {
                    "key": "my.scope.attribute",
                    "value": { "stringValue": "some scope attribute" }
                  }
                ]
              },
              "logRecords": [ ... ]
             }
           ]
         }
       ]
    }
    

###  `resource`
    
    
      {
        ...
        "resource": {
          "labels": {
            "project_id": "PROJECT_ID"
          },
          "type": "global"
        },
        ...
    }
    

###  `otel`
    
    
      {
        ...
        "otel": {
          "resource": {
            "attributes": {
              "gcp.project_id": "PROJECT_ID",
              "gcp.resource_type": "global"
            }
          },
          "scope": {
            "attributes": {
              "my.scope.attribute": "some scope attribute"
            },
            "name": "my.library",
            "version": "1.0.0"
          }
        },
       ...
      }
    

Because Cloud Logging log entries are self-contained and don't link to external resource schemas, all OTLP resource, scope, and entity metadata is copied into each log entry.

### Metric data ingestion

OTLP for Prometheus metrics only works when using the OpenTelemetry Collector version 0.140.0 or newer.

When metrics are ingested into Cloud Monitoring by using an OpenTelemetry Collector and the `otlphttp` exporter or sent directly by using an OpenTelemetry SDK, the OTLP metrics are mapped to Cloud Monitoring metric structures. To get information about those mappings, see the following:

  * [Mapping between OTLP resources and Cloud Monitoring monitored resources](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/v1.metrics#mr-mapping).
  * [Mapping between OTLP metrics and Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/v1.metrics#metric-mapping).



Google Cloud Observability converts metrics into the Prometheus time-series format. Metric names must have either no domain or the domain `prometheus.googleapis.com`. After conversion, the metric name includes the `prometheus.googleapis.com` prefix and an additional suffix, based on the OTLP point kind. The resulting Cloud Monitoring metric has the following structure:
    
    
    prometheus.googleapis.com/{metric_name}/{suffix}
    

Additionally, for each unique OpenTelemetry resource, the conversion adds a `target_info` metric that contains all resource attributes except `service.name`, `service.instance.id`, and `service.namespace`.

**Note:** Value-type collisions can occur if you previously sent `INT64` `target_info` metrics. If you encounter collisions, the best long-term solution for this is for you to delete the metric descriptor for the `INT64` `target_info` metrics. To delete this descriptor from your metric scope, use this [Golang script](https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/fea30dcac16250c5bef3b4e030629021aa28320e/examples/scripts/delete_metric_descriptors/delete_target_info.go).

Because metric names and label keys in Cloud Monitoring don't support full UTF-8, metric data can be rejected:

  * Metric names that don't conform to the regular expression `[a-zA-Z][a-zA-Z0-9_:./-]*` are rejected. The only special characters allowed in metric names are in the set `_:./-`.
  * Data points containing attributes (that is, label keys) that don't conform to the regular expression `[a-zA-Z_][a-zA-Z0-9_.]*` are rejected. The only special characters allowed in label keys are in the set `_.`. All special characters are allowed in label values.



To prevent rejection of your metrics for these reasons, use the [`replace_pattern`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/ottl/ottlfuncs#replace_pattern) function to transform your metric names and attributes.

### Trace data ingestion

Regardless of whether you use the Telemetry API or the Cloud Trace API, incoming trace data is stored in a format consistent with OTLP. However, we recommend using the Telemetry API because it provides higher ingestion quotas than the Cloud Trace API.

The following is an example of trace data that might be sent from an application to your Google Cloud project:
    
    
    {
      "resourceSpans": [
        {
          "resource": {
            "attributes": [...]
          },
          "scopeSpans": [
            {
              "scope": { ...},
              "spans": [...]
            }
          ]
        }
      ]
    }
    

Each item in each `scopeSpans.spans` array becomes a single stored span:

  * Each span's `resource` field contains a copy of the `resourceSpans.resource.attributes` data.
  * Each span's `instrumentation_scope` field contains a copy of the `scopeSpans.scope` data.
  * Each span corresponds to one entry in the `scopeSpans.spans` array. Fields such as `traceId`, `spanId`, and `kind` are mapped into similarly named fields in the trace schema.



For more information, see the following documents:

  * [Storage schema for trace data](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/trace-schema).
  * [v1.traces overview](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/v1.traces).



## Billing

Billing for log, metric, and trace data that is ingested by using the Telemetry API depends on the telemetry signal. For complete information, see the [Billing page](https://console.cloud.google.com/billing).

### Log data billing

You might see a change in your Cloud Logging storage and billing values when you use the Telemetry API to ingest logs due to a change in the log volume.

The largest changes to storage and billing for your Google Cloud project occur when both of the following are true:

  * The `resource` field contains high-cardinality attributes or a large number of attributes. These resource attributes determine the monitored resource in the resulting [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).
  * The `scopeLogs` field contains a large number of items in the `logRecords` arrays. The `scopeLogs.scope` fields are copied into the `otel` field for every individual log entry.



Because this resource and scope metadata is copied onto every individual log entry, your stored log volume can increase.

To minimize storage volume, we recommend the following:

  * Use an OpenTelemetry Collector processor, such as a `transform` processor, to drop unnecessary resource or scope attributes before exporting the data.
  * If you don't need the additional metadata preserved in the `otel` field, then use the legacy mapping option, `gcp.use_legacy_mapping`, which prevents the `otel` field from being populated.

**Note:** If you plan to use the volume of the `resourceLogs` object to estimate the volume of the resulting `LogEntry` objects, then send one `logRecord` object per `resourceLogs` object. Otherwise, your estimates won't properly account for fields that are duplicated in each `LogEntry` object.

### Metric data billing

Billing for OTLP metrics is accounted for under the "Prometheus Samples Ingested" SKU, the same one used for metrics from Google Cloud Managed Service for Prometheus.

### Trace data billing

The API that you use to send trace data to your project doesn't affect how charges are computed for that data.

## Querying your log, metric, and trace data

You can use the explorer pages—Logs Explorer, Metrics Explorer, and Trace Explorer—to query your log, metric, and trace data. You can also use the Observability Analytics page to analyze your log and trace data by using SQL.

The following tips might be helpful when you query your metric data using the Metrics Explorer:

  * **Important** : Querying metric names and label keys with special characters other than the colon (`:`) and the underscore (`_`) requires you to wrap them in braces (`{}`) and quotes (`"`), according to [PromQL's UTF-8 spec](https://prometheus.io/docs/guides/utf8/#querying). For example, the following are valid queries:

    * `{"my.metric.name"}`
    * `{"my.metric.name", "label.key.KEY"="value"}`
  * Retaining the `le` label when querying exponential histograms might return unexpected results. The more typical ` histogram_quantile(.99, sum by (le) (metric))` queries are expected to work.

  * Delta metrics might not query properly in certain circumstances, such as very sparse deltas.




## Limits and quotas

The [Telemetry API limits](https://docs.cloud.google.com/stackdriver/quotas) apply to all signal types.

The following quotas and limits also apply:

  * Log data: The [Cloud Logging API quotas and limits](https://docs.cloud.google.com/logging/quotas) apply.
  * Metric data: The [Cloud Monitoring API quotas and limits](https://docs.cloud.google.com/monitoring/quotas) apply. For example, metrics can't have more than 200 labels.

The default quota for metrics ingested by the Telemetry API is 60,000 requests per minute. At a maximum batch size of 200 points per request, this quota is an effective default quota of 200,000 samples per second. You can request a quota increase. 

  * Trace data: There are no additional quotas or limits that apply.




## What's next

  * For information about migrating to the `otlphttp` exporter from another exporter, see [Migrate to the OTLP exporter](https://docs.cloud.google.com/stackdriver/docs/otlp/migrate-collector-to-otlp-exporters).
  * For instructions about deploying and using the OpenTelemetry Collector with the Telemetry API, see [Deploy and use the collector](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/deploy-collector).
  * For information about writing OTLP-formatted logs to the Telemetry API, see [Write OTLP-formatted logs to the Telemetry API](https://docs.cloud.google.com/stackdriver/docs/otlp-logs/write-logs-to-api).
  * For information about sending metrics to the Telemetry API from applications that use SDKs, see [Use SDKs to send metrics from applications](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/use-sdks).
  * For information about using an OpenTelemetry Collector and the Telemetry API with OpenTelemetry zero-code instrumentation, see [Use OpenTelemetry zero-code instrumentation for Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/otel-zerocode-java-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
