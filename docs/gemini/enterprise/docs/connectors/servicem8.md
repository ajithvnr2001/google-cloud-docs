---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:44.330608+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The ServiceM8 connector for Gemini Enterprise lets you manage jobs and schedule activities in ServiceM8 datasets.

## Supported actions

When the ServiceM8 connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Add job note | Adds a note to a job specified by its UUID.  
Change job status | Change the status of a job.  
Compose email message | Compose and send an email message linked to a Job UUID.  
Create job | Create a new job with client and scheduling information.  
Create job activity | Create a scheduled booking for a staff member to attend the job.  
Send job to queue | Send a job to a queue with expiry date.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search using the ServiceM8 data store, you need to enable the following scopes:

Scope | Purpose  
---|---  
`mcp` | Allows the app to connect to the ServiceM8 Model Context Protocol (MCP) server.  
`mcp_client` | Allows the app to act as an MCP client to search data and perform actions in ServiceM8.  
  
## Limitations

This section outlines known issues and limitations that may affect your use of the ServiceM8 data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing ServiceM8 data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The ServiceM8 data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a connector with ServiceM8, see [Set up a ServiceM8 data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicem8/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
