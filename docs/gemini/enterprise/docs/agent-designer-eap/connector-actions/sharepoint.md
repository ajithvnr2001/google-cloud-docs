---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/connector-actions/sharepoint/
title: Workflows overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:51.442714+00:00
---

# Workflows overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/connector-actions/sharepoint/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Workflows overview Stay organized with collections  Save and categorize content based on your preferences. 

**Workflows** are agents that you can build using [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder) in your Gemini Enterprise web app. These agents are designed to execute a sequence of steps or actions, which can include a mix of AI automation and human intervention, based on a configured trigger. Workflow responses can be deterministic or non-deterministic based on the overall orchestration logic of the agent.

Workflows are ideal for the following use cases:

  * **Multi-step processes** with defined sequence logic. For example, automating an employee onboarding checklist across tools like Gmail and Calendar.
  * Tasks with AI automation and human approvals. For example, drafting a report with AI that requires a user **sign-off** before publishing.
  * Complex orchestrations with conditional logic. For example, routing sales leads to different teams based on region and budget.



The following features are available in Workflow Builder:

  * **Create a workflow with natural language** : Describe your workflow in plain language and generate a workflow scaffold automatically.
  * **Use workflow templates** : Browse and start from prebuilt templates for common business use cases.
  * **Set up workflow triggers** : Run workflows automatically when data changes in connectors.
  * **Connect connectors to agent steps** : Enable read and write-back tools (such as Gmail, Jira, and Google Drive) within your Gemini Agent steps to search data, send messages, and manage records.
  * **Use flow control steps** : Add conditional branching, data filtering, and loops to your workflow.
  * **Connect MCP servers** : Connect MCP servers as workflow steps or as tools for Gemini Agent steps.
  * **Use human-in-the-loop steps** : Add human review, approval, and information request steps to your workflow.
  * **Add existing agents to your workflow** : Hand off tasks to other specialized AI agents within your workflow.
  * **Manage workflow versions** : Save, share, compare, and restore workflow versions.
  * **Edit a workflow with natural language** : Edit existing workflows by describing changes in natural language.
  * **View workflow execution logs** : Monitor workflow runs with **step-by-step** execution traces.
  * **Share a workflow** : Share live workflows with other users in your organization.



## Supported connectors

Workflows support these connectors:

  * Gmail
  * Google Calendar
  * Google Chat
  * Google Drive
  * Slack
  * Jira
  * ServiceNow
  * Confluence
  * OneDrive
  * SharePoint
  * Outlook



## Before you begin

Before exploring these new features, do the following:

  * Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure you have a Gemini Enterprise web app with the necessary data stores connected. For more information, see [About apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores).



## Workflow canvas

Workflow Builder offers a hybrid canvas that combines the ease of natural language prompts with the control of a visual editor.

  * **Conversational designer** : The conversational designer, accessible at the start of workflow creation and within the visual editor, provides a conversational interface to build and refine your workflow using natural language prompts. This is ideal for users who prefer a **no-code** development experience and want to use natural language to build their workflows.

    * ![A conversational designer interface at the start of workflow creation.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/chat-box.png)
    * ![A conversational designer interface within the workflow canvas.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/chat-box-2.png)
  * **Editor canvas** : The editor canvas provides a visual representation of the workflow. It provides a logical flow of nodes that represent the steps and connections between them. The visual editor is ideal for users who want to refine the workflow logic, add conditional logic, and integrate with various tools and applications.

![The workflow editor tab.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/editor-tab.png)

    * **Preview** : The preview tab provides a live preview of the workflow, letting you run simulations to test the workflow's flow and make any necessary adjustments.

![The workflow preview tab.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/preview-tab.png)

    * **Runs** : The runs tab provides a list of all the workflow runs, including the date and time of each run, the trigger that started the run, and the current status of the run.

![The workflow runs tab.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/runs.png)




## Workflow components

A workflow consists of the following components:

  * **Triggers**
  * **Steps**
  * **Variables**



### Triggers

_Triggers_ are events that start the execution of a workflow. The following table lists the supported triggers for workflows:

Trigger | Description | Configuration fields  
---|---|---  
**Manual trigger** | Triggers the execution of the workflow on demand. Users can launch the workflow by entering `@` and the workflow name from a Gemini Enterprise app chat prompt.  | 

  * **Input fields** : Optional or required input fields that users can provide when launching the workflow.

  
