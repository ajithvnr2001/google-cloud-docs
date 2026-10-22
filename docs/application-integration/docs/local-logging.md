---
url: https://docs.cloud.google.com/application-integration/docs/local-logging/
title: Local logging \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:56.789592+00:00
---

# Local logging  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/local-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Local logging

This document describes how integration execution logs are saved in Application Integration and how to enable local logging for your integrations.

## Overview

Local logging refers to the integration's data or metadata that is saved during its execution. Application Integration uses the saved data to generate the [integration execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs). 

You can set the **Local logging** to any of the following three modes:

  * **Enable(sync):** The log data is persisted (written) during integration's execution. In this mode, Application Integration writes the log data synchronously after each execution step. This mode guarantees the generation of logs for all the integration executions. 

Use this mode if your priority is to have a guaranteed generation of logs, and a latency in integration execution time is acceptable.

  * **Enable(async):** By default, local logging for an integration is enabled in async mode. The log data is persisted (written) at fixed intervals or after the completion of the integration's execution, whichever is earlier. In this mode, the integration takes a relatively lesser time to execute when compared to `Enable(sync)` mode, because Application Integration writes the log data asynchronously during the integration execution. However, this mode doesn't guarantee the generation of logs for all the executions. In rare cases, it's possible that logs aren't generated for an integration execution. 

Use this mode if your priority is to run your integrations with reduced latency, and the guaranteed generation of logs is relatively of a lesser importance.

  * **Disable:** The execution logs aren't generated for the integration. Disabling the local logging improves the overall integration latency, as log events aren't generated for request and response parameters, and other integration variables.



## Configure local logging

To configure the local logging for your integration, do the following steps:

  1. Open your integration in the [integration editor](https://docs.cloud.google.com/application-integration/docs/integrations-ui-layout).
  2. In the toolbar, click **settings Integration settings**.
  3. From the **Local logging** list, select the local logging mode. By default, **Local logging** is set to **Enable(async)**.
![image showing local logging options](https://docs.cloud.google.com/static/application-integration/images/dbp_options.png)![image showing local logging options](https://docs.cloud.google.com/static/application-integration/images/dbp_options.png)
  4. Click **Done**.

**Tip:** Disabling the local logging improves the overall integration latency, as log events aren't generated for request and response parameters, and other integration variables. 

## Retention period

The retention period for integration execution logs is 90 days. If you want to modify the retention period, you must enable Cloud Logging and configure the retention period for your project. For more information, see [Logging retention](https://docs.cloud.google.com/logging/docs/routing/overview#logs-retention).

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
