---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations/
title: Recommendations roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:54.707152+00:00
---

# Recommendations roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Recommendations roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Recommendations. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Recommendations roles

Role | Permissions  
---|---  
  
#### Recommendations AI Admin Beta

(`roles/automlrecommendations.admin`) Full access to all Recommendations AI resources.  |  `automlrecommendations.*`

  * `automlrecommendations.apiKeys.create`
  * `automlrecommendations.apiKeys.delete`
  * `automlrecommendations.apiKeys.list`
  * `automlrecommendations.catalogItems.create`
  * `automlrecommendations.catalogItems.delete`
  * `automlrecommendations.catalogItems.get`
  * `automlrecommendations.catalogItems.list`
  * `automlrecommendations.catalogItems.update`
  * `automlrecommendations.catalogs.getStats`
  * `automlrecommendations.catalogs.list`
  * `automlrecommendations.catalogs.update`
  * `automlrecommendations.eventStores.getStats`
  * `automlrecommendations.eventStores.list`
  * `automlrecommendations.events.create`
  * `automlrecommendations.events.get`
  * `automlrecommendations.events.list`
  * `automlrecommendations.events.purge`
  * `automlrecommendations.events.rejoin`
  * `automlrecommendations.placements.create`
  * `automlrecommendations.placements.delete`
  * `automlrecommendations.placements.getStats`
  * `automlrecommendations.placements.list`
  * `automlrecommendations.recommendations.create`
  * `automlrecommendations.recommendations.delete`
  * `automlrecommendations.recommendations.list`
  * `automlrecommendations.recommendations.pause`
  * `automlrecommendations.recommendations.resume`
  * `automlrecommendations.recommendations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `retail.catalogs.list` `retail.catalogs.update` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.create` `retail.products.delete` `retail.products.export` `retail.products.get` `retail.products.import` `retail.products.list` `retail.products.purge` `retail.products.update` `retail.retailProjects.*`

  * `retail.retailProjects.acceptDataTerms`
  * `retail.retailProjects.get`

`retail.userEvents.*`

  * `retail.userEvents.create`
  * `retail.userEvents.import`
  * `retail.userEvents.purge`
  * `retail.userEvents.rejoin`

`serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Recommendations AI Editor Beta

(`roles/automlrecommendations.editor`) Editor of all Recommendations AI resources.  |  `automlrecommendations.apiKeys.create` `automlrecommendations.apiKeys.list` `automlrecommendations.catalogItems.*`

  * `automlrecommendations.catalogItems.create`
  * `automlrecommendations.catalogItems.delete`
  * `automlrecommendations.catalogItems.get`
  * `automlrecommendations.catalogItems.list`
  * `automlrecommendations.catalogItems.update`

`automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.*`

  * `automlrecommendations.eventStores.getStats`
  * `automlrecommendations.eventStores.list`

`automlrecommendations.events.create` `automlrecommendations.events.get` `automlrecommendations.events.list` `automlrecommendations.placements.create` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.create` `automlrecommendations.recommendations.list` `automlrecommendations.recommendations.pause` `automlrecommendations.recommendations.resume` `automlrecommendations.recommendations.update` `resourcemanager.projects.get` `resourcemanager.projects.list` `retail.catalogs.list` `retail.catalogs.update` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.create` `retail.products.delete` `retail.products.export` `retail.products.get` `retail.products.import` `retail.products.list` `retail.products.update` `retail.retailProjects.get` `retail.userEvents.create` `retail.userEvents.import` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Recommendations AI Viewer Beta

(`roles/automlrecommendations.viewer`) Viewer of all Recommendations resources except `apiKeys`. To view all resources, including `apiKeys`, grant the Recommendations AI Admin Viewer role (`roles/automlrecommendations.adminViewer`).  |  `automlrecommendations.catalogItems.get` `automlrecommendations.catalogItems.list` `automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.*`

  * `automlrecommendations.eventStores.getStats`
  * `automlrecommendations.eventStores.list`

`automlrecommendations.events.get` `automlrecommendations.events.list` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `retail.catalogs.list` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.export` `retail.products.get` `retail.products.list` `retail.retailProjects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Recommendations AI Admin Viewer Beta

(`roles/automlrecommendations.adminViewer`) Viewer of all Recommendations AI resources.  |  `automlrecommendations.apiKeys.list` `automlrecommendations.catalogItems.get` `automlrecommendations.catalogItems.list` `automlrecommendations.catalogs.getStats` `automlrecommendations.catalogs.list` `automlrecommendations.eventStores.*`

  * `automlrecommendations.eventStores.getStats`
  * `automlrecommendations.eventStores.list`

`automlrecommendations.events.get` `automlrecommendations.events.list` `automlrecommendations.placements.getStats` `automlrecommendations.placements.list` `automlrecommendations.recommendations.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `retail.catalogs.list` `retail.operations.*`

  * `retail.operations.get`
  * `retail.operations.list`

`retail.placements.*`

  * `retail.placements.predict`
  * `retail.placements.search`

`retail.products.export` `retail.products.get` `retail.products.list` `retail.retailProjects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Recommendations AI Service Agent 

(`roles/automlrecommendations.serviceAgent`) Recommendations AI service uploads catalog feeds from Cloud Storage, reports results to the customer Cloud Storage bucket, writes logs to customer projects, and writes and reads Stackdriver metrics for customer projects.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.update` `bigquery.tables.create` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `cloudnotifications.activities.list` `dataflow.jobs.*`

  * `dataflow.jobs.cancel`
  * `dataflow.jobs.create`
  * `dataflow.jobs.get`
  * `dataflow.jobs.list`
  * `dataflow.jobs.snapshot`
  * `dataflow.jobs.updateContents`

`dataflow.messages.list` `dataflow.metrics.get` `logging.logEntries.create` `logging.logEntries.route` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.buckets.create` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Recommendations permissions

Permission | Included in roles  
---|---  
  
#### `automlrecommendations.apiKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.apiKeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.apiKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `automlrecommendations.catalogItems.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.catalogItems.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.catalogItems.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.catalogItems.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.catalogItems.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.catalogs.getStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.catalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.catalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.eventStores.getStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.eventStores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `automlrecommendations.events.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `automlrecommendations.events.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.events.purge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `automlrecommendations.events.rejoin`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)   
  
#### `automlrecommendations.placements.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.placements.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.placements.getStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.placements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.recommendations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.recommendations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.recommendations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Recommendations AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.viewer) (`roles/automlrecommendations.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)  [Retail Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.viewer) (`roles/retail.viewer`)  [Recommendations AI Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.adminViewer) (`roles/automlrecommendations.adminViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Retail Merchant Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantApprover) (`roles/retail.merchantApprover`)  [Retail Merchant Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.merchantCreator) (`roles/retail.merchantCreator`)   
  
#### `automlrecommendations.recommendations.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.recommendations.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
#### `automlrecommendations.recommendations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Recommendations AI Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.admin) (`roles/automlrecommendations.admin`)  [Recommendations AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/automlrecommendations#automlrecommendations.editor) (`roles/automlrecommendations.editor`)  [Retail Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.admin) (`roles/retail.admin`)  [Retail Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/retail#retail.editor) (`roles/retail.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