**Schedule trigger** | Triggers the execution of the workflow at a specified frequency.  | 

  * **Frequency** : The frequency at which the workflow is triggered. You can specify the frequency in minutes, hours, days, weeks, months, or use a custom cron expression. 
  * **Time zone** : The time zone for the frequency.

  
**Event trigger** | Triggers the execution of the workflow when data changes in a connector.  | 

  * **Connector** : The connected application that generates the event.
  * **Filter** : The criteria that must be met for the event to trigger the workflow.

  
**Note:** Event triggers define the starting condition for a workflow based on external connector activity (such as receiving an email). They are configured as workflow triggers and don't appear as intermediate step nodes in the canvas flow. 

### Steps

_Steps_ are individual tasks that the workflow performs. Each step is executed in sequence, and the outcome of each step can influence the next step.

The following table lists the supported steps, categorized by the type of action that they perform:

Category | Step | Description | Configuration fields  
---|---|---|---  
**Agent nodes** | Gemini Agent |  An **AI-powered** agent that you can configure to read, reason, and respond based on **predefined** instructions.  |  **Input fields:**

  * **Instructions** : The instructions for the Gemini Agent.
  * **Knowledge** : The additional files or resources that the Gemini Agent can access to generate responses. When a Google Drive or OneDrive data store is configured, **Add from Drive** and **Add from OneDrive** options are available. These options let you select specific files or folders, restricting the agent's search to only those resources. The search is performed live on each agent run, so any changes to the source files are immediately reflected. **Important** : If the full Drive or OneDrive tool is enabled on the same agent node, it takes precedence and grants the agent unrestricted search access. The recommended workaround is to use two distinct `Gemini Agent` nodes. The first node should use the restricted knowledge for searching, and the second node can use the full tool for other functionalities like writing updates. 
  * **Connected apps** : Select which connectors and actions the agent can access at runtime. You can granularly select search actions and enable or disable data modification actions. For more information, see Configure Agent node connectors and actions.
  * **Model** : The Gemini model that the Gemini Agent uses. **Note:** Only Gemini 3.0 and later models are supported. 

**Output fields:** The response from the Gemini Agent is captured as a variable that can be passed as input to subsequent steps in the workflow.

  * **Output format** : You can specify the output as plain text or in a structured JSON format. 
  * **JSON schema** : When using structured output, you can define a manual JSON schema to specify the format and data types of the output variables, ensuring consistent data handling throughout the orchestration. 

  
**Flow control** | **Condition** | Conditions are logical statements that determine how the workflow executes the steps. They define the criteria that must be met for a step to execute, and can be based on the outcome of previous steps or external data sources.  |  **Input fields:**

  * **Branch name** : The name of the branch to execute if the condition is true.
  * **Variable** : The variable to evaluate. You can select a variable from the output of previous steps.
  * **Operator** : The operator (such as `contains`, `equals`, `greater than`) to use for the evaluation.
  * **Value** : The value to compare with the variable. You can specify a static value, or select a variable from the output of previous steps.
  * **\+ Condition** : You can add additional conditions using logical operators such as `AND` and `OR`.

  
**Human in the loop** | **Request info** |  Lets you request information from a human user.  |  **Input fields:**

  * **Message** : The message to display to the user. You can specify a static message, or select a variable from the output of previous steps.
  * **Questions** : The questions to ask the user. You can specify the type of answer you are requesting (such as short answer, paragraph, date, email, **single-select** , or **yes or no**).

**Output fields:** The questions that the user answered.  
  
### Configure Agent node connectors and actions

When you configure a **Gemini Agent** node, you can control which connectors and actions the agent can access at runtime. You can restrict the agent to read-only search operations or enable mutative write-back actions.

#### At a glance: Agent node action capabilities

Capability | Action category | Selection granularity | Example use case  
---|---|---|---  
**Search & query** | `Search For Data` | **Per-action** (toggle individual actions on or off) | Broad queries, looking up tickets, searching across knowledge bases.  
**Data modification** | `Add Or Update Data` | **Connector-level** (all-or-nothing toggle) | Creating tickets, updating issue status, sending emails.  
  
#### Attach and authorize a connector

### App

To attach a connector to an agent node, do the following:

  1. In the workflow canvas, click the **Gemini Agent** node to open its configuration pane.
  2. Under **Connected apps** , locate the connector you want to attach (such as **Jira** , **Gmail** , or **Google Drive**).
  3. Toggle the connector switch to **On**. 
     * If this is the first time you or your organization is using the connector, complete the prompted OAuth authorization flow to grant the required permissions.
  4. Click the expand arrow (expand_more) next to the connector name to turn on the actions supported by the connector.



