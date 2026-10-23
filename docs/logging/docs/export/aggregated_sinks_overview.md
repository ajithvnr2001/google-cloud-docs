---
url: https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview/
title: Aggregated sinks overview \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:26.452169+00:00
---

# Aggregated sinks overview  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Aggregated sinks overview Stay organized with collections  Save and categorize content based on your preferences. 

Aggregated sinks let you collate and route log entries from all resources within a folder or organization to a supported destination. You can use aggregated sinks to store your log data in a central location and control whether child resources store duplicate copies.

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

## About aggregated sinks

An aggregated sink is a folder- or organization-level [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) that routes log entries from both the resource where the sink is defined and all of its child resources. Like a project-level sink, an aggregated sink has a destination and a filter that determines which log entries to route, but a project-level sink routes log entries only from a single project.

### Types of aggregated sinks

You can create two types of aggregated sinks— _intercepting_ and _non-intercepting_ —depending on whether you want child resources to also route the log entries. When aggregated sinks exist in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) of a log entry, the Log Router sends the log entry to those sinks first, and the sink type determines what happens next:

Intercepting aggregated sink
    

An intercepting aggregated sink prevents log entries from being routed to sinks in child resources, except for the `_Required` sinks in the resources where the log entries originate. An intercepting aggregated sink can be useful in preventing duplicate copies of log entries from being stored in multiple places.

For example, suppose that you need to enable [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) for auditing purposes. To simplify your analysis, you want to store these logs in a central location. However, for security and cost reasons, you also want to prevent these logs from being stored at the project level. For this scenario, you can create an intercepting aggregated sink.

Non-intercepting aggregated sink
    

A non-intercepting aggregated sink doesn't affect how log entries are routed to other sinks. That is, even when a log entry matches the filter of a non-intercepting aggregated sink, that log entry is then forwarded to other sinks in the log entry's resource hierarchy. A non-intercepting aggregated sink lets you maintain visibility of log entries in the resources in which they were generated.

For example, you might create a non-intercepting aggregated sink that routes all log entries generated from the folders contained by an organization to a central log bucket. The log entries are stored in the central log bucket. However, because the sink is non-intercepting, the Log Router also sends log entries to the log sinks in the resource in which they were generated.

### Routing examples

This section illustrates how a log entry that originates in a project might flow through the sinks in its resource hierarchy.

#### Example: No aggregated sinks exist

When no aggregated sinks exist in the resource hierarchy of the log entry, the log entry is sent to the log sinks in the project where the log entry originates. A project-level sink routes the log entry to the sink's destination when the log entry matches the sink's inclusion filter but doesn't match any of the sink's exclusion filters. 

#### Example: A non-intercepting aggregated sink exists

Assume that a non-intercepting aggregated sink exists in the resource hierarchy for a log entry. After the Log Router sends the log entry to the non-intercepting aggregated sink, the following occurs:

  1. The non-intercepting aggregated sink routes the log entry to the sink's destination when the log entry matches the inclusion filter but doesn't match any exclusion filter.

  2. The Log Router sends the log entry to the log sinks in the project where the log entry originated.

A project-level sink routes the log entry to the sink's destination when the log entry matches the sink's inclusion filter but doesn't match any of the sink's exclusion filters. 




#### Example: An intercepting aggregated sink exists

Assume that an intercepting aggregated sink exists in the resource hierarchy for a log entry. After the Log Router sends the log entry to the intercepting aggregated sink, one of the following occurs:

  * The log entry matches the inclusion filter but doesn't match any exclusion filter:

    1. The log entry is routed to the destination of the intercepting aggregated sink.
    2. The log entry is sent to the `_Required` sink in the project where the log entry originated.
  * The log entry doesn't match the inclusion filter or it matches at least one exclusion filter:

    1. The log entry isn't routed by the intercepting aggregated sink.
    2. The Log Router sends the log entry to the log sinks in the project where the log entry originated.

A project-level sink routes the log entry to the sink's destination when the log entry matches the sink's inclusion filter but doesn't match any of the sink's exclusion filters. 




## Supported destinations for aggregated sinks

This section lists which destinations are supported for aggregated sinks.

### Intercepting sinks

The destination of an intercepting aggregated sink must be a Google Cloud project.

The log sinks in the destination project reroute the log entries to their destinations. All destinations except projects are supported. For example, the log sinks in the destination project might reroute log entries to a log bucket.

### Non-intercepting sinks

This section describes the supported destinations for non-intercepting aggregated sinks.

**Note:** To use the visualization and analysis tools of Cloud Logging or to use Error Reporting, you must store your log entries in log buckets. These log buckets don't have to be in the same resource where the log entries originate. For example, you might configure an aggregated sink to route log entries to a Google Cloud project, and then configure the sinks in that project to reroute the log entries to local log buckets.

The destination of a sink can be in a different resource from the sink. For example, you can use a log sink to route log entries from one project to a log bucket stored in a different project.

The following destinations are supported:

Google Cloud project
    

