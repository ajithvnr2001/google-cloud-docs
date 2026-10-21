---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:30.385693+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Confluence Cloud data store for Gemini Enterprise lets you search and perform actions on your spaces, pages, and user information.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Confluence Cloud versions

The Confluence Cloud data store supports Confluence REST API versions v1.

## Supported actions

When the Confluence Cloud data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create page | Creates a new Confluence page in a specified space with content and a title.  
Update page | Updates the title or content of an existing Confluence page.  
Create blog post | Creates a new Confluence blog post in a specified space with content and a title.  
Create space | Creates a new Confluence space with a specified name and key.  
Download attachment | Downloads an attachment from a Confluence page.  
Upload attachment | Uploads an attachment to a Confluence page.  
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB.



### Required scopes

To enable Gemini Enterprise to perform search and data ingestion using the Confluence Cloud data store, you need the following scopes:

Usage reason | Permission | Description  
---|---|---  
**Data ingestion** | `read:content-details:confluence` | Allows the data store to read content details in Confluence.  
`read:attachment:confluence` | Allows the data store to download and read attachments.  
`read:comment:confluence` | Allows the data store to read comments.  
`read:page:confluence` | Allows the data store to read pages.  
`read:whiteboard:confluence` | Allows the data store to read whiteboards.  
`read:space:confluence` | Allows the data store to read spaces.  
`read:group:confluence` | Allows the data store to read groups.  
`read:user:confluence` | Allows the data store to read users.  
`read:content.metadata:confluence` | Allows the data store to read content metadata.  
`read:configuration:confluence` | Allows the data store to read configurations.  
**Federated search** | `search:confluence` | Allows the data store to perform search queries in Confluence.  
**Actions** | `write:page:confluence` | Allows the data store to create and update pages in Confluence.  
`write:attachment:confluence` | Allows the data store to upload attachments to Confluence pages.  
`write:blogpost:confluence` | Allows the data store to create and update Confluence blog posts.  
`write:space:confluence` | Allows the data store to create and update Confluence spaces.  
`write:confluence-space` | Allows the data store to manage Confluence space information, including create, update, and delete operations.  
`write:confluence-content` | Allows the data store to write content in Confluence.  
`write:confluence-file` | Allows the data store to upload attachments to Confluence.  
`read:attachment:confluence` | Allows the data store to download and read attachments.  
`read:comment:confluence` | Allows the data store to read comments.  
`read:configuration:confluence` | Allows the data store to read configurations.  
`read:confluence-content.all` | Allows the data store to read all Confluence content.  
`read:confluence-space.summary` | Allows the data store to read space summaries.  
`read:content-details:confluence` | Allows the data store to read content details in Confluence.  
`read:content.metadata:confluence` | Allows the data store to read content metadata.  
`read:group:confluence` | Allows the data store to read groups.  
`read:me` | Allows the data store to read current user information.  
`read:page:confluence` | Allows the data store to read pages.  
`read:space:confluence` | Allows the data store to read spaces.  
`read:space-details:confluence` | Allows the data store to read space details.  
`read:task:confluence` | Allows the data store to read tasks.  
`read:user:confluence` | Allows the data store to read users.  
`search:confluence` | Allows the data store to perform search queries in Confluence.  
  
For information on how to configure these scopes, see [Enable OAuth 2.0 and configure scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#enable-oauth-scopes).

## Rate limits for data ingestion

The Confluence Cloud data store supports a default rate limit of 20 queries per second (QPS) for data ingestion. These rate limits apply exclusively to the ingestion of data from the Confluence Cloud data store.

## Limitations

This section outlines known issues and limitations that may affect your use of the Confluence Cloud data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Confluence Cloud data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Confluence Cloud data store is supported only in the `global`, `us`, and `eu` locations.



The following are the limitations for the Confluence Cloud ingestion data store:

  * The legacy user management model is not supported for integration with Confluence Cloud. Only the centralized user management model is supported. For more information, see [Atlassian organization consolidation guide](https://support.atlassian.com/atlassian-cloud/kb/atlassian-organization-consolidation-guide/)
  * The appearance of the macros that you added on Confluence pages might differ from user to user based on their access permissions.
  * The data store doesn't support incremental sync for the spaces entity.
  * You can't use a Google Cloud service account to authenticate to Confluence Cloud.
  * The data store doesn't include archived pages in a full sync operation, and those pages are indexed as deleted.
  * The data store doesn't support spaces and entities shared using anonymous access, guest links, or public URLs.



## What's next

  * To create and configure a data store with Confluence Cloud, see [Set up a Confluence Cloud data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
