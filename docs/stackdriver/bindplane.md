---
url: https://docs.cloud.google.com/stackdriver/bindplane/
title: About Bindplane \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:18.670677+00:00
---

# About Bindplane  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/bindplane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  About Bindplane Stay organized with collections  Save and categorize content based on your preferences. 

[Bindplane](https://bindplane.com/google) is a unified telemetry pipeline built on OpenTelemetry. Bindplane combines standardized telemetry, scalable fleet management, and streamlined controls, simplifying telemetry operations for Google Cloud Observability and Google Security Operations customers.

![Bindplane lets you collect telemetry from a variety of sources and export
that data to Cloud Monitoring and Cloud Logging.](https://docs.cloud.google.com/static/stackdriver/images/bindplane-capabilities.png)

Bindplane enhances Google Cloud's built-in telemetry-collection capabilities, empowering teams to do the following:

  * **Deploy and manage** thousands of OpenTelemetry Collectors with simplified configurations.
  * **Collect** metrics, logs, and traces seamlessly from hybrid cloud and on-premises environments.
  * **Process** telemetry data using powerful OpenTelemetry processors.
  * **Route** data to destinations such as Cloud Monitoring, Cloud Logging, Cloud Trace, and Google Security Operations for deeper insights and analytics.



## Partnership

Bindplane has been a trusted partner since 2018. In 2025, Bindplane and Google [expanded their partnership](https://bindplane.com/blog/bindplane-expands-partnership-with-google-cloud), with a shared commitment to deliver OpenTelemetry-based observability and security solutions for enterprises.

## OpenTelemetry contributions

Bindplane is a leading contributor to the [OpenTelemetry project](https://opentelemetry.io/) and is deeply committed to advancing open-source observability standards. Some of Bindplane's most notable contributions include the following:

  * Donating its open-source, high-performance log agent in 2021, laying the foundation for logging, a key pillar of observability within the OpenTelemetry Collector.
  * Contributing over [30 Receivers](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver) to the OpenTelemetry Collector, spanning critical enterprise observability and security use cases.
  * Contributing significantly to the design and implementation of [Connectors](https://opentelemetry.io/docs/collector/building/connector/) to support advanced routing within the collector.
  * Contributing significantly to the design and implementation of the [Open Agent Management Protocol (OpAMP)](https://opentelemetry.io/docs/specs/opamp), enabling remote management of the OpenTelemetry Collector.



## Bindplane architecture and security

Bindplane is a lightweight web server that uses OpAMP to remotely deploy and manage OpenTelemetry collectors to collect, process, and send telemetry to the Google Cloud APIs for ingestion.

![Bindplane uses collectors to gather and send telemetry from a large number of sources to Google Cloud.](https://docs.cloud.google.com/static/stackdriver/images/bindplane-architecture.png)

  * By default, Bindplane deploys and manages the [Bindplane Distro for OpenTelemetry (BDOT) Collector](https://github.com/observIQ/bindplane-otel-collector) but can also manage custom distributions of the OpenTelemetry Collector.
  * Telemetry data is sent directly to the Google Cloud APIs from the collectors and does not pass through the Bindplane server.
  * Collectors will run independently of Bindplane in the event of an outage or permanent disconnection.
  * Bindplane can be deployed on any premise or cloud, allowing organizations to tailor implementation to organizational security policy.



### Bindplane availability for Google Cloud customers

Bindplane (Google Edition) is free to Google Cloud Observability and Google Security Operations customers. For more information about Bindplane's benefits, features, and use cases, see Bindplane's [Google Integration document](https://bindplane.com/google).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
