---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps/
title: Use human-in-the-loop steps \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:50.915047+00:00
---

# Use human-in-the-loop steps  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Use human-in-the-loop steps Stay organized with collections  Save and categorize content based on your preferences. 

You can add human-in-the-loop steps to your workflow to pause execution and require human input before proceeding.

Workflow Builder provides two step types: requesting information from a user and requiring approval before the agent takes further action.

## Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## Human-in-the-loop step types

Workflow Builder provides two human-in-the-loop step types:

  * **Request info** : Pause the workflow and ask the user one or more questions. Use this step when the workflow needs additional information or clarification to proceed.
  * **Approval** : Pause the workflow and present outputs for human review and approval. Use this step when the workflow produces outputs that require human sign-off before downstream steps execute.



## Add a request info step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow or create a new workflow.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Human in the loop** to expand the section.
  5. Click **Request info**.
  6. The request info step appears in your workflow, and its configuration panel opens on the right.
  7. In the **Message** field, enter the message to display to the user when the workflow pauses. This message provides context about why input is needed.
  8. In the **Info to request** section, configure the questions to ask the user. For each question, do the following: 
     1. Enter the question text in the question field.
     2. Select the input type from the list (for example, **Short answer**).
  9. To add more questions, click **Add question**.
  10. To configure additional settings, click **More**.



## Add an approval step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow or create a new workflow.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Human in the loop** to expand the section.
  5. Click **Approval**.
  6. The approval step appears in your workflow, and its configuration panel opens on the right.
  7. Configure the approval settings, including what information is presented to the reviewer.



When a workflow run reaches a human-in-the-loop step, the run pauses and appears with a **Needs Review** status in the **Runs** tab. For more information, see [View workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).

## What's next

  * Learn how to [view workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).
  * Learn how to [use flow control steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps).
  * Learn how to [manage workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
