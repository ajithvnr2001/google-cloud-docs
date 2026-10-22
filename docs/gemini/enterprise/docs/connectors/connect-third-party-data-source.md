---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source/
title: Connect a third-party data source \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:43.947728+00:00
---

# Connect a third-party data source  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect a third-party data source Stay organized with collections  Save and categorize content based on your preferences. 

When you connect a third-party data source, Gemini Enterprise creates a _data store_ and associates _entity_ data stores with it for each specified entity. Entity types are specific to the connected data source (for example, Jira Cloud entities include issues, attachments, comments, and worklogs).

  * To import data from a Google data source instead, see [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

  * If you are using customer-managed encryption keys, see [Register single-region keys for third-party connectors](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#third-party-connectors-key-registration).

  * If you want outbound traffic from the data store to originate from a fixed set of IP addresses (for example, to allowlist them on the source system), and if the data store supports it, see [Configure static IP egress](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress).




**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Sources by launch stage

Visit a source-specific page for information on how to connect that source to Gemini Enterprise.

The following tables list each supported connector with the value to use in the [`discoveryengine.managed.allowedDataSources`](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources) organization policy. Where available, the connector name links to its setup instructions.

### Generally available

Data source | Value for `allowedDataSources`  
---|---  
[Box](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box) | `box`  
[Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud) | `confluence`  
[Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc) | `confluence_server`  
[Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox) | `dropbox`  
[GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github) | `github`  
[Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal) | `google_calendar`  
[Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive) | `google_drive`  
[Google Mail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail) | `google_mail`  
[HubSpot](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot) | `hubspot`  
[Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud) | `jira`  
[Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc) | `jira_server`  
[Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id) | `azure_active_directory`  
[Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook) | `outlook`  
[Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams) | `teams`  
[Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday) | `monday`  
[OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive) | `onedrive`  
[ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow) | `servicenow`  
[SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint) | `sharepoint`  
[Slack](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack) | `slack`  
  
### Public preview

Data source | Value for `allowedDataSources`  
---|---  
[Adobe Workfront](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/adobe-workfront) | `adobe_workfront`  
[AirOps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops) | `airops`  
[Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable) | `airtable`  
[Aiwyn Tax](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/aiwyn_tax) | `aiwyn_tax`  
[AllTrails](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/alltrails) | `alltrails`  
[Apollo GraphOS](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/apollo-graphos) | `apollo_graphos`  
[Asana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/asana) | `asana`  
[Atlan](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/atlan-mcp) | `atlan_mcp`  
[Attio](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/attio) | `attio`  
[Autodesk Product Help](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/autodesk-product-help) | `autodesk_product_help`  
[AWS Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/aws-marketplace) | `aws-marketplace`  
[Bitly](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/bitly) | `bitly`  
[Blockscout](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/blockscout) | `blockscout`  
[Calendly](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/calendly) | `calendly`  
[Campfire](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/campfire) | `campfire`  
[Cisco Workspaces](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/cisco-workspaces) | `cisco_workspaces`  
[Clay](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clay) | `clay`  
[Cohesity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/cohesity) | `cohesity`  
[CoinDesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/coindesk) | `coindesk`  
[CourtListener](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/courtlistener) | `courtlistener`  
[Courtroom5](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/courtroom5) | `courtroom5`  
[Crossbeam](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crossbeam) | `crossbeam`  
[Crypto](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crypto) | `crypto`  
[Custom MCP Server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server) | `custom_mcp`  
[Descript](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/descript) | `descript`  
[Dice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dice) | `dice`  
[DirectBooker](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/directbooker) | `directbooker`  
[Docusign](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign) | `docusign`  
[D&B Commercial Graph](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d-and-b-commercial-graph) | `dun_and_bradstreet`  
[D&B Finance Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_finance_analytics) | `d_b_finance_analytics`  
[D&B Risk Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_risk_analytics) | `d_b_risk_analytics`  
[Daloopa](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/daloopa) | `daloopa`  
[Dynamics 365](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365) | `dynamics365`  
[Egnyte](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/egnyte) | `egnyte`  
[Excalidraw](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/excalidraw) | `excalidraw`  
[FactSet AI-Ready Data](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/factset_ai_ready_data) | `factset_ai_ready_data`  
[Fibery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fibery) | `fibery`  
[Finnhub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/finnhub) | `finnhub`  
[Fiscal.ai](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fiscal-ai) | `fiscal_ai`  
[Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice) | `freshservice`  
[Fullstory](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/fullstory) | `fullstory`  
[Gamma](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gamma) | `gamma`  
[GitLab](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab) | `gitlab`  
[Globalping](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/globalping) | `globalping`  
[GoDaddy](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/godaddy) | `godaddy`  
[Gong](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gong) | `gong`  
[Google Chat](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat) | `google_chat`  
[Compute Engine](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/google-compute-engine) | `google_compute_engine`  
[Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch) | `googlestitch`  
[Grafana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/grafana) | `grafana`  
[Grafana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/grafana) | `grafana`  
[Granted](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/granted) | `granted`  
[Guru](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/guru) | `guru`  
[Hex](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hex) | `hex`  
[Hugging Face](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/huggingface) | `huggingface`  
[iManage platform](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/imanage-platform) | `imanage_platform`  
[Intercom](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/intercom) | `intercom`  
[Invideo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/invideo) | `invideo`  
[Kiwi](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi) | `kiwi`  
[Kiwi.com](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi-com) | `kiwi_com`  
[Lastminute](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lastminute) | `lastminute`  
[LegalZoom](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/legalzoom) | `legalzoom`  
[Linear](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear) | `linear`  
[Lovable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lovable) | `lovable`  
[LumApps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lumapps) | `lumapps`  
[MailerLite](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mailerlite) | `mailerlite`  
[Mercury](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mercury-mcp) | `mercury_mcp`  
[Mermaid Chart](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mermaid_chart) | `mermaid_chart`  
[Microsoft Learn](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn) | `microsoft_learn`  
[Microsoft Outlook (OpenAPI)](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook) | `outlookopenapi`  
[Midpage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/midpage) | `midpage`  
[Miro](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/miro) | `miro`  
[Moody's](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/moody_s) | `moody_s`  
[MSCI](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/msci) | `msci`  
[NetDocuments](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/netdocuments) | `netdocuments_us_vault`  
[Nexla](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/nexla-mcp-studio) | `nexla_mcp_studio`  
[Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion) | `notion`  
[Omni Analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/omni_analytics) | `omni_analytics`  
[Open Targets](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/open_targets) | `open_targets`  
[Oracle NetSuite](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/oracle_netsuite) | `oracle_netsuite`  
[PagerDuty](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty) | `pagerduty`  
[PandaDoc](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pandadoc) | `pandadoc`  
[Pendo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pendo_mcp) | `pendo_mcp`  
[pg-aiguide](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pg_aiguide) | `pg_aiguide`  
[Pylon](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pylon) | `pylon`  
[Ramp](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ramp-mcp) | `ramp_mcp`  
[Relativity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/relativity) | `relativity`  
[S&P Global - Deterministic Retrieval](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/s_p_global) | `s_p_global`  
[Salesforce](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/connect-salesforce) | `salesforce`  
[Sanity](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sanity) | `sanity`  
[ServiceM8](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8) | `servicem8`  
[Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify) | `shopify`  
[Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet) | `smartsheet`  
[Solve Intelligence](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/solve-intelligence) | `solve_intelligence`  
[Sourcegraph](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sourcegraph) | `sourcegraph`  
[Squarespace](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/squarespace) | `squarespace`  
[Starburst](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/starburst) | `starburst`  
[Streak](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/streak) | `streak`  
[Stripe](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/stripe) | `stripe`  
[Superhuman Mail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/superhuman-mail) | `superhuman_mail`  
[Supermetrics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/supermetrics) | `supermetrics`  
[Supabase](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/supabase) | `supabase`  
[SurveyMonkey](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/surveymonkey) | `surveymonkey`  
[Taskrabbit](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/taskrabbit) | `taskrabbit`  
[Tavily](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/tavily) | `tavily`  
[Trivago](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/trivago) | `trivago`  
[Twilio Docs](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/twilio_docs) | `twilio_docs`  
[Vanta](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/vanta) | `vanta`  
[Viator](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/viator) | `viator`  
[Webex Meetings](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/webex-meetings) | `webex_meetings`  
[Windsor.ai](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/windsor-ai) | `windsor`  
[Wix](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wix) | `wix`  
[Wrike](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wrike) | `wrike`  
[Zapier](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zapier) | `zapier`  
[Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk) | `zendesk`  
[Zoho Books](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks) | `zohobooks`  
[Zoho CRM](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohocrm) | `zohocrm`  
[Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk) | `zohodesk`  
[Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects) | `zohoprojects`  
[ZoomInfo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zoominfo) | `zoominfo`  
  
### Private preview

To connect data sources that are in private preview, contact your Google account team and request to be added to the allowlist.

  * [Connect Confluence Data Center On-premises with data ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc)
  * [Connect Jira Data Center On-premises with data ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc)
  * [Connect Salesforce with data ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/connect-salesforce)



## Supported actions

Expand the data store name in the following list to reveal the available actions for each.

**Note:** Not all third-party data stores support actions, such as data stores supporting limited functionality (federated search only or search only).

AsanaLaunch date | Action | Description  
---|---|---  
06/05/26 | Create project | Create a new project with optional sections and tasks in a single operation.  
Create project status update | Post a status update to a project or portfolio.  
Create tasks | Create one or more tasks immediately without visual preview or asking for confirmation.  
Update tasks | Update one or more tasks in a single operation.  
Delete task | Delete task from Asana.  
AirOpsLaunch date | Action | Description  
---|---|---  
6/4/26 | Add grid column | Add a new column to a grid table.  
Add URLs to knowledge base | Add one or more URLs to a knowledge base for indexing.  
Create action grid | Create a grid with power agents for taking action on AEO insights.  
Create grid | Create a new grid (spreadsheet-like table for organizing and processing data).  
Create grid sheet | Create a new sheet (table) within an existing grid.  
Create knowledge base direct upload | Initiate a direct file upload to a knowledge base.  
Create report | Create a new analytics report for a Brand Kit.  
Manage knowledge base | Create or update a knowledge base.  
8/28/26 | Update knowledge base document metadata | Update metadata for a document in a knowledge base.  
7/29/26 | Suggest Brand Kit edits | Suggest edits to a Brand Kit's fields without applying them.  
Write grid | Create or update rows in a grid table.  
AirtableLaunch date | Action | Description  
---|---|---  
8/28/26 | Create records for table | Create new records in a specific table.  
8/11/26 | Update records for table | Update existing records in a specific table.  
6/23/26 | Create base | Create a new base in a specified workspace.  
Create field | Create a new field in an existing table.  
Create record comment | Create a new comment on a specific record.  
Create table | Create a new table in an existing base.  
Update table | Update an existing table's name and/or description.  
BitlyLaunch date | Action | Description  
---|---|---  
08/17/26 | Create QR code | Create a QR code.  
Create short link | Create a short link.  
Update QR code | Update a QR code.  
Update short link | Update short link properties.  
Box

Box supports the tools exposed by Box as actions within the data store. For a list of supported tools, see the [Box MCP tools documentation](https://docs.box.com/en/box-mcp/tools).

Box (Legacy)Launch date | Action | Description  
---|---|---  
1/23/26 | Upload file | Uploads a new document or file to a specific folder in Box.  
Download file | Downloads a file from Box.  
12/19/25 | Copy file | Creates a duplicate of a file within a destination folder while leaving the original file unchanged.  
ClayLaunch date | Action | Description  
---|---|---  
9/22/26 | Find and enrich company | Find and enrich a single company by domain or LinkedIn URL.  
Find and enrich contacts at company | Search for contacts at a company by role, title, name, or department.  
Find and enrich list of contacts | Find and enrich specific named contacts at their companies.  
Confluence CloudLaunch date | Action | Description  
---|---|---  
8/5/26 | Create blog post |  Creates a new Confluence blog post in a specified space with content and a title.   
Create space | Creates a new Confluence space with a specified name and key.  
Update page | Updates the title or content of an existing Confluence page.  
1/23/26 | Upload attachment | Uploads a file to be attached to a specific page.  
Download attachment | Retrieves the actual file content of a specific attachment.  
12/19/25 | Create page | Creates a new Confluence Cloud page.  
Confluence Data CenterLaunch date | Action | Description  
---|---|---  
3/4/26 | Download attachment | Downloads an attachment from a Confluence Data Center page.  
2/19/26 | Upload attachment | Uploads an attachment to a Confluence Data Center page.  
DescriptLaunch date | Action | Description  
---|---|---  
8/17/26 | Import media | Import media into a Descript project.  
Prompt project agent | Query, create, and edit Descript projects using natural language.  
Publish project | Publish a Descript project composition.  
DropboxLaunch date | Action | Description  
---|---|---  
1/28/26 | Download file | Downloads a file from Dropbox.  
1/23/26 | Upload file | Uploads a new file to a specified path within a Dropbox account.  
12/12/25 | Create folder | Creates a folder in Dropbox.  
Copy file or folder | Copies a file or folder in Dropbox.  
EgnyteLaunch date | Action | Description  
---|---|---  
7/29/26 | Create comment | Create a new comment (note) on an existing file in Egnyte.  
Create folder | Create a new folder in Egnyte.  
Create link | Create a link to a file or folder in Egnyte.  
Upload file | Upload a file.  
FreshserviceLaunch date | Action | Description  
---|---|---  
8/03/26 | Create ticket note | Adds a note (conversation) to an existing ticket in Freshservice.  
7/12/26 | Update ticket | Updates an existing ticket in Freshservice.  
6/23/26 | Create ticket | Creates a new ticket in Freshservice.  
Place service catalog item request | Submits a request for a service catalog item.  
GammaLaunch date | Action | Description  
---|---|---  
8/17/26 | Generate Gamma | Creates a new presentation, document, webpage, or social media post in Gamma.  
GitHubLaunch date | Action | Description  
---|---|---  
07/15/26 | Create gist | Create a new GitHub Gist.  
Dismiss notification | Mark a GitHub notification as read or done.  
Manage notification subscription | Ignore, watch, or delete a notification thread subscription.  
Manage repository notification subscription |  Ignore, watch, or delete a repository's notification subscription.   
Mark all notifications read |  Mark all notifications as read, optionally scoped to a repository.   
Reply to pull request comment | Add a reply to an existing pull request comment.  
Star repository | Star a repository on behalf of the authenticated user.  
Trigger Actions workflow | Trigger a GitHub Actions workflow (run, cancel, or rerun jobs).  
Unstar repository | Unstar a repository on behalf of the authenticated user.  
Update gist | Update an existing GitHub Gist.  
Write discussion comment | Add, reply to, update, delete, or mark/unmark as answer a discussion comment.  
Write GitHub project | Create or update GitHub Projects (project, items, fields, status updates).  
Write repository label | Create, update, or delete a label on a repository.  
03/18/26 | Create or update file | Create or update a single file in a repository.  
Fork repository | Fork a repository to your account or a specified organization.  
Push files | Push multiple files to a repository in a single commit.  
Write issue | Create or update an issue in a repository.  
03/11/26 | Add comment to pending review | Add a review comment to your latest pending pull request review.  
Add issue comment | Add a comment to a specific issue or pull request.  
Create branch | Create a new branch in a repository.  
Merge pull request | Merge a pull request.  
Update pull request | Update an existing pull request.  
HexLaunch date | Action | Description  
---|---|---  
08/11/26 | Create thread | Create a Hex Thread to ask questions about your data.  
Continue thread | Add follow-up questions to an idle thread.  
HubSpotLaunch date | Action | Description  
---|---|---  
03/18/26 | Manage CRM Objects | Manages CRM objects in HubSpot.  
Jira CloudLaunch date | Action | Description  
---|---|---  
8/5/26 | Assign issue | Assigns an existing Jira issue to a specified user.  
Create project |  Creates a new Jira project with a specified name, key, project type, and template.   
Create worklog | Adds a time-tracking worklog entry to a Jira issue.  
Get board | Gets a board in Jira.  
Get issues for board | Gets issues for a board in Jira.  
Link issues |  Creates a link between two Jira issues (for example, blocks, is blocked by, relates to).   
List boards | Lists boards in Jira.  
Update project |  Updates an existing Jira project's settings, such as name, key, description, or lead.   
Update worklog | Updates an existing worklog entry on a Jira issue.  
1/23/26 | Upload attachment | Uploads an attachment to an existing issue in Jira.  
12/19/25 | Change issue status | Changes a Jira issue's status.  
12/12/25 | Create comment | Creates a comment on a Jira issue.  
Update comment | Edits an existing comment.  
Create issue | Creates a new Jira issue (requires summary, project ID, and issue type ID).  
Update issue | Updates an existing issue in Jira Cloud. You need to provide the issue ID to identify it, and you can modify various fields such as the summary, description, and assignee.  
Jira Data CenterLaunch date | Action | Description  
---|---|---  
2/19/26 | Create issue | Creates a new issue or ticket.  
Update issue | Changes the details of a ticket, like updating its summary, description, priority, or assignee.  
Change Issue Status | Changes the status of an issue.  
Create comment | Adds a comment on an issue.  
Update comment | Modifies an existing comment on an issue.  
Download attachment | Downloads an attachment from an issue.  
Upload attachment | Adds an attachment to an issue.  
LinearLaunch date | Action | Description  
---|---|---  
2/6/26 | Save comment | Saves a comment to a Linear issue.  
Save issue | Saves an issue in Linear.  
Save a project | Saves a new Linear project.  
LovableLaunch date | Action | Description  
---|---|---  
7/29/26 | Deploy project | Deploy (publish) a project to production hosting on lovable.app.  
Enable database | Provision a cloud PostgreSQL database (Supabase) for a project.  
Send message | Send a chat message to a project's AI agent.  
Set workspace knowledge | Set the workspace's knowledge content.  
6/23/26 | Add connector | Add a connector to a workspace.  
Remix project | Remix (fork) an existing project into a workspace.  
Set project knowledge | Set a project's knowledge content.  
Set project visibility | Set a project's visibility level: draft, private, or public.  
Microsoft OneDriveLaunch date | Action | Description  
---|---|---  
9/17/26 | Copy folder | Copies a folder in OneDrive to a destination folder.  
Move file | Moves a file in OneDrive to another folder.  
Move folder | Moves a folder in OneDrive to another folder.  
Rename file | Renames a file in OneDrive.  
Rename folder | Renames a folder in OneDrive.  
Share file or folder | Shares a file or folder in OneDrive with specified recipients.  
Update file properties | Updates metadata properties on a file in OneDrive.  
1/23/26 | Upload file | Uploads a file to OneDrive.  
Download file | Downloads a file from OneDrive.  
12/12/25 | Create folder | Creates a new folder in OneDrive at a specified path.  
Copy file | Copies a file in OneDrive from a source to a destination.  
Microsoft OutlookLaunch date | Action | Description  
---|---|---  
9/22/26 | Create message |  Creates a new draft email message in the signed-in user's mailbox.   
Reply to message | Replies to an email message.  
Update message |  Updates an existing draft email message in the signed-in user's mailbox.   
9/17/26 | Add attachments | Adds an attachment to an existing message.  
Forward mail | Forwards an email message.  
Move mail | Moves an email message to another folder.  
Create calendar | Creates a new calendar for the signed-in user.  
Update calendar | Updates an existing calendar for the signed-in user.  
RSVP to event |  Responds (accept, decline, or tentatively accept) to a calendar event invitation.   
Create Word document | Creates a new Word (.docx) document in the user's OneDrive.  
Convert Word document to PDF |  Converts a Word (.docx) document stored in OneDrive or SharePoint to PDF.   
Create PowerPoint presentation |  Creates a new PowerPoint (.pptx) presentation in the user's OneDrive.   
Convert PowerPoint to PDF |  Converts a PowerPoint (.pptx) presentation stored in OneDrive or SharePoint to PDF.   
1/23/26 | Download attachment | Downloads an attachment from an email.  
12/19/25 | Create contact | Creates a new Outlook contact.  
Update contact | Updates an existing Outlook contact.  
12/12/25 | Create event | Creates a new event.  
Update event | Updates an existing event.  
Send mail | Sends an email, including attachments.  
Microsoft SharePointLaunch date | Action | Description  
---|---|---  
9/17/26 | Discard check out document | Discards the check out of a document in a SharePoint library.  
Share resource |  Shares a file, folder, or site in SharePoint with specified recipients.   
Update file properties | Updates metadata fields on a document in a SharePoint library.  
Update page | Updates an existing page on a SharePoint site.  
Update list | Updates properties of an existing SharePoint list.  
Create list item | Creates a new item in a SharePoint list.  
Update list item | Updates an existing item in a SharePoint list.  
List lists | Lists all SharePoint lists on a site.  
Get list item | Retrieves a specific item from a SharePoint list.  
Get list fields | Retrieves column field definitions for a SharePoint list.  
3/11/26 | Add page | Creates a new page on the SharePoint site.  
Check out document | Checks out a document from a SharePoint library.  
Check in document | Checks a document into a SharePoint library.  
Rename attachment or document | Renames an attachment or a document in a SharePoint library.  
Move attachment or document | Moves a document from a SharePoint library to a destination library, folder, or another SharePoint site.  
1/23/26 | Upload document | Uploads a file to a SharePoint list item.  
Download document | Downloads a file attached to a SharePoint list item.  
12/12/25 | Create folder | Creates a new folder in a specified path.  
Add list | Creates a new structured data list (for example, tasks, contacts) on SharePoint.  
Microsoft TeamsLaunch date | Action | Description  
---|---|---  
9/17/26 | Update channel message | Updates an existing message in a Microsoft Teams channel.  
Update chat message | Updates an existing message in a Microsoft Teams chat.  
Create channel | Creates a new channel in a Microsoft Teams team.  
Update channel | Updates an existing channel in a Microsoft Teams team.  
Create chat | Creates a new chat in Microsoft Teams.  
Update chat | Updates an existing chat in Microsoft Teams.  
Add member to channel | Adds a member to a Microsoft Teams channel.  
Create schedule | Creates a schedule for a team in Microsoft Teams Shifts.  
Create time off entry | Creates a time-off entry in Microsoft Teams Shifts.  
Update time off entry | Updates an existing time-off entry in Microsoft Teams Shifts.  
12/19/25 | Send channel message | Sends a message to a specified channel.  
Send chat message | Sends a message in a chat.  
MiroLaunch date | Action | Description  
---|---|---  
8/11/26 | Create doc | Create doc  
Update doc | Update doc  
MondayLaunch date | Action | Description  
---|---|---  
3/17/26 | Change item column values | Changes the column values of an item in Monday.  
Create board | Creates a new board in Monday.  
Create column | Creates a new column in Monday.  
Create dashboard | Creates a new dashboard in Monday.  
Create doc | Creates a new doc in Monday.  
Create form | Creates a new form in Monday.  
Create group | Creates a new group in Monday.  
Create item | Creates a new item in Monday.  
3/4/26 | Create workspace | Creates a new workspace in Monday.  
NotionLaunch date | Action | Description  
---|---|---  
03/11/26 | Create database | Creates a new database in Notion.  
Update database | Updates the attributes of a database in Notion.  
Create page | Creates a new page in Notion.  
Update page | Updates attributes of a Notion page.  
2/19/26 | Create comment | Creates a new comment on a Notion page or block.  
PagerDutyLaunch date | Action | Description  
---|---|---  
5/25/26 | Create incident | Create an incident synchronously without a corresponding event from a monitoring service.  
Update incident | Acknowledge, resolve, escalate, or reassign an incident.  
Add note to incident | Add a note to an incident's timeline.  
Create service | Create a new service.  
Update service | Update an existing service.  
Create user | Create a new user account in PagerDuty.  
Update user | Update an existing user's details.  
Create on-call override | Create an override for a specific user covering a specified time range on a schedule.  
Search | Search for incidents, services, users, schedules, and escalation policies.  
List on-call entries | List the on-call entries during a given time range.  
List log entries | Get the full timeline of an incident.  
SalesforceLaunch date | Action | Description  
---|---|---  
6/23/26 | Create case | Creates a case in Salesforce.  
ServiceM8Launch date | Action | Description  
---|---|---  
7/31/26 | Add job note | Adds a note to a job specified by its UUID.  
Change job status | Change the status of a job.  
Compose email message | Compose and send an email message linked to a Job UUID.  
Create job | Create a new job with client and scheduling information.  
Create job activity | Create a scheduled booking for a staff member to attend the job.  
Send job to queue | Send a job to a queue with expiry date.  
ServiceNowLaunch date | Action | Description  
---|---|---  
12/12/25 | Create incident | Creates a new ServiceNow incident to report and track service interruptions.  
Update incident | Updates an existing ServiceNow incident using its system ID.  
ShopifyLaunch date | Action | Description  
---|---|---  
3/11/26  
Create order | Creates a new order in Shopify.  
Send fulfillment request | Sends a fulfillment request for an order on your Shopify site.  
3/4/26 | Create customer | Creates a new customer in Shopify.  
Update customer | Updates an existing customer in Shopify.  
SmartsheetLaunch date | Action | Description  
---|---|---  
8/11/26 | Add rows | Adds one or more new rows to a sheet.  
7/29/26 | Add favorites | Marks one or more assets (sheets, reports, dashboards, folders, workspaces, or templates) as favorites for the current user.  
Create sheet | Creates a new sheet in a folder or workspace, either from scratch with custom column definitions or based on an existing template.  
Create workspace | Creates a new workspace.  
Update rows | Updates one or more rows in a sheet.  
SlackLaunch date | Action | Description  
---|---|---  
5/26/26 | Send Slack message | Send a Slack message.  
Schedule Slack message | Schedule a Slack message.  
Create Slack canvas | Create a Slack canvas.  
Send Slack message draft | Send a Slack message draft.  
StreakLaunch date | Action | Description  
---|---|---  
8/30/26 | Add call log | Add a call log entry to a box with notes and duration.  
Add thread to box | Add a Gmail thread to a box.  
Assign box | Assign a box to users by email address.  
Create box | Create a new box in a pipeline.  
Create comment | Create a new top-level comment on a box.  
Create contact | Create a team contact and link it to a box.  
Create organization | Create a team organization and link it to a box.  
Create task | Create a new task in a box.  
Regenerate box summary | Regenerate and return a fresh AI summary for a box.  
Update box | Update a box.  
Update box stage | Move a box to a different stage in its pipeline.  
Update task | Update a task.  
SupabaseLaunch date | Action | Description  
---|---|---  
8/17/26 | Apply migration | Applies a migration to the database.  
Deploy edge function | Deploys an Edge Function to a Supabase project. If the function already exists, this will create a new version.  
Execute SQL | Executes raw SQL in the Postgres database.  
Pause project | Pauses a Supabase project.  
Restore project | Restores a Supabase project.  
Windsor.aiLaunch date | Action | Description  
---|---|---  
09/10/26 | Contact Windsor | Send feedback, support, or feature requests to Windsor.ai.  
Execute action | Execute a write action on a Windsor.ai connector account.  
WrikeLaunch date | Action | Description  
---|---|---  
5/15/26 | Create folder/project | Create a new folder/project in Wrike.  
6/5/26 | Create task | Create a new task in Wrike.  
Update folder/project | Update an existing folder/project in Wrike.  
Update task | Update an existing task in Wrike.  
ZendeskLaunch date | Action | Description  
---|---|---  
3/4/26 | Update article | Updates an existing article in Zendesk.  
2/19/26 | Update ticket | Updates an existing ticket in Zendesk.  
Create category | Creates a new category in Zendesk.  
Update post | Updates a post in Zendesk.  
Merge tickets | Merges multiple tickets in Zendesk.  
Add a comment to a ticket | Adds a comment to a ticket in Zendesk.  
1/30/26 | Create ticket | Creates a new ticket in Zendesk.  
Zoho BooksLaunch date | Action | Description  
---|---|---  
5/15/26 | Create Contact | Create a new contact in zohobooks.  
Create Customer Payment | Create a new customer payment in zohobooks.  
Create Estimate | Create a new estimate in zohobooks.  
Create Invoice | Create a new invoice in zohobooks.  
Create Item | Create a new item in zohobooks.  
Create Purchase Order | Create a new purchase order in zohobooks.  
Create Sales Order | Create a new sales order in zohobooks.  
Create Tax | Create a new tax in zohobooks.  
Update Contact | Update an existing contact in zohobooks.  
Update Estimate | Update an existing estimate in zohobooks.  
Update Invoice | Update an existing invoice in zohobooks.  
Update Item | Update an existing item in zohobooks.  
Update Purchase Order | Update an existing purchase order in zohobooks.  
Update Sales Order | Update an existing sales order in zohobooks.  
Zoho DeskLaunch date | Action | Description  
---|---|---  
8/28/26 | Update event | Updates the details of an event.  
6/23/26 | Create call | Creates a new call.  
Send reply | Sends an email reply.  
Update call | Updates the details of a call.  
Update task | Updates the details of a task.  
5/15/26 | Create event | Adds an event entry to your help desk portal.  
Create task | Creates a task in your help desk portal.  
Create ticket | Creates a ticket in your helpdesk.  
Create ticket comment | Adds a comment to a ticket.  
Mark ticket as read | Marks a ticket as read by the user.  
Update ticket | Updates the details of an existing ticket.  
7/12/26 | Update ticket comment | Updates a comment on a ticket.  
Zoho ProjectsLaunch date | Action | Description  
---|---|---  
5/15/26 | Create task list | Add a Task list to the project.  
Update issue | Update an issue in a project.  
Update phase | Update a phase in a project.  
Update task | Modify details of the task in a project.  
6/5/26 | Create default tasklist | Create default tasklist for a project.  
Create phase | Create a phase in a project.  
Create project issue | Create an issue in a project.  
Update project | Modify details of an existing project.  
6/23/26 | Create project | Create a new project in the Zoho Projects portal.  
Create task | Add a task to the project.  
Update task list | Modify details of the task list in a project.  
ZoomInfoLaunch date | Action | Description  
---|---|---  
7/12/26 | Submit feedback | Use this tool to submit feedback on ZoomInfo MCPs or other feedback for ZoomInfo.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
