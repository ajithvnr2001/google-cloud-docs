---
url: https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc/
title: Trigger a workflow with events or Pub/Sub messages \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:36.846874+00:00
---

# Trigger a workflow with events or Pub/Sub messages  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Trigger a workflow with events or Pub/Sub messages Stay organized with collections  Save and categorize content based on your preferences. 

You can use an Eventarc trigger to execute a workflow as a result of an event or a set of events. The events are routed from an event provider to interested event receivers.

Eventarc delivers events to the event receiver in the CloudEvents format through an HTTP request. The Workflows service converts the event to a JSON object (following the [CloudEvents specification](https://docs.cloud.google.com/eventarc/docs/workflows/cloudevents)) and passes the event into the workflow execution as a [workflow runtime argument](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).

An execution of your workflow is triggered:

  * When an **audit log is created** that matches the trigger's filter criteria. For example, see this quickstart in which you trigger Workflows with [events from BigQuery using Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/workflows/quickstart-cal).
  * In response to **direct events** such as an update to a Cloud Storage bucket or an update to a Firebase Remote Config template. For example, see this quickstart in which you trigger Workflows with [direct events from Cloud Storage](https://docs.cloud.google.com/eventarc/docs/workflows/quickstart-storage).
  * By **messages published to a Pub/Sub topic**. For example, see this quickstart in which you trigger Workflows with [Pub/Sub messages](https://docs.cloud.google.com/eventarc/docs/workflows/quickstart-pubsub).



Note the following:

  * Events are considered delivered as soon as the workflow execution starts, and the actual execution takes place asynchronously in the Workflows services.

  * Executions triggered by events are not retried if the workflow execution starts, but later fails. For more information, see the [Event retry policy](https://docs.cloud.google.com/eventarc/docs/overview#event_retry_policy).

  * The Workflows deduplication window to ensure exactly-once processing of events is 24 hours.

  * When using Workflows as the destination for an Eventarc trigger, events larger than the maximum Workflows argument size will fail to trigger workflow executions. For more information, see [Quotas and limits](https://docs.cloud.google.com/workflows/quotas).

  * In projects protected by a service perimeter, when routing events to Workflows destinations for which the Pub/Sub push endpoint is set to a Workflows execution, you can only create new Pub/Sub push subscriptions through Eventarc. Note that the service account used for push authentication for the Workflows endpoint must be included in the service perimeter. For more information, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls).




## Create a trigger using the Google Cloud CLI

You can create a trigger by running a `gcloud eventarc triggers create` command along with required and optional flags.

For more information, see the **gcloud** instructions in the "Create a trigger" section when [creating a trigger for a specific provider, event type, and Workflows destination](https://docs.cloud.google.com/eventarc/docs/targets#triggers).

## Create a trigger using the console

The following steps show you how to create a trigger on the **Workflows** page in the Google Cloud console.

### Before you begin

  1. Enable the Eventarc and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,pubsub.googleapis.com)

  2. Create a [service account](https://docs.cloud.google.com/workflows/docs/authentication) so that Eventarc can make requests to the Workflows API:

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts)

     2. Select a project and then click **Create service account**.

     3. In the **Service account name** field, enter a name that is between 6 and 30 characters.

It can contain lowercase alphanumeric characters and dashes. After you create a service account, you cannot change its name.

     4. Click **Create and continue**.

     5. Grant your new service account the [workflows.invoker](https://docs.cloud.google.com/workflows/docs/access-control#roles) role so that the account has permission to trigger your workflow. In the **Select a role** list, select **Workflows > Workflows Invoker**.

If you are developing a production app, always grant the least permissive roles possible. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).

     6. Click **Done**.

  3. To allow the principal that will run your Eventarc commands the ability to act as an Identity and Access Management (IAM) service account, [grant a role that allows the principal to impersonate the service account](https://docs.cloud.google.com/iam/docs/service-account-permissions#roles).




### Configure the trigger

  1. If you don't already have a workflow that you want to trigger, [create and deploy one](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#creating_a_workflow).

  2. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  3. On the Workflows page, select a workflow to go to its details page.

  4. On the **Workflow Details** page, click _edit_ **Edit**.

  5. On the **Edit workflow** page, select **Add new trigger > Eventarc**.

The **Eventarc trigger** pane opens.

  6. Follow the instructions to [create a trigger for a specific provider, event type, and Workflows destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) and refer to the **Console** instructions in the "Create a trigger" section.

  7. Select the **Service account** that invokes your workflow.

This specifies the IAM service account to which you previously granted the `workflows.invoker` role so that the account has permission to trigger your workflow.

  8. Click **Save trigger**.

**Note:** If you are updating an existing workflow, you do _not_ need to redeploy the workflow. However, if you are creating a new workflow, you must also deploy the workflow.

The Eventarc trigger is listed on the **Triggers** tab of the **Workflows Details** page.

  9. If you want to update or delete the trigger, you must edit the workflow:

     1. On the **Workflow Details** page, click _edit_ **Edit**.
     2. In the **Triggers** section, find the trigger you want to update or delete.
     3. Click _edit_ **Edit resource** or _delete_ **Delete resource**.



Your workflow execution is now triggered by the events that match your trigger's filter criteria.

## Create a trigger using Terraform

You can create a trigger for a workflow using Terraform. For details, see [Trigger a workflow using Eventarc and Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

## What's next

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
