---
url: https://docs.cloud.google.com/dataform/docs/cloud-logging/
title: Monitor runs \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:02.640054+00:00
---

# Monitor runs  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Monitor runs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following:

  * Monitor execution logs.
  * View Logging logs for Dataform.
  * Configure alerts for failed workflow invocations.



## Before you begin

To monitor execution logs, ensure you do the following:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. [Trigger a run](https://docs.cloud.google.com/dataform/docs/trigger-execution) at least once.




### Required roles

To get the permissions that you need to view execution logs, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on the Dataform repository where workflow executions are being tracked
  * Verifying the setup of an execution: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role gives you read-only access to all the features of Cloud Logging. For more information on the Identity and Access Management permissions and roles that apply to Logging data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

To create and manage log-based alerts, ensure that your IAM role includes the permissions that are described in [Roles required to create and use log-based alerting policies](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).

## Monitor execution logs

This section shows you how to view execution logs in Dataform.

You can view the logs of all the executions that are triggered in a repository, and the logs of executions that were triggered in a workspace in the last 24 hours.

### Inspect repository execution logs

To view the logs of all the executions triggered in a repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Go to your repository.

  3. Click **Workflow Execution Logs**.

  4. To view the details of an execution, click the execution.

  5. To view the details of an action within the execution, click **View details**.




### Inspect workspace execution logs

To view the logs of the 1,000 most-recent executions that were triggered in a workspace in the last 24 hours, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Go to your repository and select your workspace.

  3. In your workspace, click **Executions**.

  4. To view details of an execution, click the execution.

  5. To view details of an action within the execution, click **View details**.




## View Logging logs for Dataform

This section shows you how to view Cloud Logging logs for Dataform workflow invocations.

Each Dataform workflow invocation is logged using [Logging](https://docs.cloud.google.com/logging/docs). Logging is automatically enabled for Dataform workflow invocations, which can incur Logging billing charges. For more information, see [Dataform pricing](https://cloud.google.com/dataform/pricing).

### View logs

  * To view logs, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)




For information about filtering Logging logs in Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Dataform logs are indexed by Dataform repository.

### Log format

Dataform sends workflow invocation log messages in the following format:
    
    
    {
      "insertId": "14ip1tza5",
      "jsonPayload": {
        "terminalState": "SUCCEEDED",
        "workflowInvocationId": "1678383230-ac4ed48c-eb70-4555-b2b0-cda54d13edfa",
        "@type": "type.googleapis.com/google.cloud.dataform.logging.v1.WorkflowInvocationCompletionLogEntry"
      },
      "resource": {
        "type": "dataform.googleapis.com/Repository",
        "labels": {
          "repository_id": "repository-name-example",
          "resource_container": "PROJECT_ID",
          "location": "us-central1"
        }
      },
      "timestamp": "2023-03-09T17:34:06.965981805Z",
      "severity": "INFO",
      "logName": "projects/project-name-example/logs/dataform.googleapis.com%2Fworkflow_invocation_completion",
      "receiveTimestamp": "2023-03-09T17:34:07.362371980Z"
    }
    

### What is logged

Dataform log entries contain information that is useful for monitoring and debugging your workflow invocations.

Log entries contain the following types of information:

  * `receiveTimestamp`
  * `release_config_id`
  * `repository_id`
  * `resource_container`
  * `workflow_invocation_id`
  * `workflow_config_id`
  * `severity`: can be `INFO`, `WARNING`, or `ERROR`
  * `terminalState`: can be `SUCCEEDED`, `CANCELED`, or `FAILED`
  * `timestamp`
  * `@type`



### Configure metrics and alerts with Cloud Monitoring

You can use Monitoring to observe trends in your logs and to notify you when conditions that you describe occur.

To provide Monitoring with data from your logs, Logging offers you the following:

  * Log-based metrics, which you can use as follows: 
    * To create alerting policies that notify you of changes over time.
    * To create charts that display changes over time.
  * Log-based alerts, which notify you anytime a specific event appears in a log.



For more information about log-based metrics and log-based alerts, see [Monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs).

To learn how to configure log-based alerts for Dataform workflow invocations, see [Configure alerts for failed workflow invocations](https://docs.cloud.google.com/dataform/docs/monitor-runs#configure-alerts-failed-workflow-invocations).

## Configure alerts for failed workflow invocations

This section shows you how to configure log-based alerts for failed Dataform workflow invocations using the Logs Explorer.

You can use Monitoring to observe trends in Logging logs for Dataform workflow invocations and to notify you when conditions that you describe occur.

Each Dataform workflow invocation is logged using [Logging](https://docs.cloud.google.com/logging/docs). Logging is automatically enabled for Dataform workflow invocations, which can incur Logging billing charges. For more information, see [Dataform pricing](https://cloud.google.com/dataform/pricing).

To receive alerts when a Dataform workflow invocation fails, you can [create log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).

You can create log-based alerts from the **Logs Explorer** page in the Google Cloud console or by using the Monitoring API. This section describes how to create log-based alerts for Dataform workflow invocation failure using Logs Explorer.

To configure log-based alerts for failed Dataform workflow invocations, follow these steps:

  1. In the Google Cloud console, select **Logging** , and then select **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the **Query** pane, select **Show query** and enter the following query:
         
         resource.type="dataform.googleapis.com/Repository"
             jsonPayload.@type="type.googleapis.com/google.cloud.dataform.logging.v1.WorkflowInvocationCompletionLogEntry"
             jsonPayload.terminalState="FAILED"
          

This query alerts you of all failed Dataform workflow invocations.

     1. Optional: To filter failed workflow invocations by a release configuration, append the following to the query:
            
            jsonPayload.releaseConfigId="RELEASE_CONFIGURATION_ID"
            

Replace `RELEASE_CONFIGURATION_ID` with the ID of the release configuration.

     2. Optional: To filter failed workflow invocations by a workflow configuration, append the following to the query:
            
            jsonPayload.workflowConfigId="WORKFLOW_CONFIGURATION_ID"
            

Replace `WORKFLOW_CONFIGURATION_ID` with the ID of the workflow configuration.

The following query alerts you when a Dataform workflow invocation that's related to both the `daily` release configuration and the `production` workflow configuration fails:
    
    resource.type="dataform.googleapis.com/Repository"
     jsonPayload.@type="type.googleapis.com/google.cloud.dataform.logging.v1.WorkflowInvocationCompletionLogEntry"
     jsonPayload.terminalState="FAILED"
     jsonPayload.releaseConfigId="daily"
     jsonPayload.workflowConfigId="production"
    

  3. Optional: To validate the query, use **Run query** in the **Query results** pane.

  4. In the header of the **Query results** pane, click **Create alert**. When your window is narrow, the **Create alert** option might appear on the **Actions** menu instead.

  5. In the **Alert details** pane, give the alert a name and description:

     1. Enter a name for your alert in the **Alert Name** field. For example: `Dataform: workflow failure`.

     2. Enter a description of this alert. You can also include information that might help the recipient of a notification diagnose the problem. The following string summarizes the reason for the alert:
            
            Log-based alert in project ${project} detected a failed Dataform workflow.
            

For information about how you can format and tailor the content of this field, see [Annotate notifications with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

  6. To advance to the next step, click **Next**.

  7. In the **Choose logs to include in the alert** pane, check the query and results by clicking **Preview logs**.

We recommend building the query in the Logs Explorer **Query** pane. The query that you built in the **Query** pane is also displayed on this pane.

You can edit the query in this pane, if necessary. If you edit the query, then check the results by clicking **Preview logs**.

  8. Click **Next**.

  9. Select the minimum time between notifications. This value lets you control the number of notifications that you get from this alert if it is triggered multiple times. For this example, select **5 min** from the options.

  10. Optional: Select the incident autoclose duration. By default, the incident autoclose duration is set to 7 days.

  11. Click **Next**.

  12. Select one or more notification channels for your alert. For this example, select an email notification channel.

If you already have an email notification channel configured, then you can select it from the list. If not, click **Manage notification channels** and add an email channel. For information about creating notification channels, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  13. Click **Save**.




Your log-based alert is now ready to test. For instructions to test the alert, see [Test the example log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-test).

## What's next

  * Learn about [manually triggering runs](https://docs.cloud.google.com/dataform/docs/trigger-execution).
  * Learn how to [schedule runs with Workflows and Cloud Scheduler](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflows-cloud-scheduler).
  * Learn how to [configure compilation overrides with the Dataform API](https://docs.cloud.google.com/dataform/docs/configure-compilation#configure-compilation-overrides-with-api).
  * Learn about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) and [Monitoring](https://docs.cloud.google.com/monitoring).
  * Learn about [Logging pricing](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
