---
url: https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini/
title: Administer Gemini on your Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:37.771602+00:00
---

# Administer Gemini on your Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Administer Gemini on your Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This documentation page is for Looker (Google Cloud core) instances. Gemini in Looker can also be enabled in Looker (original) instances. For information about enabling Gemini in Looker for Looker (original) instances, see the [Admin settings – Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.

This documentation page describes how to administer Gemini in Looker features for a Looker (Google Cloud core) instance. It covers the following topics:

  * How to enable and disable Gemini in Looker features for a Looker (Google Cloud core) instance
  * The permissions that are required to use Gemini in Looker features



This page is intended for users who have the [Looker Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role for the Looker (Google Cloud core) instance and the Looker Admin (`roles/looker.admin`) role for the Google Cloud project in which the instance resides.

## What is Gemini in Looker?

Gemini in Looker represents a series of features in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

For more information about the types of tasks that Gemini in Looker can assist with, see the [Gemini in Looker overview](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) documentation page. 

## Understand the compliance capabilities of Gemini in Looker features

Conversational analytics is not yet included in [FedRAMP High or FedRAMP Medium](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-data-boundaries) authorization boundaries. Before you enable the **Gemini in Looker** setting for your Looker instance, discuss with your authorizing body whether Gemini for Google Cloud's compliance offerings meet the needs of your organization.

For Looker (Google Cloud core) instances, each [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) that becomes available will add Gemini in Looker features to the default offerings as that package's change requirements and processes are met. Conversational analytics in Looker respects the compliance capabilities of the associated Looker (Google Cloud core) instance, with the following exception:

Data Residency (DRZ) support, specifically for data-at-rest, is available to all Looker customers. All data-at-rest that is associated with Conversational Analytics resides strictly within the Looker instance and is confined to a single region. Data in transit and machine learning (ML) are processed using a global service.

### Feature administration and governance

Although you enable Gemini in Looker in the Google Cloud console, you don't administer how Gemini operates from either the Google Cloud console or the Google Admin console. After Gemini is enabled, you administer all features directly within the Looker instance.

Gemini in Looker has independent data handling, retention, and logging behaviors when it's compared to standalone Gemini applications (such as the [Gemini web app](https://gemini.google.com)). For more information, see [Data governance, history retention, and log auditing](https://docs.cloud.google.com/looker/docs/gemini-overview-looker#data-governance-history-retention-log-auditing).

## Before you begin

To get the permissions that you need to enable Gemini for a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance resides. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To perform the following tasks, you must be a [Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) for the Looker (Google Cloud core) instance:

  * Enable the individual settings for features that use Gemini assistance in the Looker (Google Cloud core) instance
  * Grant users permissions to use Gemini in Looker features



## Enable and disable Gemini

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To enable Gemini in Looker for Looker (Google Cloud core), follow these steps in the Google Cloud console:

  1. Navigate to the Google Cloud project that hosts the Looker (Google Cloud core).
  2. Navigate to the [**Instances** page](https://docs.cloud.google.com/looker/docs/looker-core-view-console), and click the name of the instance for which you want to enable Gemini.
  3. Click **Edit**.
  4. Expand the **Gemini in Looker (Google Cloud core)** section.
  5. Select **Gemini**. When this setting is enabled, a Looker admin can selectively enable [available Gemini in Looker features](https://docs.cloud.google.com/looker/docs/gemini-overview-looker#available-features-looker) from the Looker (Google Cloud core) instance **Admin** panel.
  6. To enable the Gemini in Looker features that are available in Preview, select **Trusted Tester features**. When this setting is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. **This setting must be enabled in order for users to access Gemini features that are in Preview.**
  7. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).



To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

## Selectively enable and disable individual Gemini in Looker features

The **Gemini in Looker** page in the **Platform** section of the Looker (Google Cloud core) **Admin** panel displays information about the enablement status of the **Gemini** , **Trusted Tester features** , and **Trusted Tester data use** settings for the instance, which are managed in the Google Cloud console. This page is also where Looker admins can manage the enablement settings for individual Gemini in Looker features.

A green check mark next to **Gemini Enable status** indicates that Gemini in Looker features that are generally available can be enabled for the instance. A green check next to **Trusted Tested features enablement status** indicates that Gemini in Looker features that are in Preview can be enabled for the instance.

To enable individual Gemini in Looker features, follow these steps in the Looker (Google Cloud core) instance:

  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Turn on the following toggles to enable each of their corresponding generally available features: 
     * **Conversational Analytics** — enables [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)
       * **Advanced Analytics** — allows Conversational Analytics data agent creators to enable [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) for all conversations with their data agent. The **Conversational Analytics** setting must also be enabled to use Advanced Analytics.
     * **Looker Assistants** — enables the [**Visualization Assistant**](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini), the [**Expression Assistant**](https://docs.cloud.google.com/looker/docs/gemini-expression-asst), and [**Starter Questions**](https://docs.cloud.google.com/looker/docs/gemini-quick-starts) (for the New Explore experience) or **AI Quick Starts** (for the classic Explore). 
       * [**Semantic Search**](https://docs.cloud.google.com/looker/docs/finding-content#searching_for_saved_content) — enables users to search for saved content in Looker using natural language queries.
     * **Verified Queries** — enables [verified queries](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#define-verified-queries), which are predefined pairs of natural language questions and their exact, corresponding Explore queries that teach your data agent how to handle complex business requests. The **Conversational Analytics** setting must also be enabled to use verified queries. The **Verified Queries** setting is enabled by default.
  3. Turn on the following toggles to enable each of their corresponding Preview features: 
     * **Enable Dashboard Agents** — allows users to create [data agents from a dashboard](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) using Conversational Analytics.
     * **Enable Dashboard Summary** — displays a summary of the dashboard for scheduled dashboard deliveries. This setting requires the **Conversational Analytics** , **Enable Trusted Tester Features** , and **Enable Dashboard Agents** settings to be enabled.
     * **LookML Assistant** — allows users to write natural language prompts that produce Gemini-generated suggestions for LookML parameters, which they can add to their project files.
     * **Agentic Workflows** — allows users to prompt Conversational Analytics agents and conversations to generate [agentic workflows](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows) to monitor changes in data.
     * **Admin Assistant** — assists Looker admins in [managing Looker roles](https://docs.cloud.google.com/looker/docs/gemini-admin-asst).
     * **Explore NL Summary** — allows users to view a [Gemini-generated summary of a Looker Explore](https://docs.cloud.google.com/looker/docs/explore-summary-gemini).
     * **Explore Insight Assistant** — enables the [**Insight Assistant**](https://docs.cloud.google.com/looker/docs/gemini-insight-asst), which allows users to ask natural language questions about an Explore, and create and modify queries based on the Explore.
     * **Publish to Gemini Enterprise** — allows owners of [Conversational Analytics data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) to publish the agents in Gemini Enterprise when they also have a role that contains the [`publish_agent_externally`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#publish_agent_externally) permission. When you enable this setting, you must provide the following information about the target Gemini Enterprise instance: 
       * In the **GCP Project Number** field, enter the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the Google Cloud project that hosts the target Gemini Enterprise instance.
       * In the **Region** field, enter the [region](https://docs.cloud.google.com/gemini/enterprise/docs/locations) for the Gemini Enterprise instance. The region is listed under **Location** on the Gemini Enterprise **Apps** page.
       * In the **Instance ID** field, enter the specific ID of the Gemini Enterprise instance. This ID is located on the Gemini Enterprise **Apps** page. _If you change the target Gemini Enterprise instance, any agents that were published in the original Gemini Enterprise instance will be unpublished automatically._
       * In the Google Cloud console, grant the Looker-generated service account the [**Discovery Engine Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) IAM role in the Google Cloud project that hosts the Gemini Enterprise instance. The appropriate service account to use is displayed on the **Gemini in Looker** enablement page in the Looker instance.



You must grant the appropriate permissions to users before they can use Gemini in Looker features.

## Grant Gemini in Looker permission to users

**Note:** For more information about adding users to a Looker (Google Cloud core) instance so that you can update the users' settings, see the [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management) documentation page.

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

Additional Looker permissions may be needed to perform the tasks that Gemini assists with. See the Additional permissions section on this page for a list of these permissions.

### Additional permissions

To use any Gemini in Looker features, users must be granted a Looker role that contains permissions to perform the Gemini-assisted task. These permissions are summarized in the following list:

  * To use [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) or the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview) to query Looker data or to create a data agent, you must be assigned a Looker role that contains the [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) and the [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) permissions for each model that you're querying. [Additional permissions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) are required depending on how you're interacting with Conversational Analytics. This feature is available when the **Conversational Analytics** setting is enabled.
  * To use the [Visualization Assistant](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini) to create custom visualizations with Gemini assistance, you must be assigned a Looker role that contains the [`can_override_vis_config`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config) permission. The **Visualization Assistant** is available when the **Looker Assistants** setting is enabled.
  * To use [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) within Conversational Analytics data agents to translate your natural language questions into Python code and execute that code to provide advanced analysis and visualizations, you must be a assigned a role that has the same permissions that are required to use Conversational Analytics data agents.
  * To write LookML with Gemini assistance, you must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project. This feature is available when the **LookML Assistant** setting is enabled.
  * To generate Explore summaries, including the suggested purpose of the Explore and the types of data that are used in the query, you must have a role that contains the `develop` permission for at least one model in the LookML project and the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission to view and interact with Explores. This feature is available when the **Explore NL Summary** setting is enabled.
  * To generate starter question analyses, you must be assigned a Looker role that contains the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a LookML project. This feature is available when the **Looker Assistants** setting is enabled.
  * To write Looker expressions with Gemini assistance, you must be assigned a Looker role that contains the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission to use Gemini to write a table calculation expression, or a role that contains the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission to write a custom field expression. This feature is available when the **Looker Assistants** setting is enabled.
  * To use the Insight Assistant to ask questions about an Explore and then use Gemini assistance to create or modify an Explore, you must be assigned a Looker role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission. This feature is available with the **Insight Assistant** setting is enabled.
  * To use the Admin Assistant to assist you in creating and modifying Looker roles, you must have the [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role. This feature is available with the **Admin Assistant** setting is enabled.



## Provide feedback

You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in the documentation for each feature.

## Related resources

  * Gemini in Looker feature [pricing](https://cloud.google.com/looker/pricing)
  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
