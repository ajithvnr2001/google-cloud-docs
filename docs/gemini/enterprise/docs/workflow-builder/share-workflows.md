---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows/
title: Share a workflow \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:01.477651+00:00
---

# Share a workflow  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Share a workflow Stay organized with collections  Save and categorize content based on your preferences. 

Share workflows that you've created and launched using Workflow Builder with other users within your organization.

With workflow sharing, you can:

  * Share live workflows with users and groups in your organization.
  * Set up custom run schedules or event-based triggers.
  * Track preview executions and automated runs.
  * Duplicate shared workflows to customize their steps.



Depending on your app's [feature control configurations](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure-feature-controls), you might need an administrator to review and approve your request before you can share a workflow.

If you share a workflow, the people you shared the workflow with will see and use the live version.

**Caution:** When you share an agent, consider the following data access behaviors: 

  * **Knowledge files:** Any user with access to the shared agent can query and view information from files uploaded to the agent's **Knowledge** section, even if they don't have direct access or permissions to the source files. For example, if you upload a confidential file to the **Knowledge** section, all users with access to the shared agent can ask questions about that file's content.
  * **Connectors and data stores:** When an agent accesses data through connectors, user access control lists (ACLs) and permissions are preserved. Users can only query and retrieve data from data stores and connectors that their individual user accounts are authorized to access.



## Share a workflow

To share a workflow, do the following:

### App

  1. Open your Gemini Enterprise app and go to the **Agent Gallery** page.

The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents.

  2. In the **Your agents** section, find the workflow you want to share.

**Note:** You can share a workflow that is in a `draft` state, but other users can't run it until it's turned on.
  3. In the upper right header of the Workflow Builder canvas, click ![Share icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/share_icon.png)**Share**.

  4. Enter the email addresses of the users or Google Groups that you want to share the workflow with.

**Note:** You can share your workflow with individual user email addresses. Sharing with Google Groups isn't enabled for end users. A Gemini Enterprise app administrator or any user with the [Discovery Engine Admin (discoveryengine.admin)](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine) role can enable group sharing at the Gemini Enterprise app level.
  5. Click **Done**.

**Note:** If your app administrator has enabled administrator review for workflow sharing, a share request is sent to the app administrator for review and approval. After the app administrator approves the request, the workflow is shared with those in the access list. You can, at any time, edit the share request to add or remove users, or cancel the request.



## Administrator review control

By default, workflow owners can share their workflows with any user within their organization without approval from an app administrator. However, app administrators can change the app [feature control configurations](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure-feature-controls) to require administrator review and approval for sharing workflows in the app.

By default, workflow owners can't share their workflows with groups. However, the Gemini Enterprise app administrator can choose to make workflows shareable with Google Groups— with or without administrator approval.

### The sharing process

Only the initial sharing of a workflow requires administrator review and approval. Subsequent workflow revisions don't need re-approval.

Workflow sharing follows a two-step process when administrator review is enabled:

  1. The workflow owner shares the workflow with one or more users or Google Groups.

  2. The app administrator reviews the sharing request and approves or denies it.




### Review a share request

App administrators are responsible for reviewing and managing workflow sharing requests.

**Notes:**

  * This section only applies if the [Enable workflow sharing without administrator approval](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) feature is disabled in the app's feature controls.
  * Only app administrators with the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) IAM role can review and approve share requests.



### Console

To review a share request as an app administrator, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Apps** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app containing the workflow.

  3. In the app navigation menu, click **Agents**.

  4. Find the workflow with a **Review share request** action in the **User permissions** column.

![Share workflow review request](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/admin-share-request.png)

  5. Click **Review share request**.

  6. In the **Share request** pane:

     * Review the access list under **Requested to share with the following users**.
     * Optional: Modify the access list to add or remove user accounts, Google Groups, or WIF identity pools.
  7. To approve the request and grant access, click **Approve and enable**.

  8. To reject the request, click **Deny**.




## Use a shared workflow

When a workflow owner shares a workflow with you, you can access and preview its graph configuration. While the workflow graph is read-only for shared users, you can run a preview manually, configure your own trigger settings, view your own run history, or make a copy of the workflow.

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  3. Go to the **Shared with me > From your org** section.
  4. Click the shared workflow you want to view. The workflow launches in a read-only designer layout, displaying the live node graph. Note: If the shared workflow is suspended or turned off, the Workflow Builder canvas doesn't render and you can't run it, but you can still view its previous runs.

  5. Optional: To perform a manual test run of the workflow:

     * Click **Preview** in the upper right header of the Workflow Builder canvas.
     * Run the preview. If the preview run fails because a connector used by the workflow is not authorized, click **Enable Connectors** below the error message to complete the OAuth flow.



