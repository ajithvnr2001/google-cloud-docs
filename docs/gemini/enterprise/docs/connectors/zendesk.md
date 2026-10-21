---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:31:04.789726+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Zendesk data store for Gemini Enterprise lets you search and perform actions on your Zendesk data.

## Supported Zendesk versions

The Zendesk data store supports Zendesk version 24.0.9175.

## Supported actions

When the Zendesk data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create ticket | Creates a new ticket.  
Update ticket | Updates an existing ticket.  
Create category | Creates a new category.  
Update post | Updates an existing post.  
Update article | Updates an existing article.  
Merge tickets | Merges multiple tickets.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search and actions using Zendesk, you need to configure the necessary permissions within your Zendesk instance.

The following table details the required permissions based on the connection mode:

Connection mode | Scope | Purpose  
---|---|---  
**Federated search** | `read`, `users:read` | Required to perform searching across Zendesk data.  
**Federated search and actions** | `tickets:write` | Required to perform search, create, update, and merge tickets.  
`hc:write` | Required to create category and update post.  
  
For information about how to configure these permissions, see [Configure Zendesk permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config).

## Limitations

The Zendesk data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Zendesk data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Zendesk data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with Zendesk, see [Set up a Zendesk data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
