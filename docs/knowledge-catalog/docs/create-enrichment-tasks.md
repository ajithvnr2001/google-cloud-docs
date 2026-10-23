---
url: https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks/
title: Create enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:49.741288+00:00
---

# Create enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Create enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Knowledge Studio gated preview**  
Knowledge Studio is currently available as a gated preview. To view the context graph, create context sets, and run enrichment workflows, you must first request allowance for your organization.   
  
[Request preview access](https://docs.google.com/forms/d/e/1FAIpQLScw1O38BmcLIvqL1ZvpybJsLGO_Dmuq0a5RrCJIqW11iljsKQ/viewform)

Knowledge Studio enrichment tasks let you automatically document the business meaning of your data so that AI applications can query it accurately without hallucinating. These tasks use AI to scan your standard operating procedures (SOPs), code repositories, and user interactions, extracting the business logic needed to ground your AI agents.

## Before you begin

Follow these prerequisites before you create an enrichment task.

### Understand the concepts

Before you run an enrichment task, we recommend that you familiarize yourself with the core components of the enrichment architecture:

  * For an overview of how Knowledge Studio agents automate metadata generation, see [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).

  * For an overview of how metadata context grounds AI agents and simplifies data exploration, see [About data context](https://docs.cloud.google.com/knowledge-catalog/docs/about-context).

  * For an overview of the Knowledge Catalog hierarchy, including entry groups, entries, aspects, and entry links, see [About metadata](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).




### Prepare required components

Before you create an enrichment task, ensure that your environment is properly configured for AI enrichment as detailed in [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites).

Have the following components ready:

  * **Service account** : A dedicated user service account with the required roles. Throughout this documentation, we refer to this as the _execution service account_ to differentiate it from the Google-managed Knowledge Catalog service agents. The enrichment task runs as this service account and uses it to read the sources and write to the context set.

  * **Context set** : A destination context set to save the enriched metadata to. The context set also serves as the source of assets to enrich. Whatever is in the context set is enriched by default if no additional resources are added during setup. You can also create an empty context set during the task setup if one doesn't exist.

  * **Resources to enrich** (Optional): Additional data assets that you want to enrich that are not already in your destination context set. Adding these additional resources during task creation enriches them and automatically adds them to the destination context set. These resources can include BigQuery datasets, tables, or Lakehouse assets, and must already exist.

  * **Knowledge signals** (Optional): If you plan to provide the AI agent with documents or models to learn from, ensure you [prepare your Cloud Storage buckets](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#prepare-buckets), [format your `.jsonl` evaluation datasets](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#format-evaluation-sets), or [set up OAuth](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#setup-oauth) for third-party source URLs.

  * **Trace logs** (Optional): If you plan to enable agent self-learning, you must [configure agent traces](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#configure-agent-traces) by setting up scoped log views or a BigQuery agent analytics table from which the agent can learn historical interactions.

  * **Data profiling and data insights** (Recommended): To improve the quality of generated metadata proposals, enable data profiling and AI data insights on your frequently used target tables before running the task. For more information, see [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#enable-data-profiling-and-insights).




### Required roles

To set up and run enrichment tasks, different identities require specific permissions.

### The end user

To create and manage enrichment tasks, you must have the following required roles.

**Create, modify, run, and cancel enrichment tasks**

To ensure that you has the necessary permissions to create, modify, run, and cancel enrichment tasks, ask your administrator to grant the following IAM roles to you on the project: 

**Important:** You must grant these roles to you, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Dataplex DataScan Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create, modify, run, and cancel enrichment tasks. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create, modify, run, and cancel enrichment tasks:

  * Create enrichment tasks: `dataplex.agentTasks.create`
  * View enrichment tasks: `dataplex.agentTasks.get`
  * List enrichment tasks: `dataplex.agentTasks.list`
  * Delete enrichment tasks: `dataplex.agentTasks.delete`
  * Update enrichment tasks: `dataplex.agentTasks.update`
  * Run enrichment tasks: `dataplex.agentTasks.run`
  * Cancel enrichment tasks: `dataplex.agentTasks.cancel`



Your administrator might also be able to give you these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Attach the execution service account to the enrichment task config**

To ensure that you has the necessary permissions to attach the execution service account to the enrichment task config, ask your administrator to grant the following IAM roles to you on the execution service account: 

**Important:** You must grant these roles to you, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Service Account User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to attach the execution service account to the enrichment task config. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to attach the execution service account to the enrichment task config:

  * Impersonate service accounts: `iam.serviceAccounts.actAs`



Your administrator might also be able to give you these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### The execution service account

The execution service account is the identity under which the enrichment task runs and performs all operations.

**Consume required services**

To ensure that the execution service account has the necessary permissions to consume APIs during the execution of the enrichment task, ask your administrator to grant the following IAM roles to the execution service account on the project containing the enrichment task: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Service Usage Consumer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to consume APIs during the execution of the enrichment task. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to consume APIs during the execution of the enrichment task:

  * Consume quota and services: `serviceusage.services.use`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**View and profile target data content**

To ensure that the execution service account has the necessary permissions to view and profile data content within target datasets, ask your administrator to grant the following IAM roles to the execution service account on the target tables: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view and profile data content within target datasets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and profile data content within target datasets:

  * View dataset metadata: `bigquery.datasets.get`
  * View table metadata: `bigquery.tables.get`
  * Read table data: `bigquery.tables.getData`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Propose and write metadata into context sets**

To ensure that the execution service account has the necessary permissions to propose and write metadata definitions into context sets, ask your administrator to grant the following IAM roles to the execution service account on the project: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permissions: **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to propose and write metadata definitions into context sets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to propose and write metadata definitions into context sets:

  * Create metadata entries: `dataplex.entries.create`
  * Update metadata entries: `dataplex.entries.update`
  * View metadata entries: `dataplex.entries.get`
  * List metadata entries: `dataplex.entries.list`
  * Create entry groups: `dataplex.entryGroups.create`
  * Update entry groups: `dataplex.entryGroups.update`
  * Propose changes to entry groups: `dataplex.entryGroups.requestChanges`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Automatically publish enrichments (Optional)**

_(Optional)_ If you enable auto-publish on your task, include the following role:

To ensure that the execution service account has the necessary permissions to automatically approve and publish changes, ask your administrator to grant the following IAM roles to the execution service account on the project: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Dataplex Workflow Approver** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to automatically approve and publish changes. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to automatically approve and publish changes:

  * Use change requests: `dataplex.changeRequests.use`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Learn from trace logs**

_(Optional)_ If you plan to learn from existing trace logs (self-learning), include the following roles:

To ensure that the execution service account has the necessary permissions to read historical interactions from trace logs, ask your administrator to grant the following IAM roles to the execution service account on the project that owns the Gemini app: 

**Important:** You must grant these roles to the execution service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Logs Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to read historical interactions from trace logs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to read historical interactions from trace logs:

  * Access log views: `logging.views.access`
  * Read log entries: `logging.logEntries.list`



Your administrator might also be able to give the execution service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

_(Optional)_ If you plan to learn from a BigQuery agent analytics table, the execution service account also requires the **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) role on the agent analytics table.

### The Dataplex Service Agent

The Knowledge Catalog Service Agent is a Google-managed service account that Knowledge Catalog uses to perform backend operations on your behalf, such as impersonating your execution service account during an enrichment run and orchestrating BigQuery profiling jobs.

The Knowledge Catalog Service Agent uses the following email format:

`service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with your Google Cloud project number.

**Impersonate the execution service account**

To ensure that the Knowledge Catalog Service Agent has the necessary permissions to impersonate the execution service account to run the task, ask your administrator to grant the following IAM roles to the Knowledge Catalog Service Agent on the execution service account: 

**Important:** You must grant these roles to the Knowledge Catalog Service Agent, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**Service Account Token Creator** ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to impersonate the execution service account to run the task. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to impersonate the execution service account to run the task:

  * Generate Access tokens: `iam.serviceAccounts.getAccessToken`
  * Generate OpenID tokens: `iam.serviceAccounts.getOpenIdToken`
  * Sign JWTs: `iam.serviceAccounts.signJwt`
  * Sign BLOBs: `iam.serviceAccounts.signBlob`



Your administrator might also be able to give the Knowledge Catalog Service Agent these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Perform BigQuery profiling and read query history**

To ensure that the Dataplex Service Agent has the necessary permissions to perform backend BigQuery profiling and read table query history, ask your administrator to grant the following IAM roles to the Dataplex Service Agent on the project: 

**Important:** You must grant these roles to the Dataplex Service Agent, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * To grant the required permission: [**BigQuery Resource Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.resourceViewer) (`roles/bigquery.resourceViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform backend BigQuery profiling and read table query history. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform backend BigQuery profiling and read table query history:

  * View dataset metadata: `bigquery.datasets.get`
  * View table metadata: `bigquery.tables.get`
  * Read table data: `bigquery.tables.getData`
  * List BigQuery jobs: `bigquery.jobs.list`
  * View basic resource metadata: `resourcemanager.projects.get`



Your administrator might also be able to give the Dataplex Service Agent these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open the Knowledge Studio workspace

To open the task creation wizard, perform the following steps:

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the left navigation pane, select **Enrichments**.

  3. Click **\+ Create enrichment task**.




### Name the enrichment task

In the **Define** pane, perform the following steps:

  1. In the **Display name** field, provide a descriptive name for the task (for example, `Finance Dataset enrichment`).
  2. In the **Task ID** field, provide a unique ID or use the auto-generated ID.
  3. In the **Goal** field, describe the objective of the enrichment task to guide the extraction process. Provide natural language guidance detailing the business mission and AI capability goals for this context set.

For example:
         
         Curate and maintain the authoritative context set for the
         `subscription_revenue` domain. Focus on resolving metric discrepancies
         between `gross_sales`, `net_billed_revenue`, and `discount_applied`.
         Ensure all customer join keys (e.g. `customer_id`, `subscription_fk`)
         have explicit column documentation, and establish parameterized query
         templates for Monthly Recurring Revenue (MRR) and Churn Rate calculations.
         

  4. Click **Continue**.




### Configure the enrichment task parameters

The scope specifies what gets enriched, and what the agent reads.

In the **Scope** pane, perform the following steps:

  1. In the **Project** field, select the project that contains the context set.

  2. In the **Context set** field, select the context set that the task enriches and to which the task saves its results.

Your enrichment task inherits the Google Cloud region of the context set that you select.

If you don't have a context set set, click **Create new context set**.

For more information on how to create a context set, see [Create a context set](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets#create-context-set).

  3. Optional: In the **Resources to enrich** section, add BigQuery or Lakehouse resources that you want to enrich in addition to the context set.

Any resources you add must be in the same region as the context set you selected. Multi-region locations (such as `us`) successfully match single regions in that location (such as `us-central1`). Mismatched regions will cause task creation to fail.

If you select an empty context set and don't add any additional resources in this section, Knowledge Studio displays a warning. If you run the task with this configuration, it generates a semantic knowledge base based on your instructions, but it does not enrich any entries.

     1. Enter the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the target data asset.

For example:

        * **BigQuery table** : `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID`

        * **Lakehouse asset** : `//dataplex.googleapis.com/projects/PROJECT_ID/locations/LOCATION/lakes/LAKE_ID/zones/ZONE_ID/assets/ASSET_ID`

Alternatively, to select a resource visually, perform the following steps:

     1. Click **Browse** to open the **Select sources** dialog.
     2. To select from recently used resources, click the **Recent** tab and select the resources that you want to add.
     3. To browse or search all resources, click the **All** tab and do the following: 
        1. In the **Search** field, enter a search term for your BigQuery or Lakehouse resource.
        2. In the resource tree, expand the project and dataset hierarchy to locate your resource.
        3. Select the checkbox beside one or more resources. You can preview the schema and details of the selected resource in the right pane.
     4. Click **Confirm**.

To add more resources, use commas to separate the resource names.

  4. Optional: In the **Knowledge signals** section, connect the AI agent to extra sources to read for context. These resources are read-only and are not enriched.

     * **Cloud Storage buckets** : Enter the bucket name, or click **Browse** to search for a bucket. Press `Enter`, comma, or `Space` after each bucket name. The task requires whole buckets; you cannot configure it to only read individual files.
     * **Glossaries** : Enter the glossary name, or click **Browse** to search for a glossary. Press `Enter`, comma, or `Space` after each glossary name.

Ensure that any connected glossaries are located in the exact same region as your enrichment task and context set (for example, `us-central1`). Adding a glossary from an invalid multi-region location (such as `us`) causes the task creation to fail.

     * **External sources** : To connect third-party platforms such as Google Workspace, Microsoft SharePoint, GitHub, or Atlassian Confluence, you can configure them individually, or provide a YAML configuration file.

To configure sources using a YAML file:

       1. In the **Source configuration file (optional)** field, click **Browse** and select your YAML file.

To configure a source manually:

       1. Under **Connected sources** , click **Set up** next to the platform you want to configure.
       2. In the **Source URLs** field, enter the URLs for your documents, repositories, or spaces, and then press `Enter` or comma after each URL.
       3. If the platform requires authentication (such as GitHub, Atlassian, or Microsoft), attach your credentials by doing the following:

          1. Click **\+ Add connection**.
          2. In the **New connection** pane, enter the full resource name of your auth provider in the **Auth provider** field. Use the following format:   
`projects/PROJECT_ID/locations/LOCATION/authProviders/PROVIDER_NAME`
          3. Under **URI patterns** , click **\+ Add URI pattern** to specify which URLs this credential has permission to access. You can use asterisks (`*`) as wildcards (for example, `https://github.com/test-org/*`).
          4. Click **Done**.

Google Workspace resources connect directly using your task's execution service account IAM permissions, so they don't require an auth provider connection.

  5. Click **Continue**.




### Configure evaluation and self-learning

This is an optional section. In the **Improve** pane, perform the following steps:

  1. Optional: In the **Evaluation** section, configure the following fields:

For more information on formatting evaluation and curation datasets, see [Dataset schema requirements](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites#dataset-schema).

     * **Evaluation set** : To measure the impact of proposed context changes, enter a Cloud Storage URI or click **Browse** to select your `.jsonl` file.

     * **Curation set** : To provide a set of seed questions for iterative optimization, enter a Cloud Storage URI or click **Browse** to select your `.jsonl` file.

  2. Optional: In the **Publishing** section, specify the publishing cadence:

When auto-publish is enabled, auto-approved metadata changes are written directly to the context set. When disabled, the enrichment run generates drafted edits that a human reviewer must approve before they are merged into the codebase.

     * To require human review before metadata is merged into your production context set, clear the **Enable auto-publish** checkbox.

     * To automatically publish changes that meet a high quality threshold, select the **Enable auto-publish** checkbox. Use the **Auto-publish above** slider to set the minimum confidence score required for changes to go live automatically (for example, _85%_). If an evaluation dataset is configured, you can also use the **Maximum quality drop** slider to safely restrict publishing when the agent's performance drops (for example, _-5%_). Any proposals failing to meet these thresholds are queued as a change request for manual review.

  3. Optional: To find gaps in real agent conversations and keep your context current, in the **Self-learning** section, select the **Enable self-learning** toggle.

  4. Optional: If you enabled self-learning, under the **Learn from** section, add any of the following sources:

     * **Gemini Enterprise apps** : In the **Project ID** list, select the project. In the **Gemini Enterprise app** list, select the app generating conversation traces, and then click **Done**.

You can add multiple Gemini Enterprise apps.

To optimize these enrichment and self-learning capabilities, we recommend specifying a Gemini 3.8 Flash or later model in the Gemini Enterprise application. For more information about the model selection steps, see the "Create an agent using the flow builder" section in [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).

     * **BigQuery agent analytics** : In the **Table** field, enter the name of the table containing agent chat events or click **Browse** to select it visually, and then click **Done**.

You can add multiple tables.

  5. Click **Continue**.




### Configure the run settings

In the **Run** pane, perform the following steps:

  1. In the **Run as** section, click the **User service account** list and select the identity the task uses to read the sources and write to the context set. Ensure this is the identity configured in Before you begin.
  2. Under **Trigger** , select the trigger condition: 
     * **On demand** : Runs only when you click Run.
     * **Scheduled** : Runs automatically on a repeating schedule.
  3. Optional: Under **Notifications** , click **\+ Add recipient** to specify up to five email addresses to receive a report after every run.
  4. Verify the parameters in the **Summary** pane, and then click **Create**.



Your new enrichment task is saved. Depending on your trigger settings, the task either awaits its first scheduled execution or is ready to run immediately. When the task finishes an execution run, the agent queues the generated AI metadata proposals in a change request for your review.

## What's next

  * [Manage enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-tasks).
  * [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
