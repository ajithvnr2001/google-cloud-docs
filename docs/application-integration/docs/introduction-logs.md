---
url: https://docs.cloud.google.com/application-integration/docs/introduction-logs/
title: Introduction to logs \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:31:03.097800+00:00
---

# Introduction to logs  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/introduction-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to logs

This page describes the different types of logs available for Application Integration and when to use them. 

## Overview

Application Integration enables you to generate logs for your integration executions. You can use these logs to troubleshoot execution failures, monitor usage, or set alerts. There are two ways of viewing your logs: 

  * **Integration execution logs.** These logs are generated when integrations are executed. These logs can either be viewed in Application Integration and Cloud Logging. 
  * **Audit logs.** With audit logs you can understand who did what, where, and when within your integration. These logs can be only be viewed in Cloud Logging with no extra charges incurred by the logs. 

With Application Integration, you can leverage Cloud Logging features including setting alerts on these logs and custom retention by storing execution logs in Cloud Logging. 

## Application Integration logs

When you execute an integration, the execution logs are generated for that integration and stored in the region where you created your integration. You can access these logs to troubleshoot errors and view the status of each step in an integration. The following image displays the **Execution Logs** page:

![image showing the Execution Logs page](https://docs.cloud.google.com/static/application-integration/images/execution-logs.png)![iimage showing the Execution Logs page](https://docs.cloud.google.com/static/application-integration/images/execution-logs.png)

For more information about viewing logs in Application Integration, see [Integration execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs).

## Cloud Logging

[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) is a real-time log-management system with storage, search, analysis, and monitoring support. With Application Integration, you can leverage Cloud Logging features. By default, Cloud Logging is disabled for integrations. You can [enable logging for an integration](https://docs.cloud.google.com/application-integration/docs/cloud-logging#before-you-begin) by editing the unpublished version of the integration. 

Cloud Logging captures integration runtime logs for the following levels of severity:

  * **Info:** Logs containing executions logs and other details related to all integration executions: `SUCCEEDED`, `FAILED`, `PROCESSING`, `PENDING`, `SUSPENDED`, and `CANCELLED`.
  * **Error and Warning:** Logs containing executions logs and other details related to the `FAILED` and `CANCELLED` integration execution states.

For a list of integration execution states, see [Execution states](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions#state).




For information about how to view logs in Cloud Logging, see [View integration logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging).

For information about troubleshooting failed execution logs using AI, see [Troubleshoot failed execution logs using AI](https://docs.cloud.google.com/application-integration/docs/troubleshoot-failed-execution-logs).

**Note:** Cloud Logging only supports log entries that are up to 256 KiB in size. If your logs exceed this limit, the request and response parameters are not shown in the logging details. In that case, you can update the integration variables so that the value doesn't exceed the limit. Alternatively, you can [view these logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs).

### Log buckets

Integration execution logs are stored in the `_Default` bucket with the default storage location configured. You can route logs to different destinations:

  * Send logs to different log buckets with different storage locations using inclusion and exclusion filters of Cloud Logging.
  * Export the logs to different destinations like BigQuery or Pub/Sub.



For more information about Cloud Logging routing and storage, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

## Audit logs

For information about audit logs, see [View audit logs](https://docs.cloud.google.com/application-integration/docs/audit-logging). 

## Pricing

Application Integration logs don't have any additional costs but audit logs and Cloud Logging have different pricing models. For information about pricing for Cloud Logging, see [Cloud Logging pricing](https://docs.cloud.google.com/stackdriver/pricing#logging-costs). 

## Limitations

Integration logs are subject to the following limitations:

  * Cloud Logging only supports log entries that are up to 256 KiB in size. If your logs exceed this limit, the request and response parameters are not shown in the logging details. For information about Cloud Logging quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas). To resolve this error, modify the value of the integration variables so that the value doesn't exceed the limit. Alternatively, you can also [view these logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs). This limitation is applicable to [Cloud Logging logs](https://docs.cloud.google.com/application-integration/docs/cloud-logging).
  * If [local logging](https://docs.cloud.google.com/application-integration/docs/local-logging) is disabled, the execution logs are not sent to Cloud Logging even if Cloud Logging is enabled. This limitation is applicable to both [Integration execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) and [Cloud Logging logs](https://docs.cloud.google.com/application-integration/docs/cloud-logging).



## What's next

  * Learn how to [monitor you integrations using Cloud Monitoring](https://docs.cloud.google.com/application-integration/docs/cloud-monitoring)
  * Learn how to [create alerts](https://docs.cloud.google.com/application-integration/docs/alerts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
