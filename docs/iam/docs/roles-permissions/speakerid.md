---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid/
title: Speaker ID roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:12.262505+00:00
---

# Speaker ID roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Speaker ID roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Speaker ID. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Speaker ID roles

Role | Permissions  
---|---  
  
#### Speaker ID Admin 

(`roles/speakerid.admin`) Grants full access to all Speaker ID resources, including project settings.  |  `speakerid.*`

  * `speakerid.phrases.create`
  * `speakerid.phrases.delete`
  * `speakerid.phrases.get`
  * `speakerid.phrases.list`
  * `speakerid.settings.get`
  * `speakerid.settings.update`
  * `speakerid.speakers.create`
  * `speakerid.speakers.delete`
  * `speakerid.speakers.get`
  * `speakerid.speakers.list`
  * `speakerid.speakers.verify`

  
  
#### Speaker ID Editor 

(`roles/speakerid.editor`) Grants access to read and write all Speaker ID resources.  |  `speakerid.phrases.*`

  * `speakerid.phrases.create`
  * `speakerid.phrases.delete`
  * `speakerid.phrases.get`
  * `speakerid.phrases.list`

`speakerid.settings.get` `speakerid.speakers.*`

  * `speakerid.speakers.create`
  * `speakerid.speakers.delete`
  * `speakerid.speakers.get`
  * `speakerid.speakers.list`
  * `speakerid.speakers.verify`

  
  
#### Speaker ID Viewer 

(`roles/speakerid.viewer`) Grants read access to all Speaker ID resources.  |  `speakerid.phrases.get` `speakerid.phrases.list` `speakerid.settings.get` `speakerid.speakers.get` `speakerid.speakers.list`  
  
#### Speaker ID Verifier 

(`roles/speakerid.verifier`) Grants read access to all Speaker ID resources, and allows verification.  |  `speakerid.phrases.get` `speakerid.phrases.list` `speakerid.speakers.get` `speakerid.speakers.list` `speakerid.speakers.verify`  
  
## Speaker ID permissions

Permission | Included in roles  
---|---  
  
#### `speakerid.phrases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.phrases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.phrases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.viewer) (`roles/speakerid.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Speaker ID Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.verifier) (`roles/speakerid.verifier`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.phrases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.viewer) (`roles/speakerid.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Speaker ID Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.verifier) (`roles/speakerid.verifier`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.viewer) (`roles/speakerid.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `speakerid.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)   
  
#### `speakerid.speakers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.speakers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.speakers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.viewer) (`roles/speakerid.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Speaker ID Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.verifier) (`roles/speakerid.verifier`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.speakers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.viewer) (`roles/speakerid.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Speaker ID Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.verifier) (`roles/speakerid.verifier`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `speakerid.speakers.verify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Speaker ID Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.admin) (`roles/speakerid.admin`)  [Speaker ID Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.editor) (`roles/speakerid.editor`)  [Speaker ID Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/speakerid#speakerid.verifier) (`roles/speakerid.verifier`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
