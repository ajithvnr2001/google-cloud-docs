---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents/
title: Create and manage Explore data agents \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:39.314833+00:00
---

# Create and manage Explore data agents  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create and manage Explore data agents Stay organized with collections  Save and categorize content based on your preferences. 

Data agents let you curate the [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) experience for your users. With agents, you can provide Conversational Analytics with context and instructions to enable it to answer questions more effectively for specific use cases. Agents empower analysts to map business terms to specific fields, specify the best fields for filtering, and define custom calculations.

**Note:** This page describes Explore data agents — data agents that query Explores. For information about data agents for user-defined dashboards and LookML dashboards, see the [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) and [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards) [[Preview](https://cloud.google.com/products#product-launch-stages)] documentation pages, respectively.

This page guides you through the following processes:

  * Create and edit data agents
  * Share data agents with other users
  * Publish data agents to other applications
  * Delete data agents



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

The use of Conversational Analytics is managed through a combination of [content access, data access, and feature access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management). Think of a data agent as another type of Looker content — like a dashboard, Look, or folder. To interact with data agents, you must be assigned a Looker role that has the required permissions for the models that underlie the individual Explore or that the data agent will query. In some cases, you will also need access to the agent itself.

For more information about the permissions and access that are required to manage and use data agents, see the permissions table on the [Set up Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) documentation page.

Conversational Analytics Explore agents are available when a Looker admin has enabled the following features on the **Gemini in Looker** admin page:

  * **Conversational Analytics**
    * **Advanced Analytics** : To allow your agent to use [**Advanced Analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics), which translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations, turn on the **Advanced Analytics** setting. This setting is optional.
  * **Enable Trusted Tester Features**
    * **Agentic Workflows** [[Preview](https://cloud.google.com/products#product-launch-stages)]: To create [agentic workflows](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows) that instruct your agent to monitor changes in your data.
    * **Publish to Gemini Enterprise** [[Preview](https://cloud.google.com/products#product-launch-stages)]: To publish your agent to [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs), making your agent's predefined context and analytics available to a broader audience.



## Create and edit data agents

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To create a new data agent, follow these steps:

  1. Navigate to the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics).
  2. In the **Agents** tab, select **\+ New agent**. Or, in the left panel, select spark**Manage agents** , and then select **\+ New agent**.
  3. On the **New agent** page, provide the following information about your data agent.

     * **Agent name** : Enter a name for the agent. The name should be unique and descriptive.
     * **Agent description** : Briefly describe what this agent can do and the data that it uses. Users will see this description when they select the agent to [start a conversation](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation-with-an-agent) or when you share the agent with them, so make sure that the description clearly explains the agent's purpose and how it can be helpful.
     * **Data** : Follow these steps to connect to up to five existing Looker Explores: 
       1. In the **Data** field, click **\+ Select Explores**.
       2. In the **Search Explores** window, click the Explores that you want to include in the data agent. These Explores will appear in the **Selected Explores** panel of the window.
       3. To add the selected Explore to the data agent, click **Save**.
  4. **Instructions** : Provide context to help Conversational Analytics understand how to interact with your data and provide accurate and relevant responses. For examples of the types of context that you can provide, see Writing agent instructions.

  5. Optionally, select **Advanced options** to expand the section and configure the following settings:

     * **Enable Advanced Analytics** : Turn on this setting to enable [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) for all conversations with your agent.
     * **Show thinking** : Turn on this toggle to allow the agent to display its reasoning steps, generated Looker queries, and underlying data tables in all responses in each conversation.
     * **Show debug info** : Turn on this toggle to allow the agent to display the steps that it executed for all responses in each conversation.
  6. Optionally, you can test your agent to refine your instructions and its settings.

  7. To save your new data agent, click **Save**.




After you save the data agent, you can share the agent with other users and [start a conversation](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation-with-an-agent) with the agent.

### Write agent instructions

When you create a data agent, you can add free-form instructions that define your data agent's core behavior and provide it with foundational context to consider before processing a user's prompt.

**Important:** Although the **Instructions** field is optional and the structure is up to your discretion, we recommend that you provide well-structured instructions to enable the agent to give more accurate and relevant responses.

Here are some examples of the types of context that you can provide in the **Instructions** field:

  * Key fields: The most important fields for analysis
  * Excluded fields: Fields that the data agent should avoid
  * Filtering and grouping: Fields that the agent should use to filter and group data
  * Persona: A role or expertise, character, or tone that you assign to the agent



For tips and best practices for writing agent instructions, see the [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices) documentation page.

### Define verified queries

Verified queries, also referred to as _golden queries_ in some Google documentation, are predefined pairs of natural language questions and their exact, corresponding Looker Explore queries. These question-and-query pairs act as verified "gold standards" of truth that teach your agent how to handle complex business requests without guessing. Well-defined verified queries can help improve the accuracy of responses from your Explore data agent.

#### Limits of verified queries

When using verified queries, keep the following limits in mind:

  * Verified queries are available only for Explore data agents. They aren't available for standalone conversations or for dashboard data agents.
  * You must use an Explore that's already defined for the agent. If you reference an Explore that's not used by the data agent, you'll see the error message `This query will not be used as it references an Explore that has not been defined in this agent. For best results, make sure that verified queries are based on Explores used in this agent.`
  * Verified queries don't support Explore queries that contain custom fields or pivots.
  * Although there's no limit to the number of verified queries that you can add, we recommend including no more than 30 to 50 question-and-query pairs per agent.



#### Create a verified query

**Tips for defining verified queries:**

  * Include different types of questions and queries that have a variety of filters and filter values.
  * Consider the questions that a user might ask about that Explore, and write those questions in natural language.



To add a verified query to a new or an existing data agent, follow these steps:

  1. Create a new data agent, or edit an existing data agent that uses at least one Explore as a data source.
  2. On the agent creation or edit page, select **\+ Add verified query**.
  3. Under **Add verified query** , enter the natural language question and its corresponding answer: 
     * **Question** : Enter a natural language question that a user might ask.
     * **Answer** : Paste the URL of the Explore that captures the correct query or visualization.
  4. To verify the Explore query, click **Preview**. 
     * _Alternatively_ : Leave the **Answer** field blank and click **Preview** to build a query from scratch in the Explore builder, and then save the resulting URL to use.
  5. Click **Save**.



#### Edit a verified query

To edit an existing verified query, follow these steps:

  1. In your conversation with the agent, select **Edit agent**.
  2. Under **Verified queries** , find the verified query that you want to edit.
  3. Click edit **Edit verified query**.
  4. In the **Edit verified query** dialog, make changes to the question or the answer.
  5. Click **Save**.



#### Delete a verified query

To delete a verified query, follow these steps:

  1. In your conversation with the agent, select **Edit agent**.
  2. Under **Verified queries** , find the verified query that you want to delete.
  3. Click delete **Delete verified query**.



### Test an agent

When you're creating or editing an agent, the agent details page includes the **Preview your agent** pane. You can test agent settings and instructions by [starting a conversation](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation-with-an-agent) with the agent.

You must click **Update** for a change to be reflected in the preview. If the save status is `Not saved`, any updates to settings won't be reflected in the preview.

### Edit an existing data agent

To edit an existing data agent, follow these steps:

  1. On the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics), select spark**Manage agents**.
  2. On the **Manage agents** page, select the data agent that you want to edit.
  3. Update the details about the agent as needed. You can modify the details that you specified when you created the agent, including the **Agent name** , **Agent description** , **Data** , **Instructions** , and **Advanced options** settings. You can also opt to enable the [Code Interpreter](https://docs.cloud.google.com/looker/docs/studio/conversational-analytics-looker-code-interpreter) for your agent.
  4. To save your changes, click **Update**.



## Share data agents

Sharing lets other users chat with your agent and its Explores. You can share a data agent with other users by granting content access to the agent. Only a user with the appropriate permissions and content access can share an agent. Once an agent is created, it may take a few minutes for it to become shareable.

**Note:** Granting a user content access to an agent does _not_ also grant that user access to the Explore that the agent uses. When you share an agent, make sure that the users also have the permissions that they need to use Conversational Analytics with the model that the Explore is based on. Your Looker admin may need to grant these permissions.

To share a data agent, follow these steps:

  1. On the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics), select spark**Manage agents** in the left panel.
  2. Open the menu for the chosen agent by clicking its more_vert **More options** icon, and then click **Share**.
  3. Once you have added an individual or groups to the **Who can access this agent** section, and chosen what level of permissions they should have, click **Add** to place them in the shared list.
  4. If you want new users or groups to receive a notification email, select the **Email the people you have just added** checkbox.
  5. After all changes have been made, click **Save**.



You can also share an agent that you've just created or one that you're editing by clicking person_add **Share** on the agent settings page and following the aforementioned steps.

### Revoke access to a data agent

To revoke access to an agent, follow these steps:

  1. On the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics), click spark**Manage agents** in the left panel.
  2. Open the menu for the chosen agent by clicking its more_vert **More options** icon, and then click **Share**.
  3. Click the **X** next to the user or groups that should have their access removed.
  4. After all changes have been made, click **Save**.



If the removed users have an ongoing conversation, they will still have access for a minute or two while the changes propagate.

If a user tries to ask more questions once access to an agent is removed, then that user will see the message `The agent in this conversation may not be shared with you, or may have been deleted. You can view any past conversations with the agent, but can't ask new questions.`

## Publish a data agent

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can publish your data agent in [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs), making your agent's predefined context and analytics available to a broader audience, including users who may not be familiar with the Looker interface. Gemini Enterprise serves as a central hub where users can manage data agents that were created across Google Cloud applications, which helps users to find the best agent for their analytical needs.

**Note:** The Looker – Gemini Enterprise integration is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`geintegration-feedback@google.com`](mailto:geintegration-feedback@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



### Before you begin

The procedure to create a data agent in Looker and make it available to users in Gemini Enterprise involves tasks that are performed in the Looker instance, on the Gemini Enterprise page in the Google Cloud console, and in the Gemini Enterprise instance.

Users with the following roles must follow the steps that are described in the associated sections:

  1. **Data agent editors** (Looker capability): Publish the agent in Looker.
  2. **Discovery Engine Admin** (IAM role): Grant access to the agent in the Google Cloud console.
  3. **Gemini Enterprise User** (IAM role); Data agent user (Looker capability): Chat with the agent in the Gemini Enterprise instance.



Before you can publish an agent, the following requirements must be met:

  * A Looker admin must enable the **Publish to Gemini Enterprise** setting on the **Gemini in Looker** page in the **Admin** panel.
  * A Looker admin must grant you a role that contains the [`publish_agent_externally` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#publish_agent_externally). You must also be able to edit a data agent.
  * The Looker service account on the Google Cloud project that hosts the Gemini Enterprise engine must be granted the [**Discovery Engine Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) Identity and Access Management role. Granting this role assigns a Gemini Enterprise license to the account when the first data agent is published. If no Gemini Enterprise licenses are available to assign to the Looker service account, the Gemini Enterprise engine's page in the Google Cloud console displays the error "Failed to allocate quota for agent creation." A user with the [**Discovery Engine Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) Identity and Access Management role must then provision a new Gemini Enterprise license or reassign an existing license for the Looker service account.

**Note:** Publishing data agents to Gemini Enterprise isn't supported for Looker (Google Cloud core) instances that use a [private](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) or [hybrid](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) network connection. To request access to this feature for a hybrid Looker (Google Cloud core) instance, reach out to `geintegration-feedback@google.com` with your instance URL.

### Publish a data agent to Gemini Enterprise

To complete the steps that are described in this section, you must have a Looker role that contains the [`publish_agent_externally` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#publish_agent_externally) and the appropriate permissions and content access to edit data agents.

To publish an agent, follow these steps:

  1. Edit the agent.
  2. Select **Publish settings** to open the **Agent publish settings** window.
  3. In the **Agent publish settings** window, enable the **Gemini Enterprise** setting and select **Update**. Enabling this setting publishes the agent to the Gemini Enterprise instance that is displayed on the **Gemini in Looker** page in the **Admin** panel.
  4. Once you've published your agent, you can select **Share** to grant other Looker users access to your data agent, or select **Start conversation** to [open a new conversation](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation) with the data agent.



### Grant users access to the agent in Gemini Enterprise

To complete the steps that are described in this section, you must have the [**Discovery Engine Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) Identity and Access Management role for the Google Cloud project that contains the Gemini Enterprise engine.

To be able to chat with an agent in Gemini Enterprise, a user must have access to the Gemini Enterprise instance and to the individual agent.

To grant a user access to the Gemini Enterprise instance, a **Discovery Engine Admin** must assign the user the [**Gemini Enterprise User**](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) IAM role for the Google Cloud project that contains the Gemini Enterprise engine.

To grant a user access to an individual agent, the **Discovery Engine Admin** must complete the following steps in the Google Cloud console:

  1. Navigate to the Google Cloud project that contains the Gemini Enterprise engine.
  2. Open the Gemini Enterprise product page.
  3. Select the **Apps** page from the main navigation, and then select the name of the Gemini Enterprise instance.
  4. In the main navigation, select **Agents**.
  5. Select the agent that you want to grant access to.
  6. Select the **User permissions** tab.
  7. Select **Add user**.
  8. In the **Add user permissions roles to agent** window, add each user and assign them the **Agent User** role.



### Chat with the agent in Gemini Enterprise

To complete the steps that are described in this section, you must have the [**Gemini Enterprise User**](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) Identity and Access Management role for the Google Cloud project that contains the Gemini Enterprise engine. You must also have the appropriate permissions and content access to chat with the agent in the Looker instance.

To chat with a data agent in a Gemini Enterprise instance, follow these steps:

  1. Open your Gemini Enterprise instance.
  2. Select **Agents** in the main navigation.
  3. On the **Agents** page, select that agent that you would like to chat with. When you select an agent, a conversation window opens where you can ask questions about your data.



The first time you chat with an agent, you must authorize the agent's access to your Looker identity.

### Republish a data agent in Gemini Enterprise

When Looker updates data agent features or capabilities, you must update or republish your agent so that those changes take effect in Gemini Enterprise.

> Looker 26.12 introduced support for charts in agent responses. If your agent was created prior to Looker 26.12, you must update or republish your agent for it to use charts in its responses.

To update your agent, follow these steps:

  1. Edit the data agent.
  2. Modify any of your agent's metadata.
  3. Select **Update**.



To republish your data agent, follow these steps:

  1. Edit the data agent.
  2. Select **Publish settings** to open the **Agent publish settings** window.
  3. Turn off the **Gemini Enterprise** toggle and select **Update**.
  4. Wait for the agent to be removed from Gemini Enterprise.
  5. In Looker, edit the data agent to re-open the **Agent publish settings** window.
  6. Select **Publish settings** , turn on the **Gemini Enterprise** toggle, and select **Update**. 



## Delete a data agent

**Caution:** Any users with whom you have shared this data agent won't be able to ask new questions after you delete the agent; however, existing conversations with the data agent are retained.

If you delete an agent, you will also delete and unpublish the agent in Gemini Enterprise. 

To delete a data agent, follow these steps:

  1. On the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics), click spark**Manage agents** in the left panel.
  2. Open the menu for the chosen agent by clicking its more_vert **More options** icon, and then click **Delete**.
  3. In the **Delete agent?** window, click **Move to trash** to delete the data agent.



Agents that are moved to the trash will be permanently deleted after 30 days. You can permanently delete a data agent manually, or you can restore a data agent from the trash before it is permanently deleted. If you take no action, the agent will be deleted permanently after 30 days automatically.

### Permanently delete a data agent

To permanently delete a data agent, follow these steps:

  1. Navigate to the [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics).
  2. In the left navigation panel, expand the **Trash** section.
  3. To open the menu for the chosen agent, select its more_vert icon, and then click **Delete Permanently**.
  4. In the **Are you sure?** window, click **Delete forever**.



### Restore a data agent from the trash

To restore a data agent from the trash, follow these steps:

  1. Navigate to [**Conversations** page](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#navigate-to-conversational-analytics).
  2. In the left navigation panel, expand the **Trash** section.
  3. To open the menu for the chosen agent, select its more_vert icon, and then click **Restore**.



## Related resources

  * **[Conversational Analytics in Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)** : The landing page for Conversational Analytics with a list of key features links to all Conversational Analytics documentation.

  * **[Query an Explore in natural language](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data)** : Start a conversation with a Looker Explore to ask about Explore data using natural language.

  * **[Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards)** : Query and configure dashboard agents on user-defined dashboards.

  * **[Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards)** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Use LookML to configure and manage version-controlled data agents for LookML dashboards.

  * **[Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices)** : Strategies and best practices to help Looker administrators and LookML developers successfully configure optimize Conversational Analytics.

  * **[Enable Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-code-interpreter)** : Advanced Analytics within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the Advance Analytics feature's use of Python enables more complex analysis and visualizations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
