---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist/
title: Agent Assist \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:37.224951+00:00
---

# Agent Assist  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent Assist Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up Agent Assist for Contact Center AI Platform (CCAI Platform). Agent Assist provides in-the-moment assistance to your human agents, helping them resolve customer issues faster and with greater accuracy.

## Set up Agent Assist

This section shows you how to set up Agent Assist.

### Service account requirements

To use Agent Assist, you need to [create a Google Cloud Service Account and key](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent#create-a-service-account-and-key) in the project where you [created your Agent Assist conversation profile](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent#create-cp). In addition, you must grant the following IAM roles to your service account:

  * [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient)

  * [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin)

  * [Data Labeling Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datalabeling#datalabeling.admin)


**Note:** Failure to grant the correct IAM role prevents Agent Assist from working correctly.**Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

### Add an Agent Assist platform

To add an Agent Assist platform, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Assist Platform** pane, and then click **Add platform**. The **Add an Agent Assist platform** dialog appears.

  3. In the **Name** field, enter a name for your platform.

  4. In the **Service** field, select **CCAI Conversation Profile** , and then click **Create**.

  5. Click **Upload key** to upload your JSON service account key. For more information, see Service account requirements.

  6. Click close **Close** to close the dialog.




### Configure Agent Assist for calls globally

You can use Agent Assist capabilities in the agent desktop or the call adapter, but not both.

To configure Agent Assist for calls globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Assist** pane, and then click the **Agent Assist** toggle to the on position.

  3. In the **Knowledge & Guidance** section, select one of the following options:

     * **Agent Assist Hub**. Select this option to use knowledge assist, agent coaching, and conversation summarization in the [**Agent Assist Hub**](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist-hub) panel of the agent desktop.

     * **Generative Knowledge Assist**. Select this option to use generative knowledge assist in the call adapter.

  4. In the **Conversation Insights** section, select the Agent Assist capabilities that you want, and then click **Save Agent Assist**.




### Configure Agent Assist for chats globally

You can use Agent Assist capabilities in the agent desktop or the chat adapter, but not both.

To configure Agent Assist for chats globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Assist** pane, and then click the **Agent Assist** toggle to the on position.

  3. In the **Knowledge & Guidance** section, select one of the following options:

     * **Agent Assist Hub**. Select this option to use knowledge assist, agent coaching, and conversation summarization in the [**Agent Assist Hub**](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist-hub) panel of the agent desktop.

     * **Generative Knowledge Assist**. Select this option to use generative knowledge assist in the chat adapter.

  4. In the **Conversation Insights** section, select the Agent Assist capabilities that you want. If you select the **Spelling and Grammar Check** checkbox, then the following two checkboxes appear:

     * **Allow agents to turn on/off automatic checks** : Select this checkbox to let agents turn on and off spelling and grammar check in the chat adapter.

     * **Allow agents to select languages** : Select this checkbox to let agents select the language that the chat adapter uses when checking spelling and grammar.

  5. Click **Save Agent Assist**.




### Configure Agent Assist at the queue level

To configure Agent Assist at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Depending on the channel you want, click **Edit / View** in one of the following panes: **IVR (Interactive Voice Response)** , **Mobile** , or **Web**.

  3. Click a leaf queue.

  4. In the **Settings** pane, under **Agent Assist** , click **Configure**. The **Agent Assist Profile Configuration** pane appears.

  5. In the **Platform Name** field, select a platform that you added previously. The **Profile Name** field appears.

  6. In the **Profile Name** field, select a profile.

**Note:** If you intend to use the spelling and grammar Agent Assist capability, select the `spelling-and-grammar` profile.
  7. Click **Save**. The **Settings** pane appears.

  8. Under **Agent Assist** , click the **Enable Agent Assist** toggle to the on position.

**Note:** If you click the **Agent Assist** toggle to the off position, you lose your Agent Assist configuration.



### Configure Agent Assist at the team level

You can configure Agent Assist at the team level for sessions that aren't associated with a queue. This lets you use Agent Assist with the following session types:

  * Calls to direct phone numbers

  * Calls to agent extension numbers

  * Outbound calls where no queue is selected

  * Chats transferred directly to another agent

**Note:** When a chat is transferred, the originating agent and the receiving agent see Agent Assist as it's configured for their respective teams or queues. This also applies to transfers of direct inbound calls.



If an agent belongs to multiple teams, there's a hierarchy of priority that determines which team's settings apply to the agent. For more information, see [Team priority when an agent belongs to multiple teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#team-priority-multiple-teams).

To configure Agent Assist at the team level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For the team that you want to edit, click edit **edit icon**. The **Edit Team** pane appears.

  3. Go to the **Agent Assist** section, and then click expand_more **arrow-down-icon** to expand the section.

  4. Click **Configure**. The **Agent Assist Profile Configuration** pane appears.

  5. In the **Platform Name** field, select a platform that you added previously. The **Profile Name** field appears.

  6. In the **Profile Name** field, select a profile.

**Note:** If you intend to use the spelling and grammar Agent Assist capability, select the `spelling-and-grammar` profile.
  7. Click **Save**.

  8. Click the **Enable Agent Assist** toggle to the on position.

**Note:** If you click the **Agent Assist** toggle to the off position, you lose your Agent Assist configuration.



## Agent Assist for calls

The following call capabilities are available with Agent Assist. To enable these capabilities, select them when you turn on and configure Agent Assist for calls.

  * **Knowledge assist**. Provides suggestions for knowledge articles to human agents during a call. These suggestions are based on the dialog between the agent and the end-user. An agent can examine the suggestions and decide which to share with the end-user. You must [create a knowledge base](https://docs.cloud.google.com/agent-assist/docs/knowledge-base) to use knowledge assist. For quota requirements, see [Generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/quotas#generative_knowledge_assist).

  * **Generative knowledge assist**. Provides suggestions for generated knowledge articles to human agents during a call. These suggestions are based on the dialog between the agent and the end-user. For more information, see [generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/generative-knowledge-assist). For quota requirements, see [Generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/quotas#generative_knowledge_assist).

  * **Agent coaching**. This capability is available only in the [Agent Assist hub](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist-hub) panel in the agent desktop. Agent coaching provides guidance to agents in the form of coaching cards that appear during a session. These cards can include guidance on what to say, compliance reminders, or suggestions for actions to take next.

  * **Proactive generative knowledge assist**. Follows the ongoing conversation between an agent and end-user. It proactively provides search query suggestions based on the conversation context. For more information, see [generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/generative-knowledge-assist). For quota requirements, see [Proactive generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/quotas#proactive_generative_knowledge_assist).

  * **Sentiment analysis**. Analyzes messages in real time from both the human agent and the end-user to determine emotional intent. The score is visible in the agent adapter. For quota requirements, see [Sentiment analysis](https://docs.cloud.google.com/agent-assist/docs/quotas#sentiment_analysis).

  * **Real-time call transcription**. Transcribes calls in real time for agents to reference during the call or for analysis after the call. For quota requirements, see [Voice transcription](https://docs.cloud.google.com/agent-assist/docs/quotas#voice_transcription).

  * **Generative AI session summarization**. Displays a generated summary in the agent adapter when the call enters wrap-up. If there was a single human agent in the session, the summary is for the entire session. If there were multiple human agents in the session, the session is divided into segments, one for each human agent that participated. In that case, each human agent sees a summary for the segment that they participated in. An agent can insert the summary, along with their own notes, during wrap-up. The agent can then submit the summary and notes to your CRM or external storage, depending on your configuration. For more information, see [Summarization with custom sections](https://docs.cloud.google.com/agent-assist/docs/summarization-with-custom-sections). For quota requirements, see [Summarization](https://docs.cloud.google.com/agent-assist/docs/quotas#summarization).

  * **Summarization automatic evaluation**. Assesses the quality of AI generated summaries based on three metrics: accuracy, completeness, and adherence. This feature helps to evaluate the quality of summarization generators, which is crucial when tuning custom section definitions or upgrading versions that affect summarization quality. For more information, see [Summarization automatic evaluation](https://docs.cloud.google.com/agent-assist/docs/summarization-autoeval-metrics). For quota requirements, see [Summarization autoevaluation](https://docs.cloud.google.com/agent-assist/docs/quotas#summarization_autoevaluation).




### Agent experience

The following sections explain the agent experience for each Agent Assist capability.

#### Knowledge assist

This feature follows a conversation between a live agent and an end-user and provides the live agent with relevant document suggestions. Agents are alerted to knowledge assist document suggestions when the Agent Assist icon in the agent adapter has a green dot next to it.

  1. Click the **Agent Assist icon** to view the suggestions in the Knowledge tab in the agent adapter.

  2. Click the **External Link icon** next to a suggested article to share a document with the end-user.




#### Generative knowledge assist

**Note:** If a call is transferred to another agent, the knowledge articles will remain accessible to the new agent until the session ends or the transferring agent exits.

To see suggestions from generative knowledge assist, follow these steps:

  1. **Start a voice call** :

     * As soon as a voice support session begins, the generative AI knowledge assist panel will become active.
  2. **View knowledge suggestions** :

     * The system listens to the ongoing conversation and generates knowledge suggestions based on both the agent's and end-user's dialogue.

     * These suggestions appear as **Clickable tiles** in the Contact Center AI Platform agent voice adapter.

     * Each tile includes a **Title** and a short **Preview of the article**. Clicking the tile opens the full article in a new browser tab, so agents can view more detailed information.

  3. **Searching for articles** :

     * If agents need to search for a specific topic, they can manually enter keywords in the **Knowledge base search** field within the same panel.

     * Matching articles will appear in a similar tile format, allowing agents to click through and view the content.




#### Real-Time sentiment analysis

Sentiment Analysis evaluates the conversation between a human agent and an end-user to determine emotional intent. The analysis is generated in real-time to display the sentiment of the present session, or as a one-time score upon Virtual Agent escalation. Sentiment Analysis is available for both Voice and Chat.

_For Voice_ : The Sentiment feature panel displays on the Agent Adapter during a live session.

**Sentiment Analysis breakdown**

The Real-Time Sentiment Analysis displays 3 scores: last, session, and previous leg.

A (**\--**) displays when no score is available.

|   
---|---  
**last** | sentiment score for the last consumer response (updates in real-time)  
**session** | current average sentiment score (updates in real-time)  
**prev. leg** | average sentiment score of the previous segment  
  
There are three sentiments types (neutral, happy, and negative) in the Real-Time Sentiment Analysis and scores displayed fall into the following ranges:

  * Over 63 = Happy

  * Between 38 and 63 = Neutral

  * Below 38 = Negative




During the session, the Real-Time Sentiment Analysis scores are sent to the Agent Adapter. After the session, the session's average score will be posted in the CRM ticket.

#### Generated session summarization

If configured, you can add a generated summarization to your wrap-up notes for the segment of the call that you handled.

To add a generated session summarization to your wrap-up notes, follow these steps:

  1. End a call in the call adapter. The **Wrap-up** pane appears.

  2. In the **Notes** field, add your notes.

  3. Click ![The Agent Assist icon.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-assist-icon.png)**Agent Assist**. A generated session summary appears.

  4. Click **Insert summary** to add the summary to your notes.

  5. Edit or add to the notes as needed, and then click **Submit**.




## Agent Assist for chat

The following chat capabilities are available with Agent Assist. To enable these capabilities, select them when you turn on and configure Agent Assist for chat.

  * **Smart reply**. Provides chat responses to your human agents in real time during a conversation. For quota requirements, see [Smart reply](https://docs.cloud.google.com/agent-assist/docs/quotas#smart_reply).

  * **Generative knowledge assist**. Provides suggestions for generated knowledge articles to human agents during a chat. These suggestions are based on the dialog between the agent and the end-user. For more information, see [generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/generative-knowledge-assist). For quota requirements, see [Generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/quotas#generative_knowledge_assist).

  * **Agent coaching**. This capability is available only in the [Agent Assist hub](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist-hub) panel in the agent desktop. Agent coaching provides guidance to agents in the form of coaching cards that appear during a session. These cards can include guidance on what to say, compliance reminders, or suggestions for actions to take next.

  * **Proactive generative knowledge assist**. Follows the ongoing conversation between an agent and end-user. It proactively provides search query suggestions based on the conversation context. For more information, see [generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/generative-knowledge-assist). For quota requirements, see [Proactive generative knowledge assist](https://docs.cloud.google.com/agent-assist/docs/quotas#proactive_generative_knowledge_assist).

  * **Sentiment analysis**. Analyzes messages in real time from both the human agent and the end-user to determine emotional intent. The score is visible in the agent adapter. For quota requirements, see [Sentiment analysis](https://docs.cloud.google.com/agent-assist/docs/quotas#sentiment_analysis).

  * **Generative AI session summarization**. Displays a generated summary of the conversation when the chat session enters wrap-up. This summary provides a brief overview of the chat session, including the resolution, situation, and action. If there are multiple segments in the session, the summary is available at the segment level. A segment is created each time there is a transfer to a human or virtual agent. The agent can insert the summary along with their own notes. The agent can then submit the summary and notes to your CRM or external storage, depending on your configuration. For quota requirements, see [Summarization](https://docs.cloud.google.com/agent-assist/docs/quotas#summarization).

  * **Spelling and grammar correction**. Provides spelling and grammar suggestions for messages that agents type into the message field of the chat adapter. Spelling and grammar correction is available for the Mobile, Web, SMS, and WhatsApp channels. For quota requirements, see [Before you begin](https://docs.cloud.google.com/agent-assist/priv/docs/spell-grammar#before_you_begin) in the Agent Assist documentation.

**Important:** Spelling and grammar correction is in [Preview](https://cloud.google.com/products#product-launch-stages). To enable spelling and grammar correction, contact your Google Cloud account team to request access. After you have access, the option to select **Spelling and grammar correction** appears in the **Conversational Profiles** settings page. For more information, see [Create conversation profile](https://docs.cloud.google.com/agent-assist/docs/conversation-profile).



### Agent experience

The following sections explain the agent experience for each Agent Assist capability.

#### Smart Reply

Smart Reply suggests chat responses to the agent using context from the ongoing conversation. The suggested responses are in bubbles above the text entry box.

**How it works** : Suggestions appear above the text entry field. Select the suggestion that you want and paste it into the field and send the reply to the end-user.

#### Knowledge Assist

This feature follows a conversation between a human agent and an end-user and provides the human agent with relevant document suggestions.

**How it works** : The Knowledge Assist button is located in the top right hand corner of the Agent Adapter. A pink circle indicates that articles are available. Click the icon to show the articles. The icon expands to show a list of articles.

Click the **Share** button next to the article to send it to the end-user.

#### Generative knowledge assist

To see suggestions from generative knowledge assist, follow these steps:

  1. **Start a chat session** :

     * Once the chat session is active, Generative AI Knowledge Assist begins providing suggestions based on the conversation.
  2. **View knowledge suggestions** :

     * As the chat continues, the system analyzes both end-user and agent messages and displays relevant article suggestions as **Clickable tiles**.

     * Each tile shows a **Title** and a **Preview snippet**. Click the tile to open the article in a new tab for further reading.

  3. **Searching for articles** :

     * Agents can manually search for specific knowledge articles by entering keywords into the **Knowledge base search** field

     * Search results appear as tiles, similar to automatic suggestions, and can be clicked to view the article


**Note:** If a chat is transferred to another agent, the knowledge articles remain accessible to the new agent until the session ends or the transferring agent exits.

#### Real-Time Sentiment Analysis

Sentiment Analysis evaluates the conversation between a human agent and end-user to determine emotional intent. The analysis is generated in real-time to display the sentiment of the present session, or as a one-time score upon Virtual Agent escalation. Sentiment Analysis is available for both Voice and Chat.

**Sentiment Feature Panel**

_For Chat_ : The Sentiment feature panel will be displayed in an open state **by default** for all new chats. Click the **X** or the **Sentiment Stars Icon** to open or hide the panel.

**Sentiment Analysis breakdown**

The Real-Time Sentiment Analysis displays 3 scores: last, session, and previous leg.

A (**\--**) displays when no score is available.

Score | Description  
---|---  
**last** | Sentiment score for the last consumer response. Updates in real time.  
**session** | Current average sentiment score. Updates in real time.  
**prev. leg** | Average sentiment score of the previous segment.  
  
There are three sentiments types (neutral, happy, and negative) in the Real-Time Sentiment Analysis and scores displayed fall into the following ranges:

  * 40-75 = Neutral
  * Over 75 = Happy
  * Below 30 = Negative



During the session, the Real-Time Sentiment Analysis scores are sent to the Agent Adapter. After the session, the session's average score will be posted in the CRM ticket.

#### Generated session summarization

If configured, you can add a generated summarization to your [wrap-up](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat#wrap-up) notes for the segment of the chat session that you handled.

To add a generated segment session summarization to your wrap-up notes, follow these steps:

  1. End a chat in the chat adapter. The **Wrap-up** pane appears.

  2. In the **Notes** field, add your notes.

  3. Click ![The Agent Assist icon.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-assist-icon.png)**Agent Assist**. A generated session summary appears.

  4. Click **Insert summary** to add the summary to your notes.

  5. Edit or add to the notes as needed, and then click **Submit**.




## Interaction history

You can configure CCAI Platform to display the support interaction history for an end-user in the agent adapter during a session. This provides context in real time to help agents provide a better support experience and improve handle time. Managers can also view an end-user's interaction history while monitoring sessions in real time.

Saving session summarizations for interaction history requires integration with a CRM or configuring external storage.

### Before you begin

Before you can use interaction history, you must do the following:

  1. Set up Agent Assist.

  2. Do one of the following, or both, depending on your use case:

     * Configure session summarization for calls. To do this, follow these steps:

       1. Turn on and configure Agent Assist for calls. In the **Agent Assist** pane, select the **Gen AI session Summarization** and **Call details view** checkboxes.

       2. Click **Save Agent Assist**.

     * Configure session summarization for chat. To do this, follow these steps:

       1. Turn on and configure Agent Assist for chat. In the **Agent Assist** pane, select the **Gen AI session Summarization** and **Chat details view** checkboxes.

       2. Click **Save Agent Assist**.




### Configure interaction history

To configure interaction history, do the following:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Interaction History** pane.

  3. Do one of the following, or both, depending on your use case:

     * For **Call** , select the **Session Summary** checkbox.

     * For **Chat** , select the **Session Summary** checkbox.

  4. For **Data Retrieval** , select the period of time for which you want to retrieve interaction history. Retrieving interaction history doesn't delay the start of a call or chat session because the data is loaded into the agent adapter after the session connects.

  5. Click **Save**.




### Configure external storage to save session summaries

If your instance is not integrated with a CRM, you need to configure external storage to save session summaries that can appear in interaction history.

To configure external storage to save session summaries, follow the instructions in [External storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage), while including the following steps:

  1. Select the **Session Summaries** checkbox.

  2. For **Session Summaries** , add a path for your session summaries—for example, `session-summaries/{simple_session_type}-{session_id}`.




### View session summaries

You can view historical and ongoing session summaries when viewing a connected call or chat session. Each session summary includes a summary for the entire session as well as summaries for each completed session segment.

To view session summaries, follow these steps:

  1. In the CCAI Platform portal, click **Calls > Connected**. If you don't see the **Calls** menu, click menu **Menu**. The **Connected Calls** pane appears.

  2. In the **Actions** column, for the connected call that you want, click more_horiz **More** and then **Call Details**. The interaction history appears in the **Call Details** dialog.




To view interaction history for a connected chat session, follow these steps:

  1. In the CCAI Platform portal, click **Chat > Connected**. If you don't see the **Chat** menu, click menu **Menu**. The **Connected Chats** pane appears.

  2. In the **Actions** column, for the connected chat that you want, click more_horiz **More** and then **Chat Details**. The interaction history appears in the **Chat Details** dialog.




### Agent experience

Agents can view interaction history from the agent adapter in real time.

To view interaction history from the call adapter, follow these steps:

  1. Answer a call. For more information, see [Agent call adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls).

  2. Click **Details**. The **Call details** pane appears.

  3. Click **Previous interactions**. The **Previous interactions** pane appears. If you have previous interactions, they appear in this pane. Otherwise, **No summary available** appears.

  4. Click ![A clipboard icon that you click to see generated
summaries.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/clipboard-icon.png)**Generated summaries** to see generated summaries for each interaction.

  5. Click chevron_right **Forward** next to an interaction to see an expanded view of the generated summary.




To view interaction history from the chat adapter, follow these steps:

  1. Answer a chat request. For more information, see [Handle a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat).

  2. Click ![Details icon to open the Details pane in the agent
adapter.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-person.png)**Details**. The **Details** pane appears.

  3. Click **Previous interactions**. The **Previous interactions** pane appears. If you have previous interactions, they appear in this pane. Otherwise, **No summary available** appears.

  4. Click ![A clipboard icon that you click to see generated
summaries.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/clipboard-icon.png)**Generated summaries** to see generated summaries for each interaction.

  5. Click chevron_right **Forward** next to an interaction to see an expanded view of the generated summary.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
