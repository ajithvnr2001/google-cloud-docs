---
url: https://docs.cloud.google.com/gemini/enterprise/docs/release-notes/
title: Gemini Enterprise release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:10.115019+00:00
---

# Gemini Enterprise release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/release-notes/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/enterprise/docs/resources)



Send feedback 

#  Gemini Enterprise release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Gemini Enterprise. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gemini-enterprise-release-notes.xml) directly. 

## October 22, 2026

Feature

**Gemini Enterprise: Single-user quota limits**

Gemini Enterprise administrators can configure single-user quota limits on the **Usage & Spending > Usage** page in the Google Cloud console to prevent an individual user from using all of an edition's shared subscription quota pool. You can enable a single-user quota limit and set a quota multiplier for each edition and location across the Gemini Enterprise Standard, Gemini Enterprise Plus, and Gemini Enterprise Standard Emerging Market editions.

This feature is generally available (GA). For more information, see:

  * [Single-user quota limits](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#single-user-quota-limits)
  * [Configure a single-user quota limit](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage#configure-single-user-quota-limit)
  * [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#configure-single-user-quota-limit)



## October 20, 2026

Feature

**Gemini Enterprise: Antigravity Enterprise Gateway support**

Antigravity Enterprise Gateway lets organizations route model inference requests from the Antigravity app, Antigravity CLI, and Antigravity for IDEs through a centralized enterprise gateway before forwarding them to Google Cloud. This deployment enables organizations to inspect and audit model traffic, enforce custom security and network egress policies, and authenticate developers through a gateway API key without requiring individual Google Account sign-in.

Requests routed through Antigravity Enterprise Gateway use a centralized Google Cloud service account and are billed on a pay-as-you-go (PAYG) consumption basis through the Gemini Enterprise Agent Platform. This deployment model doesn't use your Gemini Enterprise seat-based subscription quotas (such as included Standard or Plus monthly allowances). You can't use a gateway and sign in with a Google Account at the same time. If you want to use your included subscription quota instead, disable the enterprise gateway and sign in with your Google Account.

This feature is generally available (GA).

For more information, see:

  * [Deploy Antigravity Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/deploy-enterprise-gateway)
  * [Connect Antigravity to an Enterprise Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/connect-enterprise-gateway).



Breaking

**Gemini Enterprise: Gemini 2.5 Pro discontinued in Canada and Japan**

Gemini 2.5 Pro has been discontinued for in-country Gemini Enterprise app deployments in Canada and Japan. Agents and chat sessions in these regions that previously used Gemini 2.5 Pro automatically switch to in-country Gemini 3.5 Flash.

Gemini 2.5 Pro remains available in the `global`, `us`, and `eu` regions.

For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations) and [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## October 16, 2026

Feature

**Gemini Enterprise: Configure citations for custom MCP data stores**

You can configure the `citation_mappings` parameter for custom Model Context Protocol (MCP) data stores using the REST API to display source citation chips when Gemini Enterprise answers questions using tools on your custom MCP server. This feature is generally available (GA).

For more information, see [Configure citations for custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custom-mcp-data-stores).

Feature

**Gemini Enterprise: Connect workflows in Workflow Builder to Confluence Data Center and Jira Data Center**

You can connect workflows in Workflow Builder to Confluence Data Center and Jira Data Center to search data and automate actions across these third-party apps.

For more information, see [Workflows overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows).

## October 15, 2026

Feature

**Gemini Enterprise: Anthropic models are available in the Gemini Enterprise app**

Administrators can make Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5—available to users in the Gemini Enterprise app. After an administrator turns on a model in the **Enable third-party models** section of the **Feature Management** tab, users can select the model in the model selector. Claude models are available in the `global` location and the `us` and `eu` multi-regions, and are charged on a pay-as-you-go basis.

This feature is generally available. For more information, see [Enable third-party models](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#enable-third-party-models).

## October 14, 2026

Feature

**Gemini Enterprise: Gemini 3.8 Flash regional availability in the United Kingdom**

Gemini 3.8 Flash is generally available (GA) in the United Kingdom.

  * **Location availability** : Supported in the UK (`europe-west2`) in-country region with in-region at-rest data residency (DRZ) and machine learning processing (MLP).
  * **App availability** : Turned on by default in the web app for the UK region. Administrators can manage access with the **Gemini 3.8 Flash** toggle under **Model availability**.



For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

Feature

**Gemini Enterprise: Gemini 4 Argon available in Workflow Builder**

Gemini 4 Argon is generally available (GA) for Workflow Builder. Gemini 4 Argon is also available in Workflow Builder workflow agents. Updates take up to a day to appear in workflow agents.

  * **Location availability** : Supported in `global`, `us`, and `eu` multi-regions, with data residency and ML processing support in `us` and `eu`. For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
  * **App availability** : Turned off by default. The toggle defaults to on beginning October 27, 2026. For instructions to turn on the model, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).



For more information, see [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder).

## October 13, 2026

Feature

**Gemini Enterprise: Gemini 4 Argon available in web app, mobile app, and AI developer tools**

Gemini 4 Argon is generally available (GA) for the Gemini Enterprise web app, mobile app, and AI developer tools.

  * **Location availability** : Supported in `global`, `us`, and `eu` multi-regions, with data residency and ML processing support in `us` and `eu`. For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
  * **App availability** : Turned off by default. The toggle defaults to on beginning October 27, 2026. Gemini 4 Argon is supported in the web app and mobile app. For more information about turning on the model, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * **AI developer tools** : Enabled by default for licensed users when **Antigravity authorized models** uses the default selection. If your organization specifies a custom model list, an administrator must manually select Gemini 4 Argon. For more information, see [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).



Feature

**Gemini Enterprise: Connect workflows in Workflow Builder to Microsoft Teams, Notion, and Salesforce**

You can connect workflows in Workflow Builder to Microsoft Teams, Notion, and Salesforce to search data and automate actions across these third-party apps.

For more information, see [Workflows overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows).

Feature

**Gemini Enterprise: Gemini 4 Argon is available in AlphaEvolve**

AlphaEvolve experiments can generate candidate programs with Gemini 4 Argon in the `global`, `us`, and `eu` regions. To use it, specify `gemini-4-argon` in the `models` field of `generationSettings`. Gemini 3.8 Flash remains the default model.

For more information, see [Supported models](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/reference-guide/api-reference#supported-models) and [AlphaEvolve limitations](https://docs.cloud.google.com/gemini/enterprise/docs/locations#alphaevolve-limitations).

## October 08, 2026

Feature

**Gemini Enterprise: Gemini 3.8 Flash regional availability in Singapore**

Gemini 3.8 Flash is generally available (GA) in Singapore (`sg`) with in-region at-rest data residency (DRZ) and machine learning processing (MLP).

For more information, see [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

Feature

**Gemini Enterprise: Anthropic Claude Opus 5.5 and Claude Sonnet 5.5 in AI developer tools**

Administrators can enable Anthropic Claude Opus 5.5 (`claude-opus-5-5`) and Anthropic Claude Sonnet 5.5 (`claude-sonnet-5-5`) for AI developer tools (Antigravity 2.0, Antigravity CLI, and Antigravity for IDEs). Third-party models are turned off by default:

  * **In-console Terms of Service consent flow** : Administrators can opt in to Claude Opus 5.5 and Claude Sonnet 5.5 directly in **Gemini Enterprise > Settings > AI developer tools > Antigravity authorized models** in the Google Cloud console without a separate Anthropic account or onboarding. For more information, see [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#enable-third-party-models).
  * **Location availability** : Third-party model inference is available in the `global`, `us`, and `eu` locations (in-country regions aren't supported). For a list of countries and regions that can access the model, see [Anthropic's Supported countries and regions](https://www.anthropic.com/supported-countries).
  * **Consumption billing** : Third-party model usage is billed as consumption on your Cloud Billing account and counts toward your project's spend cap, which covers all models. Overages must be turned on before you can enable a third-party model. For more information, see [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages) and the Cloud Billing SKUs for [Anthropic Claude Opus 5.5](https://cloud.google.com/skus?filter=opus&currency=USD&e=48754805) and [Anthropic Claude Sonnet 5.5](https://cloud.google.com/skus?filter=sonnet&currency=USD&e=48754805).
  * **Thinking levels** : Developers sign in with their existing Gemini Enterprise license and select Claude Opus 5.5 or Claude Sonnet 5.5 in the model picker at a thinking level of Low, Medium, High, or Max (for example, Claude Opus 5.5 (High)). Medium is the default.



## October 07, 2026

Feature

**Gemini Enterprise: Pay-as-you-go usage above quota enabled for Frontline, EDU, and Emerging Market editions**

You can enable pay-as-you-go usage above quota for additional Gemini Enterprise license-based editions:

  * **Frontline editions** : Frontline Starter and Frontline Worker
  * **EDU editions** : EDU and EDU Pro
  * **Emerging Market editions** : Standard Emerging Market, EDU Emerging, EDU Pro Emerging, and EDU Gov Emerging



When you enable Pay-as-you-go usage on an invoiced Cloud Billing account with an active subscription, users can continue using features at pay-as-you-go rates after reaching their pooled quota limits.

For more information, see the following resources:

  * [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#overages)
  * [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages)
  * [Overview of overages and spend controls](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview)



## October 06, 2026

Feature

**Gemini Enterprise: Control access to Antigravity features**

Administrators can control whether users in their organization have access to the following Google Antigravity features:

  * **Boost** : Uses a tiered multi-agent hierarchy to solve complex algorithmic challenges and deep debugging tasks with the `/boost` command. This feature is generally available (GA) in Antigravity.
  * **Teamwork** : Deploys a coordinated framework of autonomous subagents to execute large-scale, long-horizon projects using the `/teamwork-preview` command. This feature is in Preview in Antigravity.



These settings are generally available (GA) for administrators in Gemini Enterprise.

For more information, see [Configure feature settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#configure-feature-settings).

## October 02, 2026

Feature

**Gemini Enterprise: Federated query mode for Data Cloud connectors and Knowledge Catalog integration (Preview)**

Federated query mode is available in [Preview](https://cloud.google.com/products#product-launch-stages) for the following connectors:

  * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb#federated-query)
  * [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#federated-query)
  * [Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql#federated-query)
  * [Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner#federated-query)



Federated query mode allows Gemini Enterprise to query your operational and analytical data in place using the Model Context Protocol (MCP) and each user's own credentials, without copying or ingesting data into a data store.

In addition, the [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) integration is available in Preview. When you attach a Data Cloud connector in federated query mode, Knowledge Catalog is automatically enabled on the **Assistant** tab of your app to give the assistant read-only tools to search for data that the user has access to and retrieve technical and business context.

For more information, see the following resources:

  * [Connect to Data Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud)
  * [Best practices for Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices)
  * [Secure Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security)



## October 01, 2026

Announcement

**Gemini Enterprise: Gemini 2.5 Pro removal in Canada and Japan on October 20, 2026**

On October 20, 2026, Gemini 2.5 Pro will be removed from the Gemini Enterprise app in the Canada and Japan in-country regions. After this date, users in these regions can't select Gemini 2.5 Pro in the Gemini Enterprise app.

Gemini 2.5 Pro remains available in the `global`, `us`, and `eu` regions.

For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

Feature

**Gemini Enterprise: Turn Gemini 2.5 Pro on or off in the web app**

Administrators can turn Gemini 2.5 Pro on or off for the Gemini Enterprise web app in the `global`, `us`, and `eu` regions. Gemini 2.5 Pro remains turned on by default, so existing configurations aren't affected.

For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## September 29, 2026

Feature

**Gemini Enterprise: Support for new actions**

Support for new actions is generally available (GA) for the following data store:

  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook): Add attachments, Create message, Forward mail, Move mail, Reply to message, and Update message.



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: New data stores (Preview)**

The following data stores are available in Gemini Enterprise:

  * [D&B Finance Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_finance_analytics)
  * [Omni Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/omni_analytics)
  * [Zapier](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zapier)



These data stores are in Public Preview. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: Gemini 3.8 Flash is the default model for AlphaEvolve**

AlphaEvolve experiments can now generate candidate programs with Gemini 3.7 Flash and Gemini 3.8 Flash. Gemini 3.8 Flash is the default model AlphaEvolve uses when you do not explicitly specify a model, replacing Gemini 3.5 Flash. To use a different model, specify the one you want in the `models` field of `generationSettings`.

Experiments created before this change keep the model recorded in their configuration.

For more information, see [Supported models](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/reference-guide/api-reference#supported-models).

## September 28, 2026

Feature

**Gemini Enterprise: Configure granular access controls for apps and data stores**

Administrators can configure granular, resource-level Identity and Access Management (IAM) permissions to restrict access to specific Gemini Enterprise apps and data stores using the Google Cloud console, the Google Cloud CLI, or the REST API.

Key capabilities include:

  * **Independent resource-level permissions:** Grant **Gemini Enterprise Admin** , **Gemini Enterprise Viewer** , or **Gemini Enterprise User** roles on individual apps or data stores without granting access across the entire Google Cloud project.
  * **Custom project-level roles for restricted personas:** Create custom project-level roles for restricted administrators, restricted viewers, and restricted end users so principals can access only their assigned apps and data stores.
  * **Data store details and permissions management:** View data store configurations, connected apps, sync details, and user permissions in the Google Cloud console.



For more information, see:

  * [Configure granular access controls for apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores)

  * [Get data store and entity details](https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details).




## September 23, 2026

Feature

**Gemini Enterprise: Gemini 3.8 Flash enabled by default**

Gemini 3.8 Flash is generally available (GA) and enabled by default in the Gemini Enterprise app in the `global`, `us`, and `eu` regions. Gemini Enterprise administrators can use the **Gemini 3.8 Flash** toggle in feature management to turn off the model for their users, or turn it on for unsupported in-country regions by confirming the warning dialog to route traffic to the `global` endpoint.

For more information, see:

  * [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



## September 22, 2026

Feature

**Gemini Enterprise: D &B Risk Analytics data store**

The D&B Risk Analytics data store is generally available (GA) in Gemini Enterprise. You can connect D&B Risk Analytics to run third-party and counterparty risk workflows against your D&B Risk Analytics tenant using natural language. Supported workflows include KYB onboarding, counterparty due diligence, sanctions and adverse media screening, and supplier and financial risk assessment. The data store also supports actions, such as creating an entity, starting a screening, and updating tags and custom fields.

For more information, see [Connect D&B Risk Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_risk_analytics).

Feature

**Gemini Enterprise: New data store (Preview)**

The following data store is available in Gemini Enterprise:

  * [DirectBooker](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/directbooker)



This data store is in Public Preview. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

## September 21, 2026

Feature

**Gemini Enterprise: Transfer ownership of shared agents**

Administrators can transfer ownership of shared employee-made agents to another user or to themselves in the Google Cloud console. This is useful when reassigning agents created by departing employees or when temporary workers hand over agents to full-time staff.

Key characteristics and requirements include:

  * **Administrator only:** Only users with the Gemini Enterprise Admin role (`roles/discoveryengine.agentspaceAdmin` or `roles/discoveryengine.admin`) can transfer agent ownership. Agent owners cannot transfer ownership unless they are also administrators.
  * **Shared agents only:** Ownership transfer is supported only for agents that are already shared. Private agents cannot be transferred.
  * **Single owner:** Each agent has only one owner at a time. When ownership is transferred, the selected user becomes the sole owner, and the previous owner is retained as a permissioned user with the `agentUser` role.
  * **Agents with schedules or triggers:** If the transferred agent has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events. The new owner must enable it before being able to use the agent.
  * **Identity formats:** Administrators can transfer ownership to users with Google accounts (using email addresses) or to users in a Workforce Identity Federation (WIF) pool (using workforce identity principal identifiers).



For more information, see [Transfer agent ownership](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents#transfer-ownership).

## September 18, 2026

Feature

**Gemini Enterprise: Support for new actions (Preview)**

Support for new actions is available in Public Preview for the following data stores:

  * [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive): Copy folder, move file, move folder, rename file, rename folder, share file or folder, and update file properties.
  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook): Create calendar, RSVP to event, and update calendar.
  * [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint): Create list item, discard check out document, get list fields, get list item, list lists, share resource, update file properties, update list, update list item, and update page.
  * [Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams): Add member to channel, create channel, create chat, create schedule, create time off entry, update channel, update channel message, update chat, update chat message, and update time off entry.



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [Adobe Workfront](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/adobe-workfront)
  * [Kiwi.com](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi-com)
  * [Squarespace](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/squarespace)
  * [Starburst](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/starburst)
  * [Windsor.ai](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/windsor-ai) (actions supported)



You can search and read data from these data stores, and perform actions using natural language.

## September 17, 2026

Announcement

**Gemini Enterprise: Gemini Code Assist availability update for subscriptions**

If you're getting a new Gemini Enterprise Standard or Plus subscription or renewing an existing subscription online, the subscription no longer includes access to Gemini Code Assist features. Existing subscriptions that include Gemini Code Assist features can still access the features until the end of their subscription term.

Instead of Gemini Code Assist, you can use Antigravity for IDEs with AI developer tools. For more information, see [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview).

If you're still looking to use Gemini Code Assist with your Gemini Enterprise licenses, you can obtain a new Gemini Enterprise subscription that includes Gemini Code Assist by [contacting Google Cloud sales](https://cloud.google.com/contact).

Feature

**Gemini Enterprise: Voice input for the chat box**

You can speak your queries and prompts to Gemini Enterprise. Use the microphone button to record your voice, review and edit the transcribed text, and then submit the text.

This feature is generally available (GA). To make voice input available to users, a Gemini Enterprise administrator must turn on the **Enable speech-to-text** toggle in the Google Cloud console.

For more information, see the following:

  * [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Chat with the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat)



## September 14, 2026

Feature

**Gemini Notebook Enterprise: Rotate CMEK keys (GA)**

Rotating customer-managed encryption keys (CMEK) that protect your Gemini Notebook Enterprise instances is generally available (GA). When you make a new version of a registered key the primary version in Cloud Key Management Service (Cloud KMS), Gemini Notebook Enterprise detects the change and re-encrypts your data with the new key version automatically.

For more information, see [Rotate Cloud KMS keys](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/cmek#rotate-keys).

Feature

**Gemini Enterprise: Rotate CMEK keys (GA)**

Rotating customer-managed encryption keys (CMEK) that protect your Gemini Enterprise apps and data connectors is generally available (GA). When you make a new version of a registered key the primary version in Cloud Key Management Service (Cloud KMS), Gemini Enterprise detects the change and re-encrypts your data with the new key version automatically.

For more information, see [Rotate Cloud KMS keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#rotate-keys).

## September 11, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [D&B Risk Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_risk_analytics) (actions supported)
  * [Finnhub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/finnhub)
  * [Grafana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/grafana)



You can search and read data from these data stores, and perform actions using natural language.

Additionally, the following data store supports new actions in Public Preview:

  * [Clay](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clay): Find and enrich company, find and enrich contacts at company, and find and enrich list of contacts.



## September 10, 2026

Feature

**Gemini Enterprise: Pay-as-you-go edition and AI developer tools available for all invoiced Cloud Billing accounts**

Subscribing to the Gemini Enterprise Pay-as-you-go edition and accessing AI developer tools is available to all projects linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). Previously, only customers who received an email with the subject line _[Billing Update] New Gemini Enterprise overage billing controls launching Aug 17, 2026_ could access AI developer tools. This restriction no longer applies.

For more information, see:

  * [Compare editions of Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/editions)
  * [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview)



Feature

**Gemini Enterprise: Support for channel mentions and multi-turn conversations in the Gemini Enterprise app for Slack**

The Gemini Enterprise app for Slack has the following new capabilities:

  * **Channel mentions:** You can `@mention` the Gemini Enterprise app directly in Slack channels and conversational threads. The app returns responses privately so you can review them before choosing to share.
  * **Multi-turn conversations:** The Gemini Enterprise app remembers the context of your current session in direct messages. You can ask follow-up questions and refine previous responses. You can clear the context and start over by clicking **New chat**.



To enable these features, your Slack administrator must reinstall the Gemini Enterprise app. For more information, see [Install the Gemini Enterprise app for Slack in your Slack workspace](https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app#install-app). After the administrator reinstalls the app, end users must authorize the Slack connector. For more information, see [User authorization](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store#user_authorization). If you don't reinstall and re-authorize the Gemini Enterprise app, your Slack workspace retains the legacy experience.

These features are generally available (GA). For more information, see [Configure the Gemini Enterprise app for Slack](https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app#use-app).

## September 09, 2026

Breaking

**Gemini Notebook Enterprise: Website URL ingestion blocked by VPC Service Controls**

Projects with VPC Service Controls enabled can't add website URLs as notebook sources in Gemini Notebook Enterprise.

This is because direct website ingestion performs a live web crawl, generating outbound traffic beyond Google networks, which would violate VPC Service Controls perimeter policies.

Other source types, such as Google Docs and YouTube URLs, remain supported in projects with VPC Service Controls enabled.

## September 08, 2026

Feature

**Gemini Enterprise: Semantic search support in Google Cloud Marketplace (Preview)**

The agent search in Google Cloud Marketplace now supports semantic search, allowing you to find agents by describing their functionality (for example, "generate reports" or "translate text") without needing exact keyword matches.

For more information, see [Add and manage A2A agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents).

## September 04, 2026

Feature

**Gemini Enterprise: Monday federated data store (GA)**

Connecting a Monday data source with Gemini Enterprise using data federation is generally available (GA). You can use the Gemini Enterprise app assistant to search across your Monday boards, items, updates, and docs, and get answers grounded in that content without needing to ingest the data.

For more information, see [Set up a Monday data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/set-up-data-store).

Feature

**Gemini Enterprise: Create and manage projects**

You can create and manage projects in the Gemini Enterprise web app to build a dedicated knowledge base for your own work or to collaborate with your team. Within a project, you can upload files and chat privately with the assistant to get answers grounded in your project files and web search.

This feature is generally available (GA). To make projects available to users, a Gemini Enterprise administrator must turn on the **Enable projects** toggle in the Google Cloud console.

For more information, see the following:

  * [Create and manage projects](https://docs.cloud.google.com/gemini/enterprise/docs/projects)
  * [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)



Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [CoinDesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/coindesk)
  * [Relativity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/relativity)
  * [Streak](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/streak) (actions supported)
  * [Superhuman Mail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/superhuman-mail)



You can search and read data from these data stores, and perform actions using natural language.

## September 03, 2026

Feature

**Gemini Enterprise: Latency and error rate views for agents**

To monitor operational telemetry for your agents, use the two new views on the **Observability** tab:

  * **Latency:** Shows response times for your agents. This view displays p50 (median) and p95 (95th percentile) metrics for Time to First Token (TTFT), Time to First Answer (TTFA), and Time to Last Token (TTLT). TTFT counts the first token of any kind, including the model's thinking, while TTFA counts only the first token of the answer itself. You can also compare latencies by specific agent features, such as web search, media generation, or parametric interactions.
  * **Error rate:** Shows how your agent's requests resolve by tracking request volume and error rates. This view groups results by response class (OK, client errors, server errors, and canceled) and displays the associated client and server error codes.



This feature is generally available (GA). For more information, see [Access metrics](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics#access-metrics-for-agents).

Feature

**Gemini Enterprise: General availability of Workflow Builder (formerly Agent Designer)**

Workflow Builder (formerly known as Agent Designer) is generally available (GA) in Gemini Enterprise.

Workflow Builder enables users across your organization to build multi-step automated workflows to streamline tasks and connect to enterprise data.

Key capabilities in this release include:

  * **Workflows and on-demand execution** : Build multi-step workflows that can run on an automated schedule, trigger manually on demand, or execute via `@-mention` directly within Gemini Enterprise chat conversations.
  * **Chat agents** : Call chat agents from chat conversations using `@-mention`.
  * **In conversation** : Call workflows from a chat conversation using `@-mention`.
  * **Agent import** : Import existing A2A and ADK agents into Gemini Enterprise for centralized management, sharing, and enterprise governance.
  * **Enterprise connectors** : Connect workflows to enterprise data and applications—including Google Workspace (Gmail, Google Calendar, Google Chat, Google Drive) and third-party tools (Slack, Jira, ServiceNow, Confluence, Microsoft OneDrive, SharePoint, and Outlook)—to search data and execute actions.
  * **Enhanced Agent Gallery** : Discover and organize organization-wide and Google-created agents using keyword search, filter chips, and pinned items.
  * **Administrative controls** : Administrators can manage feature availability org-wide in the Google Cloud console, including dedicated toggles for workflows and chat agents.



For more information, see [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder).

## September 02, 2026

Feature

**Gemini Enterprise: Gemini 3.8 Flash available in Global, US, and EU regions**

Gemini 3.8 Flash is generally available (GA) in the `global`, `us`, and `eu` regions.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



## September 01, 2026

Feature

**Gemini Enterprise: Overage controls available for all invoiced Cloud Billing accounts**

Configuring overage controls in Gemini Enterprise is available to all projects linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). Previously, customers that received an email with the subject line _[Billing Update] New Gemini Enterprise overage billing controls launching Aug 17, 2026_ couldn't enable overages despite having an invoiced Cloud Billing account. This restriction no longer applies.

For more information, see [Overview of overages and spend controls](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview).

## August 31, 2026

Feature

**Gemini Enterprise: Support for federated data stores in Assured Workloads with FedRAMP High compliance**

Gemini Enterprise now supports connecting Google Workspace and third-party federated data stores to projects inside Assured Workloads folders, which automatically enforce security and compliance controls on your Google Cloud resources to meet FedRAMP High standards. This feature is generally available (GA). For more information, see

  * [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store).

  * [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).




Feature

**Gemini Enterprise: Gemini 3.5 Flash regional availability in Canada**

Gemini 3.5 Flash is available in Canada (`ca`) with in-region at-rest data residency (DRZ) and machine learning processing (MLP).

For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

Feature

**Gemini Enterprise: Gemini 3.1 Flash image available in US and EU multi-regions**

Gemini 3.1 Flash image (Nano Banana 2) for image generation is generally available in the `us` and `eu` multi-regions.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



Feature

**Gemini Enterprise: Protect sensitive data with content policies**

You can apply Sensitive Data Protection content policies to your Gemini Enterprise connectors, apps, and Gemini Notebook Enterprise notebooks.

Content policies inspect data for violating or unwanted content and block it. Content policies can block Gemini Enterprise apps from presenting sensitive or inappropriate material to users and can stop end users from uploading files that contain sensitive or inappropriate material.

This feature is generally available (GA). For more information, see [Protect sensitive data in sources](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data) and [Protect sensitive data in NotebookLM Enterprise sources](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/protect-sensitive-data).

## August 28, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [Campfire](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/campfire)
  * [Clay](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clay)
  * [CourtListener](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/courtlistener)
  * [Daloopa](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/daloopa)
  * [MSCI](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/msci)



You can search and read data from these data stores using natural language.

Additionally, the following data stores support new actions in Public Preview:

  * [AirOps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops): Update knowledge base document metadata.
  * [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable): Create records for a table.
  * [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk): Update event.



## August 26, 2026

Feature

**Gemini Enterprise: Updates to A2UI Material catalog component properties**

The [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference) has been updated to reflect the latest A2UI version v0.9 Material catalog component properties and schema:

  * **`MaterialButton`** : Added support for Material 3 styling properties (`appearance`, `disableRipple`, and `extended`), along with new variants (`icon`, `fab`, and `mini-fab`). Obsolete `color` and ARIA description properties have been removed.
  * **Validation`checks`**: Replaced the static `required` boolean property across input components (`MaterialCheckbox`, `MaterialDatepicker`, `MaterialInput`, `MaterialSelect`, and `MaterialTimepicker`) with the reactive validation `checks` rule array.
  * **`MaterialIcon` and `MaterialChips`**: Added the `tooltip` property on `MaterialIcon` and the `action` property on `MaterialChips`.
  * **Layout and input types** : Documented all supported `justify` alignment values for `MaterialColumn` and `MaterialRow`, and updated allowed input types for `MaterialInput`.



For more information, see [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference).

Feature

**Gemini Notebook Enterprise: Quizzes and Flashcards**

Flashcards and quizzes can be created from notebook sources. Select **Quiz** or **Flashcard** from the Studio panel in your notebook.

These features are generally available (GA).

## August 24, 2026

Feature

**Gemini Enterprise: D &B Commercial Graph data store (Preview)**

The D&B Commercial Graph data store is available in Public Preview in Gemini Enterprise. You can connect D&B Commercial Graph to search and import company data using natural language.

For more information, see [Connect D&B Commercial Graph](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d-and-b-commercial-graph).

Feature

**Gemini Enterprise: Cloud Monitoring observability for data connectors**

Cloud Monitoring telemetry for Gemini Enterprise data connectors (also referred to as data stores) has been updated with support for new metric dimensions and a new latency metric:

  * The `discoveryengine.googleapis.com/dataconnector/request_count` count metric has been updated to include three new dimensions: `tool_id` (the identifier of the connector tool invoked), `engine_id` (the Gemini Enterprise app identifier), and `response_code` (the gRPC response status). The existing `status` dimension remains supported.
  * A new latency metric, `discoveryengine.googleapis.com/dataconnector/request_latencies` (Beta), is available to monitor the distribution of tool invocation latency in milliseconds. It includes the dimensions `status`, `response_code`, `tool_id`, and `engine_id`.



For more information, see [Access metrics](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics).

## August 21, 2026

Feature

**Gemini Enterprise: AI developer tools on Standard Emerging Market edition**

The AI developer tools feature is available on the Gemini Enterprise Standard Emerging Market edition. Your project must be linked to an invoiced Cloud Billing account that receives an active monthly invoice to access the feature. This edition doesn't include bundled base quota or Antigravity credits.

**Note:** Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.

For more information, see the following:

  * [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview)
  * [Quotas and overages for Emerging market editions](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#quotas-emerging-market)



Feature

**Gemini Enterprise: New data stores and support for new actions (Public Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [Atlan](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/atlan-mcp)
  * [Bitly](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/bitly): Create QR code, create short link, update QR code, and update short link.
  * [FactSet AI-Ready Data](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/factset_ai_ready_data)
  * [FullStory](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fullstory)
  * [Globalping](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/globalping)
  * [Pendo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pendo_mcp)
  * [Stripe](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/stripe)



You can search and read data from these data stores using natural language.

Additionally, the following data stores support new actions in Public Preview:

  * [Descript](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/descript): Import media, prompt project agent, and publish project.
  * [Gamma](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gamma): Generate Gamma.
  * [Supabase](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/supabase): Apply migration, deploy edge function, execute SQL, pause project, and restore project.



## August 20, 2026

Feature

**Gemini Enterprise: Antigravity for IDEs available in AI developer tools**

Antigravity for IDEs is available as part of AI developer tools for Gemini Enterprise Standard, Plus, and Pay-as-you-go editions linked to an invoiced Cloud Billing account that receives an active monthly invoice. Antigravity for IDEs brings the power of Antigravity AI agents directly into your integrated development environment (IDE).

For more information, see the following:

  * [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview#tools-for-developers)
  * [Antigravity for IDEs extensions](https://antigravity.google/docs/ide/extensions)



Feature

**Gemini Enterprise and Gemini Notebook Enterprise: Autocomplete for sharing notebooks and agents with Okta**

If you use Okta as your external identity provider (IdP) with Workforce Identity Federation, you can configure System for Cross-domain Identity Management (SCIM).

Configuring SCIM enables autocomplete when sharing Gemini Notebook Enterprise notebooks and when sharing agents in Gemini Enterprise. With autocomplete, users can quickly search and select people or groups instead of entering full email addresses or group names.

This feature is generally available (GA).

For more information, see the following:

  * [Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider)

  * [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm#before_you_begin)

  * [Autocomplete for user emails and group names](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks#autocomplete)

  * [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent)

  * [Configure Workforce Identity Federation with Okta and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)




Feature

**Gemini Enterprise: Google Identity support for third-party data stores**

Google Identity is supported and recommended to manage access when connecting third-party data sources to Gemini Enterprise.

  * **What's new:** Gemini Enterprise supports Google Identity when connecting to third-party data sources with external identity providers (such as Microsoft Entra ID or Okta) using OIDC or SAML 2.0. This includes all third-party federated connectors and ingestion connectors, with the exception of Microsoft 365 data ingestion.

  * **Recommendation:** Google Identity is recommended for all new setups.

  * **Existing setups:** Customers already using Workforce Identity Federation can choose to remain on their existing configuration.




This feature is generally available (GA). For more information, see [Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

## August 18, 2026

Feature

**Gemini Enterprise: Google Sites federated connector (GA)**

The Google Sites federated connector is generally available (GA) on Gemini Enterprise. You can use the Gemini Enterprise app assistant to search across internal company websites, team sites, intranets, project hubs, and informational pages hosted on Google Sites, and get answers grounded in that content without needing to ingest the data.

For more information, see [Connect to Google Sites](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites).

Feature

**Gemini Enterprise: Gemini 3.6 Flash available in US and EU multi-regions**

Gemini 3.6 Flash is generally available in the `us` and `eu` multi-regions, and an allowlist is no longer required to use Gemini 3.6 Flash in the `us` multi-region. To make Gemini 3.6 Flash available to users in the Gemini Enterprise app, administrators must turn on the **Gemini 3.6 Flash** feature toggle in the Google Cloud console.

If an administrator previously turned on the **Gemini 3.6 Flash** toggle for an app in the `us` or `eu` multi-region and accepted the out-of-region routing warning, traffic for that app automatically routes to the app's location (`us` or `eu`). No action is required.

In regions where the model is not supported, administrators can still enable the model by acknowledging a warning that traffic routes to the `global` endpoint, which does not support regional data residency.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



Feature

**Gemini Enterprise: Access and configure AI developer tools**

AI developer tools is generally available (GA) for Gemini Enterprise Standard, Plus, and Pay-as-you-go editions with an invoiced Cloud Billing account. This launch includes access to Antigravity 2.0, Antigravity CLI, and Android Studio.

Key capabilities of AI developer tools include the following:

  * **Administrative controls** : Turn on or turn off AI developer tools, configure security policies (such as file access and terminal command execution), and manage model availability in the Google Cloud console.
  * **Usage metrics dashboard** : Monitor developer adoption, active users, token consumption, and API call volumes with integrated Cloud Monitoring and logging.



You can manage access to AI developer tools using a custom IAM role.

For more information, see the following:

  * [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview)
  * [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings)
  * [Create custom roles for AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles)
  * [View AI developer tools metrics](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics)



## August 17, 2026

Feature

**Gemini Enterprise: General availability for registering A2UI and A2A agents with Gemini Enterprise, including A2UI version v0.9 support**

Gemini Enterprise administrators can register and manage agents using [Agent to UI (A2UI)](https://a2ui.org/introduction/what-is-a2ui/) to build custom interfaces and the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) for communication with Gemini Enterprise.

With this release:

  * The feature is generally available (GA) instead of Public Preview.
  * Support is added for A2UI version v0.9, in addition to v0.8 protocols. A2UI v0.9 supports the new Material Design-based components catalog.



For more information, see:

  * [Register and manage agents using A2UI and A2A](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent)
  * [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference)
  * [Tutorial: Host an agent on Cloud Run](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/tutorial-host-agent-cloud-run)



## August 14, 2026

Feature

**Gemini Enterprise: Gemini 3.7 Flash available in the mobile app**

Gemini 3.7 Flash is generally available (GA) in the Gemini Enterprise mobile app. Mobile app users can select and use the Gemini 3.7 Flash model for their conversations within the app. To make the model available, administrators must turn on the **Gemini 3.7 Flash** feature toggle in the Google Cloud console.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



## August 13, 2026

Feature

**Gemini Enterprise: Create, upload, and share custom skills**

Skills are reusable custom instructions that help the Gemini Enterprise assistant perform specific tasks. End users can create, upload, and share skills. To enable this feature, administrators must turn on the skills and skill-sharing settings in **Feature Management**. Administrators can also configure skill availability and approve skill-sharing requests.

This feature is generally available (GA). For more information, see the following:

  * Learn how to [create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) as a Gemini Enterprise end user.
  * Learn how to [manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills) as a Gemini Enterprise administrator.



Feature

**Gemini Enterprise: Use Gemini 3.7 Flash**

Gemini 3.7 Flash is generally available (GA) in the `global`, `us`, and `eu` regions. To make Gemini 3.7 Flash available to users in the Gemini Enterprise app, administrators must turn on the **Gemini 3.7 Flash** feature toggle in the Google Cloud console.

**Note:** Gemini 3.7 Flash is not available in the Gemini Enterprise mobile app. For a correction to this release note, see the August 13th **Gemini Enterprise: Gemini 3.7 Flash availability in mobile app** release note.

For in-country regions where the model isn't supported, administrators can still enable the model by confirming a warning that traffic is routed to the `global` endpoint, which doesn't support regional data residency.

Gemini 3.7 Flash is also available in Agent Designer workflow agents. Updates take up to a day to appear in workflow agents.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



Announcement

**Gemini Enterprise: Gemini 3.7 Flash availability in mobile app**

Gemini 3.7 Flash is not available in the Gemini Enterprise mobile app. A new release note will be added when the Gemini 3.7 Flash rollout for the Gemini Enterprise mobile app is complete.

**Note:** This is a correction to the August 13th, **Gemini Enterprise: Use Gemini 3.7 Flash** release note.

## August 12, 2026

Feature

**Gemini Enterprise: GitHub connector with data federation**

The GitHub connector with data federation is generally available (GA) in Gemini Enterprise. The connector lets you search and act on GitHub repositories, issues, and pull requests directly from the Gemini Enterprise agent, with tool actions such as creating branches, adding issue comments, merging pull requests, and pushing files.

For more information, see the [Connect GitHub with data federation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github) documentation.

Feature

**Gemini Enterprise: AlphaEvolve HPC solution**

The AlphaEvolve HPC solution provides a distributed, containerized infrastructure for running large-scale evolutionary code optimization experiments on Google Cloud. If your evaluations require specialized hardware or exceed the resource limits of a single machine, use the AlphaEvolve HPC solution.

For more information, see [AlphaEvolve for HPC use cases](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/use-alphaevolve-hpc).

## August 11, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Public Preview)**

The following data stores are available in Public Preview in Gemini Enterprise:

  * [Cisco Workspaces](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/cisco-workspaces)
  * [Fibery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fibery)
  * [Gong](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gong)
  * [Guru](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/guru)
  * [Hex](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hex)
  * [LegalZoom](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/legalzoom)
  * [Mercury](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mercury-mcp)
  * [Miro](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro)
  * [Ramp](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ramp-mcp)
  * [Solve Intelligence](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/solve-intelligence)
  * [Vanta](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/vanta)
  * [Webex Meetings](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/webex-meetings)



You can search and read data from these data stores using natural language.

Additionally, the following data stores support new actions in Public Preview:

  * [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable): Update records for a table.
  * [Hex](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hex): Create threads and continue threads.
  * [Miro](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro): Create documents and update documents.
  * [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet): Add rows.



Feature

**Gemini Enterprise: Manage overages, spend limits, and costs for invoiced Cloud Billing accounts**

If your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription, administrators can enable overages, configure monthly spend limits, and monitor feature usage and costs in Gemini Enterprise:

  * **Enable overages** : Allow users to continue using features at pay-as-you-go rates after reaching pooled quotas. Overages are supported for Standard, Plus, and Standard Emerging Market editions for customers with an invoiced Cloud Billing account and at least one active, non-free-trial subscription.
  * **Set spend limits** : Configure monthly project spending caps and budget alert thresholds in Cloud Billing to prevent unexpected charges.
  * **View feature usage and costs** : Track pooled quota consumption, pay-as-you-go usage, and 30-day billing trends on the Usage & Spending page in the Gemini Enterprise console and Cloud Billing console.

**Note:** This feature only applies to projects linked to an invoiced Cloud Billing account. However, it isn't available if you received an email with the subject _[Billing Update] New Gemini Enterprise overage billing controls launching Aug 17, 2026_.**Note:** For an update to this release note, see the [September 1, 2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#September_1_2026).

For more information, see:

  * [Overview of overages and spend controls](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview)
  * [Configure overages and spend limits](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages)
  * [View feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage)
  * [View costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs)
  * [View Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs)
  * [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle)



## August 10, 2026

Feature

**Gemini Enterprise: Export user data to a CSV file**

Gemini Enterprise administrators can export user data to a comma-separated values (CSV) file to sort, filter, and analyze records offline. This feature is generally available (GA).

For more information, see [Export user data](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#export-user-data).

## August 07, 2026

Change

**Gemini Enterprise: Experimental agent telemetry aligned with OpenTelemetry generative AI semantic conventions**

Gemini Enterprise agents emit richer, standards-aligned telemetry based on the OpenTelemetry generative AI semantic conventions, in addition to the existing stable telemetry. Trace spans and Cloud Logging entries include standardized `gen_ai.*` attributes (for example, `gen_ai.agent.name`, `gen_ai.conversation.id`, `gen_ai.usage.input_tokens`, and `gen_ai.input.messages`) that describe agent, model, and tool activity.

Prompt and response message content appears in these attributes only when your observability settings allow logging of prompt inputs and response outputs; otherwise it is redacted or omitted. OpenTelemetry classifies these conventions as Development status, so this telemetry is experimental and subject to change.

For more information, see [Access traces and spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans#experimental-telemetry).

Feature

**Gemini Enterprise: Custom MCP server data stores**

You can connect your custom Model Context Protocol (MCP) server with Gemini Enterprise to securely access your company's private data, custom internal tools, and MCP-compliant third-party systems.

This feature is turned off by default. To enable it, an Organization Policy Administrator must remove the organization constraint. This feature is generally available (GA).

For more information, see:

  * [Set up your custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)
  * [Override the organization policy for Custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores)



## August 06, 2026

Change

**Gemini Enterprise: Description field removed from Custom MCP server data store**

Gemini Enterprise automatically calls your server's `tools/list` endpoint to discover and understand tools, parameter schemas, and capabilities directly. Because Gemini Enterprise routes requests using explicit tool definitions and parameter schemas, you don't need to write descriptions. This change simplifies data store setup and improves routing accuracy. Existing custom MCP data stores do not require any updates.

For more information, see [Set up a custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).

Announcement

**Gemini Enterprise: Postponed removal of Gemini 3.5 Flash in the Global region**

We have postponed the removal of Gemini 3.5 Flash from the `global` region in the Gemini Enterprise app. A revised removal schedule will be provided when available.

**Note:** This is a correction to the [July 21, 2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#July_21_2026).

## August 05, 2026

Change

**Gemini Enterprise: Clinical Trials data store no longer available**

The Clinical Trials data store is no longer available in Public Preview. The data store has returned to Private Preview.

**Note:** This is a correction to the [April 14, 2026](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#April_14_2026) release note.

## August 04, 2026

Feature

**Gemini Enterprise: End-to-end tracing support for data connectors**

Tracing support is extended end-to-end across the data connector workflow, introducing two new trace spans for better observability:

  * `execute_tool`: Represents the execution of a tool on the agent orchestration layer.
  * `invoke_connector`: Represents the request logic and execution on the connector execution layer.



These spans help you visualize end-to-end parent-child relationship workflows from the assistant prompt to the third-party API. You can search and filter for these spans in the Trace Explorer by service or span name, query them using turn-level legacy assist tokens via the `gemini_enterprise.assist_token` attribute, or look up traces using the W3C trace ID.

For more information, see [Access traces and spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans).

## August 03, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Public Preview)**

The following data stores are in Public Preview:

  * [Attio](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/attio)
  * [Cohesity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/cohesity)
  * [Descript](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/descript)
  * [Fiscal.ai](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fiscal-ai)
  * [Gamma](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gamma)
  * [iManage platform](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/imanage-platform)
  * [Moody's](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/moody_s)
  * [NetDocuments](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/netdocuments)
  * [Nexla](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/nexla-mcp-studio)
  * [Oracle NetSuite](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/oracle_netsuite)
  * [Pylon](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pylon)
  * [S&P Global - Deterministic Retrieval](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/s_p_global)
  * [Sanity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sanity)
  * [ServiceM8](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8)
  * [Supabase](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/supabase)
  * [Supermetrics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/supermetrics)
  * [SurveyMonkey](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/surveymonkey)
  * [Wix](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wix)



Additionally, support for new actions is available in Public Preview for the following data stores:

  * [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice): Create ticket notes.
  * [ServiceM8](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8): Add job note, change job status, compose email message, create job, create job activity, and send job to queue. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).



## August 01, 2026

Feature

**Gemini Enterprise: Pay for what you consume with the Pay-as-you-go edition**

The Gemini Enterprise Pay-as-you-go edition is generally available. With this edition, you pay for the feature usage your project consumes without pooled user license quotas. To get started, you need an invoiced Cloud Billing account with a one-seat minimum. You can monitor feature usage and set monthly spend limits in the Google Cloud console. This feature is rolling out gradually to eligible customers over the next few weeks.

For more information, see the following:

  * [Compare editions of Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/editions)
  * [Get a subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#get-subscription)
  * [View feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage)
  * [Set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit)



## July 29, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview:

  * [Compute Engine](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/google-compute-engine)
  * [Egnyte](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/egnyte)
  * [Sourcegraph](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sourcegraph)
  * [Tavily](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/tavily)



Additionally, support for new actions is available in Public Preview for the following data stores:

  * [AirOps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops): Suggest Brand Kit edits and write grid.
  * [Egnyte](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/egnyte): Create comments, create folders, create links, and upload files.
  * [Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch): Edit screens.
  * [Lovable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lovable): Deploy projects, enable databases, send messages, and set workspace knowledge.
  * [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet): Add favorites, create sheets, create workspaces, and update rows.



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

## July 28, 2026

Feature

**Gemini Enterprise: Microsoft Teams federated data store is generally available**

The Microsoft Teams federated data store is generally available (GA) in Gemini Enterprise. Connect Microsoft Teams to query channels, chats, teams, and messages, and execute supported actions directly from the assistant.

For more information, see [Connect Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams).

## July 27, 2026

Change

**Gemini Enterprise: Web app user interface changes**

Gemini Enterprise features an updated visual design:

  * **Side navigation** : Includes a compact layout where the logo sits in the sidebar, a Gemini icon replaces the menu icon, and user profile and notifications display at the bottom.

  * **Refreshed icon set** : Updates icons across the interface, including Library, Settings, and Send actions.

  * **Color theme** : Matches the updated Gemini color palette.




Existing functionality, integrations, and settings remain intact.

Feature

**Gemini Enterprise: Transparent thinking**

Transparent thinking is generally available (GA). During chat interactions, the assistant shares its real-time reasoning and planning in the user interface before calling tools or data sources.

An expandable section displays the tool activity between the thinking phase and the final answer. This transparency delivers a faster time to first token (TTFT) and improves perceived latency without increasing total response time.

For more information, see [Ask questions and view sources](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#ask_questions_and_view_sources).

## July 24, 2026

Feature

**Gemini Enterprise: Gemini 3.6 Flash in US multi-region**

If your project is on the allowlist, you can use Gemini 3.6 Flash in the US multi-region (`us`) with data residency at-rest (DRZ) and machine learning processing (MLP).

**Note:** For an update to this release note, see the [August 18, 2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#August_18_2026).

To request access to Gemini 3.6 Flash in the US multi-region, contact your Google account team.

For more information, see [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)

Feature

**Gemini Enterprise: Create and edit documents and slides in Canvas (GA)**

The Canvas assistant is generally available within the Gemini Enterprise web app. Canvas is a dedicated, interactive tool thats allows you to create and edit AI-generated documents and presentations directly from your chats. You can then export these to Google Workspace, Microsoft Office formats, and PDF. 

For more information, see [Create and edit documents and slides in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas).

A Gemini Enterprise app administrator must turn on the **Enable canvas** toggle in the web app feature management settings to let users use it. For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## July 22, 2026

Feature

**Gemini Enterprise: Support for unauthenticated Custom MCP Server data stores (Preview)**

When setting up a Custom MCP Server data store, you can select **No authentication** if your Model Context Protocol (MCP) server doesn't require authentication.

Creating a custom MCP Server data store is in Public Preview. For more information, see [Set up a custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).

## July 21, 2026

Feature

**Gemini Enterprise: Gemini 3.6 Flash available in the Global region**

Gemini 3.6 Flash is available in the `global` region. To make Gemini 3.6 Flash available to users in the Gemini Enterprise app, administrators must turn on the **Gemini 3.6 Flash** feature toggle.

Gemini 3.6 Flash is also available in Agent Designer workflow agents. Updates take up to a day to appear in workflow agents.

For more information, see:

  * [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
  * [Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations)



Announcement

**Gemini Enterprise: Gemini 3.5 Flash removal in the Global region**

Gemini 3.5 Flash will be removed as a model from the `global` region in the Gemini Enterprise app on August 4, 2026.

**Note:** There is a correction to this release note. See August 05, 2026.

For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## July 16, 2026

Feature

**Gemini Enterprise: Bring Your Own Identity (BYOID) for mobile apps (GA)**

The Gemini Enterprise mobile app is generally available (GA) for organizations using third-party identity providers. You can connect the mobile app to supported third-party identity providers without being on an allowlist.

For more information, see [Configure the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app).

Change

**Gemini Notebook Enterprise: NotebookLM Enterprise renamed to Gemini Notebook Enterprise**

NotebookLM Enterprise is renamed to Gemini Notebook Enterprise. Despite the rebrand, the product functionality remains the same, and the APIs still use the same endpoints. See [Create and manage notebooks (API)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks).

The Gemini Enterprise web app and the admin console display the name Gemini Notebook Enterprise. However, the subscription page still displays the name NotebookLM Enterprise.

## July 15, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Preview)**

The following data stores are available in Public Preview:

  * [Aiwyn Tax](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/aiwyn_tax)
  * [AllTrails](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/alltrails)
  * [Autodesk Product Help](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/autodesk-product-help)
  * [AWS Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/aws-marketplace)
  * [Courtroom5](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/courtroom5)
  * [pg-aiguide](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pg_aiguide)
  * [Taskrabbit](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/taskrabbit)
  * [Twilio Docs](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/twilio_docs)
  * [Viator](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/viator)
  * [ZoomInfo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zoominfo)



Additionally, support for new actions is available in Public Preview for the following data stores:

  * [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice): Update tickets.
  * [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk): Update ticket comments.
  * [ZoomInfo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zoominfo): Submit feedback.



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: Action-filtering support for Jira Data Center data stores (Preview)**

Filters configured on Jira Data Center federated data stores apply to both search queries and action execution. These filters let you specify which Jira projects are accessible to the Gemini Enterprise app assistant; mutations or retrievals on out-of-scope data fail or return no results.

This feature is in Public Preview. For more information, see:

  * [Set up a Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store) and [Add filters to a Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store)



## July 14, 2026

Announcement

**Gemini Enterprise: Idea Generation agent removal**

The Idea Generation agent which was in public preview is removed starting the week of July 14, 2026. Users can brainstorm ideas directly using the assistant.

  * For general brainstorming and creative thinking, use the Gemini Enterprise app [assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat).
  * For in-depth exploration or hypothesis generation, use [Deep Research](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant) or [Co-Scientist](https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve) agents.



## July 09, 2026

Announcement

**Gemini Enterprise: Enable skills feature management toggle is not available**

The **Enable skills** feature management toggle is not available. This feature is generally available (GA) with an allowlist in Gemini Enterprise. After your organization is added to the allowlist, end users can create and use skills directly in the app. To access this feature, contact your Google account manager.

We will update the release notes when the **Enable skills** toggle for administrators is available.

**Note:** This is a correction to the [June 17, 2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#June_17_2026).

Feature

**Gemini Enterprise: AlphaEvolve algorithm optimization agent (GA)**

The AlphaEvolve optimization service is generally available (GA) on the Gemini Enterprise agent. AlphaEvolve is a code optimization and discovery agent built on top of Gemini that helps solve the hardest algorithmic problems for your business and research. It combines creative, server-side LLM exploration with secure client-side code execution to autonomously discover new, optimized solutions that surpass human-designed baselines.

**Note:** AlphaEvolve does not support FedRAMP or DoD compliance requirements. Access for environments requiring these standards is restricted by default but can be requested through your account team.

For more information, see [AlphaEvolve documentation](https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview).

## July 07, 2026

Feature

**Gemini Enterprise: Managed organization policy constraints for data connectors (GA)**

You can use managed organization policy constraints to secure and control your data connectors in Gemini Enterprise.

With this release, the following constraints are generally available (GA):

  * **Restrict allowed data sources** : Use this policy to control which external data sources (such as Jira, Box, or Confluence) are permitted when adding a data store. For more information, see [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources).
  * **Restrict allowed egress FQDNs** : Use this policy to control the egress fully qualified domain names (FQDNs) that your data stores can connect to. For more information, see [Configure allowed egress FQDNs for data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns).



For an overview of these policies and how they interact, see [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview).

## July 06, 2026

Feature

**Gemini Enterprise: Support for Japan and UK regions (GA with allowlist)**

You can use the Gemini Enterprise app in the Japan (`asia-northeast1`) and United Kingdom (`europe-west2`) regions with at-rest data residency (DRZ) and machine learning processing (MLP) in region. You can also use the latest Gemini 3.5 Flash model in these regions with in-region at-rest DRZ and MLP.

These locations are available in GA with allowlist. To get access to these locations for use with Gemini Enterprise or NotebookLM Enterprise, contact your Google account team.

Certain limitations apply when using these regions. For more information, see [Data residency for Gemini Enterprise Standard and Plus Editions](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

## June 30, 2026

Feature

**Gemini Enterprise: Filters for Microsoft SharePoint data stores are generally available (GA)**

Filters for Microsoft SharePoint federated data stores are generally available (GA).

For more information, see [Add filters to a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store).

Feature

**Gemini Enterprise: Support for India and Singapore regions (GA with allowlist)**

You can use the Gemini Enterprise app in the India (`IN`) and Singapore (`SG`) regions with at-rest data residency (DRZ) and machine learning processing (MLP) in region. You can also use the latest Gemini 3.5 Flash model in these regions with in-region at-rest DRZ and MLP.

These locations are available in GA with allowlist. To get access to these locations for use with Gemini Enterprise or Gemini Notebook Enterprise, contact your Google account team.

Certain limitations apply when using these regions. For more information, see [Data residency for Gemini Enterprise Standard and Plus Editions](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

## June 29, 2026

Feature

**Gemini Enterprise: Jira Data Center federated data store**

The Jira Data Center federated data store is generally available (GA) in Gemini Enterprise.

For more information, see [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc).

Feature

**Gemini Enterprise: Action-filtering support for Microsoft SharePoint and OneDrive data stores (Preview)**

Filters configured on Microsoft SharePoint and Microsoft OneDrive federated data stores apply to both search queries and action execution. These filters let you specify which SharePoint sites and OneDrive paths are accessible to the Assistant; mutations or retrievals on out-of-scope data fail or return no results.

This feature is in Public Preview. For more information, see:

  * [Set up a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store) and [Add filters to a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store)
  * [Set up a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store) and [Add filters to a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store)



Feature

**Gemini Enterprise: HubSpot federated data store**

The HubSpot federated data store is generally available (GA) in Gemini Enterprise.

For more information, see [Set up a HubSpot data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot/set-up-data-store).

## June 26, 2026

Feature

**Gemini Enterprise: Confluence Data Center federated data store**

The Confluence Data Center federated data store is generally available (GA) in Gemini Enterprise.

For more information, see [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc).

## June 25, 2026

Feature

**Gemini Enterprise: Distribute licenses in the Google Cloud console**

You can distribute Gemini Enterprise licenses to projects and locations in the Google Cloud console. You can also reclaim unassigned licenses from a project.

This feature is generally available (GA). For more information, see:

  * [Distribute licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses)
  * [Reclaim unassigned licenses in a subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#reclaim-licenses)



Feature

**Gemini Enterprise: Governance for agents and MCP servers**

You can access Agent Registry from within Gemini Enterprise. Agent Registry provides a catalog of agents and custom Model Context Protocol (MCP) servers. From the catalog, you can select A2A agents or MCP servers to add to your Gemini Enterprise apps.

Furthermore, through egress policies managed by Agent Gateway, you can set allow and deny permissions on traffic going to these agents or these MCP servers.

This feature is generally available (GA). For more information, see:

  * [Import agents from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry) and

  * [Import custom MCP servers from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry).




Feature

**Gemini Enterprise: New data store and support for new actions (Public Preview)**

The Lovable data store is available in Public Preview in Gemini Enterprise. End users can search and read projects, and use natural language commands to perform actions, including adding connectors, remixing projects, and setting project knowledge and visibility. For more information, see [Connect Lovable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lovable).

Additionally, support for new actions is available in Public Preview for the following data stores:

  * [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable): Create bases, fields, tables, and record comments; update tables.
  * [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice): Create tickets; place service catalog item requests.
  * [Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch): Create and apply design systems.
  * [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk): Create and update calls; send replies; update tasks.
  * [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects): Create projects and tasks; update task lists.



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: View agent identity**

This feature is generally available (GA). As a Gemini Enterprise administrator, you can view an agent's identity on the Agent details page. This is typically the agent's SPIFFE ID.

If the SPIFFE ID is not published, the Agent Registry resource ID is displayed as a fallback. For more information, see [Agent identity](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#agent-identity).

## June 24, 2026

Feature

**Gemini Enterprise: Observability for agents (GA)**

Observability for Gemini Enterprise is generally available (GA). This includes:

  * Configuring observability settings at the app level and for individual agents.
  * Viewing metric dashboards in Metrics Explorer and on the agent's **Metrics** tab.
  * Viewing trace spans in Trace Explorer and on the agent's **Traces** tab.



For more information, see:

  * [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings)
  * [Access metrics](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics)
  * [Access traces and spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans)



## June 23, 2026

Feature

**Gemini Enterprise: Observability settings for Deep Research agents (Preview)**

You can configure observability settings for individual Deep Research agents, the same way as for Agent Designer employee-made agents. This allows you to monitor metrics in Metrics Explorer and view trace results in Trace Explorer for specific Deep Research agents.

Observability for Deep Research agents is enabled via the agent-level **Observability** toggle, not the app-level toggle used for the Core Assistant agent.

This feature is in Public Preview. For more information, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

## June 18, 2026

Feature

**Gemini Enterprise: Workflow agents (GA with allowlist)**

You can create, import, update, and use workflow agents in the Gemini Enterprise web app. These agents are designed to execute a sequence of steps or actions, which can include a mix of AI automation and human intervention, based on a configured trigger.

This feature is available as a GA with allowlist. To access this feature, contact your Google account manager. After your Google Cloud project is added to the allowlist, a Gemini Enterprise administrator must turn on the **Enable agent designer** toggle in the web app feature management settings to let users use it.

For more information, see:

  * [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)

  * [Workflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/workflow-agents) (You need to be on the allowlist to access the page.)




## June 17, 2026

Feature

**Gemini Enterprise: Create and manage skills (GA with allowlist)**

You can create, import, update, and use skills in the Gemini Enterprise web app. Skills are reusable custom instructions that help the assistant perform specific tasks.

This feature is available as a GA with allowlist. To access this feature, contact your Google account manager. After your Google Cloud project is added to the allowlist, a Gemini Enterprise administrator must turn on the **Enable skills** toggle in the web app feature management settings to let users use it.

**Note:** There is a correction to this release note regarding the **Enable skills** toggle. See [July 09, 2026](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#July_09_2026).

For more information, see:

  * [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

  * [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) (You need to be on the allowlist to access the page.)




Feature

**Gemini Enterprise: Gemini Enterprise app for Slack**

Gemini Enterprise administrators can integrate Gemini Enterprise with Slack to deliver AI-powered answers and search directly to users in their Slack workspace. Once integrated, users can interact with Gemini Enterprise through direct messages and slash commands to receive answers that incorporate data from all connected data stores.

This feature is generally available (GA). For more information, see [Configure the Gemini Enterprise app for Slack](https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app).

## June 16, 2026

Feature

**Gemini Enterprise: ServiceNow data store actions and federation**

The ServiceNow data store supports federation and assistant actions in Gemini Enterprise.

You can connect a ServiceNow site to search and read incidents, change requests, tasks, and knowledge base articles using natural language. You can also perform actions, such as creating and updating incidents, directly from the Gemini Enterprise app.

This feature is generally available (GA). For more information, see [Connect ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow).

## June 15, 2026

Feature

**Gemini Enterprise: New data stores and support for new actions (Public Preview)**

The following data stores are available in Public Preview:

  * [AirOps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops)
  * [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable)
  * [Calendly](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/calendly)
  * [Dynamics 365](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365)
  * [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice)
  * [Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch)
  * [Intercom](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/intercom)
  * [MailerLite](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mailerlite)
  * [Zoho CRM](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohocrm)



Additionally, support for new actions is available for the following data stores:

  * [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet)
  * [Wrike](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wrike)
  * [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects)



For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

Feature

**Gemini Enterprise: Observability settings for individual agents (Preview)**

You can configure observability settings for individual agents in Agent Designer employee-made agents. This allows you to monitor metrics in Metrics Explorer and view trace results in Trace Explorer for specific agents.

Observability settings for individual agents are configured inside the agent-level settings. Previously, observability was only available at the application level, which applies to the Core Assistant agent.

This feature is in Public Preview. For more information, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

## June 12, 2026

Feature

**Gemini Enterprise mobile app: General availability (GA) for Google Identity users**

The Gemini Enterprise mobile app is generally available (GA) for organizations using Google Identity as their identity provider. Users can access their agents, search enterprise data, utilize voice features, and perform interactive actions from iOS and Android devices.

With this release, administrators can display a configuration QR code on the web app homepage to enable user access by scanning the QR code. For organizations using Microsoft Entra ID, access to the mobile app is in GA with allowlist.

To learn more, see [Configure the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app) and [Use the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/use-the-mobile-app).

## June 09, 2026

Feature

**Gemini Enterprise: Share agents with Google Groups**

End users can share agents created using Agent Designer with Google Identity groups, provided an administrator has enabled this feature for the Gemini Enterprise app.

This feature is generally available (GA). For more information, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/share-agent).

## June 08, 2026

Announcement

**Gemini Enterprise: Gemini 3.5 Flash feature management toggle is no longer available after June 16, 2026**

Starting June 16, 2026, the Gemini 3.5 Flash feature management toggle is no longer available. This change applies to the Global, US, and EU multi-regions.

**Note:** This is a correction to the date mentioned previously in the [June 05, 2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#June_05_2026).

## June 05, 2026

Feature

**Gemini Enterprise: Asana data store (Preview)**

The Asana data store is available in Public Preview in Gemini Enterprise.

You can connect an Asana account to search and read projects, workspaces, teams, and tasks using natural language. You can also perform actions, such as creating projects and tasks, directly from the Gemini Enterprise app.

For more information, see [Connect Asana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/asana).

Announcement

**Gemini Enterprise: Administrator control for Gemini 3.5 Flash**

As a reminder, effective June 9, 2026, the feature management toggle for Gemini 3.5 Flash is no longer available. Gemini 3.5 Flash is enabled by default for all users in the Gemini Enterprise app and cannot be disabled.

This change applies to the Global, US, and EU multi-regions.

**Note:** The effective date has been extended by one day from the [originally announced schedule](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#May_26_2026).

## June 03, 2026

Feature

**Gemini Enterprise: DRZ and MLP compliance in the EU for Google NotebookLM Enterprise**

Gemini Enterprise is compliant with data residency (DRZ) and machine learning processing (MLP) requirements in the EU for Google NotebookLM Enterprise for adding sources and interacting with the sources (chat). However, the Discover Sources feature and Studio features, such as audio overview, slide deck, infographic, video overview, mind map, and reports, are not MLP compliant.

For more information on location limitations, see [NotebookLM limitations](https://docs.cloud.google.com/gemini/enterprise/docs/locations#notebooklm-limitations).

## June 02, 2026

Feature

**Gemini Enterprise: Gemini 3 pro image (Nano Banana Pro) and Gemini 3.1 flash image (Nano Banana 2) for image generation**

Gemini 3.1 flash image (Nano Banana 2) and Gemini 3 pro image (gemini-3.0-pro-image) are generally available (GA) in Gemini Enterprise app.

To make these models available to users in your Gemini Enterprise app, a Gemini Enterprise administrator can manage them in the feature controls:

  * **Gemini 3 pro image (Nano Banana Pro)** : Turned off by default and is only available in the Global region.

  * **Gemini 3.1 flash image (Nano Banana 2)** : Turned off by default and is only available in the Global region. If an administrator turned on this model during its Public Preview, it remains turned on in GA in the Gemini Enterprise app.




For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## June 01, 2026

Announcement

**Gemini Enterprise: Agent Designer migration to Gemini 3.5 Flash**

Agent Designer agents in the US and Global regions that previously migrated from Gemini 2.5 Flash and Gemini 2.5 Pro to Gemini 3.1 Pro have been migrated to Gemini 3.5 Flash. This migration is automatic and requires no action.

To use a different model, edit your agent's settings using either [conversational chat](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/edit-agent#edit-using-chat) or the [flow builder](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/edit-agent#edit-using-flow).

Feature

**Gemini Enterprise: Create and edit documents and slides in Canvas**

Canvas is a dedicated, interactive tool within the Gemini Enterprise web app. It allows you to create and edit AI-generated documents and presentations directly from your chats. You can then export these to Google Workspace, Microsoft Office formats, and PDF.

A Gemini Enterprise administrator must turn on the feature so that users can use it in the Gemini Enterprise app. For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

For more information, see [Create and edit documents and slides in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas).

## May 28, 2026

Feature

**Gemini Enterprise: Release of Core Assistant (General Availability) and new Trace and Metrics information for Core Assistant (Preview)**

This release includes Core Assistant, a Google-provided ("Made by Google") root agent that handles interactions when users talk to the Gemini Enterprise app without specifying any other agent.

Core Assistant is [Generally Available](https://cloud.google.com/products#product-launch-stages).

Core Assistant includes new observability and monitoring functionality:

  * **Traces** : A chronological summary and visualization of trace spans showing execution flow, duration, inputs, outputs, and precise details if OpenTelemetry trace and logging instrumentation is enabled.
  * **Metrics** : A default-on dashboard displaying session counts, latency, agent invocations, tool call counts, and error rates without any extra billing costs.



The Trace and Metrics tabs are in [Public Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Observe and trace agent behavior with Core Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant).

## May 27, 2026

Feature

**Gemini Enterprise: Slack data store**

The Slack data store is generally available (GA) in Gemini Enterprise.

You can connect a Slack Workspace to search and read conversations, files, and messages using natural language. You can also perform actions, such as sending and scheduling messages, directly from the Gemini Enterprise app chat box.

For more information, see [Connect Slack](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack).

## May 26, 2026

Feature

**Gemini Enterprise: Filter support for Google Sites data stores (Preview)**

You can add Site URL prefix filters to Google Sites data stores in Gemini Enterprise to include or exclude specific sites from search results.

This feature is in Public Preview. For more information, see [Add filters to a Google Sites data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store).

Deprecated

**Gemini Enterprise: Gemini Enterprise assist is deprecated**

The Gemini Enterprise assist feature is deprecated and shut down. Users can find comprehensive and relevant answers directly in the Gemini Enterprise documentation.

Feature

**Gemini Enterprise: Data store for PagerDuty (Preview)**

You can connect PagerDuty data stores to Gemini Enterprise.

Support for PagerDuty data stores is in Public Preview. For more information, see [Connect PagerDuty](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty).

Announcement

**Gemini Enterprise: Administrator control for Gemini 3.5 Flash**

Gemini Enterprise administrators can use the feature management toggle to turn on or turn off Gemini 3.5 Flash, controlling its visibility in the Gemini Enterprise app chat box.

The feature management toggle for Gemini 3.5 Flash will not be available after June 8, 2026. Starting June 8, 2026, Gemini 3.5 Flash is enabled by default and cannot be turned off for users in the Gemini Enterprise app.

For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## May 20, 2026

Deprecated

**Google NotebookLM Enterprise: The Podcast API is deprecated**

The [Podcast API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api) is deprecated. Google isn't allowlisting new customers.

This feature was available as GA with allowlist.

## May 19, 2026

Feature

**Gemini Enterprise: Data store for Crossbeam (Preview)**

You can connect Crossbeam data stores to Gemini Enterprise.

Support for Crossbeam data stores is in Public Preview. For more information, see [Connect Crossbeam](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crossbeam).

Feature

**Gemini Enterprise: Use Gemini 3.5 Flash (GA)**

Gemini 3.5 Flash is generally available (GA) in the Global, US, and EU regions with Gemini Enterprise. Users can select it in the model selector dropdown within the Gemini Enterprise app assistant and in Agent Designer.

As Gemini 3.5 Flash is the current GA Flash model, Gemini 2.5 Flash is removed from the model selector. Administrators can't toggle Gemini 3.5 Flash off.

For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

Feature

**Google NotebookLM Enterprise: Create slide decks and infographics**

You can create slide decks and infographics using Google NotebookLM Enterprise. This feature is generally available (GA). For more information on the usage limits, see [Usage limits](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

## May 17, 2026

Feature

**Gemini Enterprise: Agent Designer defaults to Gemini 3.1 Pro for US and Global regions**

New agents created in Agent Designer use Gemini 3.1 Pro by default in the US and Global regions. Gemini Enterprise app users can select Gemini 2.5 Pro or Gemini 2.5 Flash in the agent settings after creation. Default configurations in other regions where Gemini 3.1 Pro is not available remain unchanged.

Existing Agent Designer agents in US and Global regions that previously used Gemini 2.5 Pro or Gemini 2.5 Flash have been migrated to Gemini 3.1 Pro to provide improved performance. This version of Gemini 3.1 Pro is in Limited Availability and includes General Availability (GA) Service Level Objectives (SLOs). Gemini Enterprise app users can manually revert their agents to Gemini 2.5 Pro or Gemini 2.5 Flash in the agent settings if preferred.

For more information on creating agents in Agent Designer, see [Create an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/create-agent).

## May 15, 2026

Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data stores are available in Gemini Enterprise:

  * [Dice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dice)
  * [Midpage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/midpage)
  * [PandaDoc](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pandadoc)
  * [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet)
  * [Wrike](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wrike)
  * [Zoho Books](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks)
  * [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk)
  * [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects)



These data stores are in Public Preview. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

## May 13, 2026

Announcement

Correction: **Gemini Enterprise: EU region for Gemini 3 models is coming soon**

The availability of Gemini 3.1 Pro and 3 Flash in the EU region has been updated to "coming soon". Previously, it was listed as currently available.

For more information, see: [Using Gemini 3.1 Pro and 3 Flash in Limited Availability](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview).

## May 12, 2026

Feature

**Gemini Enterprise: Data store for GitLab (Preview)**

You can connect GitLab data stores to Gemini Enterprise.

Support for GitLab data stores is in Public Preview. For more information, see [Connect GitLab](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab).

## May 08, 2026

Feature

**Gemini Enterprise: Box data store using data federation**

Connecting a Box data source with Gemini Enterprise using data federation is generally available (GA).

For more information, see [Set up a Box data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store).

## May 07, 2026

Feature

**Gemini Enterprise: Data store for Google Sites (Preview)**

You can connect Google Sites data stores to Gemini Enterprise.

Support for Google Sites data stores is in Public Preview. For more information, see [Connect to Google Sites](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites).

Security

**Gemini Enterprise: Multiple API endpoints for the Integration Platform were inadvertently exposed.**

This issue has been resolved, and access has been restricted. No action is required from external customers.

## May 06, 2026

Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data stores are available in Gemini Enterprise:

  * [Mermaid Chart](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mermaid_chart)
  * [Blockscout](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/blockscout)
  * [Open Targets](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/open_targets)
  * [Apollo GraphOS MCP Tools](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/apollo-graphos)



These data stores are in Public Preview. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

## April 30, 2026

Announcement

**Gemini Enterprise: Access to Gemini 3.1 Pro and 3 Flash in Limited Availability**

Gemini Enterprise users have access to 3.1 Pro and 3 Flash in Limited Availability. This means that Gemini Enterprise app users get the generally available Service Level Objectives (SLOs) for these models as part of the Gemini Enterprise Service while the models are in Preview. We are currently monitoring the model's performance and determining the appropriate, long-term (SLOs) and plan to offer these SLOs soon. Additionally, we currently support standard Data Location (Data Residency or "DRZ") commitments in US/EU/global multi-regions.

**Note:** There is a correction to this release note. See May 13, 2026.

For more information, see: [Using Gemini 3.1 Pro and 3 Flash in Limited Availability](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview).

## April 28, 2026

Feature

**Gemini Enterprise: Custom MCP server data stores**

You can connect your custom Model Context Protocol (MCP) server with Gemini Enterprise to securely access your company's private data, custom internal tools, and MCP-compliant third-party systems.

This feature is turned off by default. To enable it, an Organization Policy Administrator must remove the organization constraint.

For more information, see:

  * [Set up your custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)
  * [Override the organization policy for Custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores)



## April 21, 2026

Feature

**Gemini Enterprise: View agent identity (Preview)**

As a Gemini Enterprise administrator, you can view an agent's identity on the Agent details page. This is typically the agent's SPIFFE ID.

This feature is in Public Preview. If the SPIFFE ID is not published by the publisher, the Agent Registry resource ID is displayed as a fallback. For more information, see [Agent identity](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#agent-identity).

Feature

**Gemini Enterprise: Register agents using A2UI and A2A with Gemini Enterprise (Preview)**

Gemini Enterprise administrators can register and manage agents using [Agent to UI (A2UI)](https://a2ui.org/introduction/what-is-a2ui/) to build custom interfaces and the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) for communication with Gemini Enterprise.

This feature is in Public Preview. For more information, see:

  * [Register and manage agents using A2UI and A2A](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent)
  * [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference)



## April 20, 2026

Feature

**Gemini Enterprise: Request access to Google Cloud Marketplace agents (Preview)**

End users can request access to Google Cloud Marketplace agents from Agent Gallery. Admins can configure the visibility of these agents, view purchase requests, and manage access requests.

This feature is in Public Preview. For more information, see:

  * [Browse agents with Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery)
  * [Add and manage A2A agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents)



Feature

**Gemini Enterprise: Register ADK agents hosted on Vertex AI Agent Engine**

You can register ADK agents hosted on Vertex AI Agent Engine with Gemini Enterprise. This includes agents running within Vertex AI Agent Engine in a different Google Cloud project. This feature is generally available (GA).

For more information, see:

  * [Register and manage ADK agents hosted on Vertex AI Agent Engine](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
  * [Configure cross-project ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents)



## April 15, 2026

Feature

**Gemini Enterprise: Use Gemini Enterprise Admin and Gemini Enterprise User IAM roles**

Use the Gemini Enterprise Admin and Gemini Enterprise User roles.

The Gemini Enterprise Admin and Gemini Enterprise User roles still map to the Discovery Engine admin and user roles, so existing customers do not need to make any changes.

For more information, see [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).

## April 14, 2026

Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data store are available in Gemini Enterprise:

  * [Crypto](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crypto)
  * [Excalidraw](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/excalidraw)
  * [GoDaddy](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/godaddy)
  * [Granted](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/granted)
  * [Hugging Face](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/huggingface)
  * [Invideo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/invideo)
  * [Kiwi](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi)
  * [LastMinute](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lastminute)
  * [Microsoft Learn](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn)
  * [Trivago](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/trivago)
  * [Clinical Trials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clinicaltrials)



These data stores are in Public Preview. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

**Note:** There is a correction to this release note regarding the Clinical Trials data store. See [August 05, 2026](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#August_05_2026).

## April 13, 2026

Feature

**Gemini Enterprise: Enhanced filtering for Google Chat data stores (Preview)**

You can configure filters for your Google Chat data stores using either the Google Cloud console or the API. These filters allow you to define exactly which Google Chat data is accessible to the Assistant by including or excluding specific content.

This feature is in Public Preview and is applicable for federated search only. For more information, see [Set up a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store) and [Add filters to a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store).

## April 07, 2026

Feature

**Gemini Enterprise: Dropbox federated data store**

The Dropbox federated data store is generally available (GA) in Gemini Enterprise.

For more information, see [Set up a Dropbox data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/data-store).

## April 03, 2026

Feature

**Gemini Enterprise: Jira and Confluence federated data stores**

The Jira and Confluence federated data stores are generally available (GA) in Gemini Enterprise.

For more information, see:

  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)



## April 02, 2026

Feature

**Google NotebookLM Enterprise: Autocomplete for email addresses and group names when sharing notebooks**

When sharing notebooks with users and groups, autocomplete is available to help users quickly select the correct email addresses and group names.

If your organization uses the Google Identity Provider, no action is required. If your organization uses Third-party identity and Microsoft Entra ID, a Gemini Enterprise administrator must provision a [System for Cross-domain Identity Management (SCIM) tenant for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim) to enable autocomplete. For more information about identity setup, see [Set up NotebookLM Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm).

This feature is generally available (GA). For more information, see [Share a notebook](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks).

## April 01, 2026

Feature

**Gemini Enterprise: Data connector request count metric**

Monitor the total number of requests to your Gemini Enterprise data connectors or data stores using the **Gemini Enterprise DataConnector - Gemini Enterprise DataConnector Request Count** metric in Metrics Explorer.

This feature is generally available (GA). For more information, see [Access metrics in Metrics Explorer](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics).

## March 31, 2026

Feature

**Gemini Enterprise: Support for new actions** New actions are available for the following data stores:

  * [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail)
  * [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)
  * [GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github) (Public Preview)
  * [HubSpot](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot) (Public Preview)
  * [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday) (Public Preview)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

Feature

**Gemini Enterprise: Connect Salesforce data using data federation**

You can connect Salesforce data stores to Gemini Enterprise using data federation.

For more information, see [Connect Salesforce](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce).

Feature

**Gemini Enterprise: Federated connector error logs in Logs Explorer**

You can view detailed error logs for your federated connectors in Logs Explorer. These logs include connection problems, data transformation issues, or API errors.

For more information, see [Access Gemini Enterprise connector error logs with Cloud Logging](https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging).

Feature

**Gemini Enterprise and Google NotebookLM Enterprise: BSI C5:2020 compliance**

Gemini Enterprise and Google NotebookLM Enterprise are certified for [BSI C5:2020](https://cloud.google.com/security/compliance/bsi-c5) compliance.

## March 30, 2026

Feature

**Gemini Enterprise: Include cross-domain documents feature for Google Drive (Preview)**

When configuring a Google Drive data store, the **Include cross-domain documents** feature lets you search and index documents outside your organization. Enable this setting during app creation or on the **Manage web app features** page for existing apps.

This feature is in Public Preview. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## March 26, 2026

Feature

**Gemini Enterprise: Chat with files in the Google Drive connector**

Gemini Enterprise can analyze content and generate answers from CSV, PDF, PPTX, and XLSX files in the Google Drive connector, eliminating the need to upload these files to the assistant.

This feature is generally available (GA). For more information, see [Chat with files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

## March 24, 2026

Feature

**Gemini Enterprise: Enhanced filtering for Microsoft OneDrive data stores (Preview)**

You can configure filters for your Microsoft OneDrive data stores using either the Google Cloud console or the API. These filters allow you to define exactly which content is accessible to the Assistant by including or excluding specific OneDrive paths.

This feature is in Public Preview. For more information, see [Set up a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store) and [Add filters to a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store).

Feature

**Gemini Enterprise: Get insights with the Data Insights agent (GA with allowlist)**

The Data Insights agent is a Made by Google agent that provides insights from your BigQuery data. This feature is available as a GA with allowlist. Contact your Google Cloud [sales representative](https://cloud.google.com/contact) to access this feature.

## March 23, 2026

Feature

**Gemini Enterprise: Data connector for Docusign (Preview)**

You can connect Docusign data stores to Gemini Enterprise.

Support for Docusign data stores is in Public Preview. For more information, see [Connect Docusign](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign).

## March 17, 2026

Feature

**Gemini Enterprise: Grace period for license deactivation**

To ensure a smooth transition and prevent service interruptions when a subscription ends early, we've introduced a one-week (seven days) grace period. During this time, you can continue to use the service while you transition to a new subscription.

This feature is generally available (GA). For more information, see [Handle early termination](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#handle-early-termination).

## March 13, 2026

Feature

**Gemini Enterprise: Enhanced filtering for Microsoft SharePoint data stores (Preview)**

You can configure filters for your Microsoft SharePoint data stores using either the Google Cloud console or the API. These filters allow you to define exactly which content is accessible to the Assistant by including or excluding specific SharePoint sites.

This feature is in Public Preview. For more information, see [Connect Microsoft SharePoint Online](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint).

Feature

**Gemini Enterprise: Search generated images and videos**

You can search your generated images and videos in the Gemini Enterprise assistant. You can also search for items directly in the Library.

This feature is generally available (GA). For more information, see [Search your Gemini Enterprise content](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-organize#search-your-gemini-enterprise-content) and [View, download, and search generated images and videos](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#view_download_and_search_generated_images_and_videos).

## March 12, 2026

Feature

**Gemini Enterprise: Observability settings (Preview)**

Gemini Enterprise administrators can enable observability settings to view the following data from your interactions with the assistant in your Gemini Enterprise web app:

  * View metrics in Metrics Explorer.
  * View traces and spans in Trace Explorer.



This feature is in Public Preview. For more information, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

## March 11, 2026

Feature

**Gemini Enterprise: Configure retention period for assistant chats**

Gemini Enterprise administrators can configure the retention period for assistant chat history. This feature is generally available (GA). For more information, see [Configure the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant).

Feature

**Gemini Enterprise: Support for new actions**

New actions are available for the following data stores:

  * [GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github) (Public Preview)
  * [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)
  * [Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion) (Public Preview)
  * [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify) (Public Preview)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

Feature

**Gemini Enterprise: Data connector for Google Chat (Preview)**

You can connect Google Chat data stores to Gemini Enterprise.

Support for Google Chat data stores is in Public Preview. For more information, see [Connect Google Chat](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat).

## March 04, 2026

Feature

**Gemini Enterprise: Data connector for GitHub (Preview)**

You can connect GitHub data stores to Gemini Enterprise. For more information, see [Connect GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github).

This feature is in Public Preview.

Feature

**Gemini Enterprise: Support for new actions (Preview)**

New actions are available for the following data stores:

  * [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc)
  * [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday)
  * [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify)
  * [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions). These actions are in Public Preview.

Fixed

**Gemini Enterprise: Agent Designer model configuration fix**

Fixed an issue in Agent Designer that caused agent model configurations to be cleared or fail to appear during the transition from Gemini 3 Pro (Preview) to Gemini 3.1 Pro (Preview).

Feature

**Gemini Enterprise: Chat with files in the Microsoft Outlook and Box connectors**

Gemini Enterprise can analyze content and generate answers from email attachments in the Microsoft Outlook connector and from CSV, PDF, PPTX, and XLSX files in the Box connector, removing the need to upload these files to the Gemini Enterprise assistant.

This feature is generally available (GA). For more information, see [Chat with files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

## March 03, 2026

Feature

**Gemini Enterprise: Export assistant responses to Google Docs and Google Sheets**

You can export chat responses from the assistant to Google Docs. You can also export tabular and CSV data from a response to Google Sheets.

This feature is generally available (GA). For more information, see [Export to Google Docs and Google Sheets](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#export-responses).

Feature

**Gemini Enterprise: Use Veo 3.1 for video generation**

Use Veo 3.1 to generate videos in the Gemini Enterprise web app. Veo 3.1 is replacing Veo 3.0 for video generation. For more information, see [Generate a video](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#generate_a_video).

To use this feature, a Gemini Enterprise administrator must turn on **Enable video generation** setting. For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

This feature is generally available (GA).

## February 26, 2026

Feature

**Gemini Enterprise: Support for new data stores (Preview)**

The following data stores are supported in Public Preview:

  * [HubSpot](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot)
  * [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday)
  * [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify)



## February 23, 2026

Feature

**Gemini Enterprise: Share agents created using Agent Designer**

The agent sharing feature in Agent Designer is generally available (GA) with the following enhancements:

  * **Direct sharing:** Agent owners can share agents directly with other users in their organization without prior admin approval.
  * **Configurable admin review:** Admins can turn on or turn off the requirement for manual review of sharing requests.
  * **Additional sharing controls:** Admins can share agents with Google Groups and Workforce Identity Federation (WIF) identity pools.



For more information, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/share-agent).

Feature

**Gemini Enterprise: Sharing controls for employee-made agents**

Employee-made agents can share within an organization. Admins can manage how these agents are shared by using the **Enable agent sharing** and **Enable agent sharing without admin approval** toggles in the management console.

This feature is generally available (GA). For more information, see [Configure feature controls](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls).

Feature

**Gemini Enterprise: Share Google-made agents, custom agents, and employee-made agents that are registered with Gemini Enterprise**

Admins can share the following agents:

  * Google-made agents such as Deep Research.
  * Employee-made agents created using Agent Designer.
  * Custom agents built using Agent-to-Agent (A2A) and registered with Gemini Enterprise.
  * Agents developed using Agent Development Kit (ADK) and registered with Gemini Enterprise.
  * Dialogflow agents that are registered with Gemini Enterprise.
  * Agents added from Google Cloud Marketplace



This feature is generally available (GA). For more information, see [Share agents from Google Cloud console](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents).

## February 19, 2026

Feature

**Gemini Enterprise: Use Gemini 3.1 Pro (Preview)**

You can use Gemini 3.1 Pro in Preview with Gemini Enterprise. This version replaces Gemini 3 Pro in Preview.

To make Gemini 3.1 Pro available to users in your Gemini Enterprise app, a Gemini Enterprise admin must enable the **Gemini 3.1 Pro (Preview)** toggle within the **Model availability** feature control.

If an admin had previously enabled the **Gemini 3 Pro (Preview)** toggle, then Gemini Enterprise enables the **Gemini 3.1 Pro (Preview)** toggle by default too.

For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

Feature

**Gemini Enterprise: Support for new actions**

New actions are available for these data stores:

  * [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc) (Private Preview)
  * [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc) (Private Preview)
  * [Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion) (Public Preview)
  * [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk) (Public Preview)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

Feature

**Gemini Enterprise: Chat with files in the Microsoft SharePoint connector**

Gemini Enterprise can analyze content and generate answers from XLSX and CSV files in the Microsoft SharePoint connector, eliminating the need to upload these files to the assistant.

This feature is generally available (GA). For more information, see [Chat with files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

## February 12, 2026

Feature

**Gemini Enterprise mobile app: Standard and Plus editions (GA with allowlist)**

The Gemini Enterprise mobile app is available as a GA with allowlist. The mobile app lets users interact with organizational data, engage with agents, and execute tasks seamlessly using their mobile device.

To ensure that you have the latest features, security, and best experience, you may occasionally be required to update your Gemini Enterprise mobile app, or install a new version. Some updates may be necessary to continue using the app.

Contact your account manager to access the mobile app. 

## February 09, 2026

Feature

**Gemini Enterprise: Data connector for Notion (Preview)**

You can connect Notion data stores to Gemini Enterprise. Support for Notion data sources is in Public Preview. For more information, see [Connect Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion).

## February 06, 2026

Feature

**Gemini Enterprise: Data connector for Linear (Preview)**

You can connect Linear data stores to Gemini Enterprise. Support for Linear data sources is in Public Preview. For more information, see [Connect Linear](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear).

Feature

**Gemini Enterprise: Welcome emails**

After a user signs in to Gemini Enterprise for the first time, the user receives a welcome email with tips on how to get the most out of Gemini Enterprise. Gemini Enterprise admins can turn this feature on or off from the admin settings.

This feature is generally available (GA). For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

Security

**Gemini Enterprise: Security update**

**CVE-ID:** [CVE-2026-1727](https://nvd.nist.gov/vuln/detail/CVE-2026-1727)

**Vulnerability:** Mitigation for Potential Cloud Storage Namespace Hijacking ("Bucket Squatting")

**Description:** We have addressed a security vulnerability (CVE-2026-1727) in Gemini Enterprise related to the management of Cloud Storage bucket names. The issue, commonly known as "bucket squatting," can arise if an attacker pre-emptively registers a bucket name that Gemini Enterprise services might be configured to use.

**Potential impact:** Exploitation of this vulnerability can let an attacker intercept, access, or manipulate data intended for a legitimate Gemini Enterprise-related Cloud Storage bucket.

**Status:** This vulnerability has been remediated in Gemini Enterprise. We have enhanced our systems to ensure the integrity and proper ownership of Cloud Storage resources used by the platform, which prevents this potential issue.

**Action required:** No action is required from users. The necessary fixes and safeguards have been automatically deployed to Gemini Enterprise.

## February 04, 2026

Feature

**Gemini Enterprise and Google NotebookLM Enterprise: Usage audit logs available in Cloud Logging**

Gemini Enterprise admins can access user query and response audit logs in Cloud Logging for both Gemini Enterprise and Google NotebookLM Enterprise.

This feature is generally available (GA). For more information, see:

  * [Configure usage audit logging for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs)
  * [Configure usage audit logging for Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-usage-audit-logs-for-nblme)



## February 02, 2026

Feature

**Fine-grained access control for individual Gemini Enterprise apps**

Gemini Enterprise admins can control access to individual Gemini Enterprise apps using app-level IAM policies. IAM permissions are often managed at the project level, but app-level IAM allows for more granular control.

This feature is generally available (GA). For more information, see [Configure access controls for apps](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps).

## January 30, 2026

Feature

**Gemini Enterprise: Support for new actions**

New actions are available for the following data stores:

  * [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc) (Private Preview)
  * [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk) (Public Preview)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

## January 28, 2026

Feature

**Gemini Enterprise: Support for new data stores (Preview)**

The following data stores are supported in Gemini Enterprise:

  * [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc)
  * [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc)
  * [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk)



**Download file** action has been added to [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox). For a list of actions for all available data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions). These data stores are in Public Preview.

## January 27, 2026

Change

**Gemini Enterprise: Autocomplete turned off in the chat box**

The autocomplete menu no longer appears as a user types in the chat box. Users can still use the mentions feature by typing `@` in the chat box, followed by the name of an agent, person, or file.

This feature is generally available (GA). For more information about mentions, see [Add context with mentions](https://docs.cloud.google.com/gemini/enterprise/docs//assistant-chat#add_context_with_mentions).

## January 26, 2026

Announcement

**Gemini Enterprise: Visual flow builder for existing agents**

The Agent Designer visual flow builder is available for all agents created before January 12, 2026. You can manage these agents directly from the [Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) page, or edit their logic using the enhanced visual flow builder from the **Agent Designer > Flow** tab.

This feature is generally available (GA). For more information, see [Agent Designer overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

## January 23, 2026

Feature

**Gemini Enterprise: New actions in the unified view**

New actions have been added to the following data stores:

  * [Box](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box) (Private Preview)
  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)
  * [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox)
  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
  * [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive)
  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)
  * [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)



For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

## January 12, 2026

Announcement

[Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## December 29, 2025

Feature

**Semantic search in sessions**

Gemini Enterprise and Business have expanded search capabilities to include semantic similarity, which lets you find relevant content in your chat history based on meaning rather than just keywords.

## December 23, 2025

Feature

**Gemini Enterprise: Manage actions using the updated flow (Preview)**

Use the new capabilities on the **Actions** page to:

  * Add new actions skipped during the data store creation process.

  * Enable or disable the existing actions.

  * Re-authenticate actions and verify authentication parameters.




For more information, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions). These capabilities are in Public Preview.

## December 19, 2025

Feature

**Gemini Enterprise: New actions available for data stores in the unified view (Preview)**

New actions have been added for the following data stores:

  * [Box](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box)
  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)
  * [Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams)
  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)



For a list of supported actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions). These actions are in Public Preview.

Feature

**Gemini Enterprise: Schedule agent executions for custom agents in Agent Designer (Preview)**

You can configure your custom agents, created using the Agent Designer, to execute predefined instructions and prompts on a set schedule.

Scheduled executions run automatically for personal tasks, but any action involving other people will be paused for your review and approval.

For more information, see [Schedule agent executions](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/schedule-agent). This feature is in Public Preview.

## December 17, 2025

Feature

**Gemini Enterprise: View the pooled quota usage (Preview)**

Admins can view the pooled quota usage of their licenses on the **Manage users** page. This feature is in Public Preview. For more information, see [View the pooled quota usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage#view-quota-usage).

Feature

**Gemini Enterprise: Use Gemini 3 Flash (Preview)**

You can use Gemini 3 Flash in Preview with Gemini Enterprise. To make Gemini 3 Flash available to users in your Gemini Enterprise app, a Gemini Enterprise admin must enable the **Gemini 3 Flash (Preview)** toggle in the **Model availability** feature control. For more information on feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## December 15, 2025

Feature

**Gemini Enterprise: Get user-level metrics (Preview)**

Admins can monitor user-level metrics in the **User Level** tab of the **Analytics** page. This is a [Private preview](https://cloud.google.com/products#product-launch-stages) feature. For more information, see [Metrics definitions](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics#definitions).

## December 12, 2025

Feature

**Gemini Enterprise: Unified data source creation and action flow**

The new unified process for creating a data store enables you to create the data store and the associated actions in a single, streamlined flow. This functionality allows Gemini Enterprise to perform tasks directly within the connected application.

The new **Actions** page shows you all the enabled actions for each data store. Actions are available in Public Preview and are enabled for Microsoft SharePoint, Microsoft Outlook, Microsoft OneDrive, Jira Cloud, Dropbox, and ServiceNow. For a list of supported actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

This launch includes support for the following data stores:

**Generally Available**

  * [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)
  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)
  * [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive)
  * [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)
  * [Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal)
  * [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail)



**Public Preview**

  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)
  * [Box](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box)
  * [Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams)
  * [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox)
  * [ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow)



## December 11, 2025

Feature

**Gemini Enterprise: Monitor metrics for Google NotebookLM Enterprise**

Admins can monitor Google NotebookLM Enterprise metrics in the **Agents** tab of the **Analytics** page.

For more information, see [Metrics definitions](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics#definitions).

Feature

**Google NotebookLM Enterprise: Gemini model upgrade (Preview)**

You can use Gemini 2.5 Flash with Google NotebookLM Enterprise. This feature is in Public Preview.

## December 08, 2025

Feature

**Gemini Enterprise: Share custom agents registered with Gemini Enterprise (Preview)**

Admins can share custom agents registered with Gemini Enterprise, including Agent-to-Agent (A2A), Agent Development Kit (ADK), Dialogflow agents, and agents added from Google Cloud Marketplace. For more information, see [Share custom agents](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents).

This feature is in Public Preview.

## December 05, 2025

Feature

**Gemini Enterprise: Add agents from Google Cloud Marketplace (Preview)**

Admins can add agents from Google Cloud Marketplace that use the Agent-to-Agent (A2A) protocol. After an agent is purchased and added to Gemini Enterprise, end users can access the agent through the Gemini Enterprise web app. For more information, see [Add and manage agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents).

This feature is in Public Preview.

## November 21, 2025

Feature

**Gemini Enterprise: Use Nano Banana Pro for image generation (Preview)**

You can use Nano Banana Pro (Gemini 3 Pro Image) in Public Preview with Gemini Enterprise for image generation. To make this available to users in your Gemini Enterprise app, a Gemini Enterprise admin must select **Gemini 3 Pro Image (Preview)** in the **Enable image generation** feature control. For more information about feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

Feature

**Gemini Enterprise: Save information as memories**

You can ask the assistant to save and remember specific pieces of information for reference in future conversations.

For more information, see [Save information as memories](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization#save-memories).

Feature

**Gemini Enterprise: Manage agents (Preview)**

Using the Agents page, admins can see all agents that are available to users in the Gemini Enterprise web app. For more information, see [Agents overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview).

This feature is in Public Preview.

## November 19, 2025

Feature

**Gemini Enterprise: Enhanced Agent Designer with visual flow builder (Preview)**

Agent Designer in Gemini Enterprise is enhanced with a new visual flow builder, offering a more intuitive and powerful way to create and manage complex, multi-step agents.

For more information, see [Agent Designer overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

To enable this feature for your users, a Gemini Enterprise administrator must enable the corresponding toggle in your app's feature management settings. For information about feature controls, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

**Note:** The visual flow builder is available for all new agents created after this release. Existing agents will continue to use the familiar editor to ensure backward compatibility.

## November 18, 2025

Feature

**Gemini Enterprise: Use Gemini 3 Pro (Preview)**

You can use Gemini 3 Pro in preview with Gemini Enterprise. To make Gemini 3 Pro available to users in your Gemini Enterprise app, a Gemini Enterprise admin must enable the **Gemini 3 Pro (Preview)** toggle in the **Model availability** feature control. For more information on feature controls, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

Feature

**Gemini Enterprise: View generated images and videos**

You can view chats and download your generated images and videos using the Library.

For more information, see [View and download generated images and videos](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#view_and_download_generated_images_and_videos).

Feature

**Gemini Enterprise: Microsoft OneDrive @mentions**

You can use the @ symbol within your chats to mention and reference files in the connected Microsoft OneDrive data sources.

Feature

**Gemini Enterprise: Sources from model**

In the Sources panel of an answer, Gemini Enterprise shows other sources used by the Gemini models.

## November 17, 2025

Feature

**Gemini Enterprise: Register ADK and A2A agents**

You can register your ADK agents that are hosted on the Vertex AI Agent Engine and your agents that were built using the Agent-to-Agent (A2A) protocol with Gemini Enterprise. This makes the agents available to your users on the Gemini Enterprise web app.

For more information, see:

  * [Register and manage ADK agents hosted on the Vertex AI Agent Engine](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
  * [Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent)



Change

**Gemini Enterprise: Authorize assistant actions from the chat box**

If actions are enabled for a data source, the user sees an **Enable Actions** button next to the data source listing in the assistant chat box. The user must click this button and complete authorization before they can use the assistant actions associated with the data source.

## November 05, 2025

Feature

**Gemini Enterprise: Layout parser support for DOCX, PPTX, and XLSX**

With the layout parser, support for parsing DOCX, PPTX, and XLSX file formats is generally available (GA). Both the layout and digital parsers can parse PDF, HTML, DOCX, PPTX, and XLSX files. For more information about the parsers, see [Parse and chunk documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents).

## October 31, 2025

Feature

**Gemini Enterprise: Hidden model thinking details**

When generating an answer, the details of a model's thinking are always hidden to protect sensitive information.

## October 21, 2025

Change

**Gemini Enterprise: Select individual connector instance**

Select or deselect specific connector instances, such as Jira or Confluence, using the  database  icon located in the chat box.

## October 09, 2025

Announcement

**Gemini Enterprise: Google Agentspace is part of Gemini Enterprise**

The Google Agentspace experience in the Google Cloud console and the default application is referred to as Gemini Enterprise. This includes all associated resources and documentation.

## October 02, 2025

Feature

**Gemini Enterprise: Generate images using Nano Banana**

Image generation and editing with Nano Banana (Gemini 2.5 Flash Image) is generally available (GA) in Gemini Enterprise across Global, EU, and US multi-regions.

For more information on generating images, see [Generate an image](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#generate_an_image).

Feature

**Gemini Enterprise: Configure prompt chips**

You can create, delete, edit, and enable or disable Google-provided and custom prompts that provide better guidance to your users.

For more information, see [Configure prompt chips](https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips).

## September 26, 2025

Feature

**Gemini Enterprise: Manage image and video generation on the web app**

By default, image and video generation are enabled in the Agentspace web app. To turn off these features, admins must navigate to the **Configurations > Feature Management** tab, and turn off the **Enable video generation** and **Enable image generation** options.

## September 24, 2025

Change

**Gemini Enterprise: Interface updates**

  * File uploads can be canceled at any time.
  * The Star and Share buttons appear after a user has initiated a session by submitting a prompt.



Feature

**Gemini Enterprise: Knowledge base filter for catalog entities in ServiceNow connectors**

In your ServiceNow connectors, you can filter your knowledge base entities by catalog IDs. This lets you selectively ingest only those catalog entities whose `catalogSysId` matches the filter. If no values are specified, then the connector ingests all catalog entities. This feature is generally available (GA).

For information about ServiceNow connectors, see [Connect ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow).

## September 23, 2025

Breaking

**Gemini Enterprise: Change in ACLs for incidents in ServiceNow**

The access-control list (ACL) behavior for ServiceNow incidents has significantly changed, from too permissive to least-privilege behavior. This change drastically reduces the possibility of data leaks, but might be too restrictive for your needs. 

For more information about ServiceNow, see [Connect ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow) and [Add ServiceNow actions](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-actions-servicenow).

## September 15, 2025

Feature

**Gemini Enterprise: Real-time sync (Preview)**

Real-time sync uses webhooks to receive notifications when data is created, updated, and deleted in a third-party data source. Notifications typically arrive within minutes of the event. The following data stores support real-time sync:

  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud#enable_real-time_sync)
  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud#enable_real-time_sync)
  * [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive#real-time-sync)
  * [Microsoft SharePoint Online](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint#real-time-sync)
  * [ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow#real-time-sync)



Support for real-time sync for these data stores is in Public Preview.

Feature

**Gemini Enterprise and Google NotebookLM Enterprise: Model Armor**

Model Armor helps proactively screen prompts and responses within Agentspace apps and NotebookLM Enterprise instances. For more information on how administrators can enable this feature, see:

  * [Enable Model Armor in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
  * [Enable Model Armor in Gemini Notebook Enterprise](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/enable-model-armor)



## September 11, 2025

Change

**Gemini Enterprise: Interface updates**

  * The LLM model selector has moved from the search bar to directly below the product logo in the top-left corner.
  * The web grounding tool and source has been renamed _Google Search_ and _Enterprise web search,_ depending on the type of web grounding configured.
  * The _Sources_ button in the search bar has been renamed _Data._
  * The _Data_ menu (formerly _Sources_) shows which sources are selected.



## September 05, 2025

Feature

**Google NotebookLM Enterprise: Notebook creation and management using the API**

Use standalone APIs to programmatically create and manage your notebooks.

This feature is generally available (GA). For more information, see [Create and manage notebooks using the API](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/api-notebooks).

## August 28, 2025

Feature

**Google NotebookLM Enterprise: Generate podcasts using the Podcast API (GA with allowlist)**

Use a standalone API to programmatically generate NotebookLM-style podcasts. No data store required; provide the source content directly to the [Podcast API](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.podcasts.operations).

This feature is available to select Google Cloud customers (GA with allowlist). For more information, see [Generate podcasts (API method)](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/podcast-api).

## August 21, 2025

Breaking

**Full sync in SharePoint connector to avoid duplicate documents**

Because of a change that tries to optimize the sync performance, performing an incremental sync in a [SharePoint connector data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint) can cause duplicate documents for `file` entity types. This is applicable to all SharePoint connectors created before August 21, 2025, that contain `file` entity types.

As a one-time solution, you can avoid duplication by either running a full sync manually or waiting for the next scheduled full sync. After performing the full sync, you can perform incremental syncs without generating any duplicate documents.

## August 18, 2025

Feature

**Gemini Enterprise: Export analytics**

Export metrics to a BigQuery table in your Google Cloud project using the `analytics:exportMetrics` method.

For more information, see [View and export analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics#export_metrics).

## August 12, 2025

Feature

**Gemini Enterprise: Custom starter prompts for no-code agents**

You can add starter prompts to no-code agents. Starter prompts guide users on how to interact with the agent.

For more information, see [Create a no-code agent with Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

## August 01, 2025

Feature

**Gemini Enterprise: Agent for Idea Generation (Preview)**

The Idea Generation agent helps enterprise teams innovate and solve problems. It combines advanced AI with a unique tournament-style competition framework to generate and rank ideas. This is a [Preview](https://cloud.google.com/products#product-launch-stages) feature. See [Ideate with Idea Generation agent](https://docs.cloud.google.com/gemini/enterprise/docs/idea-generation).

Feature

**Gemini Enterprise: The Data agent (Private preview)**

The Data agent can help you query your BigQuery data using natural language to give you insights and help you make well-informed, data-driven business decisions. With the Data agent, your data analysts don't need prior knowledge of SQL and helps them focus on more complex tasks. This is a [Private preview](https://cloud.google.com/products#product-launch-stages) feature.

## July 31, 2025

Announcement

**Gemini Enterprise: General Availability**

Gemini Enterprise is generally available (GA).

Feature

**Gemini Enterprise: Enhanced analytics**

The **Analytics** page has been enhanced with improvements and additions. See [View analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics).

  * Updated user interface to include improved metrics visualization.

  * New metrics to track the adoption, usage and quality, agent, and value data of an app.




Feature

**Gemini Enterprise: Data stores that connect third-party data sources using data federation (Preview)**

You can connect to these third-party data sources with data federation:

  * [Connect Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint#federated-search)
  * [Connect Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive#federated-search)
  * [Connect Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook#federated-search)



Support for these data sources is in Public Preview.

Feature

**Gemini Enterprise: Alerts for third-party data stores**

You can enable alerts for predefined tasks in your third-party data stores.

For more information, see [Configure alerts for third-party data sources](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).

Feature

**Gemini Enterprise: Personalization**

Personalize your Gemini Enterprise experience by connecting to your data sources and providing details about your role and preferences. Google Agentspace uses your data to better understand your context and deliver more relevant and useful responses.

For more information, see:

  * [Personalize your Gemini Enterprise experience](https://docs.cloud.google.com/gemini/enterprise/docs/personalization)

  * [Configure personalization and memory](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization)




Feature

**Gemini Enterprise: Agent for Deep Research**

The Deep Research agent gathers, analyzes, and understands internal and external information and generates a research report.

For more information, see [Get reports with Deep Research](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant).

Feature

**Gemini Enterprise: Actions for Gmail and Google Calendar**

Set up assistant actions for Google Calendar and Gmail using the console or API.

For more information, see [Add Google Calendar and Gmail actions](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-actions-google).

Feature

**Gemini Enterprise: Data stores that connect Google data sources**

You can connect data stores for the following Google data sources:

  * [Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)

  * [Gmail data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail) for data federation

  * [Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal) data store for data federation

  * [People search data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people) for data ingestion




Feature

**Gemini Enterprise: App user interface and chat box updates**

The app user interface and chat box have been enhanced with a wide array of new features and improvements.

  * Agents:

    * Use the ≡ navigation panel to access your agents.

    * Star (☆) your most used and recently active agents to your ≡ navigation panel for easy access.

    * Access NotebookLM from the **Agents** page.

  * Chat box and conversations:

    * Access tools and sources directly from the chat box.

    * Create images.

    * Create DOCX, PDF, and PPTX.

    * Create videos using Veo 3 Fast (available only for Agentspace apps in the _global_ and _US_ regions).

    * Paste a public URL and start a conversation with its content.

    * Use the ☆ star to mark important conversations and keep them easily accessible. The ☆ feature replaces the conversation pin functionality.

    * Web grounding is enabled by default for new Agentspace apps.

    * Use the "@mention" feature to reference Agents, documents, and people (not available for the Idea Generation Agent).

    * Search for people and hover over a mentioned person to preview or expand their information card.

    * Download table data, and copy table data as CSV files, and sheets.

    * Upload diff files, and ask Agentspace to summarize and analyze the content.

    * More file types are supported. See [File formats and size limitations](https://cloud.google.com/gemini/enterprise/docs/assistant-chat#file_formats_and_size_limitations).

    * Documents and spreadsheets can be uploaded with a maximum size of 100 MB.

    * Upload files directly from your Google Drive, Microsoft OneDrive, and Microsoft SharePoint.

    * Uploaded files: The uploaded files side panel has moved to the top-right corner of the app.

  * Prompt gallery:

    * The **Prompt gallery** landing page is deprecated.

    * Prompts are shown below the chat box for new Agentspace apps (existing Agentspace apps will receive this update after 30 days).

  * Search/Citations panel:

    * Search results no longer automatically open the **Source** panel.

    * Access citations and search results by clicking **Source**.

  * Spotlight search:

    * Search conversations and agents.

    * Find your starred items quickly using starred search.

  * Actions:

    * Create and send emails via Gmail.

    * Create a calendar event via Google Calendar.




Feature

**Gemini Enterprise: Data stores that connect third-party data sources using data ingestion**

You can connect data stores for the following third-party data sources:

  * [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)

  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)

  * [Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id)

  * [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive)

  * [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)

  * [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)

  * [ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow)




Feature

**Gemini Enterprise: Assist agent facilitates onboarding**

Gemini Enterprise Assist can help you set up and configure your data stores and authentication.

Feature

**Gemini Enterprise: Chrome Enterprise integration**

Invoke Agentspace directly from the Chrome Enterprise address bar (omnibox).

For more information, see [Configure Chrome Enterprise cloud-managed browsers](https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome).

## July 24, 2025

Change

**Gemini Enterprise: Rename Outlook events _entity_ to _calendar_ for federated search**

To maintain consistency, the _events_ entity in the Outlook data store for federated search has been renamed to _calendar_.

## July 16, 2025

Feature

**Google NotebookLM Enterprise: Discover sources**

The **Discover sources** feature in NotebookLM Enterprise lets you directly find sources on the web and import them into your notebook.

This feature helps you quickly gather sources when creating a new notebook.

Feature

**Google NotebookLM Enterprise: Share notebooks with groups**

You can share notebooks with groups, as well as with individuals.

There are some differences between sharing with group distribution lists and sharing with people (individual email addresses). For more information, see [Share notebooks](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/share-notebooks).

Feature

**Google NotebookLM Enterprise: Send email notifications when sharing a notebook**

When you share a notebook, you can choose to send email notifications to the people you're sharing it with.

For more information, see [Share notebooks](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/share-notebooks).

## July 15, 2025

Deprecated

**Gemini Enterprise: LLM system instructions removed from the app's assistant configurations**

To prevent the assistant's LLM-related system instructions from being overridden, the LLM system instructions configuration has been removed from Agentspace Enterprise.

## July 14, 2025

Feature

**Gemini Enterprise: Optimized data ingestion**

Agentspace Enterprise optimizes the amount of data that needs to be ingested during data syncs. It automatically determines the data that needs to be ingested based on the Assistant answer quality. You can use filters to decide what data needs to be ingested with each data sync.

## July 11, 2025

Change

**Gemini Enterprise: Automatically fetch ServiceNow service portal URL suffix**

The ServiceNow connector automatically fetches the `url_suffix` parameter for your service portal when you grant the connector access to the required ServiceNow tables. You can no longer manually specify the `url_suffix` parameter.

For more information, including the required tables, see [Set up user roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow#set_up_user_roles_and_permissions).

## July 09, 2025

Announcement

**Gemini Enterprise: Quotas**

Agentspace Enterprise offers the following allocation quotas in the global region (`global`), the US multi-region (`us`), and the EU multi-region (`eu`) under the Discovery Engine API:

  * Number of data stores per project
  * Number of documents per project
  * Number of engines per project
  * Number of user events



The number of data stores, documents, user events, and engines across all locations can't exceed the total per-project quota for that resource. 

For more information, see [Quotas](https://docs.cloud.google.com/generative-ai-app-builder/quotas).

## July 02, 2025

Feature

**Gemini Enterprise: Search for an exact match**

To search for an exact match, you can enclose your search query in double quotes (`"`). For example, when you search for `"Mary had a little lamb"`, Vertex AI Search looks for the phrase exactly as it is. It doesn't return search results that contain `Mary had lamb`, which has missing words; or `a little lamb had Mary`, which has the words in a different order.

This feature is available when you use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method to [get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results) for your data.

Deprecated

**Gemini Enterprise: "Sync since" parameter removed for data connectors**

To improve data quality and connector performance, the ability to set a "Sync since" window for data connectors has been removed. Agentspace Enterprise automatically determines the sync window to ensure optimal quality.

For existing connectors that have a "Sync since" window configured, the setting continues to be supported but is no longer editable.

Feature

**Gemini Enterprise: Automatically generate a title for new conversations or prompts**

When you start a new conversation or use a prompt in your app, Gemini Enterprise automatically generates a title based on your initial query or prompt.

## June 26, 2025

Feature

**Gemini Enterprise: gemini-2.5-flash/answer_gen/v1 model**

You can generate answers with the Gemini 2.5 Flash (`gemini-2.5-flash`) model. This model is tuned to address context-based question and answering tasks.

This feature is generally available (GA). For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models).

## June 25, 2025

Feature

**Gemini Enterprise: Full and incremental sync schedules for data connectors**

When configuring sync for a data connector, you can set distinct scheduling intervals for both full sync and incremental sync. You can also independently pause and resume full and incremental sync for a connector.

To ensure data consistency, the configured interval for full sync must be greater than the interval for incremental sync.

This feature is generally available (GA). For more information, see _Sync frequency_ in [Connector and data store concepts](https://docs.cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#connector_and_data_store_concepts).

## June 17, 2025

Feature

**Gemini Enterprise: Model selector on the web app search bar**

The search bar contains a model selector. For example, you can choose the Gemini 2.5 flash or the Gemini 2.5 pro model, or you can leave the selector set to **Auto** , the default setting which automatically selects the model for you. This feature is generally available (GA).

## June 16, 2025

Change

**Gemini Enterprise: Custom search**

The vertical-agnostic apps, formerly known as _generic_ search, are renamed to _custom_ search. You'll see this new name in the product console and the documentation set. The functionality and the endpoints remain the same.

## June 13, 2025

Feature

**Gemini Enterprise: App-level feature management**

As an Agentspace administrator, you can choose to turn the following features on or off for your end users in the web app:

  * [Agents gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agents-gallery)
  * [Prompt gallery](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat)
  * [No-code agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer)
  * [NotebookLM Enterprise](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/overview)



To do so, in the Google Cloud console, open the **Configurations** for your Agentspace app and toggle the options in the **Feature management** tab. This feature is generally available (GA).

## June 12, 2025

Change

**Gemini Enterprise: Gemini model for chatting with the assistant (EU)**

To improve the experience of [chatting with an assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat), for assistants in the EU multi-region, Gemini 2.5 flash is used to generate answers.

## June 11, 2025

Fixed

**Gemini Enterprise: Dialogflow agents in Agentspace assistants**

When you interact with a Dialogflow or HTTP agent integrated in an Agentspace assistant, the responses that you receive are always from the Dialogflow or HTTP agent and not from the Agentspace assistant.

For more information, see [Integrate Dialogflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent).

Feature

**Gemini Enterprise: No-code agents**

When creating a no-code agent, you can assign specific tools from your [configured assistant actions](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions). The agent can use these tools to accomplish the task in its instructions.

For more information, see [Create a no-code agent with Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

## June 10, 2025

Feature

**Gemini Enterprise: Chat about uploaded content**

When you're chatting with an Agentspace assistant [about uploaded content](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_about_uploaded_content), you can upload an XLSX file with multiple sheets. This feature is generally available (GA).

Feature

**Gemini Enterprise: No-code agents**

You can choose specific data sources when creating a no-code agent. This gives you precise control over the information an agent can access during conversations, enhancing security and relevance.

For more information, see [Create a no-code agent with Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

Change

**Gemini Enterprise: Gemini model for chatting with the assistant**

To improve the experience of [chatting with an assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat), the following upgrades have been made:

  * For assistants in the US multi-region and global region, Gemini 2.5 flash is used to generate answers.
  * Gemini 2.0 flash is used to suggest related questions at the end of a question-answer pair.



## June 09, 2025

Feature

**Gemini Enterprise: Skip layout parsing for types of HTML content**

The [layout parser](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#layout-parsing) can skip parsing specific types of HTML content. By excluding less relevant content such as boilerplate, you can improve data quality. The layout parser can exclude based on HTML tags and IDs and on CSS classes.

This feature is generally available (GA) and accessible only through the API. For more information, see [Exclude HTML content](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#exclude-html-content).

## June 03, 2025

Feature

**Gemini Enterprise: Adjust autocomplete settings to reduce risk of PII leaks (Preview)**

If you use either the search history or user events model for autocomplete suggestions and you have concerns about your users entering their personally identifiable information (PII) as search queries, then see [Reduce the risk of returning suggestions that contain PII](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete#update-thresholds).

This feature is in Public Preview.

## May 30, 2025

Feature

**Gemini Enterprise: Suggest meeting times for Outlook Calendar events**

When using the assistant to create an Outlook Calendar event, you can get the assistant to suggest meeting times based on the participants' availability. Ask the assistant to schedule a meeting, and the suitable times appear on the proposed event form. This feature is generally available (GA).

## May 12, 2025

Feature

**Gemini Enterprise: Identity mapping**

When using third-party SaaS solutions, you can ensure that Google can enforce access control correctly by mapping your identity provider (IDP) to any external identities from the SaaS applications that you plan to use with Gemini Enterprise. You can do so by creating identity mappings in an identity mapping store.

Identity mapping is generally available (GA).

For more information, see [Set up external identities](https://docs.cloud.google.com/gemini/enterprise/docs/identity-mapping).

## May 08, 2025

Change

**Gemini Enterprise: App tier is determined by license type**

You no longer need to specify the tier when creating an app.

If your users have Agentspace Enterprise licenses, they can use the search features in the apps. If they have Agentspace Enterprise Plus licenses, they can use both search and assistant features.

For information, see [About subscriptions](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) and [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

## May 05, 2025

Feature

**Search notebooks from Gemini Enterprise apps (Preview)**

If you use both NotebookLM Enterprise and Agentspace Enterprise, you can create a data store that lets your users search their notebooks as a data source. Each user can search for notebook titles and retrieve information from their notebooks in the project.

This feature is in Public Preview. For more information, see [Enable NotebookLM Enterprise as a search source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store#notebooklm-search).

## April 09, 2025

Feature

**Gemini Enterprise: Agents gallery**

The Agents gallery is a generally available (GA) portal in Gemini Enterprise that lets you access, create, and manage your agents.

For more information, see [Browse agents with Agents gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agents-gallery).

Feature

**Gemini Enterprise: Agent Designer (Private Preview)**

Create custom AI no-code agents using natural language descriptions to perform specific tasks.

For more information, see [Create a no-code agent with Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

This is a Private Preview feature, available to select, allowlisted, Google Cloud customers.

Feature

**Gemini Enterprise: Idea Generation (Private Preview)**

Idea Generation is an agent Premade by Google. Its goal is to help with innovation and problem-solving for enterprise users by combining advanced AI with a unique tournament-style competition framework to generate and rank ideas.

For more information, see [Ideate with Idea Generation agent](https://docs.cloud.google.com/gemini/enterprise/docs/idea-generation).

This is a Private Preview feature, available to select, allowlisted, Google Cloud customers.

## April 02, 2025

Feature

**Google NotebookLM Enterprise: Support for Access Transparency is GA**

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) supports Google NotebookLM Enterprise in general availability (GA).

See [Enable Access Transparency](https://docs.cloud.google.com/agentspace/docs/access-transparency).

Feature

**Google NotebookLM Enterprise: CMEK for US and EU (GA) and CMEK with EKM and HSM (GA with allowlist)**

Customer-managed encryption keys (CMEK) are generally available (GA) in the US and the EU multi-regions. If you create notebooks in a US or EU multi-region data store, you can provide your own encryption key to protect your data at rest.

Using external key manager (EKM) or hardware security module (HSM) with CMEK is in GA with allowlist.

For information, see [Customer-managed encryption keys](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/cmek).

Feature

**Gemini Enterprise: VPC Service Controls are GA**

Virtual Private Cloud Service Controls support for Gemini Enterprise is generally available (GA).

For more information, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_agentspace_enterprise) in the _VPC Service Controls_ documentation. For general information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## March 31, 2025

Feature

**Gemini Enterprise: CMEK for third-party connectors**

Customer-managed encryption keys (CMEK) are generally available (GA) for third-party data connectors.

For information about managed encryption keys for third-party connectors, see [About single-region keys for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party).

Feature

**Google NotebookLM Enterprise: HIPAA compliance**

NotebookLM Enterprise is certified for [HIPAA](https://cloud.google.com/security/compliance/hipaa) compliance.

## March 25, 2025

Feature

**Gemini Enterprise: Return corpus images in answers and with follow-ups (Preview)**

The answer method can return images in answers, along with text.

If appropriate, one image from the data store can be returned with the answer. Citations can also include images from the data store.

This feature is restricted to queries made to unstructured data stores where the layout parser is in effect and is only available through the API and is in Public Preview. For more information, see [Retrieve existing images from the data store](https://docs.cloud.google.com/gemini/enterprise/docs/answer#get-images).

Feature

**Gemini Enterprise: Generate and return charts in answers and with follow-ups (Preview)**

The answer method can include a chart in an answer, in addition to text. The chart is generated from the data in the data store. A chart is generated if there is sufficient data, and the query either asks for a chart or the answer is sufficiently complex that the method itself determines that a chart is helpful.

This feature is in Public Preview and is only available through the API. For more information, see [Generate charts for answers](https://docs.cloud.google.com/gemini/enterprise/docs/answer#get-charts).

## March 04, 2025

Feature

**Gemini Enterprise: Document-relevance scores for search results**

You can ask to have a relevance score returned for each search result associated with a query. The returned score can be used to do post-search ranking or filtering of the results. This feature is available for search apps associated with structured and unstructured data stores.

Document-relevance scores are generally available (GA). For more information, see [Get document-relevance scores with search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results#relevance-scores).

## February 27, 2025

Feature

**Gemini Enterprise: Personalize responses from the answer method**

When making a query call to the answer method, you can provide information about the user to personalize the generated answer.

This feature is generally available (GA). For more information, see [Personalize answers](https://docs.cloud.google.com/gemini/enterprise/docs/answer).

## February 07, 2025

Feature

**Gemini Enterprise: Integration of NotebookLM Enterprise**

If you use Agentspace Enterprise, you can access your notebooks and the features of NotebookLM Enterprise from within the Agentspace Enterprise web app UI by clicking the **NotebookLM** button.

This feature is generally available (GA). For more information, see [Use NotebookLM Enterprise within Agentspace Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm).

Feature

**Google NotebookLM Enterprise: Add content from Agentspace Enterprise to notebooks**

If you use Agentspace Enterprise, you can add some kinds of results, such as Google Sheets and Google Docs, from Agentspace Enterprise searches to your notebooks. Notebooks that contain sources from Agentspace Enterprise can't be shared. Also, shared notebooks can't accept sources from Agentspace Enterprise.

This feature is generally available (GA). For more information, see [Use NotebookLM Enterprise within Agentspace Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm) and [Notebooks that can't be shared](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/share-notebooks#no-sharing).

Feature

**Google NotebookLM Enterprise: Multi-regions**

NotebookLM Enterprise is available in Global, EU, and US multi-regions. When you purchase a [subscription](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/set-up-licensing) to NotebookLM Enterprise, choose which region you want for data residency.

## January 31, 2025

Change

**Google NotebookLM Enterprise: License and user management**

To use NotebookLM Enterprise, end users require a license.

In the Google Cloud console, an Agentspace administrator can purchase a subscription and licenses or request a free trial. For more information, see [Get licenses for NotebookLM Enterprise](https://docs.cloud.google.com/agentspace/notebooklm-enterprise/docs/set-up-licensing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
