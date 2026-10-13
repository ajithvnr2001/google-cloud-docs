---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards/
title: Create and manage data agents for LookML dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:39.662278+00:00
---

# Create and manage data agents for LookML dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create and manage data agents for LookML dashboards Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Data agents for LookML dashboards are in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, email [conversational-analytics-feedback@google.com](https://docs.cloud.google.com/looker/docs/conversational-analytics-feedback@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



Conversational Analytics, powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview), lets you investigate your data by asking questions in conversational language through an intuitive chat interface. When you use Conversational Analytics with a [LookML dashboard](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview), you can define and customize a data agent directly in your version-controlled LookML code.

Data agents for LookML dashboards let developers inject tailored business logic, custom instructions, and analytical settings into LookML-managed dashboards. Because LookML dashboards represent governed, version-controlled sources of truth across organizations, LookML dashboard agents ensure that AI interactions remain consistent across environments and adhere to organizational data standards.

**Note:** This page describes data agents for LookML dashboards. For information about data agents on user-defined dashboards, see the [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) documentation page. For information about Explore data agents, see the [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) documentation page.

This page covers the following topics:

  * Before you begin
  * Defining a dashboard agent in LookML
  * Using LookML constants in agent instructions
  * Associating a dashboard agent with a LookML dashboard
  * Testing LookML dashboard agents in Development Mode
  * Copying dashboard agent LookML from user-defined dashboards
  * Viewing agent details in the Looker UI
  * Querying a LookML dashboard with a dashboard agent
  * Limitations of LookML dashboard agents



## Before you begin

Before you can configure or use LookML dashboard agents, ensure that the following requirements are met:

  * **Instance requirements** : A Looker admin must enable **Conversational Analytics** on the **Gemini in Looker** admin page. The admin must also turn on the **Enable Trusted Tester Features** and the **Enabled Dashboard Agents** settings. [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) for dashboard agents, the **Advanced Analytics** admin setting must also be enabled. This setting doesn't apply to LookML dashboard agents in Looker 26.14.
  * **Permissions for developers** : To create, edit, or configure LookML dashboard agents and dashboards, you must have a Looker role with the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) and [`see_lookml_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml_dashboards) permissions, as well as access to the [LookML models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) that underlie the dashboard.
  * **Permissions for viewers** : To chat with a LookML dashboard agent, users must have the [`see_lookml_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml_dashboards) permission and access to the LookML models that underlie the dashboard tiles.



## Define a dashboard agent in LookML

