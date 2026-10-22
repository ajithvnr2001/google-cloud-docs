---
url: https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents/
title: Data agents in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:30.728894+00:00
---

# Data agents in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data agents in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

Data agents let you curate the [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview) experience for your data. When you create with an agent, you can provide it with context and instructions to answer questions more effectively for specific use cases. Agents empower analysts to map business terms to specific fields, specify the best fields for filtering, and define custom calculations.

The Conversational Analytics data agent experience differs between [legacy and new Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience). Select the **Legacy** tab or the **New** tab to learn more about the how conversations operate for each experience.

### New

Conversational Analytics data agents become available in Data Studio after they are first created in BigQuery and shared with Data Studio users.

This tab guides you through the following tasks:

  * Create and share a data agent
  * Edit a data agent
  * Chat with an agent



## Create and share a data agent

To create an agent in BigQuery and grant other users access to chat with it in BigQuery and Data Studio, follow the steps in the [Create data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#share-agent-data-studio) documentation page. Once the data agent is published, it will appear automatically in the list of agents on the **Chat with your data** page in Data Studio.

You can also copy a link from the agent in BigQuery from the agent card or the **Details** panel. From the agent card, select more_vert **Open actions** ; next, select **Copy link** , and then select **Data Studio**. From the **Details** panel, select content_copy**Copy agent link** , and then select **Data Studio**.

## Edit a data agent

Data agents are edited in BigQuery. You can [edit the agent in BigQuery](https://docs.cloud.google.com/bigquery/docs/create-data-agents#edit-agent) directly or select edit **Edit in BigQuery** from the agent **Details** panel to open the agent from Data Studio.

From BigQuery, you can revoke access to the agent or delete it.

## Chat with an agent

Data agents appear on the **Chat with your data** page. To access the **Chat with your data** page, select **Conversational Analytics** from the Data Studio navigation.

To [start a conversation with a data agent](https://docs.cloud.google.com/data-studio/conversational-analytics-data#start-a-conversation), follow these steps:

  1. Navigate to the **Chat with your data** page.
  2. Select the data agent that you'd like to converse with. You can use the **Search agents** bar to narrow down your search if needed. An agent may be unavailable if you lack the [permissions to access and chat with the agent](https://docs.cloud.google.com/bigquery/docs/create-data-agents#required-roles). You can also narrow down agents by selecting the Google Cloud project from the drop-down menu beside the search bar. When you select a project, only agents that were created in that project in BigQuery are displayed.
  3. To start the conversation, [enter your question](https://docs.cloud.google.com/data-studio/conversational-analytics-data#ask-questions) and press return (Mac) or Enter (PC).



To return to the **Chat with your data** page to chat with a different data agent, select **\+ New conversation** from the main navigation.

You can return to the conversation from the **schedule Recent** section.

## Learn more about a data agent

Data agent cards and their **Details** panel display key information about data agents.

### Agent card

The agent card appears on the **Chat with your data** page. It shows the following information about the data agent:

  * **Agent** : The name of the agent, as written the agent creator
  * **Description** : The description of the agent, as written by the agent creator
  * **Updated** : The timestamp of when the agent was last published from within BigQuery
  * more_vert **Open actions** : A menu with the following options: 
    * **Details** : Opens the **Details** panel
    * **Edit in BigQuery** : Opens the agent configuration in BigQuery
    * **Copy link** : Copies the link to the agent. Pasting this link in a web browser opens a new conversation with the agent.
    * **Send Feedback** : Opens a panel where you can submit feedback about your experience with the agent



### Agent details

The **Details** panel appears when you're chatting with a data agent. It shows the following information about the data agent:

  * **Agent** : The name of the agent, as written the agent creator
  * **Description** : The description of the agent, as written by the agent creator
  * A link to edit the agent in BigQuery
  * A link to copy the URL for the data agent. Pasting this link in a browser opens a new conversation with the data agent.
  * **Knowledge sources** : The BigQuery tables, views, or [user-defined functions (UDF)](https://docs.cloud.google.com/bigquery/docs/user-defined-functions) that you want to use as knowledge sources
  * **Project** : The Google Cloud project that contains the data agent
  * **Labels** : The [labels](https://docs.cloud.google.com/bigquery/docs/labels-intro) that were assigned to the BigQuery resources, if any
  * **Last published** : The timestamp of when the agent was last published from within BigQuery
  * **Created** : The timestamp of when the agent was created in BigQuery



### Legacy

This tab guides you through the following tasks:

  * Create and edit data agents
  * Start a conversation with an agent
  * Share data agents



## Create and edit data agents

To create a new data agent, follow these steps:

  1. In Conversational Analytics, on the **Chat with your data** page, select the **Agents** tab.
  2. Select **\+ Create agent**. Or, in the left navigation panel, select ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/spark/default/24px.svg)**Manage agents** , and then select **\+ Create agent**.
  3. On the **New agent** page, provide the following information about your data agent.

     * **Agent Name** : Enter a name for the agent. The name should be unique and descriptive.
     * **Description** : Briefly describe what this agent can do and the data that it uses. Users will see this description when they select the agent to [start a conversation](https://docs.cloud.google.com/data-studio/conversational-analytics-data#start-a-conversation-with-an-agent-legacy) or when you share the agent with them, so make sure it clearly explains the agent's purpose and how it can be helpful.
     * **Data** : Connect to a new or existing data source by following these steps:

       1. In the **Data** field, click **Select data**.
       2. In the **Select data for Agent** window, click the name of a data source.
       3. Click **Select** to add the selected data source to the data agent.

Alternatively, you can select **Connect to data** in the **Select data for agent** window to create a new data source.

Once you've selected an initial data source, you can't select a new data source. You can manage the fields that appear in the Looker Explore by selecting open_in_new **View fields**.

  4. **Instructions** : Provide context to help Conversational Analytics understand how to interact with your data and provide accurate and relevant responses. For examples of the types of context that you can provide, see Writing agent instructions.

  5. To save your new data agent, click **Save**.




After you save the data agent, you can share the agent with other users so that they can start a conversation with the agent.

### Write agent instructions

When you create a data agent, you can provide the following types of context in the **Instructions** field:

  * **Synonyms** : Alternative terms for key fields
  * **Key fields** : The most important fields for analysis
  * **Excluded fields** : Fields that the data agent should avoid
  * **Filtering and grouping** : Fields that the agent should use to filter and group data



Here are some sample instructions to adjust and test with your agent:

  * Unless stated otherwise, always filter the data on `Order Items Created Year = 2024`
  * We consider "loyal" customers to be those with `Order Items Count > 5`
  * If someone says anything about "Location," that means User City
  * If the question mentions "Seniors", those are users with `User Age > 65`
  * If a question is about Revenue, use Total Sales
  * When someone says "by product", unless they specifically say "name", group by `product category`
  * "Successful" orders means that Order Items status = "Complete"
  * Whenever there is a question of a timeline, or over time, always use `Order Item Created Date` as the field to group by



### Test an agent

When you're creating or editing an agent, the agent details page includes the **Preview your agent** pane. You can test agent settings and instructions by starting a conversation with the agent.

You must click **Update** for a change to be reflected in the preview. If the save status is `Changes not saved`, any updates to settings won't be reflected in the preview.

### Edit an existing data agent

To edit an existing data agent, follow these steps:

  1. In Conversational Analytics, click ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/spark/default/24px.svg)**Manage agents**.
  2. On the **Manage agents** page, select the data agent that you want to edit.
  3. Update the details about the agent as needed. You can modify the details that you specified when you created the agent, including the **Agent Name** , **Description** , and **Instructions** fields.

While you can't change the data source that is associated with an agent in the **Data** field, you can [manage the fields](https://docs.cloud.google.com/data-studio/edit-a-data-source) by selecting open_in_new **Manage fields**.

  4. To save your changes, click **Update**.




## Start a conversation with an agent

You can start a conversation with a data agent that you created or that another user has shared with you. To start a conversation with an agent, follow these steps:

  1. In the left navigation panel, click **\+ Create conversation**.
  2. In the **Agents** tab, select the agent that you want to start a conversation with.
  3. Type in your question and press return (Mac) or Enter (PC) to start the conversation.



You can return to the conversation from the **schedule Recent** section.

## Share data agents

Only the owner of a data agent can share an agent. The recipients of a shared data agent can see the agent's description but cannot edit the agent. Once an agent is created, it may take a few minutes for it to become shareable.

**Note:** Granting a user access to an agent does _not_ also grant that user access to the data source that the agent uses. When you share an agent, make sure that the users also have access to the data source.

### Share a data agent

To share a data agent, follow these steps:

  1. In Conversational Analytics, click ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/spark/default/24px.svg)**Manage agents**.
  2. Hold your cursor over the data agent and select person_add **Share data agent** , or select **person_add Share** while editing an existing data agent.
  3. You can invite specific people or Google Groups to share the agent. You can also share more broadly by turning on link sharing for a report.
  4. Once you have added the individuals or groups to the **People with Access** section, click **Done**.



The recipient will receive an email with a link to the data agent and should save that link for future use. When a user selects Create conversation, agents that have been shared with them will appear under **Agents**. After an agent is initially shared, users won't be able to view the instructions for that agent. Include any relevant information in the agent description.

### Revoke access to a data agent

To revoke access to an agent, remove the person or group from the list of **People with access** in the **Share** menu of the agent. If the removed user has an ongoing conversation, they will still have access for a minute or two while the changes propagate.

If a user tries to ask more questions once access to an agent is removed, then that user will see the message `The agent in this conversation may not be shared with you, or may have been deleted. You can view any past conversations with the agent, but can't ask new questions.`

## Delete a data agent

To delete a data agent, follow these steps:

  1. In Conversational Analytics, click ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/spark/default/24px.svg)**Manage agents**.
  2. On the **Manage agents** page, hold your cursor over the data agent that you want to delete.
  3. Click more_vert **More options**.
  4. Select delete **Delete**.
  5. In the **Move to trash** window, click **Move to trash** to delete the data agent.



Agents that are moved to the trash will be permanently deleted after 30 days. You can permanently delete a data agent manually, or you can restore a data agent from the trash before it is permanently deleted.

#### Permanently delete a data agent

To permanently delete a data agent, follow these steps:

  1. Navigate to Conversational Analytics.
  2. In the left navigation panel, expand the **Trash** section.
  3. Select the data agent that you want to delete.
  4. In the **Are you sure?** window, click **Delete forever**.



#### Restore a data agent from the trash

To restore a data agent from the trash, follow these steps:

  1. Navigate to Conversational Analytics.
  2. In the left navigation panel, expand the **Trash** section.
  3. Select the data agent that you want to restore.
  4. In the **Are you sure?** window, click **Restore**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
