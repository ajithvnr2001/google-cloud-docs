---
url: https://docs.cloud.google.com/looker/docs/ai-assisted-development-vscode/
title: AI-assisted development (vibe coding) with Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:43:14.926701+00:00
---

# AI-assisted development (vibe coding) with Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ai-assisted-development-vscode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  AI-assisted development (vibe coding) with Looker Stay organized with collections  Save and categorize content based on your preferences. 

The Looker extension for VS Code unlocks AI-assisted LookML development, often referred to as "vibe coding." This approach allows developers to use natural language to generate, edit, and validate LookML code by using a third-party AI agent and prebuilt skills in a local desktop IDE like Visual Studio Code (VS Code) or Cursor.

This guide explains the agentic workflow architecture and provides instructions for connecting and prompting your AI agent.

## How vibe coding works with Looker

The AI-assisted development workflow relies on a few key components:

  * **Your IDE and AI Agent** : A local editor (for example, VS Code, Claude Code, or Cursor) that is a fork of VS Code with an integrated AI copilot or agent (for example, Gemini CLI or Claude).
  * [**The Looker extension for VS Code**](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension): Provides the local environment for LookML development in VS Code, including syntax highlighting, bidirectional file synchronization with your Looker instance, autocomplete, and integrated validation.
  * [**Looker-managed MCP server**](https://docs.cloud.google.com/looker/docs/mcp): Configured on your Looker instance by a Looker admin and automatically connected by the Looker extension for VS Code. Uses the open standard [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to connect your AI agents, IDEs, and applications directly to your enterprise database and LookML models. You can also connect to a custom or self-hosted MCP server, such as the [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox).
  * **Prebuilt skill files** : Prebuilt skill files provide the AI agent with specific context, coding standards, and project-specific instructions for writing LookML. The Looker extension for VS Code automatically installs and updates skill files. You can also run the **Looker: Install Skills in this Workspace** or **Looker: Install Skills Globally** Command Palette commands in your IDE to populate or update skill files.



By combining these components, your AI agent can perform the following tasks:

  * read your local LookML files
  * inspect your database schema by using the MCP server
  * propose and apply changes to your code locally
  * run LookML validation to self-correct before you commit



## Before you begin

Before you can use an AI agent to develop LookML, you must meet the following requirements:

  1. **Configure the Looker extension** : You must have the [Looker extension for VS Code installed and configured](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension), and you must be signed in with OAuth or API keys.
  2. **Configure your MCP client** : You must connect your IDE's AI agent to the Looker-managed MCP server. See the [Use the MCP Toolbox for Databases](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox) documentation page for example instructions on configuring VS Code or other supported clients. See your client's documentation for more details.
  3. **Populate your LookML project** : [Clone your LookML repository](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension#clone-your-lookml-project) or start with an empty workspace and then [populate the workspace with your LookML project](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension#populate-your-lookml-project).
  4. **Confirm Looker permissions** : Ensure that you have at least the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) Looker permission for whatever model you want to edit.



## Prompt your AI agent

Once your AI agent is connected to the Looker MCP server and your LookML project is open, you can begin using natural language to write and modify code. The skills in your workspace help guide the agent, but providing clear and specific prompts yields the best results.

Following are some examples of how to prompt your AI agent for common LookML development tasks.

### Generate a new LookML model from a schema

You can ask the agent to inspect a specific database connection and generate a foundational LookML view.

**Prompt Example:**

> "Use the MCP tools to connect to the `ecommerce_db` connection. Inspect the schema for the `users` and `orders` tables. Generate the LookML for a `users.view.lkml` and an `orders.view.lkml` file. Include primary keys, standard dimensions for all columns, and basic measures like a count of records. Then, generate an `ecommerce.model.lkml` file that explores `orders` and joins `users` on `user_id`."

### Refactor existing LookML

You can instruct the agent to update multiple files to conform to new standards or to add new functionality that's based on existing patterns.

**Prompt Example:**

> "Review the `products.view.lkml` file. Find all dimensions of type `number` that represent a price or cost. For each of these dimensions, generate a corresponding `sum` measure and an `average` measure. Add a description to each new measure explaining what it calculates. Ensure that the new code matches the style recommended by the prebuilt skills in the workspace."

### Troubleshoot and validate LookML

The AI agent can help you identify and resolve LookML errors. While the agent can use the MCP server's validation tools proactively, you can also ask for help with specific errors that are surfaced by the Looker IDE validator.

**Prompt Example:**

> "I just ran the LookML validator and received an error: 'Inaccessible view: users. The view users cannot be reached.' I am trying to join the `users` view to the `orders` explore in the `ecommerce.model.lkml` file. Please review the model file and the `users.view.lkml` file, identify the cause of the error, and propose a fix."

## Manage changes

When the AI agent modifies your local LookML files, follow these steps:

  1. **Review the Diff** : Carefully review the changes proposed by the AI agent in your IDE's source control or diff viewer.
  2. **Validate Locally** : Always run the **Looker: Validate LookML** command from the IDE Command Palette to ensure that the generated code compiles correctly and doesn't introduce errors on the Looker server.
  3. **Sync and Deploy** : When you save a file, the extension automatically syncs it to your development branch on the Looker server. Use standard Git commands to [commit and deploy](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) your changes when they are ready.



## What's next

  * [Managing LookML files and Git with the Looker extension for VS Code](https://docs.cloud.google.com/looker/docs/manage-lookml-files-git-vscode)
  * [LookML reference overview](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