To define a dashboard agent in LookML, declare the [`agent`](https://docs.cloud.google.com/looker/docs/reference/param-agent) parameter in a LookML model file or a dedicated LookML file within your project.

A LookML dashboard agent definition uses the following syntax:
    
    
    agent: agent_name {
      advanced_analytics: yes | no
      description: "Description of the agent"
      instructions: "Custom agent prompt and instructions"
      is_dashboard_agent: yes
      show_debuginfo: yes | no
      show_thinking: yes | no
    }
    

Dashboard agents support the following LookML parameters:

  * **`agent`** : Declares a new agent and defines its name.
  * **`advanced_analytics`** : (Optional) Accepts `yes` or `no` (default is `no`). When set to `yes`, the agent can use [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) to translate natural language questions into Python code and execute that code for advanced computations and visualizations. This parameter is available for LookML dashboard agents; however, it is not functional in Looker 26.14.
  * **`description`** : (Optional) A brief description of the agent.
  * **`instructions`** : (Optional) A string that provides free-form instructions and business context to guide the agent when answering queries. If omitted, the agent uses default conversational processing without custom prompt context.
  * **`is_dashboard_agent`** : (Required for dashboard agents) Set to `yes` to identify the agent specifically as a dashboard agent.
  * **`show_debuginfo`** : (Optional) Accepts `yes` or `no` (default is `no`). When set to `yes`, the agent displays detailed execution and troubleshooting information in conversation responses.
  * **`show_thinking`** : (Optional) Accepts `yes` or `no` (default is `no`). When set to `yes`, the agent displays its step-by-step reasoning process in conversation responses.



Agents on LookML dashboards don't support [verified queries](https://docs.cloud.google.com/looker/docs/glossary#verified_query).

### Example dashboard agent definition

The following example defines a LookML dashboard agent that enforces specific filtering rules and tone:
    
    
    agent: sales_dashboard_agent {
      instructions: "Focus on revenue metrics. Always filter by the current fiscal year unless the user specifies otherwise."
      description: "LookML Dashboard Agent for sales performance analytics."
      is_dashboard_agent: yes
      advanced_analytics: yes
      show_thinking: yes
      show_debuginfo: no
    }
    

## Use LookML constants in agent instructions

If you manage multiple LookML dashboards across an organization, you can use [LookML constants](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) to share standard business rules, glossaries, or filtering requirements across agent definitions without duplicating text.

To use a constant in agent instructions, follow these steps:

  1. Define the constant in your project's [`manifest.lkml` file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files):
         
         constant: FISCAL_YEAR_RULE {
           value: "Always filter all requests by the current fiscal year unless the user explicitly specifies a different timeframe."
         }
         

  2. Reference the constant in the `instructions` parameter of your dashboard agent using `@{<var>CONSTANT_NAME</var>}` syntax:
         
         agent: finance_dashboard_agent {
           instructions: "Prioritize gross margin and operating expense metrics. @{FISCAL_YEAR_RULE}"
           is_dashboard_agent: yes
           advanced_analytics: yes
         }
         




When the agent processes queries, Looker dynamically substitutes the constant string into the agent instructions.

## Associate a dashboard agent with a LookML dashboard

To attach a dashboard agent to a LookML dashboard, configure the dashboard-level parameters in the `.dashboard.lookml` file.

The following dashboard parameters control agent behavior for LookML dashboards:

  * **[`enabled_dashboard_agent`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#enabled_dashboard_agent)** : (Optional) Accepts `true` or `false`. Determines whether users can see the spark **Chat with this dashboard** icon and interact with the dashboard agent. If omitted, this parameter defaults to `true` at the API layer.
  * **[`default_dashboard_agent`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#default_dashboard_agent)** : (Optional) Specifies the name of the LookML agent (defined with the [`agent`](https://docs.cloud.google.com/looker/docs/reference/param-agent) parameter) that serves as the default agent for the dashboard. 



### Example LookML dashboard configuration

The following snippet shows how to map the `sales_dashboard_agent` to a LookML dashboard:
    
    
    - dashboard: executive_sales_overview
      title: "Executive Sales Overview"
      layout: newspaper
      enabled_dashboard_agent: true
      default_dashboard_agent: sales_dashboard_agent
    
      elements:
      - name: total_revenue_by_quarter
        type: looker_column
        model: sales_ops
        explore: orders
        measures: [orders.total_revenue]
        dimensions: [orders.created_quarter]
    

If `enabled_dashboard_agent` is set to `true` and no `default_dashboard_agent` is specified, users can still chat with the dashboard; the agent will run without custom instructions.

## Test LookML dashboard agents in Development Mode

If the agent has already been deployed to production, LookML developers can iteratively modify agent instructions and test responses directly in the Looker UI before deploying changes to production.

**Tip:** If the agent is not yet deployed to production, the conversational interface will ignore any changes that you make to your agent configuration while in Development Mode. In this case, if you want to test out changes to your agent configuration, you could first deploy a baseline agent definition that acts as a placeholder definition for the agent. For example, the placeholder agent could include the entire [`agent`](https://docs.cloud.google.com/looker/docs/reference/param-agent) definition but have an empty `instructions` parameter value. After this baseline agent definition is deployed to production, you can make changes to your agent configuration in Development Mode and test them out in the UI.

To test any changes to a LookML dashboard agent from Development Mode, follow these steps:

  1. Ensure that the agent has at least a baseline definition deployed to production.
  2. Turn on [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  3. Edit the agent `instructions` or settings in your LookML file and save your changes.
  4. Open the LookML dashboard in the Looker UI.
  5. Select spark **Chat with this dashboard** to open the chat panel.
  6. Ask questions to test how the agent interprets and responds to your prompts.



When Development Mode is turned on, Conversational Analytics references the in-memory agent definition, LookML dashboard definition, and model files from your development branch. When you turn Development Mode off, Conversational Analytics reverts to referencing the deployed definitions from the production branch.

Any conversation history that is created during Development Mode is persisted and visible in your recent conversations list across sessions.

## Copy dashboard agent LookML from user-defined dashboards

If you prototype a dashboard as a user-defined dashboard in the UI, you can export its complete configuration—including the dashboard agent settings and instructions—into LookML code.

To copy LookML from a user-defined dashboard:

  1. Open the user-defined dashboard.
  2. Select the three-dot more_vert **Dashboard actions** menu, and then select **Get LookML**.
  3. In the **Get LookML** dialog, copy the generated dashboard LookML and the dashboard agent definition code.
  4. Paste the dashboard LookML into a `.dashboard.lookml` file, and paste the `agent` block into your model or agent LookML file.



The exported LookML preserves the state of the **Enable chat with dashboard** toggle by using the `enabled_dashboard_agent` parameter value along with any custom agent instructions.

## View agent details in the Looker UI

When viewing a LookML dashboard with an active dashboard agent, you can inspect the agent configuration from the chat panel:

  1. Select spark **Chat with this dashboard**.
  2. Select tune **Manage agent**.



For LookML dashboards, the **Manage agent** panel displays agent instructions, Advanced Analytics status, and debug options in **read-only** mode. Settings cannot be edited directly within the UI.

To edit the configuration, developers with the `develop` permission on the underlying models can click **Edit in LookML** to navigate directly to the relevant LookML file in the IDE.

**Note:** If a user does not have the `develop` permission on all models underlying the LookML dashboard, the tune **Manage agent** icon is hidden. 

## Query a LookML dashboard with a dashboard agent

To start a conversation with a LookML dashboard agent:

  1. Open the LookML dashboard.
  2. Select spark **Chat with this dashboard**.
  3. In the **Ask a question** field, enter your query in natural language.
  4. If `show_thinking` is allowed for your dashboard agent, you can choose a question mode: 
     * **Fast** : Quickly translates your query into direct LookML metric lookups.
     * **Thinking** : Evaluates complex analytical questions and displays step-by-step reasoning.
  5. Click send **Send**.



To cancel a query in progress, click stop **Stop response**.

### Manage conversations

  * **Recent conversations** : To open previous conversations, select more_vert **Menu** > **Recent conversations**.
  * **Rename a conversation** : Select more_vert next to a conversation and select edit **Rename**.
  * **Delete a conversation** : Select more_vert next to a conversation and select delete **Delete**.



## Limitations of LookML dashboard agents

LookML dashboard agents have the following limitations:

  * **Defined in LookML only** : LookML dashboard agents must be declared in LookML. You cannot create, configure, or edit them in the Looker UI.
  * **Verified queries not supported** : Data agents for LookML dashboards don't support [verified queries](https://docs.cloud.google.com/looker/docs/glossary#verified_query).
  * **Same-project requirement** : The agent must be defined in the same LookML project as the dashboard that references it.
  * **One agent per dashboard** : You can associate only one dashboard agent with a LookML dashboard.
  * **Dashboard agents only** : LookML does not support creating Explore data agents. All `agent` declarations in LookML must include `is_dashboard_agent: yes`.
  * **Advanced Analytics in Looker 26.14** : LookML dashboard agents in Looker 26.14 don't support the `advanced_analytics` parameter.
  * **Development Mode and undeployed agents** : The conversational interface ignores any changes that are made while in Development Mode to the configuration of LookML dashboard agents that have not yet been deployed to production.



## Related resources

  * **[Conversational Analytics in Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)** : The landing page for Conversational Analytics in Looker.
  * **[Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards)** : Configure and query data agents on user-defined dashboards in the Looker UI.
  * **[Building LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards)** : Create and manage version-controlled dashboards using LookML.
  * **[LookML dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard)** : Reference documentation for all LookML dashboard parameters.
  * **[`agent` parameter](https://docs.cloud.google.com/looker/docs/reference/param-agent)**: Reference documentation for the LookML `agent` parameter.
  * **[Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices)** : Guidance on writing high-quality instructions and optimizing data agents.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