#### Select action categories

Each connector organizes its actions into two distinct categories:

  * **Search For Data** : Actions that search, query, list, or retrieve records from the connected service. 
    * **Granular action selection** : Click the **Configure** icon (tune) next to **Search For Data** to view all available search actions (such as `Search Events`, `List Events`, or `List Calendars`). You can enable or disable individual actions independently.
    * **Deterministic search filters** : Limit search scopes by configuring filters using structured drop-downs or native query expressions, such as Jira Query Language (JQL), Confluence Query Language (CQL), Drive search queries, or Gmail search operators.
    * **In-line query testing** : Validate your queries directly within the configuration pane to verify that your filters return the expected results before running the workflow.
  * **Add Or Update Data** : Actions that create, modify, send, or delete records in the target application (for example, creating a Jira issue or sending an email). 
    * **Connector-level toggle** : The mutative action toggle operates at the connector level. Toggling this on grants the agent access to all supported mutative operations for that connector.



**Note:** Adding or updating data through connectors requires human review. If you toggle a connector on but disable all underlying actions in both the **Search For Data** and **Add Or Update Data** categories, the agent cannot interact with the connector at runtime.

#### Action dependency requirement

**Caution: Mutative actions depend on read-only and search actions to resolve entity identifiers at runtime.**

Mutative actions typically require the agent to first look up a record identifier (such as an issue ID, contact email, or folder ID) before performing an update, create, or delete operation.

For example, an **Update Jira issue** action requires the agent to first query Jira to obtain the internal `issue_id`. If mutative actions are enabled without their supporting search actions, the agent cannot look up the required target records, which causes runtime action execution errors (such as `ENTITY_NOT_FOUND` or missing parameter errors). When enabling mutative actions, always enable the supporting search and retrieval actions.

#### Example: Restrict an agent to read-only Jira search

### App

The following example shows how to configure a **Gemini Agent** node to search Jira issues without allowing the agent to create or modify issues:

  1. In the workflow canvas, click the **Gemini Agent** node to open its configuration pane.
  2. Under **Connected apps** , toggle **Jira** to **On** (complete OAuth authorization if prompted).
  3. Click the expand arrow (expand_more) next to **Jira**.
  4. Ensure the **Search For Data** toggle is **On** , and toggle **Add Or Update Data** to **Off**.
  5. Click the **Configure** icon (tune) next to **Search For Data** , and verify that only the desired read-only search actions (such as **Search Jira**) are enabled.



#### Action resolution and runtime precedence

When the workflow executes, Gemini Agent selects and invokes actions based on the following precedence rules:

Configuration state | Runtime action execution  
---|---  
**Search enabled** | Exposes standard list and retrieve actions for all enabled search operations.  
**Individual search action disabled** | The specific search action is omitted from the agent's action catalog.  
**Add / Update data enabled** | Exposes mutative actions alongside any enabled search actions.  
**Add / Update data disabled** | All data creation, update, and deletion actions are blocked for that connector.  
  
### Variables

_Variables_ are values that can be passed between steps in a workflow. These values are generated as the output of steps, and can be used as input for subsequent steps.

## Workflow versions

When you create a workflow, you can save it as a draft or turn it on. After you make the workflow live, you can create additional versions of the workflow, and save, compare, and restore them. Having multiple versions of a workflow can be useful in the following scenarios:

  * You want to test a new version of the workflow without disrupting the existing version.
  * You want to revert to an earlier version of the workflow.



For more information, see [Manage workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions).

## Known issues

The following are the known issues and limitations for workflows in this release:

  * [Natural language support](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI28)
  * [Email template display issues](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI29)
  * [Natural Language reliability](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI30)
  * [Runs tab loading failures](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI31)
  * [Connectors not showing after authorization](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI32)
  * [Execution timeouts under heavy load](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI33)
  * [Disabled actions failure](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI34)
  * [Model recommendation](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI35)
  * [Approval node formatting](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues#KI36)



## What's next

  * Learn how to [create a workflow with natural language](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language).
  * Learn how to [use workflow templates](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-agent-templates).
  * Learn how to [set up event triggers](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger).
  * Learn how to [share a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows).
  * Learn how to [manage workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
