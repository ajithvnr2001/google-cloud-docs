---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode/
title: Business AI Code roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:06:19.419882+00:00
---

# Business AI Code roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Business AI Code roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Business AI Code. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Business AI Code roles

Role | Permissions  
---|---  
  
#### User role for Business AI Code API 

(`roles/businessaicode.user`) A user who can use Business AI Code API  |  `businessaicode.*`

  * `businessaicode.locations.fetchQuotaStatus`
  * `businessaicode.locations.generateContent`
  * `businessaicode.locations.queryConfiguration`
  * `businessaicode.locations.selfAssignLicense`
  * `businessaicode.locations.sendTelemetry`

`cloudaicompanion.instances.exportMetrics` `cloudaicompanion.instances.queryEffectiveSetting` `cloudaicompanion.instances.queryEffectiveSettingBindings` `cloudaicompanion.licenses.selfAssign`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Business AI Code Service Agent 

(`roles/businessaicode.serviceAgent`) Gives Business AI Code Assist the permissions to call Vertex and Discovery Engine Settings API.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.predict` `discoveryengine.devToolsConfigs.get` `discoveryengine.projectOverageConfigs.get` `discoveryengine.projects.get` `monitoring.timeSeries.list`  
  
## Business AI Code permissions

Permission | Included in roles  
---|---  
  
#### `businessaicode.locations.fetchQuotaStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Discovery Engine User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.user) (`roles/discoveryengine.user`)  [User role for Business AI Code API](https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode#businessaicode.user) (`roles/businessaicode.user`)  [Gemini Enterprise User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`)  [Podcast API User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.podcastApiUser) (`roles/discoveryengine.podcastApiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `businessaicode.locations.generateContent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Discovery Engine User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.user) (`roles/discoveryengine.user`)  [User role for Business AI Code API](https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode#businessaicode.user) (`roles/businessaicode.user`)  [Gemini Enterprise User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`)  [Podcast API User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.podcastApiUser) (`roles/discoveryengine.podcastApiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `businessaicode.locations.queryConfiguration`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Discovery Engine User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.user) (`roles/discoveryengine.user`)  [User role for Business AI Code API](https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode#businessaicode.user) (`roles/businessaicode.user`)  [Gemini Enterprise User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`)  [Podcast API User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.podcastApiUser) (`roles/discoveryengine.podcastApiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `businessaicode.locations.selfAssignLicense`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Discovery Engine User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.user) (`roles/discoveryengine.user`)  [User role for Business AI Code API](https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode#businessaicode.user) (`roles/businessaicode.user`)  [Gemini Enterprise User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`)  [Podcast API User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.podcastApiUser) (`roles/discoveryengine.podcastApiUser`)   
  
#### `businessaicode.locations.sendTelemetry`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Discovery Engine User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.user) (`roles/discoveryengine.user`)  [User role for Business AI Code API](https://docs.cloud.google.com/iam/docs/roles-permissions/businessaicode#businessaicode.user) (`roles/businessaicode.user`)  [Gemini Enterprise User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`)  [Podcast API User](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.podcastApiUser) (`roles/discoveryengine.podcastApiUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