Select this destination when you want the log sinks in the destination project to reroute your log entries, or when you have created an intercepting aggregated sink. The log sinks in the destination project can reroute the log entries to any supported destination except a project.

The system-created log sinks in the destination project exclude log entries that are routed to the `_Required` log bucket in the source project. For example, if you route Admin Activity logs to another project, then both the `_Required` and `_Default` log sinks in the destination project exclude those log entries. To store those log entries, in the destination project update the [`_Default` log sink](https://docs.cloud.google.com/logging/docs/routing/overview#default-sink) or create a custom log sink.

**Note:** This is the only type of destination where log entries are rerouted. For example, if you route log entries from one project to a log bucket in another project, then those log entries aren't rerouted by the log sinks in the project that stores the log bucket.

Log bucket
    

Select this destination when you want to store your log data in resources managed by Cloud Logging. Log data stored in log buckets can be viewed and analyzed using services like the Logs Explorer and Observability Analytics.

If you want to join your log data with other business data, then you can store your log data in a log bucket and create a linked BigQuery dataset. A linked BigQuery dataset is read-only, but you can query it like any other BigQuery dataset.

BigQuery dataset
    Select this destination when you want to join your log data with other business data. The dataset you specify must be write-enabled. **Don't set the destination of a sink to be a linked BigQuery dataset**. Linked BigQuery datasets are read-only.

Cloud Storage bucket
    Select this destination when you want long-term storage of your log data. The Cloud Storage bucket can be in the project where the log entries originate, or in a different project. Log entries are stored as JSON files.

Pub/Sub topic
    Select this destination when you want to export your log data from Google Cloud and then use third-party integrations like Splunk or Datadog. Log entries are formatted as JSON and then routed to a Pub/Sub topic.

## Best practices

We recommend that the destination of an aggregated sink be a Google Cloud project. With this destination, the log sinks in the destination Google Cloud project reroute the log entries. The `_Required` sink only routes log entries that match its filter and that originate in the resource where the sink is defined. Therefore, if you want to store additional copies of log entries that match the filter of the `_Required` sink, then you must create a custom log sink or modify the filter of the `_Default` log sink.

When you create an intercepting sink, we recommend that you do the following:

  * Consider whether child resources need independent control of routing their log entries. If a child resource needs independent control of certain log entries, then verify that your intercepting sink doesn't route those log entries.

  * Add contact information to the description of an intercepting sink. This might be helpful if those who manage the intercepting sink are different from those who manage the projects whose log entries are being intercepted.

  * Test your sink configuration by first creating a non-intercepting aggregated sink to verify that the correct log entries are being routed.




## Intercepting aggregated sinks and log-based metrics

Log-based metrics are [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) metrics that are derived from the content of log entries. The way a log entry is routed determines which log-based metrics that log entry can count toward. Because an intercepting aggregated sink affects how log entries are routed, creating this type of sink can result in changes to the values of existing log-based metrics.

For more information, see [How routing log entries affects log-based metrics](https://docs.cloud.google.com/logging/docs/routing/overview#metrics).

## Aggregated sinks and VPC Service Controls

When you use aggregated sinks and VPC Service Controls, the following limitations and configuration requirements apply:

  * **Access to project logs inside a perimeter** : Aggregated sinks can access log data from projects inside a service perimeter. To restrict aggregated sinks from accessing data inside a perimeter, use Identity and Access Management to manage Cloud Logging permissions.

  * **Folder- and organization-level log data** : A VPC Service Controls service perimeter doesn't protect folder- or organization-level log data, including aggregate log data. Although you can [add a folder to a regular service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/folder-membership), doing so protects only the projects within the folder hierarchy, not folder-level resources or logs. You can't add an organization as a protected resource in a service perimeter.

To manage Logging permissions at the folder or organization level, use IAM.

  * **Ingress rules for perimeter-protected destinations** : If you route logs by using a folder- or organization-level sink to a resource that a service perimeter protects, then you must add an ingress rule to the destination service perimeter. The ingress rule must allow access to the resource from the service account (writer identity) that the aggregated sink uses. For more information, see the following pages:

    * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)
    * [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters)
    * [Set destination permissions for aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#dest-auth)
  * **Identity type restrictions in ingress and egress rules** : When a aggregated log sink routes logs to a [Cloud Storage](https://docs.cloud.google.com/storage/docs) resource that is in VPC Service Controls perimeter, the ingress or egress rule can't use `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` as the identity type. Instead, use `ANY_IDENTITY` as the identity type.

You don't need to configure an ingress rule for non-aggregated sinks.




## What's next

  * For information about how to create an aggregated sink, see the following:

    * [Collate and route organization- and folder-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)
    * [Tutorial: Aggregate and store your organization's logs](https://docs.cloud.google.com/logging/docs/central-log-storage)
  * [Route logs to supported destinations: Manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks)

  * [View logs in sink destinations](https://docs.cloud.google.com/logging/docs/export/using_exported_logs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
