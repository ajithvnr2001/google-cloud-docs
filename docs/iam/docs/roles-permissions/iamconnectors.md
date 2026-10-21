---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors/
title: IAM Connectors roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:07.294793+00:00
---

# IAM Connectors roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  IAM Connectors roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for IAM Connectors. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## IAM Connectors roles

Role | Permissions  
---|---  
  
#### Connector Admin Beta

(`roles/iamconnectors.admin`) Grants access to manage connectors, authorizations, and access events.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.create` `agentidentity.authProviders.delete` `agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authProviders.revokeAuthorizations` `agentidentity.authProviders.setIamPolicy` `agentidentity.authProviders.undelete` `agentidentity.authProviders.update` `agentidentity.authorizations.create` `agentidentity.authorizations.delete` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.authorizations.setIamPolicy` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

`iamconnectors.accessEvents.*`

  * `iamconnectors.accessEvents.get`
  * `iamconnectors.accessEvents.list`

`iamconnectors.authorizations.*`

  * `iamconnectors.authorizations.delete`
  * `iamconnectors.authorizations.get`
  * `iamconnectors.authorizations.list`

`iamconnectors.connectors.create` `iamconnectors.connectors.delete` `iamconnectors.connectors.get` `iamconnectors.connectors.getIamPolicy` `iamconnectors.connectors.list` `iamconnectors.connectors.queryWorkloads` `iamconnectors.connectors.revokeAuthorizations` `iamconnectors.connectors.setIamPolicy` `iamconnectors.connectors.undelete` `iamconnectors.connectors.update` `iamconnectors.locations.*`

  * `iamconnectors.locations.get`
  * `iamconnectors.locations.list`

`iamconnectors.operations.*`

  * `iamconnectors.operations.cancel`
  * `iamconnectors.operations.delete`
  * `iamconnectors.operations.get`
  * `iamconnectors.operations.list`

  
  
#### Connector Editor Beta

(`roles/iamconnectors.editor`) Grants access to edit connectors, authorizations, and access events.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.create` `agentidentity.authProviders.delete` `agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authProviders.revokeAuthorizations` `agentidentity.authProviders.undelete` `agentidentity.authProviders.update` `agentidentity.authorizations.create` `agentidentity.authorizations.delete` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

`iamconnectors.accessEvents.*`

  * `iamconnectors.accessEvents.get`
  * `iamconnectors.accessEvents.list`

`iamconnectors.authorizations.*`

  * `iamconnectors.authorizations.delete`
  * `iamconnectors.authorizations.get`
  * `iamconnectors.authorizations.list`

`iamconnectors.connectors.create` `iamconnectors.connectors.delete` `iamconnectors.connectors.get` `iamconnectors.connectors.getIamPolicy` `iamconnectors.connectors.list` `iamconnectors.connectors.queryWorkloads` `iamconnectors.connectors.revokeAuthorizations` `iamconnectors.connectors.undelete` `iamconnectors.connectors.update` `iamconnectors.locations.*`

  * `iamconnectors.locations.get`
  * `iamconnectors.locations.list`

`iamconnectors.operations.*`

  * `iamconnectors.operations.cancel`
  * `iamconnectors.operations.delete`
  * `iamconnectors.operations.get`
  * `iamconnectors.operations.list`

  
  
#### Connector Viewer Beta

(`roles/iamconnectors.viewer`) Grants access to view connectors, authorizations, and access events.  |  `agentidentity.accessSummaries.*`

  * `agentidentity.accessSummaries.get`
  * `agentidentity.accessSummaries.list`

`agentidentity.authProviders.get` `agentidentity.authProviders.getIamPolicy` `agentidentity.authProviders.list` `agentidentity.authProviders.queryWorkloads` `agentidentity.authorizations.get` `agentidentity.authorizations.getIamPolicy` `agentidentity.authorizations.list` `agentidentity.locations.*`

  * `agentidentity.locations.get`
  * `agentidentity.locations.list`

`iamconnectors.accessEvents.*`

  * `iamconnectors.accessEvents.get`
  * `iamconnectors.accessEvents.list`

`iamconnectors.authorizations.get` `iamconnectors.authorizations.list` `iamconnectors.connectors.get` `iamconnectors.connectors.getIamPolicy` `iamconnectors.connectors.list` `iamconnectors.connectors.queryWorkloads` `iamconnectors.locations.*`

  * `iamconnectors.locations.get`
  * `iamconnectors.locations.list`

`iamconnectors.operations.get` `iamconnectors.operations.list`  
  
#### Connector User Beta

(`roles/iamconnectors.user`) Grants access to retrieve credentials from connectors.  |  `agentidentity.authProviders.exchangeCredentials` `agentidentity.authProviders.retrieveCredentials` `agentidentity.authorizations.exchangeCredentials` `agentidentity.authorizations.retrieveCredentials` `iamconnectors.connectors.retrieveCredentials`  
  
## IAM Connectors permissions

Permission | Included in roles  
---|---  
  
#### `iamconnectors.accessEvents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.accessEvents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.authorizations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.authorizations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.authorizations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.connectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.connectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.connectors.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.connectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.connectors.queryWorkloads`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.connectors.retrieveCredentials`

|  [Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.user) (`roles/iamconnectors.user`)   
  
#### `iamconnectors.connectors.revokeAuthorizations`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.connectors.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)   
  
#### `iamconnectors.connectors.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.connectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)   
  
#### `iamconnectors.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `iamconnectors.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.admin) (`roles/iamconnectors.admin`)  [Connector Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.editor) (`roles/iamconnectors.editor`)  [Connector Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iamconnectors#iamconnectors.viewer) (`roles/iamconnectors.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
