---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup/
title: Set up Conversational Analytics in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:30.663037+00:00
---

# Set up Conversational Analytics in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Set up Conversational Analytics in Looker Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through setting up Conversational Analytics in Looker, including setup requirements, required permissions to use Conversational Analytics, and supported data sources.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

To use Conversational Analytics within a Looker instance, you and your Looker instance must meet the following requirements:

  1. Gemini in Looker must be enabled for the Looker instance. 
     * To access these features in a Looker (original) instance, a Looker admin must enable the **Gemini in Looker** setting and whichever **Conversational Analytics** setting corresponds to the content that you are using (**Conversational Analytics (Conversations page)** or **Dashboard agents**) in the [Looker (original) instance settings](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil). To use [dashboard agents with a user-defined dashboard](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) or [agentic workflows](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview), update your instance to Looker 26.8 or later. To [define and chat with LookML dashboard agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards), update your instance to Looker 26.14 or later.
     * To access these features in a Looker (Google Cloud core) instance, a user with the [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role must [enable **Gemini in Looker**](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) in the Looker (Google Cloud core) instance settings in the Google Cloud console. A Looker admin must enable the appropriate **Conversational Analytics** setting (**Conversational Analytics (Conversations page)** or **Dashboard agents**) on the **Gemini in Looker** page in the **Admin** panel of the Looker (Google Cloud core) instance.
  2. If you have configured an IP allowlist for your instance, you must configure it to allow connections from Google Cloud services: 
     * Admins for Looker (original) instances who have enabled the [**Enable Allowlist** setting](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) must also enable the [**Allow Google Cloud services** setting](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist#allow-google-cloud-services), which is supported in Looker 26.2 and later. For earlier versions, contact Support for assistance.
     * If a Looker (Google Cloud core) instance has an [IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) configured, the [**Link Google services with this instance** checkbox](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist#allowlist-services) must be selected on the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the instance's **Instance** page in the Google Cloud console in order to connect with Conversational Analytics.
  3. Optionally, an admin can enable [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) to use Python to answer advanced questions. Under **Additional options** , turn on the **Advanced Analytics** setting. Whichever **Conversational Analytics** setting corresponds to the content you are querying (**Conversational Analytics (Conversations page)** or **Dashboard agents**) must also be enabled.
  4. Optionally, an admin can enable [dashboard data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) to query both user-defined dashboards and LookML dashboards. On the **Gemini in Looker** Admin page, under **Conversational Analytics** , turn on the **Dashboard agents** setting.
  5. Optionally, an admin can enable [dashboard summaries](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards#dashboard-summaries) [[Preview](https://cloud.google.com/products#product-launch-stages)] to display a summary of the dashboard within [scheduled dashboard deliveries](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards). On the **Gemini in Looker** Admin page, under **Platform features** , select **Enable Trusted Tester Features** , and then turn on the **Enable Dashboard Summary** setting. The **Dashboard agents** setting must also be enabled.
  6. Optionally, an admin can [enable agentic workflows](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview) [[Preview](https://cloud.google.com/products#product-launch-stages)] to create dynamic workflows that monitor your data and alert you of changes. On the **Gemini in Looker** Admin page, under **Platform features** , select **Enable Trusted Tester Features** , and then turn on the **Agentic Workflows** setting. Whichever **Conversational Analytics** setting corresponds to the content you are using (**Conversational Analytics (Conversations page)** or **Dashboard agents**) must also be enabled. Agentic workflows require that your Looker instance is running Looker 26.8 or later.



### Required Looker permissions

The use of Conversational Analytics is managed through a combination of [content access, data access, and feature access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management). To perform the tasks that are described in the following table, you must be assigned a Looker role that has the required permissions for the models that underlie the individual Explore or that the data agent will query and, in some cases, access to the agent itself. If you don't have sufficient permissions to chat with a dashboard or an Explore, Looker surfaces an error.

A Looker admin can grant Looker roles and permissions on the **Roles** page in the **Admin** section of the Looker instance. For more information about Looker roles, see the [Admin settings – Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) documentation page.

The creator of the data agent can manage individual users' access to the agent by [sharing the agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#share-a-data-agent) or managing access to the agent's underlying content.

Task | Required Looker permissions on the model that underlies the data | Required level of content access  
---|---|---  
Chat with a data agent from the **Agents** tab in the Conversational Analytics interface | `access_data``gemini_in_looker``chat_with_agent` | **View** access on the data agent  
Chat with a Looker Explore from the **Explores** tab in the Conversational Analytics interface | `access_data``gemini_in_looker``chat_with_agent``chat_with_explore`  
Create, edit, share, and delete Explore data agents | `access_data``gemini_in_looker``chat_with_agent``chat_with_explore``save_agents`Users can create agents that use only the Explores for which they have been granted the `save_agents` permission on the underlying model. To edit, delete, or share a data agent that was created by another user, users must be granted a role that contains the `save_agents` permission on every model that is used by the agent. | **Manage access; Edit** on the data agent (this access is granted automatically if the user creates the agent; otherwise, **Manage access; Edit** access must be granted by the agent's creator by sharing the agent)**Manage access; Edit** on the dashboard  
Create, edit, and delete dashboard agents on user-defined dashboards ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data` (on all models underlying the dashboard)`see_user_dashboards``gemini_in_looker``chat_with_agent` (on all models underlying the dashboard)`save_agents` (on all models underlying the dashboard) | **Manage access; Edit** on the dashboard  
Create, edit, and configure LookML dashboard agents ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data` (on all models underlying the dashboard)`see_lookml_dashboards``develop` (on all models underlying the dashboard)`gemini_in_looker``chat_with_agent` (on all models underlying the dashboard) | Access to the LookML project and model files  
Chat with a dashboard agent ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data` (on all models underlying the dashboard)`see_user_dashboards` (to interact with user-defined dashboards) or `see_lookml_dashboards` (to interact with LookML dashboards)`gemini_in_looker``chat_with_agent` (on all models that underlie the dashboard) | **View** access on the dashboard (or access to the LookML model for LookML dashboards)  
Publish agents to other Google Cloud applications, such as Gemini Enterprise ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data``gemini_in_looker``chat_with_agent``chat_with_explore``save_agents` Added 26.8  `publish_agent_externally`. | **Manage access; Edit** (this access is granted automatically if the user creates the agent; otherwise, **Manage access; Edit** access must be granted by the agent's creator by sharing the agent)  
Create an agentic workflow with a dashboard agent ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data` (on at least one model that underlies the dashboard)`see_user_dashboards` (to interact with user-defined dashboards) or `see_lookml_dashboards` (to interact with LookML dashboards)`gemini_in_looker``chat_with_agent` (on at least one model that underlies the dashboard)`see_schedules` or `see_alerts` (to view the workflows that you have created on the [**Manage Workflows** user page](https://docs.cloud.google.com/looker/docs/user-workflows)) | **Manage access; Edit** on the data agent (this access is granted automatically if the user creates the agent; otherwise, **Manage access; Edit** access must be granted by the agent's creator by sharing the agent)**Manage access; Edit** on the dashboard  
Create an agentic workflow with an Explore data agent ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data``gemini_in_looker``chat_with_agent``see_schedules` or `see_alerts` | **Manage access; Edit** on the data agent (this access is granted automatically if the user creates the agent; otherwise, **Manage access; Edit** access must be granted by the agent's creator by sharing the agent)**Manage access; Edit** on the dashboard  
Create an agentic workflow within an Explore conversation ([Preview](https://cloud.google.com/products#product-launch-stages)) | `access_data``gemini_in_looker``chat_with_agent``chat_with_explore``see_schedules` or `see_alerts` | **Manage access; Edit** on the data agent (this access is granted automatically if the user creates the agent; otherwise, **Manage access; Edit** access must be granted by the agent's creator by sharing the agent)**Manage access; Edit** on the dashboard  
See [**Manage Workflows** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows) ([Preview](https://cloud.google.com/products#product-launch-stages)) | `see_schedules` or `see_alerts` and `chat_with_agent` | Content access doesn't need to be granted  
See [**Workflow Executions** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflow-executions) ([Preview](https://cloud.google.com/products#product-launch-stages)) | `see_schedules` and `chat_with_agent` | Content access doesn't need to be granted  
Create, edit, share, and delete Conversational Analytics data agents | `access_data``gemini_in_looker``admin_agents` | Content access doesn't need to be granted  
  
Looker also has the following default roles that contain subsets of these permissions for all models on the instance:

  * **Conversational Analytics Agent Manager** : With this role, a user can create, edit, share, delete, and chat with agents that they have **Manage access; Edit** access for, create workflows, and chat with Explores.
  * **Conversational Analytics User** : With this role, a user can chat with an agent that they have **View** access for and create workflows.
  * **Conversational Analytics Viewer** :  Added 26.12  With this role, users can see the agents that they have **View** access for. However, without additional permissions to access the agent's data source, these users won't be able to interact with the agent.
  * **Admin** : By default, this role (Looker Admin) has all permissions and content access across the instance.



#### Conversational Analytics Agent Manager

The **Conversational Analytics Agent Manager** role consists of the [Conversational Analytics Agent Manager permission set](https://docs.cloud.google.com/admin-panel-users-roles#gemini_ca_agent_manager) for all models that are on the Looker instance. Users with this role can create, edit, share, and delete Conversational Analytics data agents that use Looker Explores, and they can create agentic workflows.

**Note:** When a user creates a data agent, they're granted [**Manage Access, Edit** content access](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#share-data-agents) automatically; however, they must be granted this access for the data agent if they want to edit, share, or delete a data agent that was created by another user.

#### Conversational Analytics User

The **Conversational Analytics User** role consists of the [Conversational Analytics User permission set](https://docs.cloud.google.com/admin-panel-users-roles#gemini_ca_user) for all models on the Looker instance. Users with this role can chat with any Conversational Analytics data agent in Looker, as long as they have been granted [**View** access](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#share-data-agents) to the data agent, and they can create agentic workflows.

#### Conversational Analytics Viewer  Added 26.12 

The **Conversational Analytics Viewer** role consists of the [Conversational Analytics Viewer permission set](https://docs.cloud.google.com/admin-panel-users-roles#gemini_ca_viewer) for all models on the Looker instance. Users with this role can chat with any Conversational Analytics data agent in Looker, as long as they have been granted [**View** access](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#share-data-agents) to the data agent and the `access_data` permission on the appropriate models.

## Supported data sources

You can converse with the following data sources through the Conversational Analytics interface:

  * [Looker Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores)
  * [Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents)
  * [Data agents for user-defined dashboard](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards)
  * [Data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards)



When you "chat" with an Explore or a data agent, you're essentially having a conversation with a specific, predefined dataset. This is a direct way to ask questions about the data within that Explore. You can have a conversation with up to five Explores.

Explore data agents are AI-powered assistants that you can create and customize. Dashboard agents let you converse directly with user-defined or LookML dashboards. You can provide a data agent with instructions and context that are specific to your data.

For strategies and best practices to help Looker admins and LookML developers successfully configure, deploy, and optimize Conversational Analytics, including LookML best practices for Conversational Analytics, tips on when to add context to LookML versus Conversational Analytics, and best practices for setting up an Explore for use with Conversational Analytics, see the [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout-guide) documentation page.

## What's next

  * [Start a conversation with an individual Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data)
  * [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents)
  * [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards)
  * [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards)
  * [Set up an agentic workflow to monitor your data](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview) ([Preview](https://cloud.google.com/products#product-launch-stages))



## Related resources

  * [Conversational analytics in Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)
  * [Recommended setup and rollout strategy for Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout)
  * [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices)
  * [Admin settings – Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
