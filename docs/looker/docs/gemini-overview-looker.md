---
url: https://docs.cloud.google.com/looker/docs/gemini-overview-looker/
title: Gemini in Looker overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:38.040398+00:00
---

# Gemini in Looker overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-overview-looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Gemini in Looker overview Stay organized with collections  Save and categorize content based on your preferences. 

Gemini in Looker represents a series of features in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Available features in Looker

Looker admins can manage the enablement of individual Gemini in Looker features on the **Gemini in Looker** page in the **Platform** section of the **Admin** panel. When Gemini in Looker is enabled, Looker users can perform the following tasks in a Looker (Google Cloud core) instance or a Looker (original) instance:

  * [**Ask questions about and converse with your data by using Conversational Analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview): Gemini in Looker lets you ask questions about your data source by using natural language. Gemini returns Looker charts or data tables that are based on your query. You can learn more about how your response was generated and save your conversation for future reference. conversational analytics is available when the **Conversational Analytics** setting is enabled for your instance.
  * [**Generate custom Looker visualizations**](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini): Gemini in Looker lets you customize formatting options for Looker visualizations by using natural language. Gemini generates JSON formatting options from text-based prompts, which you can apply to your visualizations. You can also use prompts as a starting point for creating templates and patterns for more complex customizations and then [manually update the visualization formatting options](https://docs.cloud.google.com/looker/docs/chart-config-editor). This feature is available when the **Looker Assistants** setting is enabled for your instance.
  * [**Write Looker expressions with Gemini assistance**](https://docs.cloud.google.com/looker/docs/gemini-expression-asst): Gemini in Looker assists you in writing Looker expressions for [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields). This feature is available when the **Looker Assistants** setting is enabled for your instance.
  * [**Access advanced analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) within Conversational Analytics data agents to translate your natural language questions into Python code and execute that code to provide advanced analysis and visualizations. Advanced Analytics is available for a data agent when the **Advanced Analytics** and **Conversational Analytics** settings are enabled for your instance and when the data agent creator turned on **Enable Advanced Analytics** in the agent configuration.
  * [**Generate LookML**](https://docs.cloud.google.com/looker/docs/write-lookml-gemini) [[Preview](https://cloud.google.com/products/#product-launch-stages)]: Gemini in Looker assists you in generating LookML parameters. Gemini suggests LookML parameters that are based on a natural language prompt, which you can add to your project files. This feature is available when the **LookML Assistant** setting is enabled for your instance.
  * [**Generate a summary of an Explore**](https://docs.cloud.google.com/looker/docs/explore-summary-gemini) [[Preview](https://cloud.google.com/products/#product-launch-stages)]: Gemini in Looker generates a summary and an analysis of an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores). This feature is available when the **Explore NL Summary** setting is enabled for your instance.
  * [**Generate starter questions for an Explore**](https://docs.cloud.google.com/looker/docs/gemini-quick-starts): Gemini in Looker examines an Explore, and generates several [starter questions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using_starter_questions) in the new Explore experience, or AI Quick Starts in the classic Explore, to provide helpful starting points for quickly running and building analyses of your data. This feature is available when the **Looker Assistants** setting is enabled for your instance.
  * [**Find saved content on your Looker instance**](https://docs.cloud.google.com/looker/docs/finding-content#searching_for_saved_content): Gemini in Looker's content search moves beyond keyword matching to understand the conceptual meaning of your search queries, letting you search using business terms or analytical questions (for example, "total customer acquisition cost"). This feature is available when the **Semantic Search** setting is enabled for your instance.
  * [**Ask a question in natural language to create a query**](https://docs.cloud.google.com/looker/docs/gemini-insight-asst) [[Preview](https://cloud.google.com/products/#product-launch-stages)]: Gemini in Looker lets you ask questions in natural language to gain insights into an Explore, and then use the results to build or modify the Explore. This feature is available when the **Explore Insight Assistant** setting is enabled for your instance.
  * [**Manage Looker roles**](https://docs.cloud.google.com/looker/docs/gemini-admin-asst) [[Preview](https://cloud.google.com/products/#product-launch-stages)]: Gemini in Looker assists you with creating user roles, permission sets, and model sets, and provides information about your existing roles, permission sets, and model sets. This feature is available when the **Admin Assistant** setting is enabled for your instance.



## Enable features in Looker

To access these features in a Looker (original) instance, a Looker admin must [enable Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) in the Looker (original) instance settings. The instance must be on Looker 25.2 or later and be Looker-hosted. conversational analytics is available on Looker instances on 25.0 or later. A Looker admin can use the same instructions to subsequently disable features.

To access these features in a Looker (Google Cloud core) instance, a user with the [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role must [enable Gemini in Looker](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) in the Looker (Google Cloud core) instance settings in the Google Cloud console. A user with the Looker Admin IAM role can use the same instructions to subsequently disable features.

### Grant permissions to use Gemini in Looker features

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



## Where to interact with Gemini in Looker features

After Gemini in Looker features are enabled, you can seek Gemini assistance to perform the following tasks in Looker:

  * To use [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) to start a conversation with a Looker Explore, select chat_spark **Conversations** from the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) or the **Create** menu. You can also select **Start a conversation** from an [Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_page).
  * To use the Code Interpreter in conversational analytics to [translate your natural language questions into Python code that provides advanced analysis and visualizations](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-code-interpreter), select **Enable Advanced Analytics** when you're [creating or editing a data agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#create-and-edit-data-agents).
  * To [create visualizations in the Looker Chart Config Editor](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini), select **Visualization Assistant** from the **Edit** menu of a supported visualization in an Explore, a Look, or a dashboard.
  * To [write LookML](https://docs.cloud.google.com/looker/docs/write-lookml-gemini), enable [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) and select the **Help Me Code** icon from the side panel selector in the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide#accessing-ide).
  * To [view a summary of an Explore](https://docs.cloud.google.com/looker/docs/explore-summary-gemini), click the info **Explore Summary** info button.
  * To [generate Quick Start analyses](https://docs.cloud.google.com/looker/docs/gemini-quick-starts), from a classic Explore, in the **Try AI Quick Starts** message, click **Add**. Or, when editing an Explore, click the bolt**Quick Start** button. From the [new Explore experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview), click the [**Starter Questions**](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing_a_starter_question_from_a_blank_explore_in_the_new_explore_experience) drop-down field, or click the dynamic_form [**Show starter questions** button](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#choosing-a-starter-question-once-an-explore-has-run).
  * To [write a Looker expression](https://docs.cloud.google.com/looker/docs/gemini-expression-asst), when creating a table calculation or custom dimension, click **Help me write an expression with Gemini**.
  * To [ask questions about an Explore and create a query based on that Explore](https://docs.cloud.google.com/looker/docs/gemini-insight-asst), click the **Ask Insight Assistant** tile in a blank Explore or click the tips_and_updates **Insight Assistant** button.
  * To [create a Looker role on a Looker instance](https://docs.cloud.google.com/looker/docs/gemini-admin-asst), click the  assistant**Admin Assistant** button.



## Understand the compliance capabilities of Gemini in Looker features

Google Cloud [Preview](https://cloud.google.com/products#product-launch-stages) features are generally not in scope for formal compliance certification support and are not recommended for use with regulated workloads or sensitive data unless otherwise stated.

Conversational analytics is not yet included in [FedRAMP High or FedRAMP Medium](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-data-boundaries) authorization boundaries. Before you enable the **Gemini in Looker** setting for your Looker instance, discuss with your authorizing body whether Gemini for Google Cloud's compliance offerings meet the needs of your organization.

For Looker (Google Cloud core) instances, each [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) that becomes available will add Gemini in Looker features to the default offerings as that package's change requirements and processes are met. Conversational analytics in Looker respects the compliance capabilities of the associated Looker (Google Cloud core) instance, with the following exception:

Data Residency (DRZ) support, specifically for data-at-rest, is available to all Looker customers. All data-at-rest that is associated with Conversational Analytics resides strictly within the Looker instance and is confined to a single region. Data in transit and machine learning (ML) are processed using a global service.

### Data governance, history retention, and log auditing

Gemini in Looker has independent data handling, retention, and logging behaviors when it's compared to standalone Gemini applications (such as the [Gemini web app](https://gemini.google.com)):

  * **Retention** : Google Admin console settings don't apply to Gemini in Looker. Active conversations are retained indefinitely until a user deletes them, after which the conversations are permanently deleted after 30 days.
  * **Administration** : Administrators cannot bulk-delete conversation history or enforce custom retention periods.
  * **Auditing** : By default, raw user prompts and Gemini responses aren't recorded in System Activity or Cloud Logging. System Activity will log the query execution source (for example, `conversational_analytics`), and Cloud Logging will record only the administrative actions (for example, enabling or disabling Gemini features). However, if a Looker admin has enabled the [**End User Conversational Analytics (CA) Query Review** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#ca-user-feedback) and a user has consented to revealing their query data, then Looker admins can view that user's queries in System Activity.



## Related resources

  * Gemini in Looker feature [pricing](https://cloud.google.com/looker/pricing).
  * [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn how [Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn more about [Google Cloud compliance](https://cloud.google.com/security/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
