---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/mcp/
title: Google Cloud MCP servers roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:18.309964+00:00
---

# Google Cloud MCP servers roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud MCP servers roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud MCP servers. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud MCP servers roles

Role | Permissions  
---|---  
  
#### MCP Admin 

(`roles/mcp.admin`) Full access for interacting with Google-managed MCP servers.  |  `mcp.tools.call` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### MCP Tool User 

(`roles/mcp.toolUser`) Gives permission to call tools on any MCP server enabled by the parent project.  |  `mcp.tools.call` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Google Cloud MCP servers permissions

Permission | Included in roles  
---|---  
  
#### `mcp.tools.call`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Gemini Cloud Assist Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`)  [Gemini Cloud Assist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) (`roles/geminicloudassist.editor`)  [Gemini Cloud Assist User](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`)  [MCP Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.admin) (`roles/mcp.admin`)  [MCP Tool User](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
