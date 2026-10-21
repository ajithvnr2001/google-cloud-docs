---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:05:05.826653+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Notion data store for Gemini Enterprise lets you access and perform actions on your Notion data.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported actions

When the Notion data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create comment | Creates a new comment on a Notion page or block.  
Create database | Creates a new database in Notion.  
Update database | Updates the attributes of a database in Notion.  
Create page | Creates a new page in Notion.  
Update page | Updates attributes of a Notion page.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search and actions using Notion, you need to configure the necessary permissions within your Notion instance.

The following table details the required permissions based on the connection mode:

Connection mode | Scope | Purpose  
---|---|---  
**Federated search** | `Read content` | Required to perform searching across Notion data.  
**Federated search and actions** | `Read content` | Required to perform searching across Notion data.  
`Insert content` | Required to perform creating comments in Notion.  
`Read comments` | Required to fetch and list existing comments.  
`Insert comments` | Required to create comments.  
  
## Limitations

The Notion data store is supported only in `Global`, `US`, and `EU` locations.

## What's next

  * To configure a Notion integration for connecting to Gemini Enterprise, see [Notion configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
