---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/sample-overview/
title: Overview of collector-based instrumentation samples \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:26.770048+00:00
---

# Overview of collector-based instrumentation samples  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/sample-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Overview of collector-based instrumentation samples Stay organized with collections  Save and categorize content based on your preferences. 

To keep your application code vendor-neutral while collecting and sending telemetry to Google Cloud, you can use the OpenTelemetry collector-based instrumentation samples for [Go](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go), [Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java), [Node.js](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs), and [Python](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python).

These samples demonstrate how to configure an in-process OpenTelemetry SDK to export metrics, logs, and traces to a local OpenTelemetry collector that routes your telemetry to Google Cloud. The samples send metric and trace data in OpenTelemetry Protocol (OTLP) format to your Google Cloud project by using the Telemetry API, and send log data by using a Google Cloud exporter.

## How the samples work

The samples for Go, Java, Node.js, and Python use the [OpenTelemetry protocol](https://opentelemetry.io/docs/specs/otlp/) to collect trace and metric data. The samples configure a logging framework to write [structured logs](https://docs.cloud.google.com/logging/docs/structured-logging), and configure the OpenTelemetry collector to read from the application's `stdout` stream. For framework recommendations, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

The applications are built and deployed by using Docker. You don't have to use Docker when you instrument an application with OpenTelemetry.

You can run the samples in the Cloud Shell, on Google Cloud resources, or on a local development environment.

## Deep dive

The samples use the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/installation/) as a sidecar to receive and enrich the application's telemetry, which an exporter then sends to your Google Cloud project. The sample applications send metric and trace data to your project by using the Telemetry API, which supports the OTLP format.

The samples show how to do the following:

  1. Configure OpenTelemetry to collect metrics and traces by using the [OpenTelemetry collector](https://opentelemetry.io/docs/collector/).

The complexity of this step is language dependent. For example, in Go, you update the `main` function to initialize telemetry collection and configure the HTTP server and client.

  2. Configure a logging framework to write [structured logs](https://docs.cloud.google.com/logging/docs/structured-logging).

We recommend that your applications write structured logs, which format the log payload as a JSON object. For these logs, you can construct queries that search specific JSON paths and you can index specific fields in the log payload.

Some services, like Google Kubernetes Engine, have built-in agents that scrape structured logs and send those logs to your Google Cloud project. Other services, like Compute Engine, require that you install an agent, which scrapes and sends your logs. To learn about agents you install, see [Ops Agent overview](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent).

You don't need to install any agents to use these samples.

  3. Configure Docker files. All samples contain the following YAML files:

     * `docker-compose.yaml`: Configures the services for the application, the [OpenTelemetry collector](https://opentelemetry.io/docs/collector/), and a load generator. For example, the service for the OpenTelemetry collector, `otelcol`, specifies an image, a volume, and environment variables. The endpoint for the OpenTelemetry collector is set by the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable, which is specified in the `app` service.

     * `otel-collector-config.yaml`: Configures the OpenTelemetry collector:

       * The samples use the `otlp` receiver for metric and trace data, and the `filelog` receiver for log data.

       * The samples use the `otlphttp` exporter for metric and trace data, and the Google Cloud exporter for log data.

The `otlphttp` exporter sends data to your project by using the Telemetry API, which supports OTLP. The Google Cloud exporter converts your log data into a format compatible with the Cloud Logging API and then sends the transformed data to your Google Cloud project.

     * `docker-compose.creds.yaml`: This file optionally mounts a Google Cloud credentials file in the `otelcol` container. You need this file when you run a sample on a local machine where [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) are available only as a file.




## Required permissions

  * To get the permissions that you need to have the sample applications write log, metric, and trace data, ask your administrator to grant you the following IAM roles: 

    * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on your project
    * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on your project
    * [Cloud Telemetry Traces Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`) on your project
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your quota project

These permissions are sufficient if you run the sample in the Cloud Shell, on Google Cloud resources, or on a local development environment. To learn how to configure a quota project, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

**Note:** Production applications typically rely on a service account to provide the credentials required to write log, metric, and trace data. In those scenarios, grant the previous roles to the service account.


  * To get the permissions that you need to view your log, metric, and trace data, ask your administrator to grant you the following IAM roles on your project: 

    * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
    * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
    * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Required APIs

Enable the Cloud Logging, Cloud Monitoring, Cloud Trace, and Telemetry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable logging.googleapis.com monitoring.googleapis.com cloudtrace.googleapis.com telemetry.googleapis.com

## Alternative instrumentation approaches

You might be interested in other samples that illustrate different configurations:

  * [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/stackdriver/docs/instrumentation/migrate-to-otlp-endpoints) describes how to use in-process instrumentation to send trace data directly to your Google Cloud project.

We recommend that you use an OpenTelemetry collector to export your telemetry data when your environment supports use of a collector. If you can't use a collector, then you must use an in-process exporter that directly sends data to your Google Cloud project.

  * [Correlate metrics and traces by using exemplars](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/exemplars) describes how to configure a Go application to generate exemplars. An _exemplar_ is an example data point attached to a metric data point. You can use exemplars to correlate your trace and metric data.

  * [Use the Ops Agent and OpenTelemetry Protocol (OTLP)](https://docs.cloud.google.com/trace/docs/otlp) describes how you can configure the Ops Agent and an OTLP receiver to collect metrics and traces from an application.




## What's next

To learn more about collectors, see [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

Explore the samples that use collector-based exports.

  * [Go sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java)
  * [Node.js sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)
  * [Python sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
