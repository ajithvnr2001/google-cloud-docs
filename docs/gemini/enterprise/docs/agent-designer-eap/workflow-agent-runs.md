---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/workflow-agent-runs/
title: Workflow runs \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:18:25.547860+00:00
---

# Workflow runs  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/workflow-agent-runs/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Workflow runs Stay organized with collections  Save and categorize content based on your preferences. 

A workflow run is an instance of a workflow that is executed by a trigger. The **Runs** tab in the workflow canvas lets you monitor and manage the execution logs of your workflow. Monitoring workflow runs is helpful for tracking automated tasks, debugging failed executions, and reviewing the performance of your workflow versions.

## Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## View runs for all workflows

To view all workflow runs for your web app, do the following:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app.
  4. Click **Runs** to view all workflow runs for your web app.

The **Runs** tab displays a list of all workflow runs for your web app as shown in the following image. ![List of all workflow runs in the Runs tab](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/all-runs.png)




## View runs for a specific workflow

To view the execution logs of a workflow, do the following:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.
  3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app.
  4. Go to the **Your agents** section and click the workflow to view its execution logs.
  5. Click the **Runs** tab.

The **Runs** tab displays a list of all executions, including simulations performed in the **Preview** tab and automated runs initiated by a trigger. Selecting an individual run from the list lets you view granular details about that specific execution, including the workflow version details. ![List of workflow runs for a specific workflow in the Runs tab](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/runs.png)




## Filter runs by status

### App

In the **Runs** tab, use the filter chips at the top of the run list to filter by status. Available filters include the following:

  * **Running** : Runs that are in progress.
  * **Needs Review** : Runs that are paused at a human-in-the-loop step awaiting review.
  * **Completed** : Runs that finished successfully.
  * **Error** : Runs that encountered an error.
  * **Date** : Filter runs by date range.



To apply a filter, click a filter chip. To remove the filter, click the chip again.

## Understand the run details

The following table lists and describes the information that is displayed in the **Runs** tab.

Field | Description  
---|---  
Input/Trigger | The trigger that started the run.  
Status | The current state of the run, such as `Completed`, `Running`, or `Error`.  
Started | The date and time when the run started.  
**Note:** Runs that reach a human-in-the-loop step display a **Needs Review** status. For more information, see [Use human-in-the-loop steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps).

## What's next

  * Learn how to [use human-in-the-loop steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps).
  * Learn how to [manage workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions).
  * Learn how to [set up event triggers](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
