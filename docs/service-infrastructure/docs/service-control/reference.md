---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/
title: Overview \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:21:01.379570+00:00
---

# Overview  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Service Control provides control plane functionality to managed services, such as logging, monitoring, and status checks. This page provides an overview of what it does and how it works.

### Why use Service Control?

When you develop a cloud service, you typically start with the business requirements and the architecture design, then proceed with API definition and implementation. Before you put your service into production, you need to deal with many control plane issues:

  * How to control access to your service.
  * How to send logging and monitoring data to both consumers and producers.
  * How to create and manage dashboards to visualize this data.
  * How to automatically scale the control plane components with your service.



Service Control is a mature and feature-rich control plane provider that addresses these needs with high efficiency, high scalability, and high availability. It provides a simple public API that can be accessed from anywhere using JSON REST and gRPC clients, so when you move your service from on-premise to a cloud provider, or from one cloud provider to another, you don't need to change the control plane provider.

Services built using Google Cloud Endpoints already take advantage of Service Control. Cloud Endpoints sends logging and monitoring data through Google Service Control for every request arriving at its proxy. If you need to report any additional logging and monitoring data for your Cloud Endpoints service, you can call the Service Control API directly from your service.

The Service Control API definition is open sourced and available on [GitHub](https://github.com/googleapis/googleapis/tree/master/google/api/servicecontrol). By changing the DNS name, you can easily use alternative implementations of the Service Control API.

### Architecture

Google Service Control works with a set of _managed services_ and their _operations_ (activities), _checks_ whether an operation is allowed to proceed, and _reports_ completed operations. Behind the scenes, it leverages other Google Cloud services, such as [Google Service Management](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started), [Stackdriver Logging](https://docs.cloud.google.com/logging), and [Stackdriver Monitoring](https://docs.cloud.google.com/monitoring), while hiding their complexity from service producers. It enables service producers to send telemetry data to their consumers. It uses caching, batching, aggregation, and retries to deliver higher performance and availability than the individual backend systems it encapsulates.

![The overall architecture of a service that uses Google Service Control.](https://docs.cloud.google.com/static/service-infrastructure/docs/service-control/images/arch.svg)

**Figure 1** : Using Google Service Control.

The Service Control API provides two methods:

  * [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check), used for: 
    * Ensuring valid consumer status
    * Validating API keys
  * [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report), used for: 
    * Sending logs to Stackdriver Logging
    * Sending metrics to Stackdriver Monitoring



We'll look at these in more detail in the rest of this overview.

### Managed services

A [managed service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services) is a network service managed by [Google Service Management](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started). Each managed service has a unique name, such as `example.googleapis.com`, which must be a valid fully-qualified DNS name, as per RFC 1035.

For example:

  * Google Cloud Pub/Sub (`pubsub.googleapis.com`)
  * Google Cloud Vision (`vision.googleapis.com`)
  * Google Cloud Bigtable (`bigtable.googleapis.com`)
  * Google Cloud Datastore (`datastore.googleapis.com`)



Google Service Management manages the lifecycle of each service's configuration, which is used to customize Google Service Control's behavior. Service configurations are also used by Google Cloud Console for displaying APIs and their settings, enabling/disabling APIs, and more.

### Operations

Google Service Control uses the generic concept of an _operation_ to represent the activities of a managed service, such as API calls and resource usage. Each operation is associated with a managed service and a specific service consumer, and has a set of properties that describe the operation, such as the API method name and resource usage amount. For more information, see the [Operation definition](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation).

### Check

The [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) method determines whether an operation should be allowed to proceed for a managed service.

For example:

  * Check if the consumer is still active.
  * Check if the consumer has enabled the service.
  * Check if the API key is still valid.



By performing multiple checks within a single method call, it provides better performance, higher reliability, and reduced development cost to service producers compared to checking with multiple backend systems.

### Report

The [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) method reports completed operations for a managed service to backend systems, such as logging and monitoring. The reported data can be seen in Google API Console and Google Cloud Console, and retrieved with appropriate APIs, such as the Stackdriver Logging and Stackdriver Monitoring APIs.

### Next steps

  * Read our [Getting Started guide](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started) to find out how to set up and use the Google Service Control API.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
