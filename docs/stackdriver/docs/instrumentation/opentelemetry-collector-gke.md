---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke/
title: Deploy Google-Built OpenTelemetry Collector on Google Kubernetes Engine \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:54.670776+00:00
---

# Deploy Google-Built OpenTelemetry Collector on Google Kubernetes Engine  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Deploy Google-Built OpenTelemetry Collector on Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to run the [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel) on Google Kubernetes Engine to collect OTLP logs, metrics, and traces from instrumented applications and then export that data to Google Cloud.

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

  4. Enable the Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Telemetry, Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com,logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

  8. A Kubernetes cluster. If you don't have a Kubernetes cluster, then follow the instructions in the [Quickstart for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

  9. The following command-line tools:

     * `gcloud`
     * `kubectl`

The `gcloud` and `kubectl` tools are part of the Google Cloud CLI. For information about installing them, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components). To see the gcloud CLI components you have installed, run the following command:
    
    gcloud components list
            




## Configure permissions for the Collector

If you have disabled GKE workload identity, then you can skip this section.

To ensure that the OpenTelemetry Collector's kubernetes service account has the necessary permissions to export telemetry, ask your administrator to grant the following IAM roles to the OpenTelemetry Collector's kubernetes service account on your project: 

**Important:** You must grant these roles to the OpenTelemetry Collector's kubernetes service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
  * [Logging Log Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
  * [Cloud Trace Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the OpenTelemetry Collector's kubernetes service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To configure the permissions, use the following [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) commands:
    
    
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
        --role=roles/logging.logWriter \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/opentelemetry/sa/opentelemetry-collector
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
        --role=roles/monitoring.metricWriter \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/opentelemetry/sa/opentelemetry-collector
    gcloud projects add-iam-policy-binding projects/PROJECT_ID \
        --role=roles/cloudtrace.agent \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/opentelemetry/sa/opentelemetry-collector
    

Before running the commands, replace the following variables:

  * PROJECT_ID: The identifier of the project.
  * PROJECT_NUMBER: The Google Cloud project number.



## Deploy the Collector

The Collector pipeline can be deployed directly from the vetted examples provided by the [Self-Managed OTLP Kubernetes Ingestion repo](https://github.com/GoogleCloudPlatform/otlp-k8s-ingest/tree/main/k8s/base). You can deploy directly from GitHub with the following commands after replacing PROJECT_ID with the ID of your Google Cloud project:
    
    
    export GOOGLE_CLOUD_PROJECT=PROJECT_ID
    export PROJECT_NUMBER=PROJECT_NUMBER
    kubectl kustomize https://github.com/GoogleCloudPlatform/otlp-k8s-ingest.git/k8s/base | envsubst | kubectl apply -f -
    

Before running the commands, replace the following variables:

  * PROJECT_ID: The identifier of the project.
  * PROJECT_NUMBER: The numeric identifier of the project.



## Configure the Collector

We provide an OpenTelemetry Collector configuration for you to use with the Google-built Collector. This configuration is designed to deliver high volumes of OTLP metrics, logs, and traces with consistent GKE and Kubernetes metadata attached. This configuration is also designed to prevent common ingestion issues. You can add to the configuration, but we strongly recommend that you don't remove elements.

This section describes the provided configuration, the key components like exporters, processors, receivers, and other available components.

### Provided Collector configuration

You can find the Collector configuration for Kubernetes environments in the [`otlp-k8s-ingest` repository](https://github.com/GoogleCloudPlatform/otlp-k8s-ingest/blob/main/config/collector.yaml): 
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    exporters:
      googlecloud:
        log:
          default_log_name: opentelemetry-collector
        user_agent: Google-Cloud-OTLP manifests:0.5.0 OpenTelemetry Collector Built By Google/0.131.0 (linux/amd64)
      googlemanagedprometheus:
        user_agent: Google-Cloud-OTLP manifests:0.5.0 OpenTelemetry Collector Built By Google/0.131.0 (linux/amd64)
      # The otlphttp exporter is used to send traces to Google Cloud Trace using OTLP http/proto
      # The otlp exporter could also be used to send them using OTLP grpc
      otlphttp:
        encoding: proto
        endpoint: https://telemetry.googleapis.com
        # Use the googleclientauth extension to authenticate with Google credentials
        auth:
          authenticator: googleclientauth
    
    
    extensions:
      health_check:
        endpoint: ${env:MY_POD_IP}:13133
      googleclientauth:
    
    
    processors:
      filter/self-metrics:
        metrics:
          include:
            match_type: strict
            metric_names:
            - otelcol_process_uptime
            - otelcol_process_memory_rss
            - otelcol_grpc_io_client_completed_rpcs
            - otelcol_googlecloudmonitoring_point_count
      batch:
        send_batch_max_size: 200
        send_batch_size: 200
        timeout: 5s
    
      k8sattributes:
        extract:
          metadata:
          - k8s.namespace.name
          - k8s.deployment.name
          - k8s.statefulset.name
          - k8s.daemonset.name
          - k8s.cronjob.name
          - k8s.job.name
          - k8s.replicaset.name
          - k8s.node.name
          - k8s.pod.name
          - k8s.pod.uid
          - k8s.pod.start_time
        passthrough: false
        pod_association:
        - sources:
          - from: resource_attribute
            name: k8s.pod.ip
        - sources:
          - from: resource_attribute
            name: k8s.pod.uid
        - sources:
          - from: connection
    
      memory_limiter:
        check_interval: 1s
        limit_percentage: 65
        spike_limit_percentage: 20
    
      metricstransform/self-metrics:
        transforms:
        - action: update
          include: otelcol_process_uptime
          operations:
          - action: add_label
            new_label: version
            new_value: Google-Cloud-OTLP manifests:0.5.0 OpenTelemetry Collector Built By Google/0.131.0 (linux/amd64)
    
      resourcedetection:
        detectors: [gcp]
        timeout: 10s
    
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
    
      # The relative ordering of statements between ReplicaSet & Deployment and Job & CronJob are important.
      # The ordering of these controllers is decided based on the k8s controller documentation available at
      # https://kubernetes.io/docs/concepts/workloads/controllers.
      # The relative ordering of the other controllers in this list is inconsequential since they directly
      # create pods.
      transform/aco-gke:
        metric_statements:
        - context: datapoint
          statements:
          - set(attributes["top_level_controller_type"], "ReplicaSet") where resource.attributes["k8s.replicaset.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.replicaset.name"]) where resource.attributes["k8s.replicaset.name"] != nil
          - set(attributes["top_level_controller_type"], "Deployment") where resource.attributes["k8s.deployment.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.deployment.name"]) where resource.attributes["k8s.deployment.name"] != nil
          - set(attributes["top_level_controller_type"], "DaemonSet") where resource.attributes["k8s.daemonset.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.daemonset.name"]) where resource.attributes["k8s.daemonset.name"] != nil
          - set(attributes["top_level_controller_type"], "StatefulSet") where resource.attributes["k8s.statefulset.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.statefulset.name"]) where resource.attributes["k8s.statefulset.name"] != nil
          - set(attributes["top_level_controller_type"], "Job") where resource.attributes["k8s.job.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.job.name"]) where resource.attributes["k8s.job.name"] != nil
          - set(attributes["top_level_controller_type"], "CronJob") where resource.attributes["k8s.cronjob.name"] != nil
          - set(attributes["top_level_controller_name"], resource.attributes["k8s.cronjob.name"]) where resource.attributes["k8s.cronjob.name"] != nil
    
      # When sending telemetry to the GCP OTLP endpoint, the gcp.project_id resource attribute is required to be set to your project ID.
      resource/gcp_project_id:
        attributes:
        - key: gcp.project_id
          # MAKE SURE YOU REPLACE THIS WITH YOUR PROJECT ID
          value: ${GOOGLE_CLOUD_PROJECT}
          action: insert
      # The metricstarttime processor is important to include if you are using the prometheus receiver to ensure the start time is set properly.
      # It is a no-op otherwise.
      metricstarttime:
        strategy: subtract_initial_point
    
    receivers:
      # This collector is configured to accept OTLP metrics, logs, and traces, and is designed to receive OTLP from workloads running in the cluster.
      otlp:
        protocols:
          grpc:
            endpoint: ${env:MY_POD_IP}:4317
          http:
            cors:
              allowed_origins:
              - http://*
              - https://*
            endpoint: ${env:MY_POD_IP}:4318
      otlp/self-metrics:
        protocols:
          grpc:
            endpoint: ${env:MY_POD_IP}:14317
    
    service:
      extensions:
      - health_check
      - googleclientauth
      pipelines:
        logs:
          exporters:
          - googlecloud
          processors:
          - k8sattributes
          - resourcedetection
          - memory_limiter
          - batch
          receivers:
          - otlp
        metrics/otlp:
          exporters:
          - googlemanagedprometheus
          processors:
          - k8sattributes
          - memory_limiter
          - metricstarttime
          - resourcedetection
          - transform/collision
          - transform/aco-gke
          - batch
          receivers:
          - otlp
        metrics/self-metrics:
          exporters:
          - googlemanagedprometheus
          processors:
          - filter/self-metrics
          - metricstransform/self-metrics
          - k8sattributes
          - memory_limiter
          - resourcedetection
          - batch
          receivers:
          - otlp/self-metrics
        traces:
          exporters:
          - otlphttp
          processors:
          - k8sattributes
          - memory_limiter
          - resource/gcp_project_id
          - resourcedetection
          - batch
          receivers:
          - otlp
      telemetry:
        logs:
          encoding: json
        metrics:
          readers:
          - periodic:
              exporter:
                otlp:
                  protocol: grpc
                  endpoint: http://${env:MY_POD_IP}:14317
                  insecure: true
    

