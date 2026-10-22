---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel/
title: Overview of the Google-Built OpenTelemetry Collector \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:43.995478+00:00
---

# Overview of the Google-Built OpenTelemetry Collector  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Overview of the Google-Built OpenTelemetry Collector Stay organized with collections  Save and categorize content based on your preferences. 

The [Google-Built OpenTelemetry Collector](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/tree/v0.163.0/google-built-opentelemetry-collector) is Google's open-source build of the [OpenTelemetry Collector](https://opentelemetry.io), built from upstream components using a secure supply chain on Google infrastructure. OpenTelemetry, which is part of the [Cloud Native Computing Foundation](https://www.cncf.io), provides open source APIs, libraries, and SDKs to collect distributed [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) traces, metrics, and logs for application monitoring.

The Google-Built OpenTelemetry Collector lets you send correlated OTLP traces, metrics, and logs to [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) and other backends from applications instrumented by using [OpenTelemetry SDKs](https://opentelemetry.io/docs/concepts/instrumentation). The Collector also captures metadata for Google Cloud resources, so you can correlate application performance data with infrastructure telemetry data. Using the Google-built Collector with Google Cloud Observability provides insights to improve the performance of your applications and infrastructure. For more information about the Collector, see Description of the Google-Built OpenTelemetry Collector.

Starting with version 0.134.0, the Google-Built OpenTelemetry Collector is built to the [Supply-chain Levels for Software Artifacts (SLSA) level 3](https://slsa.dev/spec/v1.1/levels#build-l3-hardened-builds) standard. The collector code and its dependencies are continually scanned for vulnerabilities. For more information, see Security features.

## Use the Google-Built OpenTelemetry Collector

You can use the Google-built Collector to collect telemetry data from your applications running on Kubernetes (including Google Kubernetes Engine (GKE)), Container-Optimized OS, standalone containers, or directly in a host environment (including Compute Engine). The following documents describe how to configure and deploy the Google-built Collector in the following environments:

  * [GKE](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke)
  * [Compute Engine](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gce)
  * [Container-Optimized OS](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-cos)
  * [Cloud Run](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-cloud-run)

**Note:** To collect Prometheus metrics from Cloud Run containers, use the [Prometheus sidecar for Cloud Run](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar).



These instructions can also be used to configure the open-source upstream [OpenTelemetry Collector](https://opentelemetry.io) to export data to Google Cloud Observability.

If you don't have an application ready to use the Collector, then you can deploy the OpenTelemetry demo with the Google-built Collector. For more information, see Try the OpenTelemetry demo.

For information about using OpenTelemetry instrumentation to generate traces, metrics, and logs from your applications, see the following documents:

  * [Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers)
  * [Choose an instrumentation approach for your application](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Generate traces and metrics with OpenTelemetry instrumentation](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach#samples)



## Description of the Google-Built OpenTelemetry Collector

The Google-Built OpenTelemetry Collector is built by using upstream OpenTelemetry components and tooling, while being built and retrieved entirely from Google build-test-release infrastructure (Artifact Registry). The Google-built Collector is compatible with an OpenTelemetry Collector build from the upstream repository. It is also hosted as a Docker image for flexible deployment on any container-based system, including Kubernetes and GKE.

The Google-built Collector provides a Google-curated package with the components most users will need for a rich observability experience on Google Cloud. You don't need to select components and manually build your own Collector. By using the Google-built Collector, you can:

  * Collect metadata for Google Cloud resources so you can correlate application performance data with infrastructure telemetry data.
  * Route telemetry data to Google Cloud Observability or the backend of your choice by using exporters, including [backends that natively support OpenTelemetry](https://opentelemetry.io/ecosystem/vendors).
  * Simplify onboarding with recommended configurations and best practice self-monitoring, including health checks and batch processing.
  * Use the hosted Docker image for flexible deployment on any container-based system, including Kubernetes and GKE.



## Best practices

OpenTelemetry maintains a list of best practices for [configuring the OpenTelemetry Collector](https://opentelemetry.io/docs/security/config-best-practices) and for [scaling the Collector](https://opentelemetry.io/docs/collector/scaling). This section makes some additional recommendations.

### Use the OTLP gRPC exporter

Use the [OTLP gRPC](https://github.com/open-telemetry/opentelemetry-collector/blob/main/exporter/otlpexporter/) exporter to connect to the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), `telemetry.googleapis.com`. The Telemetry API accepts all telemetry—logs, metrics, and traces—in the vendor-neutral OTLP format. Sending telemetry to the Telemetry API means that the data flowing from the OpenTelemetry Collector is preserved at maximum fidelity in Google Cloud storage. 

### Use the health-check extension

The health-check extension enables an HTTP URL that can be probed to check the status of the OpenTelemetry Collector. Using this extension provides the following benefits:

  * **Early problem detection** : Health checks facilitate proactive monitoring of the Collector's status, enabling the detection of potential issues before these issues negatively impact telemetry data. This preventative measure helps ensure the reliability of the observability pipeline.
  * **Improved troubleshooting** : When problems occur, health checks offer valuable insights into the Collector's current state. This information simplifies the diagnosis and resolution process, reducing downtime and streamlining troubleshooting efforts.
  * **Enhanced reliability** : Continuous monitoring of the Collector's health ensures consistent operation and prevents unexpected failures. This proactive measure enhances the overall reliability of the observability system and minimizes the risk of data loss or gaps in telemetry data.



On Kubernetes and GKE, the health-check extension is compatible with Kubernetes liveness and readiness probes. For information about setting up these probes, see [Kubernetes best practices: Setting up health checks with readiness and liveness probes](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes).

On Cloud Run, a single health-check extension can serve as the endpoint for both startup and liveness probes in your Cloud Run service configuration.

### Use the batch processor

The [batch processor](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/batchprocessor/README.md) collects traces, metrics, or logs and bundles them into batches for transmission. Using the batch processor provides the following benefits:

  * **Minimizes outgoing connections** : By grouping data transmissions into batches, the OpenTelemetry Collector significantly reduces the number of outgoing connections. This consolidated approach lowers quota usage and has the potential to lower overall network costs.
  * **Improved data compression** : Batching enables more efficient data compression, reducing the overall size of the data transmitted.
  * **Flexibility in batching strategy** : Support for both size-based and time-based batching provides flexibility to optimize for different scenarios. Size-based batching ensures that batches reach a certain size before being sent, while time-based batching sends batches after a specific time interval has elapsed. This flexibility lets you fine-tune the batching strategy to align with the specific characteristics of your data and the particular requirements of your application.



### Use the `googlesecretmanager` provider

The [`googlesecretmanager` provider](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/confmap/provider/googlesecretmanagerprovider) lets you store sensitive information needed by configuration files in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), a service designed specifically for securely storing, accessing, and managing sensitive data. Using the `googlesecretmanager` provider offers the following benefits:

  * **Enhanced security** : Your configuration files don't contain sensitive information like passwords.
  * **Reduced risk of exposure** : Secret Manager fetches secrets during initialization of the Collector, which prevents plaintext secrets from accidentally being recorded in logs.



For information about using this provider, see [Manage secrets in Collector configuration](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-use-secretmgr).

## Release notes

The Google-Built OpenTelemetry Collector is versioned in sync with the upstream OpenTelemetry Collector. The current version is **v0.163.0** ; the corresponding Docker image, stored in Artifact Registry, is **us-docker.pkg.dev/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector/otelcol-google:0.163.0**. For each new version, the changes that are most relevant to Google Cloud users are included on this page.

  * 0.163.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.163.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.163.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.163.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.163.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.163.0)
  * 0.162.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.162.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.162.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.162.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.162.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.162.0)
  * 0.160.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.160.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.160.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.160.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.160.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.160.0)
  * 0.159.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.159.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.159.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.159.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.159.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.159.0)
  * 0.156.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.156.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.156.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.156.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.156.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.156.0)
  * 0.155.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.155.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.155.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.155.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.155.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.155.0)
  * 0.154.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.154.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.154.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.154.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.154.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.154.0)
  * 0.151.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.151.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.151.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.151.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.151.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.151.0)
  * 0.150.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.150.0.
    * Built with Go version 1.26.2.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.150.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.150.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.150.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.150.0)
  * 0.148.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.148.0.
    * The [`google.golang.org/grpc`](https://pkg.go.dev/google.golang.org/grpc) package is updated to v1.79.3 to resolve [CVE-2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186).
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.148.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.148.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.148.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.148.0)
  * 0.147.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.147.0.
    * Built with Go version 1.26.1 to resolve [CVE-2025-68121](https://nvd.nist.gov/vuln/detail/cve-2025-68121).
    * Known Issue: The gRPC-based `otlp` exporter now configures `round_robin` client-side load balancing strategy by default. When using the `otlp` exporter to send data to the Telemetry API, certain environments may experience excessive logs with `connect: network is unreachable` errors if IPV6 isn't functioning properly. For more information, see [network unreachable" errors](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-troubleshooting#network-is-unreachable-errors).
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.145.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.145.0)
      * [Release notes (v0.146.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.146.0)
      * [Release notes (v0.147.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.147.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.145.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.145.0)
      * [Release notes (v0.146.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.146.0)
      * [Release notes (v0.147.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.147.0)
  * 0.144.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.144.0.
    * Compute Engine packages for Google-Built OpenTelemetry Collector are now available. See [the Compute Engine instructions page](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gce) for more information. 
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.144.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.144.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.144.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.144.0)
  * 0.143.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.143.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.142.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.142.0)
      * [Release notes (v0.143.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.143.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.142.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.142.0)
      * [Release notes (v0.143.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.143.0)
  * 0.141.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.141.0.
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.139.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.139.0)
      * [Release notes (v0.140.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.140.0)
      * [Release notes (v0.141.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.141.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.139.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.139.0)
      * Upstream release of OpenTelemetry Collector Contrib v0.140.0 was skipped because of a [CI failure](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44346#issue-3638031767)
      * [Release notes (v0.140.1)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.140.1)
      * [Release notes (v0.141.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.141.0)
  * 0.138.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.138.0.
    * Added 1 component: 
      * [signalmetricsconnector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.138.0/connector/signaltometricsconnector)
    * OpenTelemetry Collector Core repository: 
      * [Release notes](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.138.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.138.0)
  * 0.137.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.137.0.
    * Added 3 components: 
      * [prometheusremotewriteexporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.137.0/exporter/prometheusremotewriteexporter)
      * [googlecloudpubsubreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.137.0/receiver/googlecloudpubsubreceiver)
      * [googlecloudpubsubexporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.137.0/exporter/googlecloudpubsubexporter)
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.136.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.136.0)
      * [Release notes (v0.137.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.137.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.136.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.136.0)
      * [Release notes (v0.137.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.137.0)
  * 0.135.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.135.0.
    * Added 2 components: 
      * [prometheusexporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.135.0/exporter/prometheusexporter)
      * [prometheusremotewritereceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.135.0/receiver/prometheusremotewritereceiver)
    * Google-Built OpenTelemetry Collector now links to BoringCrypto for FIPS 140-2 compliance.
    * Fixed a known issue that would cause config files mounted in the container at the `/etc/otelcol-google` directory to have permission errors.
    * OpenTelemetry Collector Core repository: [Release notes (v0.135.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.135.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.135.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.135.0)
  * 0.134.0:

    * Google-Built OpenTelemetry Collector: 
      * Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.134.0.
    * Beginning of support for new security features. 
    * The opencensus receiver has been removed from both upstream and Google-Built OpenTelemetry Collector.
    * OpenTelemetry Collector Core repository: [Release notes (v0.134.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.134.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.134.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.134.0)
  * 0.131.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.131.0.
    * OpenTelemetry Collector Core repository: [Release notes (v0.131.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.131.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.131.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.131.0)
  * 0.130.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.130.0.
    * The known issue in the Prometheus Receiver in the previous version is now fixed.
    * The [healthcheckv2extension](https://github.com/open-telemetry/opentelemetry-collector/tree/main/extension/healthcheckv2extension) component has been added.
    * OpenTelemetry Collector Core repository: [Release notes (v0.130.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.130.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.130.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.130.0)
  * 0.129.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.129.0.
    * Known Issue Advisories: 
      * [Prometheus Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/prometheusreceiver): Basic authentication for URLs stopped working ([issue link](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/40520)); 
        * This issue affects version 0.127.0, 0.128.0 and 0.129.0.
        * To mitigate, use version 0.126.0 or lower.
    * OpenTelemetry Collector Core repository: [Release notes (v0.129.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.129.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.129.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.129.0)
  * 0.128.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.128.0.
    * OpenTelemetry Collector Core repository: [Release notes (v0.127.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.128.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.127.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.128.0)
  * 0.127.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.127.0.
    * OpenTelemetry Collector Core repository: [Release notes (v0.127.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.127.0)
    * OpenTelemetry Collector Contrib repository: [Release notes (v0.127.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.127.0)
  * 0.126.0:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core and OpenTelemetry Collector Contrib version v0.126.0.
    * Added new components: 
      * Processors: `metricstarttime`
      * Providers: `googlesecretmanager`. For information about using this provider to eliminate plaintext secrets in your Collector configuration, see [Manage secrets in Collector configuration](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-use-secretmgr).
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.125.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.125.0)
      * [Release notes (v0.126.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.126.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.125.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.125.0)
      * [Release notes (v0.126.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.126.0)
  * 0.124.1:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core version v0.124.0, and OpenTelemetry Collector Contrib v0.124.1.
    * Added new components: 
      * Receivers: `dockerstats`, `jmx`, `redis`, `statsd`, `syslog`
      * Processors: `metricsgeneration`
    * OpenTelemetry Collector Core repository: 
      * [Release notes (v0.123.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.123.0)
      * [Release notes (v0.124.0)](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.124.0)
    * OpenTelemetry Collector Contrib repository: 
      * [Release notes (v0.123.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.123.0)
      * [Release notes (v0.124.0)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.124.0)
      * [Release notes (v0.124.1)](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.124.1)
  * 0.122.1:

    * Google-Built OpenTelemetry Collector: Update to OpenTelemetry Collector Core version v0.122.1, and OpenTelemetry Collector Contrib v0.122.0.
    * Added new component: [`googleclientauthextension`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.122.0/extension/googleclientauthextension)
    * Known Issue Advisories: 
      * If you use OTLP export of collector self-telemetry, then note the following OpenTelemetry Collector issue: <https://github.com/open-telemetry/opentelemetry-collector/issues/12701>
    * OpenTelemetry Collector Core repository: [Release notes](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.122.1)
    * OpenTelemetry Collector Contrib repository: [Release notes](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.122.0)
  * 0.121.0: 

    * Google-Built OpenTelemetry Collector: Initial release
    * OpenTelemetry Collector Core repository: [Release notes](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.121.0)
    * OpenTelemetry Collector Contrib repository: [Release notes](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.121.0)



## Security features

Starting with version 0.134.0, the Google-Built OpenTelemetry Collector offers Docker images that are built to the [Supply-chain Levels for Software Artifacts (SLSA) level 3](https://slsa.dev/spec/v1.1/levels#build-l3-hardened-builds) standard and offer the following security features:

  * Secure build: The CI/CD pipeline for the Google-Built OpenTelemetry Collector generates [attestations](https://slsa.dev/spec/v1.1/attestation-model) for each container-image release. These attestations include a [verification summary attestation (VSA)](https://slsa.dev/spec/v1.1/verification_summary), which is attached as an asset to each release on [GitHub](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/releases).

  * Vulnerability scanning and patching: The Google-Built OpenTelemetry Collector is continually scanned for vulnerabilities, and we strive to follow [FedRamp SLOs](https://www.fedramp.gov/resources/documents/CSP_Continuous_Monitoring_Strategy_Guide.pdf) for vulnerability remediation. We prioritize user security by regularly rebuilding the Collector with updated package dependencies. Our CI/CD pipeline is engineered to quickly integrate critical security fixes and dependency updates. This commitment minimizes exposure to known vulnerabilities, providing you with a continuously secure and up-to-date product.

  * Verified and secure releases: We enforce Google-internal code-integrity policies to ensure that only artifacts meeting our strict security criteria are released to production. This process means you always receive software that has successfully passed extensive internal security checks.




## Supportability

For all Google-Built OpenTelemetry Collector client-side issues, including feature requests, bug reports, and general questions, open an issue in the appropriate GitHub repository. These repositories are monitored by Google, and issues are triaged and addressed on a best-effort basis.

  * [Google-Built OpenTelemetry Collector packaging repository](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector/issues), for issues related to the following:

    * Packaging
    * Deployment on Google Cloud
    * Authentication within Google Cloud
    * Requests for the addition of new OpenTelemetry components
  * [OpenTelemetry Collector Contrib repository](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues), for issues related to the following:

    * Google-specific OpenTelemetry components, for example: 
      * `googlecloudexporter`
      * `googlemanagedprometheusexporter`
      * `googleclientauthextension`
      * `resourcedetectionprocessor`
    * Non-Google-specific OpenTelemetry components managed by the upstream community
**Note:** When opening an issue in the Contrib repository, fill out the issue template accurately so that your issue can be routed to the correct owner.



For issues related to the Google-Built OpenTelemetry Collector's use of Google Cloud Observability services and APIs, like server errors or quotas, contact [Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support).

## Pricing

There is no charge for deploying and using the Google-Built OpenTelemetry Collector.

When you send telemetry data to Google Cloud, you are billed by ingestion volume. For information about costs associated with the ingestion of traces, logs, and Google Cloud Managed Service for Prometheus metrics, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

## Try the OpenTelemetry demo

This section describes how to deploy and run the [OpenTelemetry demo for Google Cloud](https://github.com/GoogleCloudPlatform/opentelemetry-demo) with the Google-Built OpenTelemetry Collector.

This section is optional. If you are ready to integrate the Google-built Collector into your own deployments, see the following documents:

  * Deploy the Collector on [Google Kubernetes Engine](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke)
  * Deploy the Collector on [Container-Optimized OS](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-cos)
  * Deploy the Collector on [Cloud Run](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-cloud-run)



### Before you begin

The OpenTelemetry demo requires a Kubernetes cluster that has Workload Identity Federation configured. For information about setting up Workload Identity Federation for your cluster, see [Use Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

### Update the demo to use the Google-built Collector

By default, the OpenTelemetry demo uses the upstream OpenTelemetry Collector. To use the Google-Built OpenTelemetry Collector instead, do the following:

  1. Clone the OpenTelemetry demo repository:
         
         git clone https://github.com/GoogleCloudPlatform/opentelemetry-demo.git
         

  2. Go to the `kubernetes` directory.
         
         cd kubernetes
         

  3. Edit the file `opentelemetry-demo.yaml` to replace the line for the Collector image to use. The line looks like the following, although the version might be different:
         
         image: "otel/opentelemetry-collector-contrib:0.108.0"
         

Replace the value of the `image:` field with `us-docker.pkg.dev/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector/otelcol-google:0.163.0`, so that the line looks like the following, and then save the file:
         
         image: "us-docker.pkg.dev/cloud-ops-agents-artifacts/google-cloud-opentelemetry-collector/otelcol-google:0.163.0"
         




### Deploy the demo

Deploy the demo by applying the updated `opentelemetry-demo.yaml` file:
    
    
    kubectl apply --namespace otel-demo -f opentelemetry-demo.yaml
    

### Connect to the demo

After you have applied the updated configuration, you can forward the data to a local port. For example, to connect to the demo at `localhost:8080`, issue the following command:
    
    
    kubectl port-forward --n otel-demo svc/opentelemetry-demo-frontendproxy 8080:8080
    

You can then use your browser to connect to the demo at `localhost:8080`.

### View telemetry

The OpenTelemetry demo sends metrics, traces, and logs to Google Cloud by using the Google-Built OpenTelemetry Collector. For information about the specific telemetry sent by the demo, see [Seeing telemetry](https://github.com/GoogleCloudPlatform/opentelemetry-demo/#seeing-telemetry) in the documentation for the demo.

#### View your metrics

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




#### View your traces

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

#### View your logs

From the Logs Explorer, you can inspect your logs, and you can also view associated traces, when they exist.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate a log entry from your instrumented app. To view the details, expand the log entry.

  3. Click ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Traces** on a log entry with a trace message, and then select **View trace details**.

A **Trace details** panel opens and displays the selected trace.




For more information about using the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
