---
url: https://docs.cloud.google.com/docs/get-started/developer-environment/
title: Set up a local development environment \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:25.026790+00:00
---

# Set up a local development environment  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/developer-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Set up a local development environment Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to configure a local development environment for Google Cloud. This document covers the core tools required to build, test, and run applications with Google Cloud services:

  * **gcloud CLI** : Manage cloud resources, configure projects, and set up local Application Default Credentials (ADC).
  * **Cloud Client Libraries** : Access Google Cloud APIs programmatically using idiomatic libraries in your preferred programming language.



This document also shows how to install the `google-cloud-developer` plugin to get help with Google Cloud tasks and coding in a number of different agents.

For an overview of other tools and interfaces across Google Cloud, see [Ways to interact with Google Cloud](https://docs.cloud.google.com/docs/get-started/interact-with-resources).

## Before you begin

Ask your organization administrator to complete the following prerequisites:

  * **Provision your user identity** : Assign a Cloud Identity or Google Workspace account.
  * **Grant project access and IAM roles** : Assign the required Identity and Access Management (IAM) roles for your project.
  * **Enable billing** : Verify Cloud Billing is enabled on your project.



For organization-wide setup, see the [Google Cloud Setup guided flow](https://docs.cloud.google.com/docs/enterprise/cloud-setup).

## Set up the gcloud CLI and authentication

Configure gcloud CLI (`gcloud`) to manage resources and authenticate your local environment:

  1. [Install gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) on your local workstation.
  2. Run `gcloud init` in your terminal to sign in and select your default project.
  3. Run `gcloud auth application-default login` to configure Application Default Credentials (ADC). ADC enables local client libraries to authenticate automatically against your project.

**Note:** If you need a zero-install browser terminal, you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/features) as an alternative.

## Install Cloud Client Libraries

To access Google Cloud services programmatically from your application code:

  1. [Enable required Cloud APIs](https://docs.cloud.google.com/apis/docs/getting-started) for your project.
  2. Install [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) for your programming language (such as Java, Python, or Go). Your code authenticates automatically using ADC.



## Install the `google-cloud-developer` plugin

If you use an agent such as Claude Code CLI, Antigravity CLI, or Codex CLI to assist you in your development work, you can install the `google-cloud-developer` plugin to get help with Google Cloud tasks and coding. This plugin includes:

  * Skills to help with account creation, billing setup, project management, and authentication to Google Cloud services and APIs.
  * The `finding-google-skills` skill, which locates and runs the right Google product skill on demand, thus avoiding the need to preload Google skills.
  * The [Developer Knowledge](https://developers.google.com/knowledge/mcp) remote MCP server, which provides the ability to search Google's official developer documentation and retrieve information for Google's products such as Google Cloud, Firebase, Android, Maps, and more.



Install the `google-cloud-developer` plugin using the following instructions based on your agent.

### Antigravity CLI

  1. Install the plugin by specifying its location in the [Google Agent Skills](https://g.dev/cloud/agent-plugins) repository:
         
         agy plugin install https://github.com/google/skills/plugins/cloud/google-cloud-developer
         

  2. Enable the Developer Knowledge API in your Google Cloud project by using the gcloud CLI:
         
         gcloud services enable developerknowledge.googleapis.com --project=YOUR_PROJECT_ID
         




### Claude Code CLI

  1. Add the Google plugins marketplace and then install the plugin:
         
         claude plugin marketplace add google/skills
         claude plugin install google-cloud-developer@google-plugins
         

  2. Enable the Developer Knowledge API in your Google Cloud project by using the gcloud CLI:
         
         gcloud services enable developerknowledge.googleapis.com --project=YOUR_PROJECT_ID
         

  3. Create an API key for the Developer Knowledge API by following the instructions [Create and secure the API key](https://developers.google.com/knowledge/quickstart#create-secure-key). Save the key you create in a secure location.

  4. Export the API key to your environment before starting Claude Code CLI:
         
         export DEVELOPERKNOWLEDGE_API_KEY=YOUR_API_KEY
         

**Note:** The `DEVELOPERKNOWLEDGE_API_KEY` environment variable needs to be set in the environment before you start Claude Code CLI. You might consider adding this export command to your shell's startup script (such as `.bashrc`, `.zshrc`) for convenience.



### Codex CLI

  1. Add the Google plugins marketplace and then install the plugin:
         
         codex plugin marketplace add google/skills
         codex plugin add google-cloud-developer@google-plugins
         

  2. Enable the Developer Knowledge API in your Google Cloud project by using the gcloud CLI:
         
         gcloud services enable developerknowledge.googleapis.com --project=YOUR_PROJECT_ID
         

  3. Create an API key for the Developer Knowledge API by following the instructions [Create and secure the API key](https://developers.google.com/knowledge/quickstart#create-secure-key). Save the key you create in a secure location.

  4. Enable authenticated access to the Developer Knowledge MCP server by updating `~/.codex/config.toml` (or your project's `.codex/config.toml`) to include the following lines:
         
         [mcp_servers.developer-knowledge]
           url = "https://developerknowledge.googleapis.com/mcp"
           env_http_headers = { "X-Goog-Api-Key" = "DEVELOPERKNOWLEDGE_API_KEY" }
         

  5. Export the API key to your environment before starting Codex:
         
         export DEVELOPERKNOWLEDGE_API_KEY=YOUR_API_KEY
         

**Note:** The `DEVELOPERKNOWLEDGE_API_KEY` environment variable needs to be set in the environment before you start Codex. You might consider adding this export command to your shell's startup script (such as `.bashrc`, `.zshrc`) for convenience.**Note:** After performing this configuration update, a status of _not logged in_ for the Developer Knowledge MCP server is expected and doesn't block access to the server.



## Alternative tools and environments

If your workflow requires specific development environments or infrastructure tooling, consider the following:

  * **IDEs and extensions** : Develop in [VS Code](https://docs.cloud.google.com/code/docs/vscode) or [supported JetBrains IDEs](https://docs.cloud.google.com/code/docs/intellij) with Cloud Code support.
  * **Cloud workspaces** : Use containerized, managed cloud environments with [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview).



## What's next

  * Learn about [Authentication in Google Cloud](https://docs.cloud.google.com/docs/get-started/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
