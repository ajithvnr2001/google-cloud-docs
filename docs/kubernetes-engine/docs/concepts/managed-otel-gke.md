---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke/
title: Managed OpenTelemetry for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:09.026951+00:00
---

# Managed OpenTelemetry for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Managed OpenTelemetry for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes Managed OpenTelemetry for Google Kubernetes Engine (GKE), which lets you send [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) traces, metrics, and logs to Google Cloud Observability from applications running on GKE. Managed OpenTelemetry provides the only managed solution by Google Cloud for collecting trace data on GKE.

To use Managed OpenTelemetry for Google Kubernetes Engine (GKE), applications need to be already instrumented to generate signals using the OpenTelemetry protocol. For details, see Supported workloads.

Managed OpenTelemetry for GKE has two components:

  * **Managed collection** : The managed collector provides an in-cluster OpenTelemetry Protocol endpoint as a destination for workloads to send traces, metrics, and logs in OTLP format, without having to manage a collector.
  * **Automatic configuration** : A [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) called `Instrumentation` enables an automatic configuration for your GKE workloads to generate and ingest correlated OpenTelemetry traces, metrics, and logs. This approach supports the [Agent Development Kit (ADK)](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk) and [multimodal prompts and responses data](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#multimodal-prompts-responses).

You can use the `Instrumentation` custom resource for workloads that use the OpenTelemetry SDK and are configured with standard OpenTelemetry environment variables. This `Instrumentation` custom resource, `instrumentations.telemetry.googleapis.com`, is a different resource from `Instrumentation` resource for the OpenTelemetry operator.




For steps to use the Managed OpenTelemetry for GKE, see [Deploy Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke).

Managed OpenTelemetry for GKE lets you collect OTLP telemetry without having to manage and operate an OpenTelemetry collector. Running your own collector can incur overhead, including authentication, configuration, upgrades, and monitoring. However, if you need collector-level filtering and controls, you can use the [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel) instead of this managed service.

OpenTelemetry provides APIs, libraries, and SDKs to generate distributed traces, metrics, and logs for application monitoring. For more information about OpenTelemetry, see the documentation about [OpenTelemetry](https://opentelemetry.io/) and the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/). For more details about generating and collecting your application's runtime behavior data, see [Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview).

## How Managed OpenTelemetry for GKE works

Managed OpenTelemetry for GKE has two components: managed collection and automatic configuration.

### Managed collection

Managed collection provides an in-cluster OTLP endpoint by deploying a managed OpenTelemetry collector to your cluster. This in-cluster OTLP endpoint receives traces, metrics, and logs in OTLP format. To receive data from a workload, the workload must be configured to send data to the collector.

The managed collector's endpoint is: `http://opentelemetry-collector.gke-managed-otel.svc.cluster.local:4318`.

The managed collection sends the collected data to Google Cloud Observability. The data is then available in the following services:

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview)
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview)



