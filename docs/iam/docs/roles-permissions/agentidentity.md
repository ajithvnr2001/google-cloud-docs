---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity/
title: Agent Identity API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:11.657094+00:00
---

# Agent Identity API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Agent Identity API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Agent Identity API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Agent Identity API roles

Role | Permissions  
---|---  
  
#### Agent Identity Admin 

(`roles/agentidentity.admin`) Grants access to manage auth providers, authorizations, and access summaries.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.create` `agentidentity.authProviders.delete` `agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authProviders.revokeAuthorizations` `agentidentity.authProviders.setIamPolicy` `agentidentity.authProviders.undelete` `agentidentity.authProviders.update` `agentidentity.authorizations.create` `agentidentity.authorizations.delete` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.authorizations.setIamPolicy` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

  
  
#### Agent Identity Editor 

(`roles/agentidentity.editor`) Grants access to edit auth providers, authorizations, and access summaries.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.create` `agentidentity.authProviders.delete` `agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authProviders.revokeAuthorizations` `agentidentity.authProviders.undelete` `agentidentity.authProviders.update` `agentidentity.authorizations.create` `agentidentity.authorizations.delete` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

  
  
#### Agent Identity Viewer 

(`roles/agentidentity.viewer`) Grants access to view auth providers, authorizations, and access summaries.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

  
  
#### Agent Identity User 

(`roles/agentidentity.user`) Grants access to retrieve and exchange credentials from auth providers and authorizations.  |  `agentidentity.authProviders.exchangeCredentials` `agentidentity.authProviders.retrieveCredentials` `agentidentity.authorizations.exchangeCredentials` `agentidentity.authorizations.retrieveCredentials`  
  
## Agent Identity API permissions

Permission | Included in roles  
---|---  
  
#### `agentidentity.accessSummaries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.accessSummaries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authProviders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `agentidentity.authProviders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `agentidentity.authProviders.exchangeCredentials`

|  [Agent Identity User](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.user) (`roles/agentidentity.user`)  [Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)   
  
#### `agentidentity.authProviders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `agentidentity.authProviders.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authProviders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authProviders.queryWorkloads`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authProviders.retrieveCredentials`

|  [Agent Identity User](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.user) (`roles/agentidentity.user`)  [Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)   
  
#### `agentidentity.authProviders.revokeAuthorizations`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `agentidentity.authProviders.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)   
  
#### `agentidentity.authProviders.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `agentidentity.authProviders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `agentidentity.authorizations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `agentidentity.authorizations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `agentidentity.authorizations.exchangeCredentials`

|  [Agent Identity User](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.user) (`roles/agentidentity.user`)  [Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)   
  
#### `agentidentity.authorizations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authorizations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authorizations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.authorizations.retrieveCredentials`

|  [Agent Identity User](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.user) (`roles/agentidentity.user`)  [Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)   
  
#### `agentidentity.authorizations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)   
  
#### `agentidentity.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `agentidentity.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Agent Identity Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.admin) (`roles/agentidentity.admin`)  [Agent Identity Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.editor) (`roles/agentidentity.editor`)  [Agent Identity Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/agentidentity#agentidentity.viewer) (`roles/agentidentity.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
