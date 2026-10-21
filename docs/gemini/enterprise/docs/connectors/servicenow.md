---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:53:07.005674+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The ServiceNow connector for Gemini Enterprise lets you search and perform actions on your data and records.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Connector types

Gemini Enterprise supports two connector types, letting you choose how you want to access your records:

  * **[Federated search](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred-auth-code)** : Access your records in real-time directly from your ServiceNow app without data ingestion. This mode uses the Authorization Code grant flow, which requires a redirect-based process to obtain access tokens.

  * **[Data ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred-for-ingestion-connector)** : Synchronize and index your records within a local data store for high-performance search. This mode uses Resource Owner Password Credentials (ROPC), utilizing direct credentials (username and password) to obtain secrets.




Ensure your ServiceNow app registration is configured with the correct authentication flows based on your use case:

  * If configuring Actions, federated search, or both, configure the Authorization Code flow.
  * If configuring data ingestion only, configure the ROPC flow.
  * If configuring data ingestion along with Actions, you must support both the ROPC flow and the Authorization Code flow.



## Supported ServiceNow versions

The ServiceNow connector supports ServiceNow API version v2 and later.

## Supported actions

When the ServiceNow connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action  | Description   
---|---  
Create incident  | Create a new incident record in ServiceNow to report and track a service interruption.   
Update incident  | Update an existing incident in ServiceNow using its unique system ID.   
**Note:** Additional read-only actions are also available.

## Limitations

This section outlines known issues and limitations that may affect your use of the ServiceNow data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing ServiceNow data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The ServiceNow data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a connector with ServiceNow, see [Set up a ServiceNow data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
