---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-conversations/
title: Analyze data with conversations \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:52.576320+00:00
---

# Analyze data with conversations  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-conversations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Analyze data with conversations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create, edit, and delete conversations in Cloud SQL for MySQL. Conversations are persisted chats with a [data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents). 

You can ask data agents multi-part questions that use common terms—for example, "sales" or "most popular"—without specifying table field names, or defining conditions to filter the data. The chat response provides the answer to your question as text and code, and it generates charts when appropriate. The response includes the reasoning behind the results.

You can create a conversation with a data agent. When you create a direct conversation, the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview) interprets your question without the context and processing instructions offered by a data agent.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the Cloud SQL, Data Analytics API with Gemini, and Gemini for Google Cloud APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,geminidataanalytics.googleapis.com,cloudaicompanion.googleapis.com)




### Required roles

To work with data agents, you must have IAM permissions that match your use case. The following table lists required roles based on whether you're creating and publishing agents, provisioning agents in Gemini Enterprise, or discovering and using agents. For more information, see [Conversational Analytics API Identity and Access Management roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

Use case | Required roles  
---|---  
Create, edit, publish, share, and delete agents | 

  * To create data agents in a project: Gemini Data Analytics Data Agent Creator (`roles/geminidataanalytics.dataAgentCreator`) on the project. This role automatically grants you the Gemini Data Analytics Data Agent Owner role on the data agents that you create.
  * To edit, share, or delete a data agent: Gemini Data Analytics Data Agent Owner (`roles/geminidataanalytics.dataAgentOwner`) on the agent or project.
  * To edit a data agent in a project: Gemini Data Analytics Data Agent Editor (`roles/geminidataanalytics.dataAgentEditor`) on the project.
  * To view data agents in a project: Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`) on the project.
  * Additionally, you must have the following roles to create or edit a data agent: 
    * An IAM user or service account added at the instance level. For more information, see [Add an IAM policy binding to a user, service account, or group](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-policy-binding).
    * The `cloudsql.studioUser` and `cloudsql.instanceUser` roles granted to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
    * Optional: If you use context sets ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) with your database data agent, to create, upload, and manage context sets: the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role granted to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
    * Database privileges granted to an IAM user or service account by signing in as the password-based user of the database. 
          
          GRANT ALL PRIVILEGES ON *.* TO 'your-iam-user@example.com';

For more information, see [Grant database privileges to an individual IAM user or service account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#grant-db-privileges).

  
Provision agents in Gemini Enterprise |  To make a published agent available to users in Gemini Enterprise, you need permissions to [register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent) in the Gemini Enterprise administration console.  
Discover and use agents | 

  * To chat with data agents: Gemini Data Analytics Data Agent User (`roles/geminidataanalytics.dataAgentUser`).
  * To view all data agents in the project: Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`).

  
  
When you manage access to Cloud SQL for MySQL database resources, consider the following layers of permissions:

  * Google Cloud IAM: controls access to the database instance as a cloud resource. This includes permissions to connect, manage the instance, and execute SQL queries, for example, using the `executeSql` permission.
  * Database permissions: control access to objects in the database—like tables, views, and schemas. These are managed using SQL commands like `GRANT` and database-specific user and role systems.



For Cloud SQL for MySQL, you need appropriate Cloud SQL IAM roles to connect to the instance and be authorized to send queries. To interact with objects like tables and views, the connecting database user must have the necessary privileges granted using the Cloud SQL for MySQL `GRANT` system. For more information, see [About Cloud SQL for MySQL users](https://docs.cloud.google.com/sql/docs/mysql/users#mysql-roles). If the agent uses a service account, you can get a database role assigned. For example, see [Manage users with IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users). 

## Create conversations

You can create persistent conversations with an agent or with a data source in the Google Cloud console for Cloud SQL for MySQL from the **Agent Catalog** tab on the **Agents** page.

### Create a conversation with a data agent

To create a conversation with a data agent, you first [create a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents) and publish it. You can also initiate a conversation with agents that others share with you.

To create a conversation with a data agent in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the Cloud SQL for MySQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. From either the **My agents** or **Shared by others in your organization** section, click the agent card of the agent that you want to chat with.

  5. Click **Start a Conversation**. A new chat panel opens.

  6. In the **Ask a question** field, enter a question for the data agent. For example, "What were our total sales last quarter?" or "Show me the top 5 users by session time." You can also click one of the Gemini-suggested questions to get started.

The data agent responds by stating the action that it's taking to address your question, and then the data agent returns the results.

To see each step that the data agent takes to provide the answer to your question, click **Show reasoning** to view each message in the agent's reasoning process.

To see information about how the results were calculated, click keyboard_arrow_down **How was this calculated?** The **Summary** section now includes a generated query followed by the query result. You can copy the code and then click **Studio** to paste the code in the query editor.

When appropriate for the data, the data agent provides charts, tables, and other visualizations. To view your chat history, go to the **Conversation Management** list.

To view agent information, go to the **Details** panel. This panel includes a description of the agent and its knowledge sources.




## Manage conversations

You can open, rename, or delete a conversation on the **Agents** page.

### Open an existing conversation

  1. In the Google Cloud console, go to the Cloud SQL for MySQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. On the **Conversations** tab, in the conversations list, click the conversation you want to open.




### Rename a conversation

  1. In the Google Cloud console, go to the Cloud SQL for MySQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. On the **Conversations** tab, in the conversations list, click the conversation you want to rename.

  5. Click more_vert **View actions** > **Rename**.

  6. In the **Rename conversation** dialog, enter a new name for the conversation in the **Conversation name** field.

  7. Click **Rename**.




### Delete a conversation

  1. In the Google Cloud console, go to the Cloud SQL for MySQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. On the **Conversations** tab, in the conversations list, click the conversation you want to delete.

  5. Click more_vert **View actions** > **Delete**.

  6. In the **Delete conversation?** dialog, click **Delete**.




## Locations

Conversational analytics operates globally; you can't choose which region to use.

## What's next

  * Learn more about [conversational analytics in Cloud SQL for MySQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql). 
  * Learn more about the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview).
  * [Create a data agent in Cloud SQL for MySQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
