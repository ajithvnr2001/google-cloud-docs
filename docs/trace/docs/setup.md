---
url: https://docs.cloud.google.com/trace/docs/setup/
title: Instrument for Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:04.711314+00:00
---

# Instrument for Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Instrument for Cloud Trace Stay organized with collections  Save and categorize content based on your preferences. 

You can instrument your applications for Cloud Trace to capture distributed tracing data, examine latency for individual requests, and view the aggregate latency across your services in the Trace console.

This document provides an overview of instrumentation approaches and configuration options. For step-by-step instructions for specific programming languages, see the language-specific setup pages.

## When to instrument your application

**Note:** Trace data is automatically captured for some configurations and for some Google Cloud services, so you might not need to instrument your application. For more information, see [Configurations with automatic tracing](https://docs.cloud.google.com/trace/docs/overview#configurations_with_automatic_tracing). 

Instrument your application to collect specific information that helps you understand its performance and troubleshoot failures. Several open-source instrumentation frameworks collect log, metric, and trace data, and can send that data to any vendor, including Google Cloud. For your agentic applications, some frameworks can collect your prompts and responses or pass context that allows tracing of some remote [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) calls.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

## How to instrument applications

There are several approaches that you can use to instrument your application:

  * **Recommended** : Use [OpenTelemetry](https://opentelemetry.io), configure your application with an OTLP exporter that sends trace data to a collector, and configure the collector to send trace data to your Google Cloud project by using the Telemetry (OTLP) API. To learn more about our recommendations, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

  * Use [OpenTelemetry](https://opentelemetry.io) and configure your application with an OTLP exporter that sends your trace data to your Google Cloud project by using the Telemetry API.

  * If you write applications that run on Compute Engine, then you can use the Ops Agent and the OpenTelemetry Protocol (OTLP) receiver to collect traces and metrics from your application. The Ops Agent can also collect logs, but not by using OTLP. For more information, see [Use the Ops Agent and OTLP](https://docs.cloud.google.com/trace/docs/otlp) and [Ops Agent overview](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent).

  * Directly invoke either the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) or the [Cloud Trace API](https://docs.cloud.google.com/trace/api).

  * For [Spring Boot](https://spring.io/projects/spring-boot) applications, configure them to forward the trace data they collect to Cloud Trace. For information about this procedure, see [Spring Cloud for Google Cloud: Cloud Trace](https://googlecloudplatform.github.io/spring-cloud-gcp/reference/html/index.html#cloud-trace).

  * Use [Cloud Trace client libraries](https://docs.cloud.google.com/trace/docs/client-libraries) or use the Cloud Trace exporter for OpenTelemetry.




### Instrumentation samples

The instrumentation samples we provide use [OpenTelemetry](https://opentelemetry.io):

  * For samples that use a collector-based export, see the following:

    * [Go](https://docs.cloud.google.com/trace/docs/setup/go)
    * [Java](https://docs.cloud.google.com/trace/docs/setup/java)
    * [Node.js](https://docs.cloud.google.com/trace/docs/setup/nodejs)
    * [Python](https://docs.cloud.google.com/trace/docs/setup/python)

These samples send metric and trace data that follows the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp) (OTLP) format to your project by using the Telemetry API. The samples use a Google Cloud exporter for log data.

  * For information about how to use a direct export of trace data and send that data to the Telemetry API, see [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/trace/docs/migrate-to-otlp-endpoints).

  * For samples that show you how to configure an agentic application to collect prompts and responses, see [Observability for AI agent developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers).



  * For information about Google Cloud MCP servers that can generate trace spans, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).



### Create custom spans

While OpenTelemetry and client libraries allow you to create custom spans, you might not need to create them manually because these libraries automatically create spans at RPC boundaries.

You can also add information relevant to your application by adding custom annotations and tags to existing spans, or you can create new child spans with their own annotations and tags to trace the application's behavior with finer granularity.

Libraries typically maintain a global trace context that holds information about the current span, including its trace ID and sampling status. Applications can access the current span through the global trace context. Because the context is global, make sure that multi-threaded applications propagate context across threads to maintain accurate trace data.

### Force trace sampling

You can't force spans to be sampled because each component in the request path makes an independent [sampling decision](https://docs.cloud.google.com/trace/docs/trace-sampling). However, you can influence downstream components by setting the [`sampled` flag](https://www.w3.org/TR/trace-context/#sampled-flag) in the trace header to `true`. This setting is a hint to child components to sample the request. For more information about trace headers, see [Protocols for context propagation](https://docs.cloud.google.com/trace/docs/trace-context#context-propagation-protocols).

  * Your applications: You configure how the instrumentation logic respects the `sampled` flag. For example, when using [OpenTelemetry](https://opentelemetry.io), you can use the [`ParentBased` sampler](https://opentelemetry.io/docs/specs/otel/trace/sdk/#parentbased) to ensure that the parent's sampling flag is respected.

  * Google Cloud services: Each service determines its own tracing support. In general, services accept the parent sampling flag as a hint while enforcing their own sampling rate limits.




### Correlate metrics and traces with exemplars

You can correlate metric data with traces by using exemplars. An _exemplar_ is a representative sample request or span associated with a metric measurement. For example, an exemplar can contain a link to a trace, which lets you correlate your metric and trace data. For an OpenTelemetry-based example, see [Correlate metrics and traces by using exemplars](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/exemplars).

You might see system-generated exemplars on dashboard charts that display SQL query results for trace data. These exemplars link specific query results directly to traces. For more information, see [Generate and display trace exemplars](https://docs.cloud.google.com/trace/docs/analytics-chart#show-trace-exemplars).

## Configure your project and platform

This section describes the required APIs and Identity and Access Management (IAM) roles, and explains how to configure authentication credentials for your platform..

### Enable APIs

By default, Google Cloud projects have the Cloud Trace API and Telemetry API enabled, and you don't need to take any action. However, security constraints defined by your organization might have disabled one or both of these APIs. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment).

Enable the Telemetry and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=telemetry.googleapis.com,cloudtrace.googleapis.com)

### Grant IAM roles

The required IAM roles depend on whether you are viewing trace data in the Google Cloud console or writing trace data to your project:

  * To get the permissions that you need to view trace data by using the Google Cloud console, ask your administrator to grant you the [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`) IAM role on your project. 



  * To get the permissions that you need to write trace data by using the Cloud Trace API, ask your administrator to grant you the [Cloud Trace Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) IAM role on your project. 



  * To get the permissions that you need to write trace data by using the Telemetry API, ask your administrator to grant you the [Cloud Telemetry Writer role ](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.writer) (`roles/telemetry.writer`) IAM role on your project. 




### Authenticate

This section describes how to authenticate when your applications run on Google Cloud and when they run elsewhere.

#### Run on Google Cloud

When your application runs on Google Cloud, you generally don't need to provide authentication credentials. However, some language client libraries require the project ID even when hosted on Google Cloud.

Verify that your Google Cloud platform has the [Cloud Trace API access scope](https://developers.google.com/identity/protocols/googlescopes#cloudtrace) enabled. For the following configurations, the default access-scope settings include the Cloud Trace API access scope:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs)

**Note:** If you use Autopilot or if you enable Workload Identity Federation for GKE for your GKE cluster, then ensure that you [configure your application to use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to).
  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible)

  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)

  * [Cloud Run](https://docs.cloud.google.com/run/docs)




If you use custom access scopes, then you must ensure that [Cloud Trace API access scope](https://developers.google.com/identity/protocols/googlescopes#cloudtrace) is enabled. For example, if you use the Google Cloud CLI to create a GKE cluster and if you specify the `--scopes` flag, then ensure the scope includes `trace.append`. The following command illustrates setting the `--scopes` flag:
    
    
    gcloud container clusters create example-cluster-name --scopes=https://www.googleapis.com/auth/trace.append

#### Run locally and elsewhere

If your application runs outside Google Cloud, then you must provide authentication credentials to the client library. The [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) must be granted the Cloud Trace Agent role (`roles/cloudtrace.agent`). For information about roles, see [Control access with IAM](https://docs.cloud.google.com/trace/docs/iam).

Google Cloud client libraries use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/production) to find your application's credentials. You can provide these credentials in one of three ways:

  * Run `gcloud auth application-default login`

  * Place the service account key file in a default path for your operating system. The following lists the default paths for Windows and Linux:

    * Windows: `%APPDATA%/gcloud/application_default_credentials.json`

    * Linux: `$HOME/.config/gcloud/application_default_credentials.json`

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path to your service account:

### Linux/macOS
        
        export GOOGLE_APPLICATION_CREDENTIALS=path-to-your-service-accounts-private-key

### Windows
        
        set GOOGLE_APPLICATION_CREDENTIALS=path-to-your-service-accounts-private-key

PowerShell:
        
        $env:GOOGLE_APPLICATION_CREDENTIALS="path-to-your-service-accounts-private-key"




## What's next

  * Instrumentation samples
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)
  * [Quotas and limits](https://docs.cloud.google.com/trace/docs/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
