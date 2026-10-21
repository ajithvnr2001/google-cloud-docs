---
url: https://docs.cloud.google.com/data-studio/conversational-analytics-setup/
title: Set up Conversational Analytics in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:18.076822+00:00
---

# Set up Conversational Analytics in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/conversational-analytics-setup/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Set up Conversational Analytics in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through setting up Conversational Analytics in Data Studio, including setup requirements, supported data sources, and how to connect to supported data sources. Select the **Legacy** tab or the **New** tab to learn more about the setup for each [experience](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

### New

## Before you begin

To use a BigQuery data source with Conversational Analytics, you must have the following [BigQuery Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control):

  * The `bigquery.jobs.create` IAM permission on the billing project
  * The `roles/bigquery.dataViewer` IAM role on the project, dataset, or table that is being queried



To create, edit, manage, and delete data agents in Data Studio or BigQuery, you must have the permissions that are described in the [Create data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#required_roles) documentation page. This page also describes the roles that are necessary for chatting with data agents that are created in BigQuery and shared to Data Studio.

To create conversations, you must have the permissions that are described in the [Analyze data with conversations](https://docs.cloud.google.com/bigquery/docs/create-conversations) documentation page.

If another user shares a data agent with you, they're granting you access to the agent, but you might not have access to the underlying Google Cloud project. Ask an administrator to grant you access to the project with a role such as Viewer (`roles/viewer`), Editor (`roles/editor`), or Owner (`roles/owner`).

## Supported data sources

Although you cannot create Conversational Analytics data agents within Data Studio, you can [chat with data agents](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents) that were created in BigQuery and published to Data Studio.

## Select a Google Cloud project

To use Conversational Analytics in Data Studio, you must have access to a Google Cloud project. If you don't have access to a project, contact an administrator.

When you load the **Conversations** page in Data Studio, you must select a Google Cloud project. If you have access to only one project, Data Studio opens that project automatically.

**Important:** Because Data Studio only displays projects from your recent projects list, you must [open a project in the Google Cloud console](https://docs.cloud.google.com/resource-manager/docs/view-update-projects) at least once before you can select it in Data Studio.

### Legacy

## Before you begin

Before Data Studio users can use [legacy Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience), the following requirements must be met:

  1. An administrator must [enable Gemini in Data Studio](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio). During the Preview period, an administrator must also enable the [**Trusted Tester features**](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio).
  2. Optionally, an administrator must [enable the Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter) to access advanced analytics.



Each user must belong to a [Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/pro-subscription-overview).

### Additional data source requirements

Some data sources have additional requirements, such as the following:

  * To use Conversational Analytics with a Looker Explore as a data source, users must be granted the [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) and [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) permissions for the Explore's underlying model.
  * To use a BigQuery data source with Conversational Analytics, you must have the following [BigQuery Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control):

    * The `bigquery.jobs.create` IAM permission on the billing project
    * The `roles/bigquery.dataViewer` IAM role on the project, dataset, or table that is being queried



## Supported data sources

Conversational Analytics can connect to the following data sources:

  * Looker Explores
  * BigQuery tables
  * [Google Sheets](https://docs.cloud.google.com/data-studio/connect-to-google-sheets)
  * [CSV files in Data Studio](https://docs.cloud.google.com/data-studio/upload-csv-files)



### Best practices for setting up a data source

Setting up a data source in the ideal manner can help Conversational Analytics provide the most helpful answers. Consider following these best practices when creating a data source:

  * You can exclude fields that shouldn't be used for analysis entirely, or [hide them](https://docs.cloud.google.com/data-studio/create-rename-copy-hide-and-remove-fields) in the data source.
  * Field [descriptions](https://docs.cloud.google.com/data-studio/model-your-data#description) can be added or edited to give context to Conversational Analytics.
  * If you are seeing unexpected results, check your data source and confirm that the field [types](https://docs.cloud.google.com/data-studio/model-your-data#type) and default aggregation settings are correct.



## Connect to data

You can start a conversation with the following data sources when using Conversational Analytics:

  * A Looker Explore
  * A data agent that is built with a Looker Explore
  * A BigQuery table



### Connect to Looker data

To use a Looker [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) as a data source in Conversational Analytics, follow these steps:

  1. In Conversational Analytics, on the **Chat with your data** page, select the **Data sources** tab.
  2. Select **Connect to data** , and then select **Looker** from the drop-down menu. ![](https://docs.cloud.google.com/static/data-studio/images/conversational-analytics-looker-connector-explores.png)
  3. In the **Connect to a Looker Instance** section, in the **Enter Looker Instance URL** field, enter the URL for your Looker instance. If the instance URL is invalid or doesn't meet the Looker connector requirements, Conversational Analytics displays an error message.

**Note:** If you've previously linked a Looker instance, you can select that instance from the **Saved Looker Instance** list.
  4. If you're connecting to a Looker instance for the first time, click **Connect Looker Account**.

  5. If Conversational Analytics displays the **Link your Google Account and Looker window** , review the information about how Data Studio will access your Looker account. To link your accounts and proceed, select **Agree and continue**.

  6. Once you have linked to a Looker instance, select an Explore from the list, and then click **Connect** to start a conversation.




After you connect to an Explore, it'll appear in the list of available data sources on the **Chat with your data** page.

### Connect to a data agent

To chat with a data agent that is built with a Looker Explore, follow the instructions to create a data agent on the [Data agents in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents#start-a-conversation-legacy) documentation page.

### Connect to BigQuery data

You can start a conversation directly with a BigQuery table or with a [data agent](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents#create-and-edit-data-agents-legacy) that is built with a BigQuery table.

To use a BigQuery table as a data source with Conversational Analytics, follow these steps:

  1. In Conversational Analytics, on the **Chat with your data** page, select the **Data sources** tab.
  2. Select **Connect to data** , and then select **BigQuery** from the drop-down menu.
  3. In the **Select data** window, select one of the following tabs to connect to a BigQuery dataset or to browse public datasets.


  * **Recent Projects** : Lists the BigQuery projects that you accessed most recently.
  * **All Projects** : Lists all the BigQuery projects that you have access to.
  * **Public Datasets** : Lists [BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data).
  * **Enter Project ID** : Lets you specify the unique [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for a specific project.

**Note:** Optionally, you can change the associated billing project by choosing an option from the **Billing project** drop-down.

  1. Select a BigQuery project in the **Recent Projects** or **All Projects** tab, or enter a project ID in the **Enter Project ID** tab. Optionally, use the **Search Projects** search bar to filter the list. (If you're connecting to a public dataset, proceed to the next step.)
  2. The **Select data** window displays the **Datasets** tab, or it displays **Public Datasets** if you're connecting to a public dataset. Select a BigQuery dataset. Optionally, use the **Search Datasets** search bar to filter the list.
  3. The **Select data** window displays the **Table** tab. Select the table that you want to connect to in the **Table** tab. Optionally, use the **Search Tables** search bar to filter the list.
  4. Click **Connect**.



After you connect to a BigQuery table, it'll appear in the list of available data sources on the **Chat with your data** page.

**Tip:** To view a project, a dataset, or a table in BigQuery, hold your cursor over the relevant list item to reveal the open_in_new **View in BigQuery** option. For example, if you hold your cursor over a project name, Conversational Analytics displays the open_in_new **View project in BigQuery** option.

## What's next

  * [Start a conversation directly with your data](https://docs.cloud.google.com/data-studio/conversational-analytics-data)
  * [Converse with data agents](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
