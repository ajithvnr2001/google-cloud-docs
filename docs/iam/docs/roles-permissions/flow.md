---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/flow/
title: Flow roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:56:03.796071+00:00
---

# Flow roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Flow roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Flow. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Flow roles

Role | Permissions  
---|---  
  
#### Flow Admin Beta

(`roles/flow.admin`) Full access to all Flow resources. Intended for project administrators.  |  `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Flow Editor Beta

(`roles/flow.editor`) Create and manage Flow generated media. Intended for content creators.  |  `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### FlowService Service Agent 

(`roles/aisandbox.serviceAgent`) Grants FlowService Service Agent permissions to manage resources in the consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict` `aiplatform.interactions.create` `aiplatform.interactions.get` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use`  
  
#### Flow Service Agent 

(`roles/flow.serviceAgent`) Grants Flow Service Agent permissions to manage resources in the consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict` `aiplatform.interactions.create` `aiplatform.interactions.get` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use`  
  
## Flow permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
