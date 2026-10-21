---
url: https://docs.cloud.google.com/stackdriver/docs/otlp/migrate-collector-to-otlp-exporters/
title: Migrate collectors to use OTLP exporters \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:17.777302+00:00
---

# Migrate collectors to use OTLP exporters  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/otlp/migrate-collector-to-otlp-exporters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Migrate collectors to use OTLP exporters Stay organized with collections  Save and categorize content based on your preferences. 

The [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) is an implementation of the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). Support for OTLP lets you add generic `otlphttp` and `otlp_grpc/otlp_logs` exporters to your collector configuration, avoiding vendor-specific exporters. Applications can send log, metric, and trace data to the Telemetry API.

This guide applies to you if your collector's configuration uses the [`googlecloud` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlecloudexporter) or the [`googlemanagedprometheus` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/googlemanagedprometheusexporter):

  * **Log data** : Migrate from the [`googlecloud` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlecloudexporter) to the `otlp_grpc/otlp_logs` exporter.

  * **Metric data** : Migrate from the [`googlemanagedprometheus` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/googlemanagedprometheusexporter) to the `otlphttp` exporter.

  * **Trace data** : Migrate from the [`googlecloud` exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlecloudexporter) to the `otlphttp` exporter.




To migrate to OTLP exporters, perform the following steps:

  1. Enable the Telemetry API
  2. Authorize the collector service account
  3. Set the `GOOGLE_CLOUD_PROJECT` environment variable
  4. Add the `googleclientauth` extension
  5. Add the `otlphttp` and `otlp_grpc/otlp_logs` exporters
  6. Add processors
  7. Update service pipelines
  8. Validate your configuration
  9. Migrate dashboards and alerting policies
  10. Remove vendor-specific exporters



## Enable the Telemetry API

The OTLP exporters write to the Telemetry API, so that API must be enabled in your project. To enable the Telemetry API, run the following command:
    
    
    gcloud services enable telemetry.googleapis.com
    

## Authorize the collector service account

The collector authenticates against Google Cloud APIs using the identity of the environment where it runs. The service account running your collector must have permission to use the Telemetry API to write log, metric, and trace data. Additionally, because the Telemetry API is a consumer API, you must explicitly specify the Google Cloud project whose quota is consumed by API calls and grant the service account the permissions needed to consume that project's quota.

### Required roles

**Note:** This document assumes that your API quota is being drawn from the same Google Cloud project that is the destination of the Telemetry API calls. If you use a separate quota project, then grant the Service Usage Consumer role on that quota project.

To ensure that the service account running your collector has the necessary permissions to send log, metric, and trace data, ask your administrator to grant the following IAM roles to the service account running your collector on your project: 

**Important:** You must grant these roles to the service account running your collector, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Cloud Telemetry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.writer) (`roles/telemetry.writer`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



These predefined roles contain the permissions required to send log, metric, and trace data. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to send log, metric, and trace data:

  * `logging.logEntries.create`
  * `monitoring.timeSeries.create`
  * `telemetry.traces.write`
  * `serviceusage.services.use`



### Kubernetes service account

If you deploy the collector on Google Kubernetes Engine (GKE) using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), then grant the required roles to your Kubernetes service account.

You can use the following commands to grant the required roles if your API quota is being drawn from the same Google Cloud project that is the destination of the Telemetry API calls. Before you run the commands, replace PROJECT_ID with the ID of your project. However, if you use a separate quota project, then replace PROJECT_ID in the second command with the ID of your quota project:
    
    
    export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/telemetry.writer \
      --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/opentelemetry/sa/opentelemetry-collector \
      --condition=None
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/serviceusage.serviceUsageConsumer \
      --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/opentelemetry/sa/opentelemetry-collector \
      --condition=None
    

### Service account for Workload Identity Federation for GKE

