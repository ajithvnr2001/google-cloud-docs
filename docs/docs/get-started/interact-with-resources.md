---
url: https://docs.cloud.google.com/docs/get-started/interact-with-resources/
title: Ways to interact with Google Cloud \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:50.002443+00:00
---

# Ways to interact with Google Cloud  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/interact-with-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Ways to interact with Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides a wide range of interfaces and tools to help you be more productive. Whether you prefer a point-and-click graphical interface, a cloud-hosted development environment, or an AI-assisted command-line, you can choose the path that best aligns with your workflow. Mix and match these interfaces and tools to create pipelines for development, deployment, and monitoring.

## Graphical interfaces

Use graphical interfaces for visual resource management, administrative tasks, and high-level overviews of your cloud footprint.

### Google Cloud console

If you prefer to manage your Google Cloud projects and resources through a graphical user interface, use the web-based [Google Cloud console](https://console.cloud.google.com/). It serves as your primary hub for:

  * **Resource creation and orchestration** : Deploy, scale, and monitor cloud infrastructure.
  * **Administration and governance** : Manage Identity and Access Management (IAM) (IAM) policies, configure billing accounts, and audit system activity.
  * **Data management and visualization** : Store, query, and process data across databases and analytics services.
  * **Integrated assistance** : Use AI-assisted features to ask questions about your architecture or troubleshoot errors as they appear.



To ensure proper console functionality, see [Allow access to Google Cloud console domains](https://docs.cloud.google.com/docs/get-started/required-domains).

### Google Cloud mobile app

The [Google Cloud mobile app](https://cloud.google.com/app), available on [iOS](https://itunes.apple.com/us/app/google-cloud-console/id1005120814) and [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.cloudconsole), is a mobile companion to the web-based Google Cloud console. Use it to monitor services, respond to incidents, and perform basic resource management directly from a mobile device.

**Note:** The mobile app is optimized for on-the-go monitoring, alerting, and incident triage. For complex resource provisioning or detailed administrative configuration, use the web-based Google Cloud console or developer tools.

## Development environments

Development environments offer pre-configured, contextual, and often cloud-hosted spaces to build and manage your applications.

### Cloud Shell (and Cloud Shell Editor)

[Cloud Shell](https://docs.cloud.google.com/shell/docs) provides a web-based command-line environment that includes the Google Cloud CLI and other command-line tools. Use Cloud Shell as an interactive, web-based terminal to interact with Google Cloud without installing anything locally.

Cloud Shell also comes with [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/editor-overview), a built-in code editor that lets you browse file directories, view and edit files, and maintain continued access to Cloud Shell. Cloud Shell Editor is available by default with every Cloud Shell instance and is based on [Code OSS](https://github.com/microsoft/vscode).

### Antigravity 2.0

For agent orchestration, [Antigravity 2.0](https://antigravity.google/docs/get-started) provides a GUI environment to manage parallel autonomous subagents, run scheduled tasks, and orchestrate workflows across editor, terminal, and browser.

### Cloud Workstations

[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) provides managed, customizable development environments on Google Cloud. Platform teams can use Cloud Workstations to provide developers with standardized, containerized IDEs (such as IntelliJ IDEA or VS Code). This approach helps to ensure consistent security across the organization by keeping development environments within your Virtual Private Cloud (VPC) network.

### Cloud Code

[Cloud Code](https://docs.cloud.google.com/code/docs) extends supported integrated development environments (IDEs)—including VS Code, IntelliJ IDEA, and Cloud Shell Editor—to help you build and deploy applications on Google Cloud. Use Cloud Code for cluster management for Google Kubernetes Engine, direct deployment to Cloud Run, and Gemini-powered code assistance within your IDE.

## Developer tools

Developer tools include command-line interfaces (CLIs), programmatic client libraries, and utilities that enable modern software engineering practices.

### Google Cloud SDK

The [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/overview) provides programmatic access to Google Cloud through command-line tools and client libraries:

  * **Cloud Client Libraries** : Use language-idiomatic libraries (such as Python, Go, and Java) to call Google Cloud APIs directly within your application code. For centralized client library installation and setup instructions, see [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).
  * **Google Cloud CLI** : Use the primary command-line tool to manage and configure Google Cloud resources, create scripts, and automate CI/CD pipelines. For centralized installation and setup instructions, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).



### AI-powered command-line tools

AI-powered command-line interfaces let you manage Google Cloud resources and develop applications using natural language. For example, the [Antigravity CLI](https://antigravity.google/docs/cli) is an agentic command-line tool that supports coding, code generation, research, task management, and cloud orchestration.

### MCP servers and Agents

The [Model Context Protocol (MCP)](https://docs.cloud.google.com/discover/what-is-model-context-protocol) is an open standard that acts as a bridge between AI models and your data sources or tools. Connect your AI applications (such as Antigravity IDE, VS Code, or Cursor) to remote MCP servers to gather more context, ground responses in product data, or perform specific tasks:

  * **Developer Knowledge MCP server** : Provide your AI tools with direct access to the latest Google Cloud documentation and best practices. For more information, see [Connect to the Developer Knowledge MCP server](https://developers.google.com/knowledge/mcp).
  * **Google Cloud remote MCP servers** : Enable large language models (LLMs) to use Google and Google Cloud services in your AI applications through remote MCP servers and product-specific tools. For an overview of MCP architecture and capabilities, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).
  * **Agent Registry** : Discover, reuse, and govern autonomous AI agents and MCP tools across your organization using [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) as a centralized catalog.



#### Discover remote MCP servers and Agent Skills

Google Cloud offers remote MCP servers for a growing subset of products. These remote servers run on Google infrastructure and provide HTTP endpoints for your AI applications. To discover whether remote MCP servers and agent skills exist for a given product, use the following methods:

  * **Review supported products** : To check if a Google Cloud product offers a remote MCP server, toolsets, or reference documentation, see the centralized [Supported products](https://docs.cloud.google.com/mcp/supported-products) table. This page provides the direct MCP server endpoints, MCP reference documentation, and user guides for each supported service.
  * **Discover capabilities programmatically** : Once a remote MCP server is configured for your project or registered in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview), AI applications can programmatically discover the server's capabilities—such as available tools, prompts, and data resources—using standard MCP discovery methods (for example, `tools/list`, `prompts/list`, and `resources/list`) or by querying the Agent Registry API.
  * **Explore the[Google Agent Skills](https://github.com/google/skills) repository on GitHub**: This repository contains Agent Skills for Google products and technologies, including Google Cloud.



### Infrastructure as code (IaC) tools

For teams practicing DevOps, Google Cloud supports industry-standard [infrastructure as code](https://docs.cloud.google.com/docs/iac) (IaC) tools—such as Terraform, Pulumi, and Config Connector—to manage infrastructure through declarative configuration files.

Using IaC lets you store your infrastructure definitions in source control, enabling repeatable deployments, automated testing, and audit logging as part of your change management process.

## Integrated AI assistance

Google Cloud also includes direct AI integration into developer workflows for contextual knowledge and assistance.

### Gemini for Google Cloud (web and mobile)

Gemini for Google Cloud offers generative AI-powered assistance to Google Cloud users, including developers and data scientists. Gemini for Google Cloud is embedded in many Google Cloud products and provides an integrated assistance experience using the context of your specific project:

  * **In the Google Cloud console** : Use the integrated Gemini Cloud Assist sidebar to ask natural language questions about your environment (for example, "Why is my GKE cluster showing a high error rate?") or to generate complex BigQuery SQL from a prompt.
  * **In the Google Cloud mobile app** : Use voice and chat interfaces to monitor incidents and get AI-driven troubleshooting summaries while away from your desk.
  * **In development environments** : Use **Gemini Code Assist** in your IDE to write, refactor, and document application code.
  * **For infrastructure lifecycle management** : Use **Gemini Cloud Assist** to design, deploy, and optimize your cloud resources.



To explore more of what Gemini for Google Cloud offers, see [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
