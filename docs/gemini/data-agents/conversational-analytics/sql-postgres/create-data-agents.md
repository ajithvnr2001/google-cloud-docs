---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents/
title: Create data agents \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:52.706346+00:00
---

# Create data agents  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Create data agents Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Conversational data agents let you interact with your database data using a natural language interface. By building these agents, you help users "talk to their data," unlocking insights from operational databases without requiring them to write complex SQL queries.

At a high level, a data agent is a combination of persona, a set of data sources, with access to a set of business knowledge critical for its purposes. 

For application developers, these agents provide the following benefits:

  * High accuracy: by using authored context, you can achieve high accuracy for specific business questions. _Authored context_ is the primary key factor that agent creators can use to improve accuracy. It includes schema descriptions, system instructions, and structured context that provides additional information about expected database queries.
  * Reduced complexity: agents translate natural language into SQL queries, execution, and even data summarization or visualization.
  * Flexibility: you can draft agents for personal testing, or you can publish them to make them available to other users in your project or programmatically using the API.



## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the Cloud SQL, Data Analytics API with Gemini, and Gemini for Google Cloud APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,geminidataanalytics.googleapis.com,cloudaicompanion.googleapis.com)




### Required roles

To work with data agents, you must have IAM permissions that match your use case. The following table lists required roles based on whether you're creating and publishing agents, provisioning agents in Gemini Enterprise, or discovering and using agents. For more information, see [Conversational Analytics API IAM roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

Use case | Required roles  
---|---  
Create, edit, publish, share, and delete agents | 

  * To create data agents in a project: Gemini Data Analytics Data Agent Creator (`roles/geminidataanalytics.dataAgentCreator`) on the project. This role automatically grants you the Gemini Data Analytics Data Agent Owner role on the data agents that you create.
  * To edit, share, or delete a data agent: Gemini Data Analytics Data Agent Owner (`roles/geminidataanalytics.dataAgentOwner`) on the agent or project.
  * To edit a data agent in a project: Gemini Data Analytics Data Agent Editor (`roles/geminidataanalytics.dataAgentEditor`) on the project.
  * To view data agents in a project: Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`) on the project.
  * Additionally, you must have the following roles to create or edit a data agent: 
    * An IAM user or service account added to the instance. For more information, see [Manage users with IAM database authentication for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles).
    * The `cloudsql.studioUser` and `cloudsql.instanceUser` roles granted to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
    * Optional: If you use context sets ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) with your database data agent, to create, upload, and manage context sets: the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role granted to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
    * Database privileges granted to an IAM user or service account by signing in as the `postgres` user. 
          
          GRANT ALL ON SCHEMA public TO public;

For more information, see [Grant database privileges to an individual IAM user or service account](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges).

  
Provision agents in Gemini Enterprise |  To make a published agent available to users in Gemini Enterprise, you need permissions to [register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent) in the Gemini Enterprise administration console.  
Discover and use agents | 

  * To chat with data agents: Gemini Data Analytics Data Agent User (`roles/geminidataanalytics.dataAgentUser`).
  * To view all data agents in the project: Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`).

  
  
When you manage access to Cloud SQL for PostgreSQL database resources, consider the following layers of permissions:

  * Google Cloud IAM: controls access to the database instance as a cloud resource. This includes permissions to connect, manage the instance, and execute SQL queries, for example, using the `executeSql` permission.
  * Database permissions: control access to objects in the database—like tables, views, and schemas. These are managed using SQL commands like `GRANT` and database-specific user and role systems.



