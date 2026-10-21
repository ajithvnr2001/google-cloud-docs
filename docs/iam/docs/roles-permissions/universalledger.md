---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger/
title: Universal Ledger roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:03:24.806972+00:00
---

# Universal Ledger roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Universal Ledger roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Universal Ledger. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Universal Ledger roles

Role | Permissions  
---|---  
  
#### Universal Ledger Admin Beta

(`roles/universalledger.admin`) Grants access to endpoints and networks, including the ability to submit transactions. Currently, this role has the same permissions as the Universal Ledger Editor role.  |  `universalledger.*`

  * `universalledger.endpoints.get`
  * `universalledger.endpoints.list`
  * `universalledger.endpoints.readNetwork`
  * `universalledger.endpoints.submit`
  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
#### Universal Ledger Editor Beta

(`roles/universalledger.editor`) Grants access to endpoints and networks, including the ability to submit transactions.  |  `universalledger.*`

  * `universalledger.endpoints.get`
  * `universalledger.endpoints.list`
  * `universalledger.endpoints.readNetwork`
  * `universalledger.endpoints.submit`
  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
#### Universal Ledger Viewer Beta

(`roles/universalledger.viewer`) Grants the ability to view endpoints, and query the network via an endpoint.  |  `universalledger.endpoints.get` `universalledger.endpoints.list` `universalledger.endpoints.readNetwork` `universalledger.locations.*`

  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
#### Universal Ledger Endpoint Viewer Beta

(`roles/universalledger.endpointViewer`) Grants the ability to read the endpoints for a given project.  |  `universalledger.endpoints.get` `universalledger.endpoints.list` `universalledger.locations.*`

  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
#### Universal Ledger Network User Beta

(`roles/universalledger.networkUser`) Grants full access to the GCUL Network, including the ability to send transactions.  |  `universalledger.*`

  * `universalledger.endpoints.get`
  * `universalledger.endpoints.list`
  * `universalledger.endpoints.readNetwork`
  * `universalledger.endpoints.submit`
  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
#### Universal Ledger Network Viewer Beta

(`roles/universalledger.networkViewer`) Grants the ability to retrieve a specific endpoint and query the network with it.  |  `universalledger.endpoints.get` `universalledger.endpoints.list` `universalledger.endpoints.readNetwork` `universalledger.locations.*`

  * `universalledger.locations.get`
  * `universalledger.locations.list`

  
  
## Universal Ledger permissions

Permission | Included in roles  
---|---  
  
#### `universalledger.endpoints.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.viewer) (`roles/universalledger.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Universal Ledger Endpoint Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.endpointViewer) (`roles/universalledger.endpointViewer`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)  [Universal Ledger Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkViewer) (`roles/universalledger.networkViewer`)   
  
#### `universalledger.endpoints.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.viewer) (`roles/universalledger.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Universal Ledger Endpoint Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.endpointViewer) (`roles/universalledger.endpointViewer`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)  [Universal Ledger Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkViewer) (`roles/universalledger.networkViewer`)   
  
#### `universalledger.endpoints.readNetwork`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.viewer) (`roles/universalledger.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)  [Universal Ledger Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkViewer) (`roles/universalledger.networkViewer`)   
  
#### `universalledger.endpoints.submit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)   
  
#### `universalledger.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.viewer) (`roles/universalledger.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Universal Ledger Endpoint Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.endpointViewer) (`roles/universalledger.endpointViewer`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)  [Universal Ledger Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkViewer) (`roles/universalledger.networkViewer`)   
  
#### `universalledger.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Universal Ledger Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.admin) (`roles/universalledger.admin`)  [Universal Ledger Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.editor) (`roles/universalledger.editor`)  [Universal Ledger Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.viewer) (`roles/universalledger.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Universal Ledger Endpoint Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.endpointViewer) (`roles/universalledger.endpointViewer`)  [Universal Ledger Network User](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkUser) (`roles/universalledger.networkUser`)  [Universal Ledger Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/universalledger#universalledger.networkViewer) (`roles/universalledger.networkViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
