---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:18.991262+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Confluence Data Center data store for Gemini Enterprise lets you search and perform actions on page content, attachments, and comments.

The Confluence Data Center connector supports the following connection modes, which have different launch stages:

  * **Federated search and actions** : Generally available (GA).
  * **Data ingestion** : In Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).



## Supported Confluence Data Center versions

The Confluence Data Center data store supports Confluence Data Center version 7.19.0 and later.

## Supported actions

When the Confluence Data Center connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Upload attachment | Add an attachment to a Confluence Data Center page.  
Download attachment | Download an attachment from a Confluence Data Center page.  
**Note** : The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB. 

## Required scopes

To enable Gemini Enterprise to perform necessary search, actions, and data ingestion, the following scopes are required:

Connection mode | Scopes | Purpose  
---|---|---  
Data ingestion | `READ` | Required to ingest Confluence page content, attachments, and comments.  
Federated search and actions | `WRITE` | Required to search Confluence page content, attachments, and comments, and to upload attachments.  
  
For information about how to configure these scopes, see [Set up OAuth 2.0 authentication and OAuth scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenter-configuration#create-oauth-app-link).

## Limitations

  * Enforcing a VPC Service Controls perimeter on existing Confluence Data Center data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).

  * When creating a new application or adding a data store to an existing application, it's recommended that you add a data store with actions belonging to a single connector type. For example, don't associate two Confluence Data Center data stores with actions enabled to the same application.

  * The Confluence Data Center data store is supported only in Global, US, and EU locations.




## What's next

  * To create and configure a data store with Confluence Data Center, see [Set up a Confluence Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
