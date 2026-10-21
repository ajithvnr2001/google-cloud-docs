---
url: https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflow-executions/
title: Admin settings \u2013 Workflow Executions \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:34:06.360464+00:00
---

# Admin settings – Workflow Executions  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflow-executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings – Workflow Executions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [looker-workflows-fb@google.com](mailto:looker-workflows-fb@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



The **Workflow Executions** page in the **Alerts & Schedules** section of the **Admin** menu shows the recent history of workflow activity. To view the **Workflow Executions** page, you must be assigned a role that contains the `see_schedules` and `chat_with_agent` permissions.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

You can view workflows on the [Admin settings – Workflows](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows) page. The workflow specifies when content should be sent to specific addresses.

A new workflow is created each time that content is sent. For example, if a workflow specifies sending specific content to certain addresses every Monday, then Looker will make a new workflow each Monday to send that content to the specified addresses.

## Filter workflows by execution status

At the top of the **Workflow Executions** page, you can filter the workflows by job status:

  * **All** : all recent workflows
  * **Running** : only workflows that are running
  * **Successful** : only workflows that were completed successfully
  * **Failed** : only workflows that failed to be completed successfully



## Information included

The following information is included for each workflow execution or job:

Column | Definition  
---|---  
Time | When the workflow execution began  
Status | Whether the workflow execution is complete (green checkmark) or returned an error (red alert icon)  
Stage | The current stage of a running workflow execution  
User | The user that created the workflow  
Source | The type of content, displayed as `Workflow`  
Name | The name of the workflow, which also serves as a link to the workflow content  
Type | The delivery destination, such as `Email` or `Slack`  
Message | For a failed execution, the error message. For a successful execution, `success`  
Runtime | How long the workflow execution ran or has been running  
  
## Troubleshoot workflow execution error messages

You can use the error messages displayed in the **Message** column to diagnose and resolve workflow execution failures. Common error messages include the following:

### Recipient and allowlist errors

  * **`Unauthorized emails in plan: ["<email_address>"]`**: 
    * **Cause** : One or more recipient email addresses belong to a domain that is not included in your Looker instance's [email domain allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-general-email-domain-allowlist).
    * **Resolution** : Add the recipient's domain to the admin email allowlist, or edit the workflow to remove unauthorized email addresses.



### Agent and entity errors

  * **`Agent execution failed: unexpected message received`** : 
    * **Cause** : The Gemini Data Agent encountered a runtime error or unexpected response while interpreting directives or generating the natural language insights summary.
    * **Resolution** : Review and refine the natural language directives in the workflow configuration to ensure instructions are clear and specific.
  * **`entity WorkflowAgent missing`** : 
    * **Cause** : The primary data agent, dashboard, or Explore associated with the workflow was deleted, renamed, or modified.
    * **Resolution** : Recreate or update the workflow with an active data agent or accessible Explore.



### User permission and account errors

  * **User permission or model access failures** : 
    * **Cause** : The user who created the workflow lacks access to the models underlying the Explore or dashboard.
    * **Resolution** : Ensure the workflow owner has the required permissions in [**Admin > Users / Roles**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles), or recreate the workflow under an active, authorized user.
  * **Disabled user account** : 
    * **Cause** : The workflow owner's Looker user account has been disabled or deactivated.
    * **Resolution** : Re-enable the user account or recreate the workflow under an active user.



### Scheduler queue and timeout errors

  * **`Job is no longer processing @<state>`** (where `<state>` is `execute` or `deliver`) or **`Job was expected to dequeue by @<time>`**: 
    * **Cause** : The workflow remained in the scheduler queue for an hour or longer without being completed, typically due to temporary database connection timeouts or system resource constraints.
    * **Resolution** : The workflow will attempt to run again at its next scheduled interval. You can also programmatically retry failed runs using the Looker API ([`run_scheduled_plan_once`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/run_scheduled_plan_once)).



## Related resources

  * [Agentic workflows overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview)
  * [Create a triggered agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows)
  * [Create a scheduled agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-scheduled-agentic-workflows)
  * [Admin settings – Workflows](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows)
  * [Manage your agentic workflows](https://docs.cloud.google.com/looker/docs/user-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
