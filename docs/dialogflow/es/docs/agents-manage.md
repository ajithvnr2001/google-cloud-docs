---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-manage/
title: Create and manage agents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:35.913673+00:00
---

# Create and manage agents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Create and manage agents Stay organized with collections  Save and categorize content based on your preferences. 

All agent-related menus and information are found at the top of the left sidebar menu at the Dialogflow Console. There, you'll see a list of the agents associated with your account and the option to create a new agent.

## Create an agent

**Note:** You can only create one agent per [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region) for a GCP project. If you need multiple agents in the same region, you will need to create multiple projects.

To create an agent with the console (common), follow these steps:

  1. You must have a [role with full or edit access](https://docs.cloud.google.com/dialogflow/es/docs/access-control#roles) in order to create an agent.
  2. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  3. If requested, sign in to the Dialogflow console. See [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console) for more information.
  4. Click **Create Agent** in the left menu. (If you already have other agents, click the agent name, scroll to the bottom and click **Create new agent**.)
  5. Enter your agent's name, default language, default time zone and GCP project, then click the **Create** button. (You can change the [agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) after creation.)



To create an agent with the API (uncommon), see [Create an agent with the API](https://docs.cloud.google.com/dialogflow/es/docs/how/agent-create-api).

## Delete an agent

**Caution:** Deleting an agent **cannot** be undone. [Export](https://docs.cloud.google.com/dialogflow/docs/agents-settings#export_and_import) your agent to keep a backup if necessary.

  1. You must have a [role with full access](https://docs.cloud.google.com/dialogflow/docs/access-control#roles) in order to delete an agent in the Dialogflow Console.

**Note:** Either full or edit access can delete an agent when using the API.
  2. Before deleting an agent, you must remove access for all users besides yourself:

     * If you are the only user with the Owner/Admin role, you can [use the Dialogflow Console to remove other users](https://docs.cloud.google.com/dialogflow/docs/access-control#df-console).
     * If more than one user has the Owner/Admin role, you must [use the GCP Console to remove other users](https://docs.cloud.google.com/dialogflow/docs/access-control#gcp-console).
  3. To delete an agent:

     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Select the agent you wish to delete.
     3. Click on the settings _settings_ button next to the agent's name.
     4. Select the **General** tab, and scroll down to the bottom.
     5. Click **Delete this agent**. If you do not see the **Delete this agent** button, it is because you do not have the required Owner/Admin role.
     6. Enter **DELETE** in the text field.
     7. Click **Delete**.



If you [delete your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), all Dialogflow ES agents and data associated with the project are deleted within 60 days of project deletion. If you receive an error when attempting to delete a project due to an existing lien, see the troubleshooting documentation [section on project liens](https://cloud.google.com/dialogflow/docs/support/troubleshooting?agent=any&category=any#project-lien).

[ Previous arrow_back  Agents  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview)

[ Next Prebuilt agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-prebuilt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
