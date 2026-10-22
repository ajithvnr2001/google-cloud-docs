---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings/
title: Configure AI developer tools settings \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:42.661985+00:00
---

# Configure AI developer tools settings  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure AI developer tools settings Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

Use the AI developer tools settings page in Gemini Enterprise to configure developer tools, enforce security and compliance controls, turn Google Antigravity features on or off, and manage model availability for your organization.

## Before you begin

Make sure you have the following:

  * **Invoiced Cloud Billing account** : To use AI developer tools, your project must have Cloud Billing enabled. AI developer tools are available for invoiced accounts only. For more information, see [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

  * **Supported editions** : To access AI developer tools, users must have a subscription to the Gemini Enterprise Standard, Plus, Standard Emerging Market, or Pay-as-you-go edition.

**Note:** Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.
  * **Supported regions** : For more information about regional availability and feature limitations, see [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

  * **Required roles** : You must have the **Gemini Enterprise Admin** (`roles/discoveryengine.agentspaceAdmin`) role to configure AI developer tools settings.

**Note** : The Gemini Enterprise Admin role doesn't grant permissions to access AI developer tools. Administrators must explicitly grant users the Gemini Enterprise User role, even if they already have the Gemini Enterprise Admin role. 

  * **Required APIs** : Your project must have the following APIs enabled:

    * **Discovery Engine API** (`discoveryengine.googleapis.com`): Provides core platform services, security and compliance controls, and settings management for Gemini Enterprise.
    * **Business AI Code API** (`businessaicode.googleapis.com`): Provides AI-powered code generation for Antigravity in Gemini Enterprise. You must enable this API on your project to let authorized principals reach the service from your project.

**Note:** Enabling the API is required, but it doesn't automatically grant user access on its own. Users still need both an appropriate IAM role and a Gemini Enterprise license to use the service.

When you turn on the **AI developer tools** toggle in the Google Cloud console, the system checks your project configuration and automatically enables these required APIs if you haven't already enabled them.




## Turn on AI developer tools

The availability of AI developer tools depends on your Gemini Enterprise subscription type:

  * **New Standard, Plus, or Pay-as-you-go subscriptions** : AI developer tools is enabled by default in the location where you purchased the subscription if it is supported for that location or region.

  * **Existing subscriptions** : An administrator must manually enable AI developer tools in the Google Cloud console for each location to activate the tools for licensed users.




To manually enable AI developer tools for an existing Gemini Enterprise subscription, follow these steps:

  1. In the Google Cloud console, go to **Gemini Enterprise**.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Settings** , and select the **AI developer tools** tab.

  3. Turn on the **AI developer tools** toggle.

  4. Configure the settings in the **Security**, **Compliance**, **Features**, and **Model availability** sections.




## Configure security settings

As an administrator, you can prevent unauthorized data exposure across developer interfaces. Use the settings in this section to restrict access to external sources and manage automated execution permissions. For example, you can enforce mandatory security policies to prevent users from overriding safety rules, and require approval before AI agents run terminal commands or select links.

### Manage security policies

You can configure security policies to control how AI agents access local files outside their working folders and execute terminal commands in developer workspaces.

Setting | Description | Default status  
---|---|---  
Outside of file access policy |  Specify the agent's permission level for accessing files outside of its designated working folders. The following options are available: 

  * **Deny** : Prevents the agent from accessing files outside its working folders.
  * **Always ask** : Prompts the user for permission before the agent accesses files outside its working folders.
  * **Allow** : Permits the agent to access files outside its working folders without prompting.

| Deny  
Terminal auto-execution mode |  Enable this setting to let agents run terminal commands automatically to streamline multi-step workflows. The following options are available: 

  * **Require review** : Prompts the user for approval before running any terminal command.
  * **Proceed in sandbox** : Automatically runs commands in a secure, isolated environment.
  * **Always proceed** : Automatically runs commands in the current environment without prompting.

| Always proceed  
Sandbox mode |  Enable this setting to restrict agent tools to a secure, isolated local sandbox.  | Disabled  
  
### Manage external web access

If your security policy requires controlling agent access to external websites to prevent data exfiltration, these settings let you limit browser access or restrict it to a list of allowed URLs.

Setting | Description | Default status  
---|---|---  
Browser access |  Enable this setting to control external web access. This prevents data exfiltration and defines organizational boundaries.  | Disabled  
Allowed URLs |  Specify a list of allowed URLs that the agent can access in the browser. When configured, the system blocks all other URLs. This setting applies only to the Antigravity browser agent. You can run the browser agent in Antigravity by typing the `/browser` command in the chat field. | None. By default, no URLs are blocked.  
Browser JavaScript auto-execution mode |  Enable this setting to let agents run JavaScript to support advanced web-based coding and testing tasks. The following options are available: 

  * **Disabled** : Prevents the agent from running JavaScript.
  * **Request review** : Prompts the user for approval before the agent runs JavaScript.
  * **Allowed** : Permits the agent to run JavaScript automatically.

| Disabled  
  
### Manage Model Context Protocol (MCP)

You can configure access to Model Context Protocol (MCP) servers, which lets AI agents securely access additional data sources and tools.

Setting | Description | Default status  
---|---|---  
MCP servers |  Enable this setting to manage access to Model Context Protocol (MCP) servers to securely extend the AI's data context.  MCP is required to use IDEs that support the Agent Client Protocol (ACP), such as Android Studio and JetBrains IDEs. In these environments, administrator controls operate on a best-effort basis because the IDEs can inject their own MCP tools that aren't subject to enforcement.  | Disabled  
Allowed server configuration |  This setting lets administrators define specific server configurations for MCP server access. Administrators define the allowlist as a JSON object with configurations for local and remote MCP servers. The UI provides real-time validation for the following fields: 

  * **Local MCP servers (`local_servers`)**: 
    * `id` (string): The unique identifier of the MCP server. 
    * `command` (string, optional): The command to run the local MCP server. If specified, this overrides the user's local configuration. 
    * `args` (array of strings, optional): The arguments passed to the command. If specified, these override the user's local configuration. 
  * **Remote MCP servers (`remote_servers`)**: 
    * `id` (string): The unique identifier of the MCP server. 
    * `url` (string, optional): The endpoint URL of the remote MCP server. Required for custom remote servers and optional for pre-configured remote servers. 



#### Example configuration
    
    
    {
      "mcpServers": {
        "local_servers": [
          {
            "id": "gopls-mcp-server",
            "command": "go",
            "args": [
              "run",
              "golang.org/x/tools/gopls@latest",
              "mcp"
            ]
          }
        ],
        "remote_servers": [
          {
            "id": "bigquery"
          },
          {
            "id": "custom-remote-server",
            "url": "https://mcp.example.com/mcp"
          }
        ]
      }
    }

| Not configured  
  
## Configure compliance settings

If your organization operates in a regulated industry or has specific internal policies, you might need to maintain audit logs of AI interactions for compliance. This section's settings let you configure logging and data retention policies to meet your legal and regulatory requirements.

Setting | Description | Default status  
---|---|---  
Prompts and responses logging |  Enable this setting to record interactions between developers and the AI to compute usage metrics and maintain an audit trail for security reviews. The system stores logs securely within your organization's project, and Google never accesses the logs for model training or human review.  | Disabled  
Metadata logging |  Enable this setting to record product metadata to help you track usage and analytics across your organization, including [third-party model token consumption](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage). The system stores logs securely within your organization's project, and Google never accesses the logs for model training or human review.  | Disabled  
  
## Configure feature settings

Some Antigravity features offer advanced multi-agent capabilities to help developers tackle complex tasks. Because these features can increase token usage and costs, use the settings in this section to control access for users in your organization. To access enabled features, users must use Antigravity app version 2.18.0 or later, or Antigravity CLI version 1.2.10 or later.

To turn a feature on or off, follow these steps:

  1. In the Google Cloud console, go to **Gemini Enterprise**.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Settings** and select the **AI developer tools** tab.

  3. In the **Features** section, click **Edit**.

  4. For each feature, turn the toggle on or off.

Setting | Description | Default status  
---|---|---  
`/boost` command |  Enable this setting to let users run a tiered multi-agent hierarchy to solve complex algorithmic challenges and deep debugging tasks. For more information, see [Boost deep reasoning](https://antigravity.google/docs/boost).  | Enabled  
`/teamwork-preview` command |  Enable this setting to let users deploy a coordinated framework of autonomous subagents to execute large-scale, long-horizon projects (Preview). For more information, see [Teamwork agent teams](https://antigravity.google/docs/teamwork).  | Enabled  
  5. Click **Save**.




## Configure model availability

Use the settings in this section to authorize specific AI models and manage access levels. This ensures developers only use AI models that comply with your organization's safety and usage policies. For example, you can give developers access to preview models for experiments, or restrict tools to use only authorized models.

### Key considerations before configuring models

Before you configure models, consider the following:

  * **Policy alignment:** Enabling a model in Gemini Enterprise doesn't override Gemini Enterprise Agent Platform organization policies. To prevent pay-as-you-go requests that exceed your standard quota from failing, ensure that the allowed models match across both platforms.

  * **Data residency:** Preview models and the Gemini 3 Pro Image model are available only in the `global` region. Therefore, they don't support data residency (DRZ) or machine learning (ML) regional processing commitments in the US or EU multi-regions.

  * **Third-party model inference and data handling:** Third-party models are available only after an administrator enables them and accepts the provider's terms. When a developer selects an enabled third-party model, Gemini Enterprise sends the prompt and the code context needed for that request to the model, with the same processing and protections as Gemini models. Prompts and responses aren't used to train models. Third-party model inference is available in the `global`, `us`, and `eu` locations. In-country regions aren't supported. To see the list of countries and regions that can access the model, see Anthropic's [Supported countries and regions](https://www.anthropic.com/supported-countries). For more information on data residency, see [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

  * **Hybrid execution and billing disclosures:** Gemini models draw from your organization's pooled edition seat credits, while administrator-enabled third-party models are billed as pay-as-you-go usage on your Cloud Billing account. When a developer selects an enabled third-party model (such as **Anthropic Claude Opus 5.5** or **Anthropic Claude Sonnet 5.5**) for primary reasoning, planning, tool orchestration, and code generation tasks, Antigravity continues to use lightweight Gemini models in the background for client-side coordination—such as context management and summaries—and Gemini 3 Pro Image for image generation. Using these models can incur charges. For more information, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages) and [Track third-party model token usage](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage).




### Configure authorized models

You can configure authorized models to control which AI models are available to your AI developer tools.

The **Antigravity authorized models** setting operates as an allowlist:

  * **Default selection (empty)** : When the field is empty, all supported Gemini models are permitted. Newly released Google models become available automatically to licensed users.
  * **Custom model list** : When you select one or more specific models, only the selected models are permitted. Unselected models and newly released models aren't available to developers until an administrator manually selects them.



To configure authorized models:

  1. In the Google Cloud console, go to **Gemini Enterprise**.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Settings** , and then select the **AI developer tools** tab.

  3. In the **Model availability** section, click **Edit**.

  4. In the **Antigravity authorized models** field, select the models that you want to permit. To permit all supported models, leave the field empty.

  5. Click **Save**.


Setting | Description | Default status  
---|---|---  
Antigravity authorized models |  Specify which AI models the Antigravity tool is authorized to use within the project. Leave the field empty to allow all supported Gemini models. If you specify a custom list of models, the setting acts as an allowlist, and newly released or unselected models must be manually added to become available. In addition to Gemini models made by Google, administrators can opt in to enable third-party models, including **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5**. For information about each model's capabilities, limitations, and safety evaluations, see the model cards for [Anthropic Claude Opus 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/opus-5-5) and [Anthropic Claude Sonnet 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/sonnet-5-5).  |  Empty (all Gemini models permitted). Third-party models are turned off by default and require administrator consent.   
  
### Supported models

AI developer tools (**Antigravity app** , the **Antigravity CLI** , and **Antigravity for IDEs**) support the following Gemini models and partner models. A _licensed user_ is a developer assigned an active Gemini Enterprise seat license (Standard, Plus, or Pay-as-you-go). For more information, see [Manage licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses).

Model display name | Provider | Availability in Gemini Enterprise  
---|---|---  
**Gemini 4 Argon** | Google |  Enabled by default for licensed users when default model selection is active (empty list). If a custom model list is configured, the model must be manually selected.   
**Gemini 3.8 Flash** | Google |  Enabled by default for licensed users when default model selection is active. If a custom model list is configured, the model must be manually selected.   
**Gemini 3.7 Flash** | Google |  Enabled by default for licensed users when default model selection is active. If a custom model list is configured, the model must be manually selected.   
**Gemini 3.6 Flash** | Google |  Enabled by default for licensed users when default model selection is active. If a custom model list is configured, the model must be manually selected.   
**Gemini 3.1 Pro (Preview)** | Google |  Enabled by default for licensed users when default model selection is active. If a custom model list is configured, the model must be manually selected.   
**Anthropic Claude Opus 5.5** | Anthropic |  Turned off by default. Requires administrator opt-in (see Enable or turn off third-party models).   
**Anthropic Claude Sonnet 5.5** | Anthropic |  Turned off by default. Requires administrator opt-in (see Enable or turn off third-party models).   
  
For information about quotas and pooled edition credits, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages) and [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages). For third-party model pricing, see the Cloud Billing SKUs for [Anthropic Claude Opus 5.5](https://cloud.google.com/skus?filter=opus&currency=USD&e=48754805) and [Anthropic Claude Sonnet 5.5](https://cloud.google.com/skus?filter=sonnet&currency=USD&e=48754805).

### Thinking level for third-party models

Developers can use **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5** at a thinking level of Low, Medium, High, or Max. Each level appears as a separate entry in the model picker, for example **Anthropic Claude Opus 5.5 (High)**. Medium is the default. When you enable a third-party model, all of its thinking levels are available to developers. You can't restrict individual thinking levels.

### Enable or turn off third-party models

Third-party models are billed as pay-as-you-go usage and require overages. Before you enable a third-party model, [turn on overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages). If overages are turned off later, developers can't use third-party models until overages are turned back on. To control costs, you can [set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit) for your project. The limit applies to all models, including third-party models.

To enable or manage third-party models (such as **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5**) in the Google Cloud console:

  1. In the Google Cloud console, go to **Gemini Enterprise**.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Settings** , and then select the **AI developer tools** tab.

  3. In the **Antigravity authorized models** setting, turn on the toggle for the third-party model that you want to enable.

  4. In the embedded Terms of Service dialog that appears, review and accept the third-party terms.




If you turn off a third-party model, developers lose access to it shortly afterwards.

If the model provider restricts access to a third-party model for your organization, developers can't use that model. To resolve the issue, contact [Google Cloud Support](https://docs.cloud.google.com/support/docs).

For developer instructions on signing in to Antigravity and selecting models, see the [Antigravity enterprise documentation](https://antigravity.google/docs/enterprise/).

### Security considerations for third-party models

AI models, including third-party models, can follow instructions hidden in content they process, such as files, web pages, or tool output. This is known as _prompt injection_. Antigravity provides the following protections when developers use third-party models:

  * **Administrator opt-in:** Third-party models are off by default. Developers can use a third-party model only after an administrator enables it.
  * **Provider safety protections:** Third-party models include the provider's built-in safety protections. For more information, see [Claude safety](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/safety).
  * **Your security policies:** The security policies and external web access settings that you configure apply to agents regardless of the model that a developer selects.



**Best practices**

  * Enable only the third-party models that your developers need.
  * Set **Terminal auto-execution mode** to **Require review** or **Proceed in sandbox** , so that developers approve commands before they run.
  * Keep **Outside of file access policy** set to **Deny**.
  * Turn on **Browser access** and limit agents to a list of **Allowed URLs**.
  * Turn on **Sandbox mode** for projects that work with untrusted code, dependencies, or web content.
  * Encourage developers to review the commands and code changes that agents propose before approving them.
  * [Set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit) for your project.



## What's next

  * [Track third-party model token usage](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage)
  * [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics)
  * [Create custom roles for AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles)
  * [Turn off AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-turn-off)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
