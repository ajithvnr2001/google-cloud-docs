---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows/
title: Edit a workflow \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:51.682372+00:00
---

# Edit a workflow  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Edit a workflow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to edit an existing workflow using natural language prompts or the visual editor. You can refine your workflow's logic, add or remove steps, update instructions for Gemini agents, or adjust integrations with tools and data sources.

## Before you begin

Before using this feature, create a workflow. For information about creating a workflow, see [Create a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows).

## Edit a workflow using natural language

### App

To edit a workflow using natural language prompts, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow in the flow builder.
  3. In the prompt bar in the flow builder, click **What would you like to change?**
  4. Enter a description of the change you want to make. For example:

     * "Add a condition step that checks if the email has attachments."
     * "Change the Gemini agent step's model to Gemini-2.5-flash."
     * "Update the instructions to be more direct."
     * "Add a loop that processes each search result."
**Note:** If you select a specific node in the flow builder before entering a prompt, any changes requested are limited to that node. Edits will only be made to other parts of the workflow if the requested changes don't make sense for the node, or changes to other parts of the workflow are required to produce a valid configuration.
  5. Click **Submit** or press **Enter**.

Gemini Enterprise applies the requested changes to your workflow.

  6. Review the updated workflow. Optionally, use the **Diff** and **Undo** options to view or revert changes as needed.

  7. To preview and test your workflow, switch to the **Preview** tab and click **Start simulation**.

  8. To make your updated workflow live, click **Turn on** (or click **Update** if the workflow is already live).


**Note:** Natural language editing does not support all node types. If you request a change to an unsupported node, Gemini Enterprise provides an informative message and the node can be configured manually instead.

## Edit using the visual editor

### App

To edit a workflow using the visual editor, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents** and go to the **Your agents** section.
  3. Locate the workflow that you want to edit.
  4. Click more_vert **Actions menu** , and select **Edit**.

The workflow canvas appears with the last saved draft version of the workflow.

  5. Optional: To select another workflow version, click the **Turn on** or **Update** drop-down and select **Version history**. In the **Version history** pane, select the version that you want to modify.

  6. Click the component (trigger or step) in the canvas that you want to modify.

The configuration pane for the component opens.

  7. Update the fields for the selected component, such as changing the schedule frequency or updating instructions for a Gemini Agent node.

  8. To add new steps, click **\+ Add step** and select the required node type.

  9. To preview and test your workflow, switch to the **Preview** tab and click **Start simulation**.

  10. To make your updated workflow live, click **Turn on** (or click **Update** if the workflow is already live).




## What's next

  * Learn how to [run test simulations for your workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/simulate-workflows).
  * Learn about [workflow versions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows#versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
