---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language/
title: Create a workflow with natural language \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:11.665952+00:00
---

# Create a workflow with natural language  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create a workflow with natural language Stay organized with collections  Save and categorize content based on your preferences. 

You can create an agent in Workflow Builder by describing your agent's function in plain language.

Gemini Enterprise generates a workflow scaffold based on your description, including steps, conditions, and actions. You can then refine the generated workflow in the visual flow builder.

## Before you begin

Before using this feature, make sure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## Create an agent using a natural language prompt

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the sidebar, click **Agents**.
  3. Click **Create agent**.
  4. In the **Describe your agent** field, enter a description of your agent's function. For example: "Prioritize messages and draft professional replies" or "Summarize my emails from yesterday."

**Tip:** Provide enough context about the workflow's purpose, boundaries, and expected behavior. You can prompt Gemini to ask clarifying questions to refine the workflow.
  5. Click **Submit** or press **Enter**.

Gemini Enterprise generates a workflow scaffold in the flow builder. The generated workflow is a starting point. You can add, remove, or reconfigure steps to match your requirements. For more information, see [Edit an agent with natural language prompts](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows#natural-language).

  6. Click any step in the flow builder to view and edit its configuration in the configuration panel.

  7. To test your workflow, click the **Preview** tab.

  8. When the workflow is ready, click **Turn on** to make it live.

Turning on a scheduled workflow starts it on the configured schedule. Turning on an event-triggered workflow begins listening for the configured events. Note: Not all node types can be added or edited with natural language prompts. If editing with natural language is not supported for nodes in your workflow, you can continue to edit those nodes manually.




## What's next

  * Learn how to [use agent templates](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-agent-templates).
  * Learn how to [edit an agent with natural language](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows).
  * Learn how to [configure Agent node connectors and actions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