For Cloud SQL for PostgreSQL, you need appropriate Cloud SQL IAM roles to connect to the instance and be authorized to send queries. To interact with objects like tables and views, the connecting database user must have the necessary privileges granted using the Cloud SQL for PostgreSQL `GRANT` system. For more information, see [About PostgreSQL users and roles](https://docs.cloud.google.com/sql/docs/postgres/users#postgresql-roles). If the agent uses a service account, you can get a database role assigned. For example, see [Manage users with IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles). 

## Create a data agent

The following sections describe how to create a data agent. After you create an agent, you can edit its settings.

### Configure basics

  1. In the Google Cloud console, go to the Cloud SQL for PostgreSQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. Click the **Agents** tab.

  5. Select a database and sign in using your IAM account.

  6. Click **New agent**. The **New agent** page opens.

  7. In the **Editor** section, in the **Agent name** field, enter a descriptive name for the data agent—for example, `Q4 sales data` or `User activity logs`.

  8. In the **Agent description** field, enter a description of the data agent. A good description explains what the agent does, what data it uses, and helps you determine if this is the correct data agent to use for a conversation—for example, `What are the top 10 selling products in Q2?`

  9. In the **Knowledge sources** section, click **Add source**. The **Add data** page opens.

  10. Select tables that the agent will focus on when answering questions. To view additional knowledge sources, select keyboard_arrow_down **Show more**.

  11. Click **Add**. The new agent page reopens.




#### Customize table and field descriptions

To improve conversational data agent accuracy, you can optionally provide additional table metadata. Only the data agent uses this metadata, and it doesn't affect the source table. You can add the following metadata:

  * **Schema descriptions:** add descriptions for your tables and columns to help the agent understand your data. If you don't add descriptions, the agent uses the schema descriptions from your data definitions.



Follow these best practices when you add table and field descriptions:

  * Add descriptions to your data definition rather than just to your data agent definition. This makes sure that other agents also benefit from the descriptions.
  * To prototype the appropriate description to help data agents understand your data, add descriptions to your specific agent. After you verify that the description has the intended impact, then you can decide whether to add the description in your data definition.



To customize table and field descriptions for an agent, perform the following steps:

  1. In the **Agent Catalog** tab, open the agent that you want to customize.
  2. Click **Edit Agent**.
  3. In **Knowledge Sources** , find the table you want to customize and then click **Customize**.
  4. Add a description in **Table Description** or accept the suggestion from Gemini.
  5. In **Fields** , review the Gemini-suggested descriptions for the columns in the table.
  6. Manage the suggested field descriptions: 
     * To accept suggestions, select the descriptions you want, and click **Accept suggestions**.
     * To reject suggestions, select the descriptions you want, and click **Reject suggestions**.
  7. To edit a field description, click edit **Edit** next to the field. 
     1. In **Description** , enter a description of the field.
     2. Click **Update** to save your edits.
  8. Click **Update** to save the customization for the table.
  9. Repeat these steps for each table that you want to customize.



#### Create verified queries

**Note:** Verified queries can be added only for the "Guided" mode

You can select verified queries from a list generated by the system, or create your own.

To create a verified query for the data agent, do the following:

  1. In the **Agent Catalog** tab, open the agent that you want to customize.
  2. Click **Edit Agent**.
  3. In **Verified queries** , click **View Gemini-generated suggestions**.

     1. In **Review suggested verified queries** , review the suggested verified queries. 
     2. Select the quereies that apply to your use case.
     3. Click **Add** to add the queries to the context.
**Note:** To edit the suggested queries, expand the suggested query and click **Edit**.
  4. Optional. To create your own verified query, in **Verified queries** , click **Add query**.

     1. In **Question** , enter the question that can be answered by the verified query.
     2. Click **Generate SQL** to let Gemini generate a verified query that corresponds to the question that you added.
     3. Click **Run** and verify that the query returns the results that you expect.
     4. Review the response and modify the verified query, if required.
     5. Click **Add**.
  5. Repeat these steps to create additional verified queries.




### Add labels to data agents

In the **Agent Settings** section, you can create labels to organize your Google Cloud resources. Labels are key-value pairs that let you group related objects together or with other Google Cloud resources.

  1. In the **Agent Catalog** tab, open the agent to which you want to add a label.
  2. Click **Edit Agent**.
  3. In the **Agent Settings** section, click **Add label**. The **Manage labels** pane opens.
  4. Click **Add label**.
  5. In the **key** and **value** fields, enter your key-value pair for the label.
  6. If you want to add more labels, click **Add label** again.
  7. To delete a label, click delete.
  8. When you're finished, click **Add**. The new agent page reopens.



Continue to the next section to place the agent in draft mode or to publish the agent.

### Preview and publish the agent

  1. In the **Preview** section, enter an example question in the **Ask a question** field, and then press **Enter**.

To verify that the data agent returns the data that you expect, review the agent's response. If the response is not what you expect, change the settings in the **Editor** section to refine the data agent configuration until you get satisfactory responses. You can continue to test and modify your agent to refine the agent's results.

  2. Click **Save**.

  3. To place the data agent in draft mode, which you can re-edit later, click arrow_back **Go back** to return to the **Agent Catalog** page. Because your agent is now in draft mode, it appears in the **My draft agents** section on the **Agent Catalog** tab.

To publish your agent, remain on the agent creation page and proceed to the next step.

  4. To publish the data agent and make it available for use in the project, click **Publish**. Publishing the agent lets other users— who have access to the same database tables—view and converse with your agent, benefiting from the instructions and context that you created.

You can create conversations with the data agent by using the **Agents** page in the Google Cloud console. You can also build your own interface to chat with the data agent by using the Conversational Analytics API.

  5. Optional: In the **Your agent has been published** dialog, click **Share** to share the data agent with other users.

     1. In the **Share permissions** pane, click **Add principal**.
     2. In the **New principals** field, enter one or more principals.
     3. Click the **Select a role** list.
     4. In the **Role** list, select one of the following roles: 
        * Gemini Data Analytics Data Agent User (`roles/geminidataanalytics.dataAgentUser`): grants permission to chat with the data agent.
        * Gemini Data Analytics Data Agent Editor (`roles/geminidataanalytics.dataAgentEditor`): grants permission to edit the data agent.
        * Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`): grants permission to view the data agent.
     5. Click **Save**.
  6. Optional: You can publish the data agent to Gemini Enterprise. For more information, see Publish a data agent in Gemini Enterprise.

  7. To return to the new agent page, click **Close**. After you save or publish your agent, you can see it in the **Agent Catalog**.




## Manage data agents

You can find existing agents in the **Agent Catalog** tab, which consists of three sections:

  * **My agents** : a list of all agents that you create and publish. You can modify and share published agents with others.
  * **My draft agents** : agents that you haven't published yet. You can't share draft agents.
  * **Shared by others in your organization** : agents that others create and share with you. If others grant you permissions, you can edit these shared agents.



### Edit a data agent

To edit a data agent, follow these steps:

  1. In the Google Cloud console, go to the Cloud SQL for PostgreSQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. Sign in to **Agents** using Identity and Access Management (IAM) authentication.

  5. Click the **Agent Catalog** tab.

  6. Locate the agent card of the data agent that you want to modify.

  7. To open the data agent in the agent editor, click more_vert **Open actions** and then click **Edit** on the agent card.

  8. Edit the data agent's configuration as needed.

  9. To save your changes without publishing, click **Save**.

  10. To publish your changes, click **Publish**. In the **Share** dialog, you can either share the agent with others, or you can click **Cancel**.

  11. To return to the **Agents** pane, click arrow_back **Go back**.




### Share a data agent

Follow these steps to share a published data agent. You can't share draft agents.

  1. In the Google Cloud console, go to the Cloud SQL for PostgreSQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. Sign in to **Agents** using Identity and Access Management (IAM) authentication.

  5. Click the **Agent Catalog** tab.

  6. Locate the agent card of the data agent that you want to modify.

  7. To open the data agent in the agent editor, click more_vert **Open actions** > click **Edit** on the agent card.

  8. To share the data agent with other users, click **Share**.

  9. In the **Share permissions** pane, click **Add principal**.

  10. In the **Add principals** field, enter one or more principals.

  11. Click **Select a role**.

  12. In the **Role** list, select one of the following roles:

     * Gemini Data Analytics Data Agent User (`roles/geminidataanalytics.dataAgentUser`): grants permission to chat with the data agent.
     * Gemini Data Analytics Data Agent Editor (`roles/geminidataanalytics.dataAgentEditor`): grants permission to edit the data agent.
     * Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`): grants permission to view the data agent.
  13. Click **Save**.

  14. To return to the agent editing page, click **Close**.

  15. To return to the **Agents** pane, click arrow_back **Go back**.




