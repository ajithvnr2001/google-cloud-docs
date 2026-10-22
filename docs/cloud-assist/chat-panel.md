---
url: https://docs.cloud.google.com/cloud-assist/chat-panel/
title: Use Gemini Cloud Assist in the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:27.217279+00:00
---

# Use Gemini Cloud Assist in the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/chat-panel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Use Gemini Cloud Assist in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) panel lets you enter natural language prompts in the Google Cloud console to get in-depth explanations, suggested actions, and guided workflows to manage cloud resources efficiently.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that Gemini Cloud Assist is set up for your Google Cloud project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).



## Open and close the Gemini Cloud Assist panel

  1. In the Google Cloud console, go to any page—for example, the **Dashboard** page.

[Go to Dashboard](https://console.cloud.google.com/home)

  2. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens. You can click example prompts if they are displayed, or you can enter a prompt in the **Enter a prompt** field.

To expand the **Cloud Assist** panel to the full width of your browser window, click open_in_new **Open in full page**.

The **Cloud Assist** panel opens in a new tab. Your original session remains open in the original tab. To close the expanded view, close the tab.




## A quick example of entering a prompt in the Gemini Cloud Assist panel

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

  1. In the Google Cloud console, go to any page—for example, the **Dashboard** page.

[Go to Dashboard](https://console.cloud.google.com/home)

  2. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

  3. In the **Cloud Assist** panel, in the **Enter a prompt** field, enter the following prompt, and then click send **Send prompt** :
         
         Create a gcloud command to give the developer Google group
         access to view my Google Cloud project.

In the **Cloud Assist** panel, a response is displayed.

  4. In the **Enter a prompt** field, send a follow-up prompt:
         
         Change that to editor access.

Gemini Cloud Assist uses your conversation history for additional context when it responds to your prompts. For example, Gemini responds with an updated explanation and command.

  5. Optional: If the **Show related content** link is visible, click the link to access more information. The link is only displayed when more information is available.




## Chat panel use cases

The following sections detail additional **Cloud Assist** panel use cases.

### Access product knowledge and best practices

Gemini Cloud Assist can access up to date information on Google Cloud products and best practices for using them. It can help you compare different Google Cloud products and select the right one. It can also provide advice for configuring and using Google Cloud products in an effective, efficient, and compliant manner. Try some of the following prompts:

  * `What is Secret Manager?`
  * `What is the difference between Cloud Run and Cloud Functions?`
  * `When should I use a managed instance group?`
  * `What are some best practices for using KMS?`
  * `What storage class should I use for my data?`
  * `Help me choose a regulatory control for my Google Cloud folders.`



Limitations: Due to the number of factors that can influence cost and pricing, Gemini Cloud Assist generally doesn't provide service pricing data in chat. For pricing information, visit a service's pricing page directly.

### Inspect your cloud resources, applications, and data

Gemini Cloud Assist can access information inside your cloud environment. This section shows how to ask Gemini Cloud Assist about resource configuration and metrics. It also shows how it can help query data in BigQuery or a Google Cloud database.

#### Understand resources, policies, and recent changes

To understand resources, policies, and recent changes, try some of the following prompts:

  * `What are the names of my instances and their private interface names?`
  * `List the name and network name for the subnetworks.`
  * `How many BigQuery datasets have a label whose value is "inventory"?`
  * `List all config changes in the last 24 hours.`
  * `List all users granted roles/bigquery.admin and include the attached resources.`



In addition to providing the information requested, Gemini Cloud Assist provides you with an equivalent query you can run yourself to verify the results.

Limitation: When you first submit a Gemini Cloud Assist prompt, Gemini Cloud Assist can take several minutes to set up a query environment. If your query fails, then wait a few minutes and try again.

#### Analyze resource performance

**Note:** This assistance requires enablement of the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/docs/apis) and the [Monitoring Viewer IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer).

To get a quick analysis of the performance trends of resources such as traffic, throughput, and executions, try some of the following prompts:

  * `Which of my VMs have the highest utilization?`
  * `What are the top 5 dataflow jobs with the highest estimated backlog processing time?`
  * `Total VM network bytes sent per second for each instance?`
  * `What's the QPS on my SQL databases?`



Limitations: Due to the number of factors that can influence cost and pricing, Gemini Cloud Assist generally doesn't provide cost data. For information about your cost or bill, visit the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

If you have a [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) subscription and the [Storage Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.viewer) role to access [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets), then you can send prompts about your specific buckets and objects, while you're on the corresponding Google Cloud console storage page. For example, you can send the following prompts:

  * `How many bytes are stored in my buckets in the us-central1 location?`
  * `What is my Cloud Storage usage, broken down by content type?`
  * `How many objects do I have in Standard storage smaller than 50 GB?`



#### Help with BigQuery datasets and jobs

**Note:** This assistance requires enablement of the [BigQuery API](https://docs.cloud.google.com/monitoring/docs/apis) as well as the [BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) and the [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) IAM roles.

You can ask Gemini Cloud Assist for help with your BigQuery resources directly in the **Cloud Assist** panel. Try the following prompts:

  * `How many BigQuery datasets have a label whose value is 'inventory'?`



Additionally, when you are on a BigQuery page in the Google Cloud console, you can ask for help with writing a SQL query in the **Cloud Assist** panel. For example, if you had a dataset with ride-sharing service data you might enter the following prompt: `Generate a SQL query to show me the direction and subscriber type for the 10 longest trips.`

In this example, Gemini Cloud Assist provides a specific SQL query that you can review and copy into the BigQuery query editor. You can also ask for help querying your data using Python. For example, you could prompt Gemini Cloud Assist to `Generate Python code to query the bigquery-public-data.ml_datasets.penguins table using BigQuery magics.`

For more detailed examples, see [Use Gemini Cloud Assist in BigQuery](https://docs.cloud.google.com/bigquery/docs/use-cloud-assist).

#### Help with databases

To get help with your database deployments, try the following prompts:

  * `Where are my databases located?`
  * `Show me all databases running on Postgres.`
  * `How many databases do I have in the US?`



While you're on a Google Cloud console page for a specific Cloud SQL database instance, you can also ask for database performance information and for help troubleshooting potential issues. For example, `What is the current CPU utilization of this database?`.

### Design and deploy Google Cloud applications

This section details a few examples to help design and deploy your Google Cloud applications.

#### Ask for help creating resources

You can ask Gemini Cloud Assist for help creating resources or policies using either Google Cloud CLI commands or Terraform, and Gemini Cloud Assist replies with a snippet of code that you can copy into your shell or IaC repository. For example:

  * `How do I use Google Cloud CLI to execute a Cloud Run job and set the timeout to 20 minutes?`
  * `I want to grant the user "user@company.com" the "Security Administrator" role for the "prod-subnet" subnet for project "xyz-123". What Google Cloud CLI command can I use?`
  * `Give me a Terraform configuration to create an Enterprise Plus PostgreSQL database instance with data caching.`
  * `Create a custom organization policy that requires all new VM instances to have the n2d machine type.`



Additionally, when you ask Gemini Cloud Assist to create an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview), the response includes the option to [test](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) the policy directly within the Gemini Cloud Assist chat.

#### Create a new application

You can ask Gemini Cloud Assist for help creating an application. For example: `Help me create a three tier web application for a new CMS system`.

In addition to providing some suggestions for getting started and a proposed architecture, Gemini Cloud Assist will provide a link to start building the application in the Application Design Center. This lets you transfer the context of this prompt and response directly to Google Cloud visual application design experience.

Additionally, Gemini Cloud Assist paid tier users are able to [use natural language in the **Cloud Assist** panel with the Application Design Center](https://docs.cloud.google.com/cloud-assist/design-application) to iteratively update their application architecture.

### Investigate and troubleshoot issues

You can use the **Cloud Assist** panel to get help from Gemini Cloud Assist with initial steps investigating and troubleshooting issues with your applications.

#### Create and run Gemini Cloud Assist investigations

**Note:** This assistance is available to users who have a [Premium Support contract](https://cloud.google.com/support/premium) or who have requested access through their account team. Additionally, using Gemini Cloud Assist investigations requires you to be granted the [Investigation Creator IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationCreator).

The [Gemini Cloud Assist investigations feature](https://docs.cloud.google.com/cloud-assist/investigations) helps troubleshoot infrastructure and application issues within your Google Cloud environment. You can use the investigations feature directly within Gemini Cloud Assist chat by doing the following:

  1. Ask Gemini Cloud Assist chat to help you investigate or troubleshoot an issue with your Google Cloud resources.

If Gemini Cloud Assist determines an investigation would be useful, a **Create investigation** button appears in the chat.

  2. Click **Create investigation**.

A **Create investigation** panel opens. Fields for the investigation are pre-populated with content from your chat that is potentially relevant for the investigation.

  3. Change or add any information to the pre-populated content that you think is relevant to the investigation.

  4. Click **Create**.

The **Investigation details** opens and Gemini Cloud Assist runs the investigation. From the **Investigation details** page, you can [review the investigation](https://docs.cloud.google.com/cloud-assist/create-investigation#review).




Alternatively, you can manually create an investigation at any time from the chat panel by clicking the **More actions** drop-down button and selecting **New investigation**.

#### Check for Google Cloud incidents impacting your project

**Note:** This assistance requires enablement of the [Service Health API](https://docs.cloud.google.com/service-health/docs/reference/rest) and the [Service Health Viewer IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicehealth#servicehealth.viewer).

To check for Google Cloud incidents impacting your project, try some of the following prompts:

  * `Is there something going on with Google Cloud? I'm seeing issues with my project.`
  * `What's the latest update on the Compute Engine outage in us-central1?`
  * `How is my project impacted by the Cloud Storage incident?`
  * `Is there a workaround for the BigQuery incident?`



#### Investigate database issues

To help understanding potential database, including performance, health, and compliance, try some of the following prompts:

  * `What is the current CPU utilization of this database?`
  * `Which of my queries have high latency for this database instance?`
  * `What is the slowest query for this database in this instance?`
  * `How many error log entries are there for this database instance?`
  * `What issues are affecting my databases?`
  * `What databases have NIST issues in Europe?`



### Optimize Google Cloud resources

You can use the **Cloud Assist** panel to get information that helps you to optimize costs, and recommendations that help you to optimize your resource usage.

#### Get recommendations

**Note:** This assistance requires enablement of the [Recommender API](https://docs.cloud.google.com/recommender/docs/reference/rest) and the [Recommender Viewer IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer).

To help optimize your Google Cloud resources and get specific recommendations for estimated savings and cluster reliability, try the following prompts:

  * `Give me recommendations to reduce my resource costs.`
  * `What are all the quotas for my project that are almost hitting the limit?`
  * `What BigQuery datasets should I partition or cluster?`
  * `Which of my VMs are idle?`



#### Analyze your costs

**Note:** This assistance requires enablement of the App Optimize API (`appoptimize.googleapis.com`). You also need the [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) IAM role.

Gemini Cloud Assist can help you to optimize costs and investigate cost anomalies.

  * Learn insights about recent cost and utilization changes.
  * Get cost or utilization data for a specific application or project.
  * For supported resource costs, get an explanation for cost changes.



Cost totals in Gemini Cloud Assist responses are based on your contract prices, before any [committed-use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) or other credits are applied. For an application, the total cost includes all resources that are fully used by the application and doesn't include costs for resources that are shared across applications.

Try the following prompts:

  * `Show me the top 5 resources that cost me the most last month.`
  * `How much did my GKE cluster my-cluster-id cost me last week?`
  * `What are my most expensive resources in us-central1?`
  * `What were the least cost efficient resources last month for my app web-store?`



For more information about this assistance, see [Optimize costs with Gemini assistance](https://docs.cloud.google.com/hub/docs/optimize-gemini).

For additional information about your costs or bill, visit the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

## Conversation history

Gemini Cloud Assist keeps a history of your conversations for you to view later. This information can be stored in any Google Cloud data center.

Conversations older than 180 days are automatically deleted from chat history storage. Alternatively, you can manually delete specific conversations.

**Note:** Users with the [`cloudaicompanion.topics.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topics.get) IAM permission for a project have access through the API to history created by users within the project, even though this access is not surfaced in the Google Cloud console. This permission is found in roles such as the [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role, and can be included in custom roles as well.

### View or delete a conversation in the history

  1. In the **Cloud Assist** panel, click more_vert **More actions** , and then click **Show chat history**.

The **Recent chats** panel opens, displaying any saved conversations.

  2. To view a conversation, click the conversation.

  3. Optional: To manage a single conversation, next to the conversation title, click more_vert **More actions** , and then do one of the following:

     * To delete the conversation, click **Delete chat**.
     * To rename the conversation, click **Rename chat**.



### Clear your chat session

To clear the chat session history, in the **Cloud Assist** panel, click more_vert **More actions** , and then click **New chat**.

## Manage page context sharing

As part of Gemini Cloud Assist user preferences, you can choose whether to include your current Google Cloud console page context as a data source for chat conversations. By default, **Page context sharing** is enabled to improve chat quality by letting Gemini Cloud Assist understand the context of your current page in the Google Cloud console. For privacy reasons, you can disable this setting at any time.

To enable or disable page context sharing:

  1. In the **Cloud Assist** panel, click more_vert **More actions**.

  2. Click **Page context sharing** to toggle the setting. The status icon and accessibility labels change to reflect the current state.




## Limitations

If you [set up Gemini Cloud Assist for a folder](https://docs.cloud.google.com/cloud-assist/set-up-gemini) and are using the **Cloud Assist** panel at the folder level in the Google Cloud console, then assistance and responses are limited to applications related to the folder for products that support applications. The following list includes Google Cloud products supported at the folder level:

  * [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview)
  * [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)
  * [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview)
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
  * [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)



To get assistance on other products and resources, use project picker at the top of the Google Cloud console page to select a project resource.

Additionally, you must enable [application management](https://docs.cloud.google.com/app-hub/docs/overview#application-management) on the folder to use the **Cloud Assist** panel at the folder level.

### Data residency

Conversations from the chat panel can be stored in any Google Cloud data center. You shouldn't enter information into the chat panel that is subject to residency or jurisdictional regulatory compliances.

## What's next

  * For more examples and suggestions to help you create your own prompts, see [Write better prompts for Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * To discover other ways to get Gemini assistance, see [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
