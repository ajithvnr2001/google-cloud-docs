---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues/
title: Known issues and limitations \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:01.803950+00:00
---

# Known issues and limitations  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Known issues and limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the known issues and limitations for Workflow Builder in this release.

## Known issues

This section lists known issues in Workflow Builder.

### Natural language support

Status  | **OPEN**  
---|---  
Issue  | The conversational designer does not support adding the following capabilities using natural language prompts:

  * Human-in-the-loop (HITL) approvals
  * Event triggers
  * Data filtering

To create workflows with these capabilities, you can use the UI to add these nodes to your workflow manually.  
Workaround or recommendation  | N/A   
  
### Natural Language reliability

Status  | **OPEN**  
---|---  
Issue  | Creating a workflow from natural language may occasionally result in a workflow that cannot run.   
Workaround or recommendation  | Try generating the workflow again if the first attempt fails.   
  
### Runs tab loading failures

Status  | **OPEN**  
---|---  
Issue  | Intermittent failures may occur when loading sessions in the **Runs** tab.   
Workaround or recommendation  | If sessions fail to load, try refreshing the page.   
  
### Connectors not showing after authorization

Status  | **OPEN**  
---|---  
Issue  | A connector might not show up in the UI or work using natural language immediately after being authorized.   
Workaround or recommendation  | Perform a hard reload of your browser:

  * Windows/Linux: `Ctrl + Shift + R` or `Ctrl + F5`
  * macOS: `Command + Shift + R`

  
  
### Execution timeouts under heavy load

Status  | **OPEN**  
---|---  
Issue  | Workflows may experience "Failed to build node" errors or timeouts during execution when the system is under heavy load.   
Workaround or recommendation  | Ensure only necessary connectors are enabled for the agent to reduce load.   
  
### Disabled actions failure

Status  | **OPEN**  
---|---  
Issue  | Attempting to use actions (like sending an email) that are not enabled in your environment results in execution failure.   
Workaround or recommendation  | Ensure required actions are enabled before running the workflow.   
  
### Disable actions failure

Status  | **OPEN**  
---|---  
Issue  | Workflow failed to prompt the user to enable necessary actions for workflow creation.   
Workaround or recommendation  | N/A   
  
### Model recommendation

Status  | **OPEN**  
---|---  
Issue  | For optimal performance and best results, we recommend using the 3.1 Pro model.   
Workaround or recommendation  | N/A   
  
### Approval node formatting

Status  | **OPEN**  
---|---  
Issue  | HTML and Markdown formatting in human-in-the-loop (HITL) approval steps may display as raw text when added as a sub-step.   
Workaround or recommendation  | N/A   
  
### Event-triggered workflows failing with RESOURCE_EXHAUSTED

Status  | **OPEN**  
---|---  
Issue  | Event-triggered workflows failing with a `RESOURCE_EXHAUSTED` error (generally seen when a daily quota is breached) are not retried automatically.   
Workaround or recommendation  | N/A   
  
### Connector search records returned by connector type

Status  | **OPEN**  
---|---  
Issue  | Connector search tools return a specific number of records depending on the connector type, such as Jira or Outlook.   
Workaround or recommendation  | N/A   
  
### OAuth re-run required for A2A and ADK agents

Status  | **OPEN**  
---|---  
Issue  | If you add an A2A or ADK agent that requires user OAuth for authentication, continuing the same run after the OAuth flow is complete is not supported.   
Workaround or recommendation  | The user must first authenticate, and then start a new run of the workflow.   
  
## Limitations

  * The Gmail subject field does not support non-English characters.
  * Connector actions that list entities (for example, retrieving emails) might not return all items when the total number is very large. This is because the connector's API is limited to fetching a finite number of pages, with a default page size of 20. Items beyond the capacity of the maximum pages fetched are not retrieved.



### Add an existing agent step

The [Add an existing agent step](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/add-existing-agents#add-existing-agent) feature has the following limitations:

  * **Clarifying questions support** : Existing agent steps support asking clarifying questions during workflow execution when using native protocol signals (such as A2A `input-required` or ADK `RequestInput`). Other workflow step types do not use prompt-based clarifying questions.
  * **Supported agent types** : Only agents created with the [Agent Development Kit (ADK)](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent) and [Agent-to-Agent (A2A) registered agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent) are supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
