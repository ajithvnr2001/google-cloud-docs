---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub/
title: BigQuery sharing roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:41:30.808518+00:00
---

# BigQuery sharing roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigQuery sharing roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigQuery sharing. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigQuery sharing roles

Role | Permissions  
---|---  
  
#### Analytics Hub Admin 

(`roles/analyticshub.admin`) Administer Data Exchanges and Listings  |  `analyticshub.dataExchanges.create` `analyticshub.dataExchanges.delete` `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.dataExchanges.setIamPolicy` `analyticshub.dataExchanges.update` `analyticshub.dataExchanges.viewSubscriptions` `analyticshub.listings.create` `analyticshub.listings.delete` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.listings.setIamPolicy` `analyticshub.listings.update` `analyticshub.listings.viewSubscriptions` `analyticshub.queryTemplates.*`

  * `analyticshub.queryTemplates.approve`
  * `analyticshub.queryTemplates.create`
  * `analyticshub.queryTemplates.delete`
  * `analyticshub.queryTemplates.get`
  * `analyticshub.queryTemplates.list`
  * `analyticshub.queryTemplates.update`

`analyticshub.subscriptions.*`

  * `analyticshub.subscriptions.create`
  * `analyticshub.subscriptions.delete`
  * `analyticshub.subscriptions.get`
  * `analyticshub.subscriptions.list`
  * `analyticshub.subscriptions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Editor 

(`roles/analyticshub.editor`) Editor role for Analytics Hub  |  `analyticshub.dataExchanges.create` `analyticshub.dataExchanges.delete` `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.dataExchanges.update` `analyticshub.listings.create` `analyticshub.listings.delete` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.listings.update` `analyticshub.queryTemplates.*`

  * `analyticshub.queryTemplates.approve`
  * `analyticshub.queryTemplates.create`
  * `analyticshub.queryTemplates.delete`
  * `analyticshub.queryTemplates.get`
  * `analyticshub.queryTemplates.list`
  * `analyticshub.queryTemplates.update`

`analyticshub.subscriptions.*`

  * `analyticshub.subscriptions.create`
  * `analyticshub.subscriptions.delete`
  * `analyticshub.subscriptions.get`
  * `analyticshub.subscriptions.list`
  * `analyticshub.subscriptions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Viewer 

(`roles/analyticshub.viewer`) Can browse Data Exchanges and Listings  |  `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.queryTemplates.get` `analyticshub.queryTemplates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Listing Admin 

(`roles/analyticshub.listingAdmin`) Grants full control over the Listing, including updating, deleting and setting ACLs  |  `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.listings.delete` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.listings.setIamPolicy` `analyticshub.listings.update` `analyticshub.listings.viewSubscriptions` `analyticshub.queryTemplates.get` `analyticshub.queryTemplates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Publisher 

(`roles/analyticshub.publisher`) Can publish to Data Exchanges thus creating Listings  |  `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.listings.create` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.queryTemplates.*`

  * `analyticshub.queryTemplates.approve`
  * `analyticshub.queryTemplates.create`
  * `analyticshub.queryTemplates.delete`
  * `analyticshub.queryTemplates.get`
  * `analyticshub.queryTemplates.list`
  * `analyticshub.queryTemplates.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Subscriber 

(`roles/analyticshub.subscriber`) Can browse Data Exchanges and subscribe to Listings  |  `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.dataExchanges.subscribe` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.listings.subscribe` `analyticshub.queryTemplates.get` `analyticshub.queryTemplates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Analytics Hub Subscription Owner 

(`roles/analyticshub.subscriptionOwner`) Grants full control over the Subscription, including updating and deleting  |  `analyticshub.dataExchanges.get` `analyticshub.dataExchanges.getIamPolicy` `analyticshub.dataExchanges.list` `analyticshub.listings.get` `analyticshub.listings.getIamPolicy` `analyticshub.listings.list` `analyticshub.queryTemplates.get` `analyticshub.queryTemplates.list` `analyticshub.subscriptions.*`

  * `analyticshub.subscriptions.create`
  * `analyticshub.subscriptions.delete`
  * `analyticshub.subscriptions.get`
  * `analyticshub.subscriptions.list`
  * `analyticshub.subscriptions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Analytics Hub Service Agent 

(`roles/analyticshub.serviceAgent`) Grants Analytics Hub Service Agent permissions required to manage resources in the consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `analyticshub.dataExchanges.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## BigQuery sharing permissions

Permission | Included in roles  
---|---  
  
#### `analyticshub.dataExchanges.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)   
  
#### `analyticshub.dataExchanges.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)   
  
#### `analyticshub.dataExchanges.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.dataExchanges.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.dataExchanges.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Analytics Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.serviceAgent) (`roles/analyticshub.serviceAgent`) 

  
  
#### `analyticshub.dataExchanges.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `analyticshub.dataExchanges.subscribe`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)   
  
#### `analyticshub.dataExchanges.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)   
  
#### `analyticshub.dataExchanges.viewSubscriptions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)   
  
#### `analyticshub.listings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)   
  
#### `analyticshub.listings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)   
  
#### `analyticshub.listings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.listings.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.listings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.listings.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)   
  
#### `analyticshub.listings.subscribe`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)   
  
#### `analyticshub.listings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)   
  
#### `analyticshub.listings.viewSubscriptions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)   
  
#### `analyticshub.queryTemplates.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)   
  
#### `analyticshub.queryTemplates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)   
  
#### `analyticshub.queryTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)   
  
#### `analyticshub.queryTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.queryTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.viewer) (`roles/analyticshub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Listing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.listingAdmin) (`roles/analyticshub.listingAdmin`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)  [Analytics Hub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriber) (`roles/analyticshub.subscriber`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.queryTemplates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.publisher) (`roles/analyticshub.publisher`)   
  
#### `analyticshub.subscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)   
  
#### `analyticshub.subscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)   
  
#### `analyticshub.subscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.subscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `analyticshub.subscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Analytics Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.admin) (`roles/analyticshub.admin`)  [Analytics Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.editor) (`roles/analyticshub.editor`)  [Analytics Hub Subscription Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/analyticshub#analyticshub.subscriptionOwner) (`roles/analyticshub.subscriptionOwner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