### Delete a data agent

  1. In the Google Cloud console, go to the Cloud SQL for PostgreSQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Agents**.

  4. Sign in to **Agents** using Identity and Access Management (IAM) authentication.

  5. Select the **Agent Catalog** tab.

  6. In the **Agents** section of the **Agent Catalog** tab, locate the agent card of the data agent that you want to delete.

  7. Click more_vert **Open actions** > **Delete**.

  8. In the **Delete agent?** dialog, click **Delete**. Deleting the agent permanently removes the agent from the project.

After you delete an agent, existing conversations are available in view-only mode. You can't ask new questions of the deleted agent.




## Publish a data agent in Gemini Enterprise

Publishing a data agent involves collaboration between data analysts, Gemini Enterprise administrators, and business users. To learn about the roles required for these users, see Required roles.

### Create and publish an agent

To create, edit, and publish an agent, follow these steps:

  1. Create or edit your data agent in Cloud SQL for PostgreSQL.
  2. Publish the agent. When you publish the agent, select **Gemini Enterprise** as a publishing option.
  3. To copy the A2A endpoint JSON, click **Copy JSON**.
  4. Share the A2A endpoint JSON and the list of users with your Gemini Enterprise administrator so they can register the custom agent in the Google Cloud console and configure access permissions. For more information, see Provision an agent.
  5. Share the agent with the users and groups who need access.



