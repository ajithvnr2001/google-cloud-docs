---
url: https://docs.cloud.google.com/application-integration/docs/replay-executions/
title: Introduction to replay executions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:31:03.255070+00:00
---

# Introduction to replay executions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/replay-executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to replay executions

**Preview — Replay executions**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

With Application Integration you can replay executions by rerunning the original integration as a new integration execution. Application Integration flows are designed to orchestrate communication and data exchange between different systems. These flows can be complex, involving multiple steps, and often rely on interactions with external third-party systems. As a result, your executions can sometimes fail due to various reasons including the following:

  * **Errors within the flow:** Your integration flow contains incorrect logic such as faulty data transformations or misconfigured steps.
  * **Issues with external systems:** Problems or downtime with third-party systems–such as databases, web services, or APIs–that the integration flow interacts with.
  * **Transient network errors:** Temporary glitches in connectivity between systems involved in the integration.



After debugging failures in your published integrations, you can [replay your integration executions](https://docs.cloud.google.com/application-integration/docs/replay-executions-logs). Replaying an execution regenerates the flow and reprocesses the original integration as a new integration execution.

**Note:** Replaying an execution is only available for published integrations. You cannot replay an execution for unpublished integrations.

## Benefits

Replaying an execution can be useful for the following scenarios:

  * **Trigger event handling:** When you want to rerun a failed execution, especially one triggered by an external system, replay allows you to configure the input variables that would have been provided by that event. For example, suppose that you have an integration with a Pub/Sub trigger that is triggered on receiving an event from an external application such as Jira. When you replay the execution, the trigger event from Pub/Sub is executed as it might be difficult to trigger the same event from Jira.
  * **Retrying failed executions:** If your integration fails due to transient errors or issues with external systems, you can replay the execution to re-run the flow and complete the integration.
  * **Validating published integrations with modified input values:** Replay allows you to test published integrations by re-running them with different input variable values. This saves time by avoiding the need to manually rerun the entire integration. Both masked and unmasked variables can be modified during replay.
  * **Replaying executions from point of failure:** Replay allows you to rerun executions from the point of failure in a published integration. This avoids unnecessary re-execution of successful tasks, saving debugging time and resources.



To learn more about how to replay executions, see [Replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions-logs).

## Considerations

The following considerations apply to replay executions:

  * **Execution states:** You can replay executions that have the following states: **Succeeded** , **Failed** , and **Cancelled**. To replay executions that are in other states, you must [cancel the executions](https://docs.cloud.google.com/application-integration/docs/cancel-executions). **Note:** You can't cancel an integration execution if the integration is in the **In process** state.
  * **Compatible published versions:** When you replay an execution after making changes to the published integration version, ensure that those changes are compatible with the original execution. For example, if the original execution required two input variables and the updated integration version requires only one inpute variable, then the replay execution fails.
  * **Execution mode:** Replay executions follow the same [execution mode](https://docs.cloud.google.com/application-integration/docs/triggers#execution-modes) as the original execution even if there is a change in the integration version.



## Limitations

Replaying an execution is subject to the following limitations:

  * Replaying an execution that is triggered by a [Schedule trigger](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger) isn't supported.
  * By default, replayed executions have a deadline time of 10 minutes. If the execution does not complete within the deadline, the execution status is set to `CANCELLED`.



## What's next

  * Learn about [logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/introduction-logs).
  * Learn how to [test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