### Set up your own triggers

Triggers on a shared workflow are user-specific. You can configure a custom run schedule or event filters to run a shared workflow automatically.

To set up your own triggers, do the following:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents** > **Gallery**.
  3. Go to the **Shared with me > From your org** section and click the shared workflow you want to set up a trigger for.
  4. Access the trigger configuration:

     * Select the more_vert **Actions** menu > **Set up triggers**.
     * Alternatively, open the workflow in the Workflow Builder editor canvas, click the workflow name, and select **Set up triggers**.
  5. You can configure a trigger using either of the following modes:

     * **Schedule:** Select **Run on a schedule** and configure when the workflow runs for you (such as the frequency and time zone).
     * **Event:** Select **Run on app events** and configure the event filters to specify when the workflow runs for you. For example, for a Google Drive event trigger, you can filter by fields such as **Owners** (such as a Google ID like `janedoe`), **Name** , **MIME type** , **Modified time** , or **Parent folder**. You select an operator (such as **contains** or **equals**), enter a value, and combine multiple rules using **AND** or **OR** conditions.
  6. If the workflow uses connectors that require authentication (for example, connectors used in a workflow step rather than the trigger itself), enable and authorize the connectors in the Workflow Builder canvas editor when prompted.

  7. Click **Save**. The trigger is saved and it runs the workflow automatically. You can [manually trigger the workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/simulate-workflows) to preview what will happen when the schedule or event trigger runs this workflow. If you want your workflow to stop running, select **Don't run on app events** or **Don't run on a schedule** from the **Set up triggers** dialog.




### View your runs

To view your runs, do the following:

### App

  1. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  2. Go to the **Shared with me > From your org** section and click the shared workflow.
  3. In the Workflow Builder canvas, click the **Runs** tab.
  4. Click a specific run to view its execution logs and step-by-step trace.



For more information, see [workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs#view-runs-workflow).

### Make a copy of a shared workflow

Shared workflows are read-only for shared users, except for their trigger configurations. If you want to edit and customize a shared workflow's steps, you can create a copy in your own workspace.

To create an editable duplicate of the shared workflow, do the following:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents** > **Gallery**.
  3. Go to the **Shared with me > From your org** section and click the shared workflow you want to copy.
  4. In the Workflow Builder editor canvas, click the workflow title, and select **Make a copy**. The copy is added to your **Your agents** list.



## Shared workflow dependencies

If your workflow imports and references other workflows (sub-workflows) in its workflow steps, keep the following in mind:

  * **Access requirements** : When you share a parent workflow, or when you import a workflow into your workflow, ensure that all users in your access list also have access to all imported sub-workflows.
  * **Run failures** : If a user runs a workflow without access to an imported sub-workflow, the run fails with a message asking them to request access from the owner.



## Sharing limits

When sharing a workflow, the following limits apply:

  * **Maximum 1,500 individual accounts:** Workflow Builder manages agent access using underlying Google Cloud IAM allow policies, which enforce a hard cap of 1,500 members per policy. Sharing an agent with more than 1,500 individual user accounts causes the operation to fail with the following error:
        
        The number of members in the policy (1,501) is larger than the maximum allowed size 1,500.
        

  * **Use groups to share at scale:** Each Google Groups or Workspace group counts as a single member toward the 1,500-member policy limit. If you need to share an agent with hundreds or thousands of colleagues across an organization, ask your app administrator to [enable group sharing](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls) and enter group email addresses (for example, `support-team@example.com`) instead of individual user accounts.




For a full list of system constraints, see [Workflow Builder quotas and limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits).

## Considerations

  * If the workflow owner turns on a new version or updates the live version of the workflow, all shared users automatically run the new live version on subsequent executions.

  * If a workflow is turned off or suspended, the Workflow Builder canvas doesn't render and shared users cannot run the workflow, but they can still view their past run histories and session logs in the **Runs** gallery. If the workflow is unshared, disabled, or deleted, shared users lose all access, including to their past run histories and session logs.

  * Actions that modify external data require human-in-the-loop (HITL) approval, except for emails or calendar events you send to yourself.

  * App administrators can transfer ownership of a shared workflow to another user or to themselves in the Google Cloud console. If the workflow has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events, and the new owner should enable them before using the agent. For more information, see [Transfer agent ownership](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#transfer-ownership).




## What's next

  * Learn how to [create a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows).
  * Learn how to [edit a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows).
  * Learn how to [manage workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions).
  * Learn how to [monitor workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).
  * View [Workflow Builder quotas and limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