### Exporters

The Collector configuration uses the following:

  * The OTLP gRPC exporter, to send logs, metrics, and traces to the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).
  * The [`googleclientauthextension`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.158.0/extension/googleclientauthextension) for API authentication.



### Processors

The Collector configuration includes the following processors:

  * [`batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/batchprocessor): Configured to batch telemetry requests at the Google Cloud maximum number of entries per request, or at the Google Cloud minimum interval of every 5 seconds (whichever comes first).

  * [`memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/main/processor/memorylimiterprocessor): Caps the Collector's memory usage to prevent out-of-memory crashes by dropping data points when the limit is exceeded.

  * [`resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourcedetectionprocessor): Automatically detects Google Cloud resource labels such as `project_id` and `cluster_name`. 

  * [`k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/k8sattributesprocessor): Automatically maps Kubernetes resource attributes to telemetry labels.

  * [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor): Renames metric labels that collide with labels on Google Cloud monitored resources. 




### Receivers

The Collector configuration includes only the [`otlp` receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/main/receiver/otlpreceiver). For information about instrumenting your applications to send OTLP traces and metrics to the Collector's OTLP endpoint, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

### Available components

The Google-Built OpenTelemetry Collector contains the components that most users will need to enable a rich experience within Google Cloud Observability. For a complete list of available components, see [Components](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/tree/v0.163.0/google-built-opentelemetry-collector/README.md#components) in the `opentelemetry-operations-collector` repository.

To request any changes or additions to the available components, [open a feature request](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/issues). in the `opentelemetry-operations-collector` repository.

## Generate telemetry

This section describes deploying a sample application and pointing that application to the Collector's OTLP endpoint, and viewing the telemetry in Google Cloud. The sample application is a small generator that exports traces, logs, and metrics to the Collector.

If you already have an application instrumented with an OpenTelemetry SDK, then you can point your application to the Collector's endpoint instead.

To deploy the sample application, run the following command:
    
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/otlp-k8s-ingest/main/sample/app.yaml
    

To point existing applications that use the OpenTelemetry SDK at the Collector's endpoint, set the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to `http://opentelemetry-collector.opentelemetry.svc.cluster.local:4317`.

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