### Provision an agent

To make a published agent available to users in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Gemini Enterprise**.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app where you want to register the agent.

  3. Click **Agents** > add **Add Agents**.

  4. In the **Choose an agent type** section, click **Add** for **Custom agent via A2A**.

  5. In the **Agent card JSON** field, enter the agent card details that you previously received from the data analyst in JSON format.

  6. Click **Preview agent details > Next**.

  7. To enable the agent to access Google Cloud resources on your behalf, follow these steps:

     1. Enter the **Client ID** and **Client secret** that you generated in the [Configure authorization details](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent#authorize-your-agent) section.

     2. In the **Authorization URI** field, enter the following:
            
            https://accounts.google.com/o/oauth2/v2/auth?client_id=client_id&redirect_uri=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fstatic%2Foauth%2Foauth.html&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform&include_granted_scopes=true&response_type=code&access_type=offline&prompt=consent

Replace client_id with the client ID that you generated in [Configure authorization details](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent#authorize-your-agent).

     3. In the **Token URI** field, enter the following:
            
            https://oauth2.googleapis.com/token

     4. In the **Scopes** field, enter the following:
            
            https://www.googleapis.com/auth/cloud-platform

  8. Click **Finish**.

  9. [Share the agent](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#share_an_agent) with the users or groups.




For more information, see [Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent).

### Find and use an agent

You can find and use a data agent in Gemini Enterprise using any of the following methods:

  * Locate the agent in the [Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) and start a dedicated chat.
  * Use the agent's dedicated URL to open Gemini Enterprise directly into a session with that specific Cloud SQL for PostgreSQL data agent.
  * Invoke the agent by writing an `@mention`—such as `@sales_pipeline_agent`— in the Gemini Enterprise core chat.
  * Ask a general analytical question—such as "How is our sales pipeline trending in the last 3 months?"—to let Gemini Enterprise automatically route the query to the relevant data agent.



After you've found the agent, you can interact with it by using one of the following methods:

  * Complete the one-time OAuth sign-in to securely authenticate to Cloud SQL for PostgreSQL.
  * Ask natural-language questions. The conversational analytics agent processes your requests and streams the response back to Gemini Enterprise as text, Markdown, charts, or tables.
  * View your conversation history in the history pane, where conversations are automatically saved.



## Locations

Conversational analytics operates globally; you can't choose which region to use.

## What's next

  * Learn more about [conversational analytics in Cloud SQL for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres). 
  * Learn more about the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview).
  * [Analyze data with conversations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-conversations). 
  * Learn more about how the [Gemini Data Analytics Data Agent Viewer (`roles/geminidataanalytics.dataAgentViewer`)](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/access-control#predefined-roles) role grants permission to view the data agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