If you configured a service account for Workload Identity Federation for GKE, then you can use the command in the Google Cloud Managed Service for Prometheus documentation to [authorize the service account](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#create-bind-sa), with the following changes:

  * Replace `gmp-test-sa` with your service account's name.
  * Run the command to grant the required roles to write log, metric, and trace data.



### Other service account

If you run the collector on a Compute Engine VM or outside GKE, then grant the required roles to the Google Cloud service account your deployment uses.

## Set the `GOOGLE_CLOUD_PROJECT` environment variable

Set the `GOOGLE_CLOUD_PROJECT` environment variable in your collector deployment. The result looks like the following:
    
    
    env:
    - name: GOOGLE_CLOUD_PROJECT
      value: PROJECT_ID
    

## Add the `googleclientauth` extension

Add the `googleclientauth` extension to your collector configuration. The Telemetry API is a consumer API and requires that you specify both your Google Cloud project and your quota project. The result looks similar to the following:
    
    
    extensions:
      googleclientauth:
        project: ${GOOGLE_CLOUD_PROJECT}
        quota_project: ${GOOGLE_CLOUD_PROJECT}
    

## Add the `otlphttp` and `otlp_grpc/otlp_logs` exporters

Use the `otlphttp` exporter to send OTLP-formatted metric and trace data to your project, and use the `otlp_grpc/otlp_logs` exporter to send log data. Be sure to configure both exporters with the `googleclientauth` extension.

The result looks similar to the following:
    
    
    exporters:
      # ... existing content ...
      otlphttp:
        encoding: proto
        endpoint: https://telemetry.googleapis.com
        auth:
          authenticator: googleclientauth
      otlp_grpc/otlp_logs:
        auth:
          authenticator: googleclientauth
        balancer_name: pick_first
        endpoint: telemetry.googleapis.com:443
    

For the `otlp_grpc/otlp_logs` exporter, the `endpoint` field must be specified by using the `host:port` format.

## Add processors

This section lists processors that you need to add to your collector. There are other processors that you might want to use. For example, Google-Built OpenTelemetry Collector collector configurations typically include the `memory_limiter` processor and one that transforms metric data. For an example, see [Google-Built OpenTelemetry Collector on GKE](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke).

### Add the `resource/gcp_project_id` processor

Add a `resource` processor that captures information about your Google Cloud project.
    
    
      resource/gcp_project_id:
        attributes:
          - action: insert
            value: ${GOOGLE_CLOUD_PROJECT}
            key: gcp.project_id
    

### Add the `resourcedetection` processor

If you are running on Google Cloud, then consider adding the `resourcedetection` processor. This processor can automatically discover information about your architecture.

The following configuration looks for the standard OpenTelemetry environment variables and then queries the Google Cloud metadata server to gather information about your infrastructure:
    
    
      resourcedetection:
        detectors: ["env", "gcp"]
    

### Add the `batch` processor

To more efficiently send your telemetry to your Google Cloud project, we recommend that you use the `batch` processor.

For example, the Google-Built OpenTelemetry Collector collector uses the following configuration for the batch processor:
    
    
    batch:
      send_batch_max_size: 200
      send_batch_size: 200
      timeout: 5s
    

### Add the `metricstarttime` processor

Add the `metricstarttime` processor to the configuration. This processor makes sure that cumulative metrics include both a start time and an observation time. By default, Prometheus metrics only include a current time. Therefore, if you omit this processor and your application generates Prometheus metrics, then your metric data might be rejected or you might see data spikes.

**You must add this processor if your collector receives Prometheus metrics.**
    
    
    processors:
      # This processor ensures the start time is set for Prometheus metrics.
      # Set in the pipeline before the k8sattributes processor, if used.
      # No-op for OTLP metrics.
      metricstarttime:
        strategy: subtract_initial_point
    

### Add the transform processor

To preserve the instrumentation source and version in your log data, add the following `transform` processor:
    
    
      transform/otlp_grpc/preserve_instrumentation_source_version:
        error_mode: ignore
        log_statements:
          - context: log
            statements:
              - set(attributes["instrumentation_source"], instrumentation_scope.name) where instrumentation_scope.name != ""
              - set(attributes["instrumentation_version"], instrumentation_scope.version) where instrumentation_scope.version != ""
              - set(attributes["service.name"], resource.attributes["service.name"]) where resource.attributes["service.name"] != nil
              - set(attributes["service.namespace"], resource.attributes["service.namespace"]) where resource.attributes["service.namespace"] != nil
              - set(attributes["service.instance.id"], resource.attributes["service.instance.id"]) where resource.attributes["service.instance.id"] != nil
    

## Update service pipelines

Next, update your collector's pipelines to use the `otlp_grpc/otlp_logs` and `otlphttp` exporters. For log and trace data, these instructions replace your current exporter with the appropriate OTLP exporter. For your metric data, these instructions result in double writes. This approach lets you verify that the OTLP exporter is sending metric data to your Google Cloud project. It also lets you update charts and alerting policies before you turn down the data streams from the original exporter.

Make the following changes to your collector's pipeline configurations:

  1. Add the `googleclientauth` extension to the `service` entry.
  2. For your log pipeline, replace `googlecloud/logging` with `otlp_grpc/otlp_logs` and then add the following processors to the pipeline's processors list:

     * `resource/gcp_project_id`
     * `transform/otlp_grpc/preserve_instrumentation_source_version`
     * `resourcedetection` (if you added this processor)
     * `batch`

**This configuration performs a single-write of log data.** If you want to double-write your log data, then add the `otlp_grpc/otlp_logs` exporter to the list of exporters.

  3. For your metric pipeline, add the `otlphttp` exporter to the pipeline's exporters list alongside the `googlemanagedprometheus` exporter, and then add the following processors:

     * `resource/gcp_project_id`
     * `metricstarttime`
     * `resourcedetection` (if you added this processor)
     * `batch`

**This configuration performs a double-write of metric data. After you validate the metric data stream and update charts and alerting policies, remove the Prometheus exporter.**

  4. For your trace pipeline, replace your current exporter with the `otlphttp` exporter and then add the following processors:

     * `resource/gcp_project_id`
     * `resourcedetection` (if you added this processor)
     * `batch`

**This configuration performs a single-write of trace data.**




The result of these changes is similar to the following:
    
    
    service:
      extensions: ["googleclientauth"]
      pipelines:
        logs:
          receivers: ["otlp"]
          processors:
            - resourcedetection
            - resource/gcp_project_id
            - transform/otlp_grpc/preserve_instrumentation_source_version
            - batch
          exporters: ["otlp_grpc/otlp_logs"]
        metrics:
          receivers: ["otlp"]
          processors:
            - resourcedetection
            - resource/gcp_project_id
            - metricstarttime
            - batch
          exporters: ["googlemanagedprometheus", "otlphttp"]
        traces:
          receivers: ["otlp"]
          processors:
            - resourcedetection
            - resource/gcp_project_id
            - batch
          exporters: ["otlphttp"]
    

The preceding snippet uses the `OTLP` receiver for your log, metric, and trace data. Your collector configuration might be different. For example, if you have an application that writes structured log data, then the `filelog` receiver is appropriate.

## Validate your configuration

Restart your deployment and then verify that your `otlphttp` and `otlp_grpc/otlp_logs` exporters are sending data to your Google Cloud project. To verify your configuration, do the following:

  * Query your log entries for errors related to writing telemetry data.
  * View the error rates for the Cloud Logging API, Cloud Monitoring API, and Telemetry API.
  * View time series by using Metrics Explorer.



## Migrate dashboards and alerting policies

Update your charts and dashboards as follows:

  1. If you are monitoring usage of the Cloud Logging API or Cloud Monitoring API with charts or alerting policies, then create additional charts or alerting policies to monitor the usage of the Telemetry API.

  2. If the metrics receivers include an `otlp` receiver or if your collector scrapes Prometheus metrics with UTF-8 characters, then update your charts and dashboards. The `otlphttp` exporter generates different metrics than the `googlemanagedprometheus` exporter. For more information, see Differences in the format of exported metrics.

You don't need to update your charts and dashboards if your collector only receives Prometheus metric data.

  3. If your metrics pipelines include a [`prometheus` receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md), then data-stream collisions will occur between metrics generated by the `otlphttp` and `googlemanagedprometheus` exporters. To resolve these collisions, remove the `googlemanagedprometheus` exporter.




### Differences in the format of exported metrics

The updates to metric-based charts and alerting policies are required because of the following differences between metrics exported by the OTLP and `googlemanagedprometheus` exporters:

  * The Telemetry API allows the period (`.`) and slash (`/`) characters with in metric names. The `googlemanagedprometheus` exporter converts all instances of these characters to the underscore (`_`) character. For example, an OTLP metric called `prometheus.googleapis.com/foo.bar/gauge` is exported verbatim by the OTLP exporter but is exported as `prometheus.googleapis.com/foo_bar/gauge` by the `googlemanagedprometheus` exporter.

When the metrics are ingested, Cloud Monitoring creates metric descriptors based on the names. The difference in how the period (`.`) and slash (`/`) characters are handled by the ingestion pathways means that resulting metric descriptors differ between metrics ingested by using the `googlemanagedprometheus` exporter and those ingested by using the `otlphttp` exporter. If you use both ingestion paths, then you have two sets of metrics; to get complete results when querying, you have to manually union results from the Prometheus and OTLP versions of the metrics.

  * The Telemetry API doesn't append a unit to a metric name when a unit is present, and it doesn't append a `_total` suffix to counters. So a metric exported as `prometheus.googleapis.com/foo/counter` when using the Telemetry API is exported as `prometheus.googleapis.com/foo_seconds_total/counter` by the `googlemanagedprometheus` exporter. This difference also applies to the `_total` and `_ratio` suffixes.




For more information about differences between metrics, see [Differences between the `googlemanagedprometheus` exporter and the Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/v1.metrics#telemetry-diffs).

Transformation rules don't apply to metrics with UTF-8 characters. Therefore, you must rewrite your dashboards and alerting policies either to use the new metric names or to use queries that combine the old and new metric names. **We don't recommend writing processor rules to recreate these transformations** to continue writing UTF-8 metrics as if they were collected by the `googlemanagedprometheus` exporter. Doing so retains backward compatibility, but it sacrifices forward compatibility, and you won't be able to use open-source assets that reference the UTF-8 metric names.

## Remove vendor-specific exporters

After you have validated the new data streams and updated your dashboards and alerting policies, remove the `googlecloud/logging` and `googlemanagedprometheus` exporters from your collector configuration. You might also need to remove processors that were used only by the exporters that were removed from the configuration.

You need to update both the list of exporters and the service pipelines.
    
    
    exporters:
      otlphttp: [...]
      otlp_grpc/otlp_logs: [...]
    
    ...
    service:
      extensions: ["googleclientauth"]
      pipelines:
        logs:
          receivers: ["otlp"]
          processors: [...]
          exporters: ["otlp_grpc/otlp_logs"]
        metrics:
          receivers: ["otlp"]
          processors: [...]
          exporters: ["otlphttp"]
        traces:
          receivers: ["otlp"]
          processors: [...]
          exporters: ["otlphttp"]
    

## Troubleshooting

This section describes how to resolve failures that might occur when you migrate your collector's configuration.

### Missing metric data or spikes in metric data

If your metric data is missing or contains spikes, then verify that you added the `metricstarttime` processor to the collector's configuration. For more information, see Add the `metricstarttime` processor.

You might also review your collector logs, system logs, and the data access audit logs for Monitoring. For example, if a write to a time series fails, then a data access audit log that includes the failure reason is generated.

### Error messages about writing time series

The system generates error messages when an attempt to write data to a time series fails. You can use these messages to help you understand why the write failed and how to resolve the issue.

  * Error message that indicates a value mismatch:
        
        "One or more TimeSeries could not be written: Value type DOUBLE does not match metric descriptor value type INT64."
        

This error occurs if you previously sent `INT64` `target_info` metrics because the Telemetry API sets the value type of all metrics to `DOUBLE`. The best long-term solution is to delete the metric descriptor for the `INT64` `target_info` metrics. To delete this descriptor from your metric scope, use this [Golang script](https://raw.githubusercontent.com/GoogleCloudPlatform/prometheus-engine/fea30dcac16250c5bef3b4e030629021aa28320e/examples/scripts/delete_metric_descriptors/delete_target_info.go).

  * Error message that indicates multiple sources writing time series data:
        
        "One or more TimeSeries could not be written: Points must be written in order. One or more of the points specified had an older end time than the most recent point."
        

To resolve this problem, remove the `googlemanagedprometheus` exporter from your collector's configuration. For more information, see Remove vendor-specific exporters.




## What's next

  * [Overview of collector-based instrumentation samples](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/sample-overview) refers to sample applications that you can download and install. Each sample application includes a complete collector that exports metric and trace data by using the Telemetry API.

  * [Deploy Google-Built OpenTelemetry Collector on Google Kubernetes Engine](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke) includes a complete collector configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
