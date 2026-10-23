---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/connect-mcp-servers/
title: Connect MCP servers \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:05.606803+00:00
---

# Connect MCP servers  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/connect-mcp-servers/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Connect MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

You can connect Model Context Protocol (MCP) servers to your agent workflow to extend your agent's capabilities with custom tools, resources, and APIs.

Workflow Builder provides dedicated MCP step types that let you call tools, list resources, and query servers hosted on any MCP-compatible endpoint. You can also add MCP tools to Gemini agent steps so the model can invoke them dynamically during reasoning.

## Before you begin

Before using this feature, complete the following steps:

  * Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure that your Gemini Enterprise organization has access to at least one MCP-compatible server endpoint. For more information, see [Set up a custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).



## Add an MCP step to your workflow

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or create a new agent.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **MCP servers** to expand the section.
  5. Click the MCP step you want to add.
  6. The MCP step is added to your workflow, and its configuration panel opens.
  7. Configure any additional parameters required by the selected step type.
  8. (Optional) Click **Preview** to preview the workflow and the operation of the MCP step.



## Add MCP tools to a Gemini agent step

You can add MCP tools to a Gemini agent step so the model can discover and invoke them dynamically based on context. Unlike dedicated MCP steps that run deterministically in your workflow based on an event or trigger, MCP tools added to a Gemini agent step are available for the model to call as needed during its reasoning process.

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or create a new agent.
  3. In the flow builder, click the Gemini agent step you want to configure. The agent configuration panel opens.
  4. Click **Tools & Integrations** to view available tools, including any MCP connectors available in your organization.
  5. To enable access to the tool for your agent, click the **Authorize** toggle.

The Gemini agent step can discover and invoke the authorized MCP connectors at runtime, if required.




## What's next

  * Learn how to [use flow control steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps).
  * Learn how to [set up event triggers](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger).
  * Learn how to [search with filters](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/search-with-filters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
