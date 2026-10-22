---
url: https://docs.cloud.google.com/application-integration/docs/replay-executions-logs/
title: Replay executions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:07.420435+00:00
---

# Replay executions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/replay-executions-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Replay executions

Replaying published integration execution lets you rerun an integration using the same parameters as the previous execution, using different parameters, or from a specific point of failure. For example, you can replay an execution if an integration failed due to a timeout error or if the output of an integration is not as expected. For more information about the benefits of replaying executions, see [Introduction to replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions).

The following sections describe how to replay executions from the Application Integration **Execution Logs** page.

## Required roles

To get the permissions that you need to replay executions, ask your administrator to grant you the [Application Integration Invoker ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Replay executions

To replay an execution, select one of the following options:

### Console

  1. In **Application Integration** , go to the **Logs** page. 

[Go to Application Integration Logs](https://console.cloud.google.com/integrations/logs)

The **Execution Logs** page appears displaying the lists of region specific execution logs.

  2. Click **more_vert (More actions)** for the execution log that you want to replay, and then select **refresh Replay**. 

If your execution is in the **Suspended** , **On hold** , or the **Retry on hold** state, select the **refresh Cancel and replay** option.

**Note:** You can't cancel an integration execution if the integration is in the **In process** state.
  3. In the **Replay Execution** pane, provide the following inputs: 
     1. **Reason for replaying the execution:** Enter the reason for replaying the execution. This reason is displayed in the execution log and might be useful for debugging.
     2. **Replay from point of failure:** Select to replay the execution from the point of failure. This resumes from the first failed task or trigger in the previous run. **Note:** The **Replay from point of failure** option only appears for failed executions. 
     3. **Configure input variables:** This section lets you configure the input variables for the replay execution. You can either use the existing values from the previous run or provide new values to replay.
  4. Click **Replay**.

The following image shows a sample execution log with the **Replay Execution** pane open:

![Replay executions](https://docs.cloud.google.com/static/application-integration/images/replay-execution-pane.png)![Replay executions](https://docs.cloud.google.com/static/application-integration/images/replay-execution-pane.png)




### API

Call the [`projects.locations.integrations.executions.replay` method](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions/replay) and provide the ID of the execution that you want to replay:
    
    
    curl -X POST https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/integrations/INTEGRATION_NAME/executions/EXECUTION_ID:replay -H "Authorization: Bearer $TOKEN"
      

## What's next

  * Learn about [replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions).
  * Learn about [cancelling executions](https://docs.cloud.google.com/application-integration/docs/cancel-executions).
  * Learn about [logs in Application Integration](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
