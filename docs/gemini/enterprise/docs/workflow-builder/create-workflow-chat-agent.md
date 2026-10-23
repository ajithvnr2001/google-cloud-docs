---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflow-chat-agent/
title: Create a workflow chat agent \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:47.780470+00:00
---

# Create a workflow chat agent  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflow-chat-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Create a workflow chat agent Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and configure a workflow chat agent in Workflow Builder.

## Overview

A _workflow chat agent_ functions as a powerful, multi-node workflow orchestrator to manage conversational interactions.

While a [non-workflow chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents) is restricted to a single root node with fixed attributes, a workflow chat agent lets you attach **published workflows** and **remote Application Development Kit (ADK) agents** as sub-agents. The root chat agent acts as the coordinator, dispatching user queries to the appropriate sub-agent and returning responses.

Key benefits of workflow chat agents include:

  * **Advanced Orchestration** : Nest multiple published workflow or remote ADK agents as sub-nodes to handle complex user tasks.
  * **Version History Support** : Workflow chat agents support versioning. You can save, compare, view history, and restore previous agent versions to track modifications.



## Before you begin

Before creating a workflow chat agent, complete the following prerequisites:

  * Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure you have a web app with the necessary data sources connected. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  * Verify that any workflows or remote ADK agents you want to attach as sub-agents are already **published** in your workspace repository, making them visible to the root orchestrator.



## Create a workflow chat agent

### App

To manually create a workflow chat agent, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click **\+ New agent > Workflows**.
  3. In the agent creation pane, click **Build manually**.
  4. Select the **Chat** trigger chip.

The Workflow Builder editor opens, directing you to the workflow chat agent configuration options.

  5. In the configuration pane, you can _optionally_ configure the following for your agent:

     * **Suggested prompts** : Enter a prompt that describes your agent's purpose and intended behavior.

**Tip:** See [Best practices for writing prompts to create an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent#best-practice-prompt).
     * **Knowledge** : Click add_circle **Add files** to upload any additional reference materials for your agent to use.

     * **Tools & integrations**: Open the **Tools & integrations** dialog to select the Google tools and connectors allowed for this conversational interface.

     * **Sub agents** : Browse or search to select the published workflows or remote ADK agents that you want your workflow to orchestrate. These agents will be configured as run-time sub-nodes beneath the root agent.

     * **More** : Select the model used by your workflow chat agent.

  6. Test your agent configuration:

     * Click the **Preview** tab.
     * In the chat interface, submit a test message (for example, `hello`) to evaluate your agent's responses.
  7. Save or manage agent versions (Optional):

     1. Click the drop-down arrow next to **Publish** and select **Save version**.
     2. To review or restore a version, click the drop-down arrow next to **Publish** , click **View version history** , and select the version to restore.
  8. Click **Publish** to finalize and publish your workflow chat agent.

Once published, the workflow chat agent appears in your **Agents gallery** , ready to handle incoming user requests.




## Feature limitations

Workflow chat agents have the following limitations:

  * The configuration details of an attached sub-agent are not visible inside the root chat agent configuration pane. To inspect or edit a sub-agent's workflow (such as an approval step), open the workflow individually from the **Agents gallery** page.
  * The **Schedule chat agent run** feature is not supported for workflow chat agents. Scheduling options only apply to non-workflow agents.
  * The **Share a chat agent** feature is not supported for workflow chat agents in this release.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