The managed collector can be enabled for a GKE cluster using the console or the gcloud CLI. For instructions, see [Enable Managed OpenTelemetry for GKE in a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#enable-managed-opentelemetry).

### Automatic configuration

Automatic configuration lets GKE configure workloads running on GKE to send signals to the managed collector's endpoint.

There are different methods that can be used to configure a workload. Automatic configuration uses environment variables injected in the workload's container to have the workload send signals to the managed collector. If you are manually configuring the workload, you can use other methods. For details, see Manual configuration.

When you use automatic configuration, you define the configuration using the `Instrumentation` custom resource. Then, GKE injects environment variables, such as the OTLP exporter endpoint, into the workload's containers. When the workload's containers have these environment variables, then as the workload runs OpenTelemetry data is sent to the managed collector.

Automatic configuration is available for workloads that natively support OpenTelemetry, which means that they use the OpenTelemetry SDK and are configured using standard OpenTelemetry environment variables. For more details, see [Supported workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#supported-workloads).

For instructions to configure your application using the automatic configuration, see [Configure your application to use the Managed OpenTelemetry collector](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#configure-application).

#### The `Instrumentation` custom resource

You use the `Instrumentation` custom resource to do the following:

  * Specify whether to inject the environment variables into the containers of selected Pods or of all Pods in a namespace.
  * Control the type of data that is collected (logs, metrics, and traces).
  * Control the frequency that metrics data is sent to the managed collector.
  * Control the sampling rate of trace data.



For details about how use the `Instrumentation` custom resource, see [Modify the configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#modify-configuration).

#### Inject environment variables automatically

To inject OpenTelemetry environment variables into your GKE workloads automatically, you need to configure an `Instrumentation` object in your cluster. Then, when you deploy the application in the cluster with the `Instrumentation` object, the variables are then injected by GKE.

The `Instrumentation` object needs to be in the cluster when the application is deployed and the Pods are created. If you deployed the application before you created the `Instrumentation` object, then you need to _restart_ the application's pods to trigger automatic injection of the environment variables.

#### Environment variables

When a workload is deployed to the namespace where automatic configuration is enabled, then GKE injects environment variables into the workloads' containers. These environment variables are OpenTelemetry variables from the [OpenTelemetry SDK Configuration](https://opentelemetry.io/docs/languages/sdk-configuration/).

The following list contains all of the environment variables that can be injected by Managed OpenTelemetry for GKE. The specific environment variables injected to a container depend on the configuration in the `Instrumentation` custom resource.

The environment variables that can be injected automatically into containers are the following:

  * OpenTelemetry exporter endpoint. 
    * `OTEL_EXPORTER_OTLP_ENDPOINT`: A base endpoint URL for any signal type. This endpoint always points to the in-cluster managed OpenTelemetry collector HTTP endpoint for logs, metrics, and traces. The endpoint is: `http://opentelemetry-collector.gke-managed-otel.svc.cluster.local:4318`.
  * Trace sampling ratio configuration. 
    * `OTEL_TRACES_SAMPLER`: Sets the [sampler](https://opentelemetry.io/docs/languages/sdk-configuration/general/#otel_traces_sampler) used to sample traces by the SDK to one of the following: 
      * `parentbased_traceidratio` when trace sampling is configured in the custom resource.
      * `parentbased_always_on` is the default value of this environment variable. It is used if this environment variable isn't configured or is null in the custom resource.
    * `OTEL_TRACES_SAMPLER_ARG`: Specifies the trace sampling ratio (between 0.0 and 1.0). If not configured in the custom resource, then 1.0 is used.
  * Delay interval between start of two consecutive metric exports. 
    * `OTEL_METRIC_EXPORT_INTERVAL`: The time interval (in milliseconds) between the start of two export attempts (min: 5000, max: 300000, default: 30000).
  * Disablement of OTLP telemetry export by signal type. Signal exporters are disabled when `tracer_provider`, `meter_provider`, or `logger_provider` are set to `null` in the `Instrumentation` file. 
    * `OTEL_TRACES_EXPORTER`: Disables export of traces when set to `none`. Default value: `otlp`.
    * `OTEL_METRICS_EXPORTER`: Disables export of metrics when set to `none`. Default value: `otlp`.
    * `OTEL_LOGS_EXPORTER`: Disables export of logs when set to `none`. Default value: `otlp`.
  * Identification of hostNetwork Pods for associating the metadata by [Kubernetes Attributes Processor](https://opentelemetry.io/docs/platforms/kubernetes/collector/components/#kubernetes-attributes-processor) of the OpenTelemetry Collector. 
    * `K8S_POD_UID`: The Pod UID of a hostNetwork Pod for populating the `k8s.pod.uid` setting in the `OTEL_RESOURCE_ATTRIBUTES` environment variable.
    * `OTEL_RESOURCE_ATTRIBUTES`: The value includes `k8s.pod.uid=$(K8S_POD_UID)` to allow the Kubernetes Attributes Processor to associate metadata, such as `k8s.namespace.name`, `k8s.deployment.name` and `k8s.node.name`, to hostNetwork Pods. The association of metadata and hostNetwork Pods allows for adding the extracted metadata to spans, metrics, and logs as resource attributes.
  * Prompts and responses. 
    * `OTEL_INSTRUMENTATION_GENAI_UPLOAD_FORMAT='jsonl'`: Instruct OpenTelemetry to format Cloud Storage objects as JSON Lines. This environment variable has a fixed value: `jsonl`.
    * `OTEL_INSTRUMENTATION_GENAI_COMPLETION_HOOK='upload'`: Instruct OpenTelemetry to upload prompt and response data instead of embedding this content in trace spans. References to the uploaded objects are included in a log entry. This environment variable has a fixed value: `upload`.
    * `OTEL_SEMCONV_STABILITY_OPT_IN='gen_ai_latest_experimental'`: Instruct OpenTelemetry to use the most recent semantic conventions for generative AI. This environment variable has a fixed value: `gen_ai_latest_experimental`.
    * `OTEL_INSTRUMENTATION_GENAI_UPLOAD_BASE_PATH`: Specify the path for objects. For example, `gs://STORAGE_BUCKET_NAME/PATH`



### Manual configuration

There are different methods that you can use to configure a workload to send signals to the managed collector's [endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke#environment_variables). If you are manually configuring your workload, then you can manually add and modify environment variables, or you can use another method such as command line flags.

We don't recommend using both manual configuration and automatic configuration together for the same workload, because the automatic configuration can override manual changes. This combination might make it more difficult to track changes to the configuration.

For details about automatic configuration, see Automatic configuration

## Supported workloads

Supported workloads are workloads that use OpenTelemetry to collect data about the application's runtime behavior. Workloads natively support OpenTelemetry if they use the OpenTelemetry SDK and are configured using standard OpenTelemetry environment variables. For example, the [Agent Development Kit (ADK)](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk) natively supports OpenTelemetry.

For more details about how your application's runtime behavior data is generated and collected, see [Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview).

If a workload supports some types of OTLP data and not others, then Managed OpenTelemetry for GKE collects the OTLP data. For example, if a workload uses the OpenTelemetry SDK to implement traces but doesn't use it for logs or metrics, then logs and metrics data is not collected by Managed OpenTelemetry for GKE. For details about how to control the type of data to collect, see [Select the signal types to collect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#select-signal-type).

OpenTelemetry configuration injection is not supported for [privileged workloads from GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).

## Billing

When you send telemetry data to Google Cloud, you are billed by ingestion volume. Metrics are billed using the Google Cloud Managed Service for Prometheus pricing, logs are billed using the Cloud Logging pricing, and traces are billed using the Cloud Trace pricing.

For information about costs associated with the ingestion of traces, logs, and Google Cloud Managed Service for Prometheus metrics, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

## Quotas

When you use Managed OpenTelemetry for GKE, the quotas for Google Cloud Observability services apply. For details, see the following:

  * [Cloud Logging quotas and limits](https://docs.cloud.google.com/logging/quotas)
  * [Cloud Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas)
  * [Cloud Trace quotas and limits](https://docs.cloud.google.com/trace/docs/quotas)



## What's next

  * To deploy the collector, see [Deploy Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke).
  * For a self-deployed alternative to Managed OpenTelemetry for GKE, see [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).
  * For information about setting up OpenTelemetry instrumentation to generate traces, metrics, and logs from your applications, see the following: 
    * [Instrumentation overview](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview)
    * [Choose an instrumentation approach for your application](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
    * [Generate traces and metrics with OpenTelemetry instrumentation](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach#samples)
  * [Add custom traces and metrics to your app with OpenTelemetry](https://docs.cloud.google.com/monitoring/custom-metrics/open-telemetry).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
