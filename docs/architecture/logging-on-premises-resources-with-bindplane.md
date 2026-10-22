---
url: https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane/
title: Log on-premises resources with BindPlane \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:37.220745+00:00
---

# Log on-premises resources with BindPlane  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Log on-premises resources with BindPlane Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-02 UTC

This document is one part of a two-part series on extending [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to include on-premises infrastructure and apps.

  * Log on-premises resources with BindPlane (this document): Read about how Logging supports logging from on-premises resources.
  * [Monitor on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane): Read about how Monitoring supports monitoring of on-premises resources.



You might consider using Logging and Monitoring for logging and monitoring of your on-premises resources for the following reasons:

  * You want a temporary solution while you move infrastructure to Google Cloud and you want to log and monitor your on-premises resources until they're decommissioned.
  * You might have a diverse computing environment with multiple clouds and on-premises resources.



In either case, with the Logging and Monitoring APIs and [BindPlane](https://observiq.com/solutions), you can gain visibility into your on-premises resources. This document is intended for DevOps practitioners, managers, and executives who are interested in a logging strategy for resources in Google Cloud and their remaining on-premises infrastructure and apps.

## Ingesting logs with Logging

You can get logs into Logging by using the API in two supported ways:

  * Use BindPlane from observIQ to ingest logs from your on-premises or other cloud sources.
  * Use the Cloud Logging API directly from your app or by using a custom agent.



### Using BindPlane to ingest Logging logs

The following diagram shows the architecture of how BindPlane ingests logs and then how those logs are ingested into Logging.

![Architecture of using Logging and BindPlane to ingest on-premises logs.](https://docs.cloud.google.com/static/architecture/images/logging-on-premises-resources-with-stackdriver-and-blue-medora-1-logging-architecture-bindplane.png)

BindPlane enables users to remotely deploy and manage agents on the hosts they want to gather logs from. For more information, read about [the architecture of BindPlane](https://observiq.com/docs/going-to-production/bindplane/architecture/architecture). This option requires the least amount of effort to deploy because it requires configuration to set up rather than development.

Advantages:

  * Requires configuration, not development.
  * Included in the cost of using [Logging](https://cloud.google.com/stackdriver/pricing).
  * Is a supported configuration by Logging product and support.
  * Can extend to logs not provided by the default configuration.



Disadvantages:

  * Requires the use of a third-party tool.
  * Might need to provide a custom configuration if the log source isn't provided by default. The provided list of logs is available in [Sources](https://observiq.com/docs/resources/sources).



### Using the Logging API directly

The following diagram shows the architecture of how logs are collected by instrumentation and ingested into Logging.

![Architecture of using the Logging API to ingest on-premises logs directly.](https://docs.cloud.google.com/static/architecture/images/logging-on-premises-resources-with-stackdriver-and-blue-medora-2-logging-directly.png)

Using the APIs directly means that you need to instrument your applications to send logs directly to the API or develop a custom agent to send logs to the API. This is the option that requires the highest level of effort because it requires development effort.

Advantages:

  * Provides flexibility because you can implement the instrumentation with client logging libraries.



Disadvantages:

  * Requires separate solution for infrastructure logs, such as a custom agent.
  * Requires code instrumentation, which might mean higher cost to implement.
  * Requires the use of batching and other scalable ingestion techniques for proper ingestion performance.
  * Support is provided for the Logging API only, not custom-developed code.



## Using BindPlane

This document covers using BindPlane from observIQ to ingest logs into Logging. Because it's included in the cost of Logging, BindPlane doesn't require development and provides a product-supported solution.

### Agents, sources, and destinations

For detailed information about agents, sources, and destinations, see the BindPlane [Quickstart Guide](https://docs.bindplane.observiq.com/docs/getting-started).

### Example use case

Enterprise customers use BindPlane to ingest logs in the following on-premises logging scenarios:

  1. Custom parsing and filtering of log data from custom application logs.
  2. Collection of operating-system events from Linux or Windows virtual machines.
  3. Ingestion of syslog streams from network or other compatible devices.
  4. Collection of Kubernetes system and application logs.



### Send logs from on-premises to Logging

After you set up BindPlane and start sending logs, those logs are sent to Logging. To view, process, and export logs, go to the [Google Cloud console](https://console.cloud.google.com/logs/query). The logs are listed as `generic_node` or `generic_task`resource types. For more information about the labels included in each resource type, see the [Logging resource list](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

Cloud Logging supports non-Cloud Logging logs through the use of two resource types:

  * **Generic Node** : Identifies a machine or other computational resource for which no other resource type is applicable. The label values must uniquely identify the node.
  * **Generic Task** : Identifies an app process for which no other resource is applicable, such as a process scheduled by a custom orchestration system. The label values must uniquely identify the task.



### View logs in Logging

On the [Logs Explorer page](https://console.cloud.google.com/logs/query), the **All resources** list includes **Generic Node** as a resource type.

The list of logs that appear on the page were captured as the `generic_node` resource type. Expand a row to see log entry details.

The log entries use a [structured logging](https://docs.cloud.google.com/logging/docs/structured-logging) format, which provides a richer format for searching the logs because the log payload is stored as a `jsonPayload`. The structured logging format makes logs more accessible because you can use the fields in the payload as a part of the search. The BindPlane agent provides a mapping from the original log entry to the structured log entry in Logging.

## Conclusion

With logs available in Logging, you can take advantage of the full use of the Logging features. Logs appear in the Google Cloud console. You can export logs with Logging exports and use them to create metrics and alerts in Monitoring by using [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

## What's next

  * [Logging and Monitoring](https://docs.cloud.google.com/stackdriver)
  * [BindPlane set-up instructions for Cloud Monitoring and Logging](https://observiq.com/docs/resources/destinations/google-cloud)
  * [Set up logs-based metrics in Logging](https://docs.cloud.google.com/logging/docs/logs-based-metrics)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-02 UTC."],[],[]] 
