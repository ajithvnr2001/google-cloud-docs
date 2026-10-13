---
url: https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.CloudSqlReference
title: Google Cloud Gemini Data Analytics V1beta Client - Class CloudSqlReference (0.14.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:24.116097+00:00
---

# Google Cloud Gemini Data Analytics V1beta Client - Class CloudSqlReference (0.14.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.CloudSqlReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Gemini Data Analytics V1beta Client - Class CloudSqlReference (0.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Gemini Data Analytics V1beta Client class CloudSqlReference.

Message representing reference to a CloudSQL database and agent context.

Only supported for the `QueryData` method.

Generated from protobuf message `google.cloud.geminidataanalytics.v1beta.CloudSqlReference`

## Namespace

Google \ Cloud \ GeminiDataAnalytics \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ database_reference` |  `[CloudSqlDatabaseReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.CloudSqlDatabaseReference)`   
Required. Singular proto that supports specifying which database and tables to include.  
`↳ agent_context_reference` |  `[AgentContextReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.AgentContextReference)`   
Optional. Parameters for retrieving data from Agent Context.  
  
### getDatabaseReference

Required. Singular proto that supports specifying which database and tables to include.

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlDatabaseReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.CloudSqlDatabaseReference)|null` |   
  
### hasDatabaseReference

### clearDatabaseReference

### setDatabaseReference

Required. Singular proto that supports specifying which database and tables to include.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CloudSqlDatabaseReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.CloudSqlDatabaseReference)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAgentContextReference

Optional. Parameters for retrieving data from Agent Context.

**Returns**  
---  
**Type** | **Description**  
`[AgentContextReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.AgentContextReference)|null` |   
  
### hasAgentContextReference

### clearAgentContextReference

### setAgentContextReference

Optional. Parameters for retrieving data from Agent Context.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AgentContextReference](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest/V1beta.AgentContextReference)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
