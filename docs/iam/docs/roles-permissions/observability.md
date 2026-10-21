---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/observability/
title: Google Cloud Observability roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:02.346805+00:00
---

# Google Cloud Observability roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Cloud Observability roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Cloud Observability. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Cloud Observability roles

Role | Permissions  
---|---  
  
#### Observability Admin 

(`roles/observability.admin`) Full access to Observability resources.  |  `observability.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`
  * `observability.buckets.create`
  * `observability.buckets.delete`
  * `observability.buckets.get`
  * `observability.buckets.list`
  * `observability.buckets.undelete`
  * `observability.buckets.update`
  * `observability.datasets.create`
  * `observability.datasets.delete`
  * `observability.datasets.get`
  * `observability.datasets.list`
  * `observability.datasets.undelete`
  * `observability.datasets.update`
  * `observability.links.create`
  * `observability.links.delete`
  * `observability.links.get`
  * `observability.links.list`
  * `observability.links.update`
  * `observability.locations.get`
  * `observability.locations.list`
  * `observability.operations.cancel`
  * `observability.operations.delete`
  * `observability.operations.get`
  * `observability.operations.list`
  * `observability.scopes.get`
  * `observability.scopes.update`
  * `observability.settings.get`
  * `observability.settings.update`
  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`
  * `observability.views.access`
  * `observability.views.create`
  * `observability.views.delete`
  * `observability.views.get`
  * `observability.views.list`
  * `observability.views.update`

  
  
#### Observability Editor 

(`roles/observability.editor`) Edit access to Observability resources.  |  `observability.analyticsViews.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`

`observability.buckets.create` `observability.buckets.get` `observability.buckets.list` `observability.buckets.update` `observability.datasets.create` `observability.datasets.get` `observability.datasets.list` `observability.datasets.update` `observability.links.*`

  * `observability.links.create`
  * `observability.links.delete`
  * `observability.links.get`
  * `observability.links.list`
  * `observability.links.update`

`observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.*`

  * `observability.operations.cancel`
  * `observability.operations.delete`
  * `observability.operations.get`
  * `observability.operations.list`

`observability.scopes.*`

  * `observability.scopes.get`
  * `observability.scopes.update`

`observability.settings.*`

  * `observability.settings.get`
  * `observability.settings.update`

`observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

`observability.views.create` `observability.views.delete` `observability.views.get` `observability.views.list` `observability.views.update`  
  
#### Observability Viewer 

(`roles/observability.viewer`) Read only access to Observability resources.  |  `observability.analyticsViews.get` `observability.analyticsViews.list` `observability.buckets.get` `observability.buckets.list` `observability.datasets.get` `observability.datasets.list` `observability.links.get` `observability.links.list` `observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.get` `observability.operations.list` `observability.scopes.get` `observability.settings.get` `observability.traceScopes.get` `observability.traceScopes.list` `observability.views.get` `observability.views.list`  
  
#### Observability Analytics User 

(`roles/observability.analyticsUser`) Grants permissions to use Cloud Observability Analytics.  |  `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `observability.analyticsViews.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`

`observability.buckets.get` `observability.buckets.list` `observability.datasets.get` `observability.datasets.list` `observability.links.get` `observability.links.list` `observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.get` `observability.operations.list` `observability.scopes.get` `observability.settings.get` `observability.traceScopes.get` `observability.traceScopes.list` `observability.views.get` `observability.views.list`  
  
#### Observability Scopes Editor 

(`roles/observability.scopesEditor`) Grants permission to view and edit Observability, Logging, Trace, and Monitoring scopes  |  `logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`monitoring.metricsScopes.link` `observability.scopes.*`

  * `observability.scopes.get`
  * `observability.scopes.update`

`observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

  
  
#### Observability View Accessor 

(`roles/observability.viewAccessor`) Read only access to data defined by an Observability View.  |  `observability.views.access`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Observability Service Agent 

(`roles/observability.serviceAgent`) Grants Observability service account the ability to list, create and link datasets in the consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.link`  
  
## Google Cloud Observability permissions

Permission | Included in roles  
---|---  
  
#### `observability.analyticsViews.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.analyticsViews.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.analyticsViews.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.analyticsViews.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.analyticsViews.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.buckets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.buckets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)   
  
#### `observability.buckets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.buckets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.buckets.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)   
  
#### `observability.buckets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)   
  
#### `observability.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.datasets.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)   
  
#### `observability.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.links.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `observability.links.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `observability.links.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `observability.links.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 
  * [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) (`roles/monitoring.notificationServiceAgent`) 

  
  
#### `observability.links.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `observability.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`) 

  
  
#### `observability.scopes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Logging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`)  [Private Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`)  [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Dataproc Hub Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.hubAgent) (`roles/dataproc.hubAgent`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Network Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.networkAdmin) (`roles/iam.networkAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Logs Configuration Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)  [Telco Automation Tier 1 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier1) (`roles/telcoautomation.opsAdminTier1`)  [Telco Automation Tier 4 Operations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.opsAdminTier4) (`roles/telcoautomation.opsAdminTier4`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 

  
  
#### `observability.scopes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.traceScopes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.traceScopes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.traceScopes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.traceScopes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.traceScopes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)   
  
#### `observability.views.access`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability View Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Custom Code Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.customCodeServiceAgent) (`roles/aiplatform.customCodeServiceAgent`) 

  
  
#### `observability.views.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.views.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
#### `observability.views.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.views.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)  [Observability Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Observability Analytics User](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)   
  
#### `observability.views.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Observability Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.admin) (`roles/observability.admin`)  [Observability Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
