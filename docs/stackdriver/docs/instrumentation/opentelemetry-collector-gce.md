---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gce/
title: Deploy Google-Built OpenTelemetry Collector on Compute Engine \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:18.359233+00:00
---

# Deploy Google-Built OpenTelemetry Collector on Compute Engine  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Deploy Google-Built OpenTelemetry Collector on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to run the [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel) on Compute Engine to collect OTLP logs, metrics, and traces from instrumented applications and then export that data to Google Cloud.

## Before you begin

Running the Google-Built OpenTelemetry Collector requires the following resources:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

  8. A Compute Engine instance. If you don't have a Compute Engine instance, then follow the instructions at [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  9. An installation of `gcloud`. For information about installing `gcloud`, see [Install the `gcloud` CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).



## Configure permissions for the Collector

By default, Compute Engine instances use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), `PROJECT_NUMBER-compute@developer.gserviceaccount.com`. This service account usually has the Identity and Access Management (IAM) roles necessary to write the metrics and logs described in this document:

  * [Monitoring Metric Writer (`roles/monitoring.metricWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter)
  * [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)
  * [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent)



If you choose to use a user-managed service account instead of the default, it must be assigned these same roles. For more information, see [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).

## Install the Collector

To install the Google-Built OpenTelemetry Collector as a package for your Compute Engine instance, complete the following steps.

### Debian & Ubuntu

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Run the following command to set up the package repository:
         
         sudo mkdir -p /etc/apt/keyrings
         sudo curl -o /etc/apt/keyrings/otelcol-google.asc https://packages.cloud.google.com/apt/doc/apt-key.gpg
         cat <<EOF | sudo tee /etc/apt/sources.list.d/otelcol-google.list
         deb [signed-by=/etc/apt/keyrings/otelcol-google.asc] https://us-apt.pkg.dev/projects/cloud-ops-agents-artifacts google-cloud-opentelemetry-collector-apt main
         EOF
         

  3. Refresh your package manager and install the package:
         
         sudo apt update
         sudo apt install otelcol-google
         

After it is installed, the Google-Built OpenTelemetry Collector is started automatically.




### CentOS, RHEL & Rocky Linux

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Run the following command to set up the package repository:
         
         cat <<EOF | sudo tee /etc/yum.repos.d/otelcol-google.repo
         [otelcol-google]
         name=Google Built OpenTelemetry Collector
         baseurl=https://us-yum.pkg.dev/projects/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector-yum
         autorefresh=0
         enabled=1
         type=rpm-md
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=http://dl.google.com/linux/linux_signing_key.pub
         EOF
         

  3. Install the package:
         
         sudo yum install otelcol-google
         

After it is installed, the Google-Built OpenTelemetry Collector is started automatically.




### SLES

  1. Open a terminal connection to your VM instance using SSH or a similar tool and ensure you have `sudo` access.

  2. Run the following command to set up the package repository:
         
         cat <<EOF | sudo tee /etc/zypp/repos.d/otelcol-google.repo
         [otelcol-google]
         name=Google Built OpenTelemetry Collector
         baseurl=https://us-yum.pkg.dev/projects/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector-yum
         autorefresh=0
         enabled=1
         type=rpm-md
         gpgkey=http://dl.google.com/linux/linux_signing_key.pub
         EOF
         

  3. Install the package:
         
         sudo zypper install otelcol-google
         

After it is installed, the Google-Built OpenTelemetry Collector is started automatically.




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows.

  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**.

  3. Run the following PowerShell command to set up the package repository:
         
         googet addrepo otelcol-google `
             https://us-googet.pkg.dev/projects/cloud-ops-agents-artifacts/repos/google-cloud-opentelemetry-collector-googet
         

  4. Install the package:
         
         googet install otelcol-google
         

After it is installed, the Google-Built OpenTelemetry Collector is started automatically.




## Deploy the Collector

The Google-Built OpenTelemetry Collector includes a minimal configuration by default that does not export telemetry. To export your telemetry, after installing the Collector, configure the Collector by overriding the default configuration. Put your configuration for the Collector in the following files:

  * For Linux: `/etc/otelcol-google/config.yaml`
  * For Windows: `C:\Program Files\Google\OpenTelemetry Collector\config.yaml`



## Configure the Collector

We provide an OpenTelemetry Collector configuration for you to use with the Google-built Collector. This configuration is designed to deliver high volumes of OTLP metrics, logs, and traces. This configuration is also designed to prevent common ingestion issues. You can add to the configuration, but we strongly recommend that you don't remove elements.

This section describes the provided configuration, the key components like exporters, processors, receivers, and other available components.

### Provided Collector configuration

You can find the Collector configuration in the `google-built-opentelemetry-collector` directory on the [`opentelemetry-operations-collector` repository](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/tree/v0.163.0/google-built-opentelemetry-collector/docs/examples/configuration/config-standard.yaml): 
    
    
    receivers:
      # Open two OTLP servers:
      # - On port 4317, open an OTLP GRPC server
      # - On port 4318, open an OTLP HTTP server
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector/tree/main/receiver/otlpreceiver
      otlp:
        protocols:
          grpc:
            endpoint: localhost:4317
          http:
            cors:
              # This effectively allows any origin
              # to make requests to the HTTP server.
              allowed_origins:
              - http://*
              - https://*
            endpoint: localhost:4318
    
    processors:
      # The batch processor is in place to regulate both the number of requests
      # being made and the size of those requests.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/batchprocessor
      batch:
        send_batch_max_size: 200
        send_batch_size: 200
        timeout: 5s
    
      # The memorylimiter will check the memory usage of the collector process.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/memorylimiterprocessor
      memory_limiter:
        check_interval: 1s
        limit_percentage: 65
        spike_limit_percentage: 20
    
      # The resourcedetection processor is configured to detect GCP resources.
      # Resource attributes that represent the GCP resource the collector is
      # running on will be attached to all telemetry that goes through this
      # processor.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourcedetectionprocessor
      # https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourcedetectionprocessor#gcp-metadata
      resourcedetection:
        detectors: [gcp]
        timeout: 10s
    
      # The resource/gcp_project_id processor sets the GCP project ID attribute on telemetry data exported via OTLP.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourceprocessor
      resource/gcp_project_id:
        attributes:
        - action: insert
          key: gcp.project_id
          value: ${GOOGLE_CLOUD_PROJECT}
    
      # The metricstarttime processor sets start time on delta metrics for OTLP export.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/metricstarttimeprocessor
      metricstarttime:
        strategy: subtract_initial_point
    
      transform/collision:
        metric_statements:
        - context: datapoint
          statements:
          - set(attributes["exported_location"], attributes["location"])
          - delete_key(attributes, "location")
          - set(attributes["exported_cluster"], attributes["cluster"])
          - delete_key(attributes, "cluster")
          - set(attributes["exported_namespace"], attributes["namespace"])
          - delete_key(attributes, "namespace")
          - set(attributes["exported_job"], attributes["job"])
          - delete_key(attributes, "job")
          - set(attributes["exported_instance"], attributes["instance"])
          - delete_key(attributes, "instance")
          - set(attributes["exported_project_id"], attributes["project_id"])
          - delete_key(attributes, "project_id")
    
      # For each Prometheus unknown-typed metric, which is a gauge, create a counter that is an exact copy of this metric.
      # The GCP OTLP endpoint will add appropriate suffixes for the counter and gauge.
      transform/prometheus_unknown_types:
        error_mode: ignore
        metric_statements:
        - context: metric
          statements:
          - copy_metric(Concat([metric.name, "unknowncounter"], ":")) where metric.metadata["prometheus.type"] == "unknown" and not HasSuffix(metric.name, ":unknowncounter")
          - convert_gauge_to_sum("cumulative", true) where HasSuffix(metric.name, ":unknowncounter")
          - set(metric.name, Substring(metric.name, 0, Len(metric.name)-Len(":unknowncounter"))) where HasSuffix(metric.name, ":unknowncounter")
    
      transform/otlp_grpc/preserve_instrumentation_source_version:
        error_mode: ignore
        log_statements:
        - context: log
          statements:
          - set(attributes["instrumentation_source"], instrumentation_scope.name) where instrumentation_scope.name != ""
          - set(attributes["instrumentation_version"], instrumentation_scope.version) where instrumentation_scope.version != ""
    
      transform/otlp_grpc/copy_service_resource_labels:
        error_mode: ignore
        log_statements:
        - context: log
          statements:
          - set(attributes["service.name"], resource.attributes["service.name"]) where resource.attributes["service.name"] != nil
          - set(attributes["service.namespace"], resource.attributes["service.namespace"]) where resource.attributes["service.namespace"] != nil
          - set(attributes["service.instance.id"], resource.attributes["service.instance.id"]) where resource.attributes["service.instance.id"] != nil
    
    exporters:
      # The otlp_grpc exporter is used to send telemetry (logs, metrics, traces) to GCP Telemetry API using OTLP gRPC.
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter/otlpexporter
      otlp_grpc:
        endpoint: telemetry.googleapis.com:443
        balancer_name: pick_first
        auth:
          authenticator: googleclientauth
    
    extensions:
      # Opens an endpoint on 13133 that can be used to check the
      # status of the collector. Since this does not configure the
      # `path` config value, the endpoint will default to `/`.
      #
      # When running on Cloud Run, this extension is required and not optional.
      # In other environments it is recommended but may not be required for operation
      # (i.e. in Container-Optimized OS or other GCE environments).
      #
      # Docs:
      # https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/healthcheckextension
      health_check:
        endpoint: 0.0.0.0:13133
      googleclientauth:
    
    service:
      extensions:
      - health_check
      - googleclientauth
      pipelines:
        logs:
          receivers:
          - otlp
          processors:
          - resourcedetection
          - resource/gcp_project_id
          - transform/otlp_grpc/preserve_instrumentation_source_version
          - transform/otlp_grpc/copy_service_resource_labels
          - memory_limiter
          - batch
          exporters:
          - otlp_grpc
        metrics/otlp:
          receivers:
          - otlp
          processors:
          - resourcedetection
          - resource/gcp_project_id
          - transform/collision
          - transform/prometheus_unknown_types
          - metricstarttime
          - memory_limiter
          - batch
          exporters:
          - otlp_grpc
        traces:
          receivers:
          - otlp
          processors:
          - resourcedetection
          - resource/gcp_project_id
          - memory_limiter
          - batch
          exporters:
          - otlp_grpc
      # Internal telemetry for the collector supports both push and pull-based telemetry data transmission.
      # Leveraging the pre-configured OTLP receiver eliminates the need for an additional port.
      #
      # Docs:
      # https://opentelemetry.io/docs/collector/internal-telemetry/
      telemetry:
        metrics:
          readers:
            - periodic:
                exporter:
                  otlp:
                    protocol: grpc
                    endpoint: http://localhost:4317
                    insecure: true
    

### Exporters

The Collector configuration uses the following:

  * The OTLP gRPC exporter, to send logs, metrics, and traces to the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).
  * The [`googleclientauthextension`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.158.0/extension/googleclientauthextension) for API authentication.



### Processors

The Collector configuration includes the following processors:

  * [`batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/batchprocessor): Configured to batch telemetry requests at the Google Cloud maximum number of entries per request, or at the Google Cloud minimum interval of every 5 seconds (whichever comes first).

  * [`memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/memorylimiterprocessor): Caps the Collector's memory usage to prevent out-of-memory crashes by dropping data points when the limit is exceeded.

  * [`resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourcedetectionprocessor): Automatically detects Google Cloud resource labels such as `project_id`. 




### Receivers

The Collector configuration includes only the [`otlp` receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/main/receiver/otlpreceiver). For information about instrumenting your applications to send OTLP traces and metrics to the Collector's OTLP endpoint, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

### Available components

The Google-Built OpenTelemetry Collector contains the components that most users will need to enable a rich experience within Google Cloud Observability. For a complete list of available components, see [Components](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/tree/v0.163.0/google-built-opentelemetry-collector/README.md#components) in the `opentelemetry-operations-collector` repository.

To request any changes or additions to the available components, [open a feature request](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/issues). in the `opentelemetry-operations-collector` repository.

## Generate telemetry

You can test your configuration by using the open-source [`telemetrygen` tool](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.163.0/cmd/telemetrygen). Instructions for downloading and running the tool are included at the link. To run the tool, you must install either Go or Docker.

After a few minutes, telemetry generated by the application begins flowing through the Collector to the Google Cloud console for each signal.

## View telemetry

The Google-Built OpenTelemetry Collector sends metrics, logs, and traces from your instrumented applications to Google Cloud Observability. The Collector also sends self-observability metrics. The following sections describe how to view this telemetry.

### View your metrics

The Google-Built OpenTelemetry Collector collects Prometheus metrics that you can view by using the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). The metrics collected depend on the instrumentation of the app, although the Google-built Collector also writes some self-metrics.

To view the metrics collected by the Google-Built OpenTelemetry Collector, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `**Prometheus Target**` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Prometheus Target**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. Metrics collected by the Google-Built OpenTelemetry Collector have the prefix `prometheus.googleapis.com`. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed.   


When the measurements for a metric are cumulative, Metrics Explorer automatically normalizes the measured data by the alignment period, which results in the chart displaying a rate. For more information, see [Kinds, types, and conversions](https://docs.cloud.google.com/monitoring/api/v3/aggregation#ts-conversion).

When integer or double values are measured, such as with `counter` metrics, Metrics Explorer automatically sums all time series. To change this behavior, set the first menu of the **Aggregation** entry to **None**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




### View your traces

To view your trace data, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the table section of the page, select a row.
  4. In the Gantt chart on the **Trace details** panel, select a span.

A panel opens that displays information about the traced request. These details include the method, status code, number of bytes, and the user agent of the caller.

  5. To view the logs associated with this trace, select the **Logs & Events** tab.

The tab shows individual logs. To view the details of the log entry, expand the log entry. You can also click **View Logs** and view the log by using the Logs Explorer.




For more information about using the Cloud Trace explorer, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

### View your logs

From the Logs Explorer, you can inspect your logs, and you can also view associated traces, when they exist.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate a log entry from your instrumented app. To view the details, expand the log entry.

  3. Click ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Traces** on a log entry with a trace message, and then select **View trace details**.

A **Trace details** panel opens and displays the selected trace.




For more information about using the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Observe and debug the Collector

The Google-Built OpenTelemetry Collector automatically provides self-observability metrics to help you monitor its performance and ensure continued uptime of the OTLP ingestion pipeline.

To monitor the Collector, install the sample dashboard for the Collector. This dashboard offers at-a-glance insights into several metrics from the Collector, including uptime, memory usage, and API calls to Google Cloud Observability.

To install the dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Dashboard Templates**.
  3. Search for the **OpenTelemetry Collector** dashboard.
  4. Optional: To preview the dashboard, select it.
  5. Click _playlist_add_ **Add dashboard to your list** and then complete the dialog.

The dialog lets you select the name of the dashboard, and add labels to the dashboard.




For more information about installing dashboards, see [Install a dashboard template](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
