---
url: https://docs.cloud.google.com/logging/docs/log-entry-data-model/
title: Log entry data model \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:40.670403+00:00
---

# Log entry data model  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/log-entry-data-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Log entry data model Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the data model used by Cloud Logging. The data model specifies the format in which your log data is stored. It also determines the dimensions over which you can query your log data.

## Data model

In Cloud Logging, a _log_ is a named collection of individual entries. You can query your data by the name of the log. Logs are composed of entries that conform to the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) structure.

Each log entry records status or describes a specific event, such as the creation of a virtual machine instance, and minimally consists of the following:

  * A timestamp that indicates either when the event took place or when it was received by Cloud Logging.
  * Information about the source of the log entry. This source is called the _monitored resource_. Examples of monitored resources include individual Compute Engine instances and Google Kubernetes Engine containers. For a complete listing of monitored resource types, see [Monitored resources and services](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).
  * A payload which must be one of the following:

    * `textPayload`: These payloads are formatted as a single string.
    * `jsonPayload`: These payloads are [structured](https://docs.cloud.google.com/logging/docs/structured-logging), so you can query by key-value pairs. We recommend that applications always write structured log data.
    * `protoPayload`: These payloads follow the format of a proto file and the fields are formatted as JSON.
  * The name of the log to which it belongs. The name of a log includes the full path of the resource to which the log entries belong, followed by an identifier. The following are examples of log names:

    * `projects/my-project/logs/stdout`
    * `projects/my-project/compute.googleapis.com/activity`



You can write queries that retrieve only those log entries where the value of a `LogEntry` field matches some criteria. For example, you can display only those log entries whose `severity` field has the value of `ERROR`.

## Log entry types

[Audit logs](https://docs.cloud.google.com/logging/docs/audit) and [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) provide information necessary to satisfy compliance regulations. Audit logs provide information about administrative activities and accesses within your Google Cloud resources. Access Transparency logs record actions taken by Google Cloud staff when accessing your Google Cloud content. For a list of supported services, see [Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services) and [Google Cloud services with Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services).

The following type of log entries are stored in the [`_Required` log bucket](https://docs.cloud.google.com/logging/docs/store-log-entries#required-bucket) in the Google Cloud project, billing account, folder, or organization in which they originate:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * Google Workspace Admin Audit logs
  * Enterprise Groups Audit logs
  * Login Audit logs


  * Access Transparency logs



All other log entries that originate in a Google Cloud project, billing account, folder, or organization are stored in the [`_Default` log bucket](https://docs.cloud.google.com/logging/docs/store-log-entries#default-bucket). However, you can change which log entries are stored in this log bucket.

## What's next

  * [Store log data](https://docs.cloud.google.com/logging/docs/store-log-entries).
  * [Route log data](https://docs.cloud.google.com/logging/docs/routing/overview).
  * [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
