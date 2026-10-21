---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/
title: Data stores \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:36.373754+00:00
---

# Data stores  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data stores Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The _Data Stores_ feature is excluded from the [Dialogflow CX SLA](https://cloud.google.com/dialogflow/sla).

_Data stores_ are used by [data store tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler) to find answers for end-user questions from your data. Data stores are a collection of websites, documents, or data in third-party systems, each of which references your data.

When an end-user asks the agent a question, the agent searches for an answer from the given source content and summarizes the findings into a coherent agent response. It also provides supporting links to the sources of the response for the end-user to learn more. The agent can provide up to five answer snippets for a given question.

## Data store sources

You can use different sources for your data:

  * **Website URLs:** Automatically crawl website content from a list of domains or web pages.
  * **BigQuery:** Import data from your BigQuery table.
  * **Cloud Storage:** Import data from your Cloud Storage bucket.
  * **AlloyDB:** Import data from your [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs) cluster.
  * **Bigtable:** Import data from a [Bigtable](https://docs.cloud.google.com/bigtable/docs) table.
  * **Firestore:** Import data from your [Firestore](https://firebase.google.com/docs/firestore) collection.
  * **Cloud SQL:** Import data from a [Cloud SQL](https://docs.cloud.google.com/sql/docs) table.
  * **Spanner:** Import data from a [Spanner](https://docs.cloud.google.com/spanner/docs) table.



### Restricted access data store sources

Google offers many additional first- and third-party data store sources as a restricted access feature. To see available sources and request access, see [additional data store sources](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#restricted_access_additional_data_store_sources).

## Website content

When adding website content as a source, you can add and exclude multiple sites. When you specify a site, you can use individual pages or `*` as a wildcard for a pattern. All HTML and PDF content will be processed.

You must [verify your domain](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) when using website content as a source.

Limitations:

  * Files from public URLs must have been crawled by the Google Search indexer to exist in the search index. You can check this with the [Google Search Console](https://search.google.com/search-console).
  * Up to 200,000 pages are indexed. If the data store contains more pages, indexing fails at that point, but any content already indexed remains.



## Import data

You can import data from BigQuery or Cloud Storage. This data can be in FAQ form or unstructured, and it can be with metadata or without metadata.

The following **Data Import Options** are available:

  * **Add/Update Data:** Adds the provided documents to the data store. If a new document has the same ID as an existing document, the new document replaces the old one.
  * **Override Existing Data:** Deletes all existing data and uploads new data. This action is irreversible.



### FAQ data store

Data stores can hold answers to frequently asked questions. When user questions are matched with high confidence to an uploaded question, the agent returns the answer to that question without modification. You can provide a title and a URL for each question and answer pair that the agent displays.

Upload data to the data store in CSV format. Each file must include a header row that describes the columns.

For example:
    
    
    "question","answer","title","url"
    "Why is the sky blue?","The sky is blue because of Rayleigh scattering.","Rayleigh scattering","https://en.wikipedia.org/wiki/Rayleigh_scattering"
    "What is the meaning of life?","42","",""
    

You can omit the `title` and `url` columns:
    
    
    "answer","question"
    "42","What is the meaning of life?"
    

During the upload process, you can select a folder where each file is processed as a `CSV` file, regardless of the file extension.

Limitations:

  * An extra space character after `,` causes an error.
  * Blank lines (even at the end of the file) cause an error.



### Unstructured data store

Unstructured data stores can contain content in the following formats:

  * `HTML`
  * `PDF`
  * `TXT`
  * `CSV`

**Note:** `CSV` files can also be imported as unstructured content. The schema requirements from the FAQ data section also apply. Metadata is generated automatically if `title` and `url` columns are provided. Each question and answer pair is indexed separately. Matching requirements are less strict than for FAQ `CSV` data stores, and the agent might rewrite the answer rather than returning it word-for-word.

You can import files from another project's Cloud Storage bucket. To do so, grant explicit access to the import process. Follow the instructions in the error message, which will contain the name of the user that needs read access to the bucket to perform the import.

Limitations:

  * The maximum file size is 2.5 MB for text-based formats and 100 MB for other formats.



### Data store with metadata

You can provide a title and `URL` as metadata. During a conversation, the agent can provide this information to help users quickly link to internal web pages that are not accessible by the Google Search indexer.

To import content with metadata, you must provide one or more [JSON Lines](https://jsonlines.org/) files. Each line of this file describes one document. You do not directly upload the actual documents; `URIs` that link to the Cloud Storage paths are provided in the JSON Lines file.

To provide your JSON Lines files, provide a Cloud Storage folder that contains these files. Do not put any other files in this folder.

Field descriptions:

Field | Type | Description  
---|---|---  
id | string | Unique identifier of the document.  
content.mimeType | string | MIME type of the document. "application/pdf" and "text/html" are supported.  
content.uri | string | URI for the document in Cloud Storage.  
structData | string | Single line JSON object with optional `title` and `url` fields.  
  
For example:
    
    
    { "id": "d001", "content": {"mimeType": "application/pdf", "uri": "gs://example-import/unstructured/first_doc.pdf"}, "structData": {"title": "First Document", "url": "https://internal.example.com/documents/first_doc.pdf"} }
    { "id": "d002", "content": {"mimeType": "application/pdf", "uri": "gs://example-import/unstructured/second_doc.pdf"}, "structData": {"title": "Second Document", "url": "https://internal.example.com/documents/second_doc.pdf"} }
    { "id": "d003", "content": {"mimeType": "text/html", "uri": "gs://example-import/unstructured/mypage.html"}, "structData": {"title": "My Page", "url": "https://internal.example.com/mypage.html"} }
    

### Data store without metadata

This type of content has no metadata. Instead, you provide URI links to the individual documents. The content type is determined by the file extension.

## Parse and chunk configuration

Depending on the data source, you can configure [parse and chunk settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents) as defined by Agent Search.

## Use Cloud Storage for a data store document

If your content is not public, storing it in [Cloud Storage](https://docs.cloud.google.com/storage/docs) is the recommended option. When you create data store documents, you provide the URLs for your Cloud Storage objects in the form: `gs://bucket-name/folder-name`. Each document within the folder is added to the data store.

When you create the Cloud Storage bucket:

  * Select the project you use for the agent.
  * Use the [Standard Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard).
  * Set the [bucket location](https://docs.cloud.google.com/storage/docs/locations) to the same location as your agent.



Follow the [Cloud Storage quickstart](https://docs.cloud.google.com/storage/docs/quickstart-console) to create a bucket and upload files.

## Languages

For supported languages, see the data store column in the [language reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).

For best performance, create data stores in a single language.

After creating a data store, you can optionally specify the data store language. If you set the data store language, you can connect the data store to an agent that is configured for a different language. For example, you can create a French data store that is connected to an English agent.

## Supported regions

For information about supported regions, see the [region reference](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail).

## (Restricted access) Additional data store sources

Additional data store types are listed in the following table. They are available as restricted access features. You can fill out the [access request form](https://docs.google.com/forms/d/1ijB9VXrn9OVVhc_9ZLJaJ0cD_laPlXduAGCtHI2N-jY/viewform?edit_requested=true) to request access. Once approved, you will be able to see these options when you create a data store in Vertex AI Agent Builder.

### Third-party data store sources

Data store source | Description  
---|---  
[Box](https://www.box.com/home) | Import data from your organization's Box site.  
[Confluence Cloud](https://developer.atlassian.com/cloud/confluence/) | Import data from your Confluence Cloud workspace.  
[Dropbox](https://www.dropbox.com/) | Import data from your Dropbox storage.  
[EntraID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id/) | Import data from your organization's EntraID system.  
[Jira Cloud](https://www.atlassian.com/software/jira) | Import data from your Jira task management system.  
[OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage) | Import data from your organization's OneDrive storage.  
[Microsoft Outlook](https://www.microsoft.com/en/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook) | Import data from Microsoft Outlook.  
[Salesforce](https://www.salesforce.com/) | Import data from Salesforce.  
[ServiceNow](https://www.servicenow.com/) | Import data from ServiceNow.  
[SharePoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration) | Import data from your organization's SharePoint system.  
[Slack](https://slack.com/) | Import data from Slack.  
[Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) | Import data from Microsoft Teams.  
  
### Set up a third-party data store using a connector

This section outlines the process of setting up a data store using third-party data. For instructions specific to each third-party data source, see the [Vertex AI Agent Builder documentation](https://docs.cloud.google.com/generative-ai-app-builder/docs/connect-third-party-data-source).

#### Identity providers

Identity providers let you manage users, groups, and authentication. When you set up a third-party data store, you can use either a Google identity provider or a third-party identity provider.

**Google identity provider:**

  * Users of the agent sign in using their Google credentials. This is any `@gmail.com` email address or any account that uses Google as the identity provider (for example, Google Workspace). This step is skipped if users talk to the agent using Google Cloud directly, because Google identity is automatically built into the system.
  * You can assign access to Google accounts using [Identity and Access Management (IAM)](https://docs.cloud.google.com/support/docs/access-control).



**Third-party identity provider:**

  * Users of the agent sign in using non-Google credentials, for example a Microsoft email address.
  * You must create a [Workforce Pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers) using Google Cloud containing the non-Google identity providers. You can then use [IAM](https://docs.cloud.google.com/support/docs/access-control) to grant access to either the entire pool or individual users within that pool.
  * This method can't be used with any Google Cloud projects set up under the `@google.com` organization.



#### Connectors

Third-party data stores are implemented using a connector. Each connector can contain multiple data stores, which are stored as entities in the Dialogflow CX system.

**Note:** Only user accounts are supported for authentication; service accounts are not supported for connectors.

  * Before you create a data store, you must set up each region with a single identity provider in **Google Cloud > Agent Builder > Settings**. All data stores in that region use the same identity provider. You can choose either a Google identity or a third-party identity in a workforce pool. The same Google credential is considered a different identity if it's in a workforce pool. For example, `test@gmail.com` is considered a different identity than `workforcePools/test-pool/subject/test@gmail.com`. 
    * [Create a workforce pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#create_a_pool) (if needed).
    * Go to [Agent Builder](https://conversational-agents.cloud.google.com/) **Settings** and select either **Google Identity** or **3rd Party Identity**. Click **Save** to save the identity to the region.
    * You can now create a data store in the region.
  * Each data store saves Access Control List (ACL) data with each document. This record tracks which users or groups have read access to which entities. During runtime, a user or group member receives responses from the agent only if the responses source from entities that they have read access to. If a user has no read access to any entities in the data store, the agent returns an empty response.
  * Because the data in the data store is a copy of the third-party instance, it needs to be periodically refreshed. You can configure the refresh intervals on a time scale of either hours or days.
  * After you configure your data store and click **Create** , it can take up to an hour for the data store to appear in your data stores list.



## Data store tracing

This feature includes two parts:

  1. Display of the data store internal execution tracings and step latencies in the agent simulator.
  2. Export of the data store internal execution tracings and step latencies into Cloud Logging and BigQuery.



### View data in the simulator

To display tracing and execution data in the agent simulator, expand the details about a conversation turn by clicking on the expander arrow to the right of the agent's response.

The **execution** tab displays the internal data store execution traces, including:

  * The original user input.
  * The query as rewritten by the data store engine.
  * Quality signals from execution steps, such as security check status, stability check status, grounding check result, and safety check status.
  * Search snippets from the data store search.
  * The list of supporting documents for the snippets.



The **latency** tab displays a time graph for various data store execution steps. The list of steps varies depending on how the data store is configured and the execution flow. Displayed data can include the following:

  * **FAQ match:** Performs an FAQ matching step.
  * **Query rewriting:** Rewrites the original user query.
  * **Search:** Performs snippet searching.
  * **Summarization:** Summarizes the response.
  * **Safety checks:** Performs safety checking steps.



### View tracing data in other locations

  * If you configure the conversational agent with [conversation history logging](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#logging-settings), you can view data store tracing in **Conversation History**.
  * If you configure the conversational agent with [Logging](https://cloud.google.com/dialogflow/cx/docs/concept/logging), you can view tracings and latencies in the cloud [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * If you configure the conversational agent with [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq), you can view tracings and latencies in an exported BigQuery table.



## What's next

To learn how to create and use a data store with an agent, see the [data store tools documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler).

[ Previous arrow_back  Playbook evaluations  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation)

[ Next Data store tools  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
