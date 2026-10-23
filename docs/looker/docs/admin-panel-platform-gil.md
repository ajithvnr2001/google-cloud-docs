---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil/
title: Admin settings \u2013 Gemini in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:27.759855+00:00
---

# Admin settings – Gemini in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings – Gemini in Looker Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This documentation page is for Looker (original) instances. For information about enabling Gemini in Looker for Looker (Google Cloud core) instances, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.

This documentation page describes how to administer Gemini in Looker for a Looker (original) instance. It covers the following topics:

  * How to enable and disable Gemini in Looker features for a Looker (original) instance
  * The permissions that are required to use Gemini in Looker features



This page is intended for users who are assigned the [Looker Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role for the Looker (original) instance.

## What is Gemini in Looker?

Gemini in Looker represents a series of features in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

For more information about the types of tasks that Gemini in Looker can assist with, see the [Gemini in Looker overview](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) documentation page. 

## Before you begin

To enable or disable Gemini in Looker and to grant users permissions to use the features that use Gemini assistance, you must be assigned the [Looker Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role for the Looker (original) instance.

Gemini in Looker features are available for Looker-hosted instances only.

[Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) has more stringent instance requirements. See the [Set up Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#setup-and-requirements) documentation page for more information.

## Selectively enable and disable Gemini in Looker features

To enable Gemini in Looker, follow these steps:

  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Under **Gemini in Looker enablement** , turn on the **Enable Gemini in Looker** setting. When this setting is enabled, you can selectively enable the features on the Looker instance that use Gemini and that are generally available. Turn on the following settings to enable each of their corresponding features: 
     * **Conversational Analytics** : 
       * **Conversational Analytics (Conversations page)** — enables access to the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data) for data agents with Explores and direct chats with an Explore.
       * **Dashboard agents** — enables [default data agents](https://docs.cloud.google.com/looker/docs/glossary#default-agent) on [user-defined dashboards and LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards).
     * **Additional options** : 
       * **Advanced Analytics** — allows Conversational Analytics data agent creators to enable [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) for conversations with their data agent. To use Advanced Analytics, you must also enable whichever Conversational Analytics setting corresponds to the content you are querying (**Conversational Analytics (Conversations page)** or **Dashboard agents**). If both the **Conversational Analytics (Conversations page)** and **Dashboard agents** settings are turned off, then **Advanced Analytics** cannot be enabled. If either **Conversational Analytics (Conversations page)** or **Dashboard agents** is enabled, **Advanced Analytics** can be enabled, but it is turned off by default.
     * **Platform features** : 
       * **Looker Assistants** — enhances creator velocity and productivity with AI assistance, including the[**Visualization Assistant**](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini), the [**Expression Assistant**](https://docs.cloud.google.com/looker/docs/gemini-expression-asst), and [**Semantic Search**](https://docs.cloud.google.com/looker/docs/finding-content#searching_for_saved_content).
  3. Under **Platform features** , optionally select **Enable Trusted Tester Features** to grant users access to the Trusted Tester capabilities of Gemini in Looker features that are in [Preview](https://cloud.google.com/products/#product-launch-stages). Turn on the following settings to enable each of their corresponding Preview features: 
     * **Enable Dashboard Summary** — displays a summary of the dashboard for scheduled dashboard deliveries. This setting requires the **Enable Trusted Tester Features** and **Dashboard agents** settings to be enabled.
     * **LookML Assistant** — allows users to write natural language prompts that produce Gemini-generated suggestions for LookML parameters, which they can add to their project files.
     * **Agentic Workflows** — allows users to prompt Conversational Analytics agents and conversations to generate [agentic workflows](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview) to monitor changes in data. This setting requires the **Enable Trusted Tester Features** setting and whichever Conversational Analytics setting corresponds to the content you are using (**Conversational Analytics (Conversations page)** for Explores or **Dashboard agents** for dashboards).
     * **Admin Assistant** — assists Looker admins in [managing Looker roles](https://docs.cloud.google.com/looker/docs/gemini-admin-asst).
     * **Explore NL Summary** — allows users to view a [Gemini-generated summary of a Looker Explore](https://docs.cloud.google.com/looker/docs/explore-summary-gemini).
     * **Explore Insight Assistant** — enables the [**Insight Assistant**](https://docs.cloud.google.com/looker/docs/gemini-insight-asst), which allows users to ask natural language questions about an Explore, and create and modify queries based on the Explore.
     * **AI-Assisted Quick Starts** — enables the [Gemini-generated Quick Start analyses](https://docs.cloud.google.com/looker/docs/gemini-quick-starts) for a Looker Explore.
     * **Publish to Gemini Enterprise** — allows owners of [Conversational Analytics data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) to publish the agents in Gemini Enterprise when they also have a role that contains the [`publish_agent_externally`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#publish_agent_externally) permission. This setting requires the **Enable Trusted Tester Features** setting and the **Conversational Analytics (Conversations page)** setting to be enabled. When you enable this setting, you must provide the following information about the target Gemini Enterprise instance: 
       * In the **GCP Project Number** field, enter the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the Google Cloud project that hosts the target Gemini Enterprise instance.
       * In the **Region** field, enter the [region](https://docs.cloud.google.com/gemini/enterprise/docs/locations) for the Gemini Enterprise instance. The region is listed under **Location** on the Gemini Enterprise **Apps** page.
       * In the **Instance ID** field, enter the specific ID of the Gemini Enterprise instance. This ID is located on the Gemini Enterprise **Apps** page. _If you change the target Gemini Enterprise instance, any agents that were published in the original Gemini Enterprise instance will be unpublished automatically._
       * In the Google Cloud console, grant the Looker-generated service account the [**Discovery Engine Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) IAM role in the Google Cloud project that hosts the Gemini Enterprise instance. The appropriate service account to use is displayed on the **Gemini in Looker** enablement page in the Looker instance.
  4. Optionally, turn on the **Enable Trusted Tester Data Use** setting. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview). This setting can be enabled only when the **Enable Trusted Tester Features** setting is enabled. Enabling **Enable Trusted Tester Features** automatically enables this setting.



To disable Gemini for a Looker (original) instance, clear the **Enable Gemini in Looker** setting.

**Important:** If you want to remove the option to enable Gemini in Gemini for a Looker (original) instance, contact Support. 

You must grant the appropriate permissions to users before they can use Gemini in Looker features, including the Code Interpreter.

## Grant the Gemini in Looker permission to users

Gemini assistance is available whilst performing various tasks in the Looker instance. To use any of these Gemini-assisted features, users must be granted a Looker [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) that applies the `gemini_in_looker` permission to the appropriate models as well as a role that contains permissions to perform the Gemini-assisted task. You can assign the `gemini_in_looker` permission in any of the following ways:

  * Grant users the **Gemini** default role
  * Grant users a custom role that contains the `gemini_in_looker` permission
  * Grant users the permissions, permission sets, or roles that are required to use Conversational Analytics
  * Add them to the **Gemini Default Users** group



### Granting the **Gemini** default role

The **Gemini** [default role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) applies all of the necessary permissions to interact with Conversational Analytics data agents and use **Gemini in Looker** to all models on the instance. You must also assign the `access_data` permission and any other permissions that may be necessary to use the specific Gemini in Looker feature.

You can assign this role to the appropriate [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#roles_2) or [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding-roles-groups).

### Granting a custom role

To restrict users from accessing Gemini in Looker features for all models on the Looker instance, you can [create a custom Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create-custom-roles) that applies the `gemini_in_looker` permission for specific models only, and assign it to the appropriate [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#roles_2) or [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding-roles-groups). You may need to remove those users from the [**Gemini Default Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#gemini_default_users) group, which is assigned the **Gemini** default role by default. You must also assign the `access_data` permission and any other permissions that may be necessary to use the specific Gemini in Looker feature.

### Granting Conversational Analytics roles or permissions

The **Conversational Analytics Agent Manager** role consists of the [**Conversational Analytics Agent Manager** permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_ca_agent_manager) for all models on the Looker instance. Users with this role can create, edit, share, and delete Conversational Analytics data agents.

The **Conversational Analytics User** role consists of the [**Conversational Analytics User** permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_ca_user) for all models on the Looker instance. Users with this role can chat with any Conversational Analytics data agent in Looker.

You can assign either of these roles to the appropriate [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#roles_2) or [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding-roles-groups). You can also [create a custom Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create-custom-roles) that applies any of the Conversational Analytics permissions to specific models.

### Adding users to the **Gemini Default Users** group

The **Gemini Default Users** group has been created automatically for all Looker (original) instances that use an [open system configuration](https://docs.cloud.google.com/looker/docs/access-levels#open_and_closed_systems_of_access_to_folders). Users in this group are assigned the [**Gemini** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini), which grants them the ability to use [Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) features when they also have a role that includes the [other required permissions to use Gemini in Looker features](https://docs.cloud.google.com/looker/docs/gemini-overview-looker#use-gil-looker).

You can [edit](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#editing-groups) the **Gemini Default Users** group to add or remove users, or to delete the group entirely. You can also [add additional roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding-roles-groups) to the group.

For more information about how users are added to this group, see the [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#default-gemini-users) documentation page.

### Additional permissions

To use any Gemini in Looker features, users must be granted a Looker role that contains permissions to perform the Gemini-assisted task. These permissions are summarized in the following list:

  * To use [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) or the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview) to query Looker data or to create a data agent, you must be assigned a Looker role that contains the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) and the [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) permissions for each model that you're querying. [Additional permissions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) are required depending on how you're interacting with Conversational Analytics. This feature is available when the **Conversational Analytics** setting is enabled.
  * To use the [Visualization Assistant](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini) to create custom visualizations with Gemini assistance, you must be assigned a Looker role that contains the [`can_override_vis_config`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config) permission. The **Visualization Assistant** is available when the **Looker Assistants** setting is enabled.
  * To use [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) within Conversational Analytics data agents to translate your natural language questions into Python code and execute that code to provide advanced analysis and visualizations, you must be a assigned a role that has the same permissions that are required to use Conversational Analytics data agents.
  * To write LookML with Gemini assistance, you must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project. This feature is available when the **LookML Assistant** setting is enabled.
  * To generate Explore summaries, including the suggested purpose of the Explore and the types of data that are used in the query, you must have a role that contains the `develop` permission for at least one model in the LookML project and the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission to view and interact with Explores. This feature is available when the **Explore NL Summary** setting is enabled.
  * To generate Quick Start analyses, you must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project. This feature is available with the **AI-assisted Quick Starts** setting is enabled.
  * To write Looker expressions with Gemini assistance, you must be assigned a Looker role that contains the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission to use Gemini to write a table calculation expression, or a role that contains the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission to write a custom field expression. This feature is available when the **Looker Assistants** setting is enabled.
  * To use the Insight Assistant to ask questions about an Explore and then use Gemini assistance to create or modify an Explore, you must be assigned a Looker role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission. This feature is available with the **Insight Assistant** setting is enabled.
  * To use the Admin Assistant to assist you in creating and modifying Looker roles, you must have the [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role. This feature is available with the **Admin Assistant** setting is enabled.



## Provide feedback

You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in the documentation for each feature.

## Related resources

  * Gemini in Looker feature [pricing](https://cloud.google.com/looker/pricing).
  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
